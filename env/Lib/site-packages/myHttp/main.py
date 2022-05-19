import urllib3
import urllib3.exceptions as exceptions
from .others import *


import warnings
warnings.filterwarnings("ignore")


defaultTestingUrl='https://apple.com'
useDefaultTestingUrl=True
defaultTimeOut=2000

def setDefaultTimeout(timeout:int):
    global defaultTimeOut
    defaultTimeOut=timeout

def setDefaultTestingUrl(url:str):
    global defaultTestingUrl,useDefaultTestingUrl
    defaultTestingUrl=url
    useDefaultTestingUrl=False

def testInternet():
    '''
    Return 0 when there is Internet connection; return -1 when there is no Internet connection.

    如果有网络连接, 返回 0; 如果没有网络连接, 返回 -1
    '''
    global defaultTestingUrl,useDefaultTestingUrl
    http1=urllib3.PoolManager()
    dic={True:3,False:1}
    try:
        r=http1.request("GET",defaultTestingUrl,timeout=dic[useDefaultTestingUrl],retries=False)
    except:
        return -1
    return 0

def http(url:str,Method:str="GET",Header:dict={},Timeout:int=None,ToJson:bool=True,Body:str="",Decode:bool=True,Retry:bool=True,ForceHttps:bool=False):
    '''
    About Timeout / 关于 Timeout:
        Default timeout is 2000ms.
        If the paramater Timeout is None, it will use dafault timeout.
        If you want to specify a timeout, just give a value to Timeout, unit is ms.
        You can set default timeout by using setDefaultTimeout()
    
    关于 status / About status:
        -1: 无网络 / No Internet Connection
        -2: 超时 / Timeout
        -3: 域名不存在 / Domian not exists
        -4: 其它问题, 主要是代理服务器设置错误 / Other problem, mainly proxy server error
        -5: 对方网站不支持 https, 但强制要求 https 链接 / The website does not support https, but you force https connection.
        -6: 上传内容过大, 未上传完就 timeout / The content to be uploaded is too big, timeout happens when not uploaded completely.
        -7: 下载内容超过内存大小 / Downloading content exceeds memory size.

        1: 不是 UTF-8 编码, text 返回空字符串 / Not UTF-8 encode, the return value of text will be empty str
        2: 不是 Json 格式(在 toJSON=True 的前提下) / Not in Json format (when toJSON=True)
        3: 对方网站不支持https, 但是却使用了https连接, 这种情况会自动切换为http连接, 若此次status不为0, 返回该status, 若为0, 返回3 / 
        The website does not support https. It will change to http automatically in this situation. If the status this time is 0, the status will be 3. If not 0, it will return this status.
    '''
    global defaultTimeOut
    backup=[url,Method,Header,Timeout,ToJson,Body,Decode,Retry]
    if(Timeout==None):
        Timeout=defaultTimeOut
    http1=urllib3.PoolManager()
    r=0
    if(ToJson):
        text={}
    else:
        text=""
    try:
        r=http1.request(Method,url,headers=Header,timeout=Timeout/1000,body=Body,retries=False)
    except exceptions.NewConnectionError as err: # 无网络/域名不存在
        if(testInternet()==-1): # 无网络
            return {'status':-1,'code':0,'text':text,'header':{},'extra':''}
        return {'status':-3,'code':0,'text':text,'header':{},'extra':''}
    except exceptions.ConnectTimeoutError: # 无网络/超时
        if(testInternet()==-1): # 无网络
            return {'status':-1,'code':0,'text':text,'header':{},'extra':''}
        # 超时
        if(Retry==False):
            return {'status':-2,'code':0,'text':text,'header':{},'extra':''}
        try:
            r=http1.request(Method,url,headers=Header,timeout=3*Timeout/1000,body=Body,retries=False)
        except:
            return {'status':-2,'code':0,'text':text,'header':{},'extra':''}
    except exceptions.ReadTimeoutError: # 无网络/超时
        if(testInternet()==-1): # 无网络
            return {'status':-1,'code':0,'text':text,'header':{},'extra':''}
        # 超时
        if(Retry==False):
            return {'status':-2,'code':0,'text':text,'header':{},'extra':''}
        try:
            r=http1.request(Method,url,headers=Header,timeout=3*Timeout/1000,body=Body,retries=False)
        except:
            return {'status':-2,'code':0,'text':text,'header':{},'extra':''}
    except exceptions.SSLError: # 对方网站不支持https, 但是却使用了https连接
        if(ForceHttps):
            return {'status':-5,'code':0,'text':text,'header':{},'extra':''}
        n=backup[0].find('https://')
        newUrl='http://'+backup[0][n+8:]
        tryAgain=http(newUrl,Method=backup[1],Header=backup[2],Timeout=backup[3],ToJson=backup[4],Body=backup[5],Decode=backup[6],Retry=backup[7])
        if(tryAgain['status']==0):
            tryAgain['status']=3
        return tryAgain
    except exceptions.ProtocolError:
        return {'status':-6,'code':0,'text':text,'header':{},'extra':''}
    except MemoryError:
        return {'status':-7,'code':0,'text':text,'header':{},'extra':''}
    except Exception as err: # 其它错误，主要为代理服务器设置错误，服务器上一般无此问题
        return {'status':-4,'code':0,'text':text,'header':{},'extra':''}
    # 以下是正常情况
    resp={}
    resp['status']=0
    resp['code']=r.status
    respHeader=dict(r.headers)
    resp['header']=respHeader
    resp['extra']=''
    text=r.data
    if(not Decode):
        resp['text']=text
        return resp
    deco=''
    try:
        deco=text.decode('utf-8')
    except:
        resp['text']=''
        resp['status']=1
        resp['extra']=text
        return resp
    if(not ToJson):
        resp['text']=deco
        return resp
    js={}
    try:
        js=toJson(deco)
    except:
        resp['text']={}
        resp['status']=2
        resp['extra']=deco
        return resp
    resp['text']=js
    return resp

