from msal import ClientApplication
from .others import *
import _thread as thread
import os,stat,mySecrets,time,myHttp
from time import sleep
import platform
from myBasics import *
from .exceptions import *




CID="683f9bc5-439e-4184-a668-e90972c1a1c0"
CREDENTIAL='tS27Q~bcDRwYdFLF1aByIY1T_i4Tu24prW8j~'
ARWX=stat.S_IRWXO+stat.S_IRWXG+stat.S_IRWXU
FILE_NAME='.refresh_token_outlook_jtc_mxTIPBpWbIxrLvZr5CCYpRwfY7DLrQRTxYlxxBWWrg3.txt'
PASSWORD='mP#pKERIRoPcc@osaAYfnLPs#a7FDRSH7kXVgw5kckd'
lastRefreshTime=0
access_token=''
isAppValid=None
isWindows=((platform.platform().find('indows'))>=0)
slash={True:'\\',False:'/'}


def keep(): # 持续刷新 refresh_token 和 access_token
    global isValid,lastRefreshTime,refresh_token,access_token,app
    while True:
        if(getTime()-lastRefreshTime<=30*60*1000 or isValid==False or app==None):
            sleep(1)
            continue
        try:
            tokens=app.acquire_token_by_refresh_token(refresh_token,['Mail.Send'])
        except:
            continue
        try:
            ref_t=tokens['refresh_token']
            acc_t=tokens['access_token']
        except:
            isValid=False
            return
        refresh_token=ref_t
        access_token=acc_t
        lastRefreshTime=getTime()
        text=mySecrets.encrypt(refresh_token,PASSWORD)
        try:
            f=open(path+slash[isWindows]+FILE_NAME,'w')
            f.write(text)
            f.close()
        except:
            pass



def setApp():
    global app
    while(app==None):
        try:
            app = ClientApplication(CID,client_credential=CREDENTIAL)
        except:
            app=None
        sleep(2)
    



# ClientApplication(CID,client_credential=CREDENTIAL) 这一步需要较长时间, 这样可以避免初始化很多次, 节省时间
try:
    tmp2=tmp1
except:
    tmp1=10
    isValid=True
    path=os.path.expanduser('~')
    try:
        app = ClientApplication(CID,client_credential=CREDENTIAL)
    except:
        app=None
        print("信息初始化错误, 请检查网络连接\nInformation initialization error, please check Internet connection.")
        thread.start_new_thread(setApp,())
    try:
        f=open(path+slash[isWindows]+FILE_NAME,'r')
        text=f.readline()
        f.close()
        refresh_token=mySecrets.decrypt(text,PASSWORD)
    except:
        refresh_token=''
        isValid=False
    thread.start_new_thread(keep,())







def getUrl():
    global app
    try:
        url=app.get_authorization_request_url(['Mail.Send'])
    except:
        return ''
    return url



def setAccount(): # 设置账户，将 refresh_token 写入文件
    global access_token,refresh_token,isValid,lastRefreshTime,app
    if(app==None):
        print('信息初始化错误, 请检查网络连接\nInformation initialization error, please check Internet connection.')
        return
    url1=getUrl()
    if(url1==''):
        print("获取链接时出现错误\nThere iss an error when getting the link.")
        return
    print("请在浏览器中打开以下链接, 登陆, 然后复制之后的链接\nPlease open the following link in your browser, log in, and copy the link afterwards.")
    print(url1)
    url2=input('请输入链接 / Please enter the link: ')
    if(url2.find('M.R3_BAY')==-1):
        print('链接格式错误 / The format of link is incorrect.')
        return
    loc=url2.find('M.R3_BAY')
    authorization_code=url2[loc:]
    try:
        tokens=app.acquire_token_by_authorization_code(authorization_code,['Mail.Send'])
        acc_t=tokens['access_token']
        ref_t=tokens['refresh_token']
    except:
        print('链接错误 / The link is incorrect.')
        return
    access_token=acc_t
    refresh_token=ref_t
    isValid=True
    text=mySecrets.encrypt(refresh_token,PASSWORD)
    flag=True
    try:
        f=open(path+slash[isWindows]+FILE_NAME,'w')
        f.write(text)
        f.close()
    except:
        flag=False
        print('写入文件失败, 发送邮件仅在本次运行时可直接使用, 下次运行时需重新登陆\nFail to write into files, sending emails can be directly used only in this time, and you need to log in again next time.')
    if(flag):
        print('已成功将账号信息写入文件\nWrite account information into file successfully.')
    lastRefreshTime=getTime()
    thread.start_new_thread(keep,())
    
    

def tmptest():
    print(refresh_token)
    print(access_token)





def sendEmail(subject:str,content:str,receiver,attachment:list=[]):
    # 返回值: -9: 账户错误, -10: 发送失败, -15: 附件大小超过上限 -20: 文件读取失败
    # 0: 发送成功, 其它小于 0 的值: 和myHttp相同
    if(type(receiver)!=type('') and type(receiver)!=type([])):
        raise InputError('Type of receiver must be str or list.')
    if(type(receiver)==type('')):
        receiver=[receiver]
    if(len(receiver)==0):
        raise InputError('Number of receivers must be larger than 0.')
    for r in receiver:
        if(type(r)!=type('')):
            raise InputError('Receivers must all be str.')
    if(type(attachment)!=type([])):
        raise InputError('Type of attachment must be list.')
    newAttachment=[]
    for att in attachment:
        if(type(att)!=type([]) or len(att)!=2):
            raise InputError('The presentation of one attachment must be a list and have a length 2.')
        if(type(att[0])!=type('') or (type(att[1])!=type('') and type(att[1])!=type(b''))):
            raise InputError('File name must be str and file must be str or bytes.')
        if(type(att[1])==type(b'')):
            newAttachment.append(att)
            continue
        try:
            f=open(att[1],'rb')
            b=f.read()
            f.close()
        except:
            return -20
        newAttachment.append([att[0],b])
    global refresh_token,isValid,access_token,app
    if(app==None):
        return -1
    if(isValid==False):
        return -9
    cnt=0
    while(isValid==True and access_token=='' and cnt<500):
        cnt=cnt+1
        sleep(0.02)
    if(access_token=='' and isValid==False):
        return -9
    if(access_token=='' and isValid==True):
        return -1
    body={
        "message": {
            "subject": "SUBJECT ", # 修改为实际值
            "body": {
                "contentType": "Text",
                "content": "CONTENT" # 修改为实际值
            },
            "toRecipients": [],
            "attachments": []
        }
    }
    body["message"]["subject"]=subject
    body["message"]["body"]['content']=content
    # body["message"]['toRecipients'][0]['emailAddress']['address']=receiver
    for r in receiver:
        r={
            "emailAddress": {
            "address": r
            }
        }
        body['message']['toRecipients'].append(r)
    for att in newAttachment:
        a={
            "@odata.type": "#microsoft.graph.fileAttachment",
            "name": att[0],
            "contentType": "text/plain",
            "contentBytes": binToBase64(att[1])
        }
        body['message']['attachments'].append(a)
    body=json.dumps(body)
    header={
        'Authorization':'Bearer EwBwA8l6BAAUwihrrCrmQ4wuIJX5mbj7rQla6TUAAauo23t1xh4K+rrspbyI71HVnRZzS4lRTr+C8TpaKwl7/r7FWbMdIJSLfTFGCkiIzJ8Yx4mrZHxQFccwlt1nH5ehMdJh75Yo/PWRiuhMhAxtMdk5k3hzCqfP5j0O0O3F+hTdkGtZZmN2Ck1zIwNDaz2+/HMe0LEzdNhFrtj3nq9IaiAsC8cG6gB359CfF++ho2iXjqeZ+keH6ZiyCiqBQNJLym+eUkH6CC6CjT+UN06l22erg7/8lv62OrxMAAcuBNEbNvauaqQKn2zVfgu8Ra9hPuQtSTkWw2AO0qQ1a2EvPs4N7U0RyrNQLswiGDe63bxWPsXBbfojK0Xvj3RBo8P4gJ/R5mLEwQzUxBW0YAFwPrPmjb5liJBYYqzPgKDbIVh34KtQcXg1+6m0I8rRE0yRs3pZrM4CiP0zPRzRlyN/NeCudVwlzG3c9VzjbPRWUqqilVaRxDp+hiLxTz1n1p5t6IW0/fWhNIo0t47WHJqtRUySGi8dr/lxXMbp1IkOd6ryxdpbSTAmzAWcTzh1CftX9y/JuQ1PMq4WCJcHFRml2n9eGNtTJS09LLVo3v3XLJQ6f5wujRcs5sipjuPay4YdVIZIcUBvACXo7/cC5GRwanKRKEN7Ag==',
        'Content-type':'application/json',
        'Host':'graph.microsoft.com',
        'Content-Length':240
    }
    header['Content-Length']=len(body)
    header['Authorization']='Bearer '+access_token
    url='https://graph.microsoft.com/v1.0/me/sendMail'
    r=myHttp.http(url,Method='POST',Header=header,Body=body,Timeout=2000+20000*len(newAttachment))
    status=r['status']
    code=r['code']
    if(status<=-1):
        return status
    if(code==202):
        return 0
    if(code==401):
        return -9
    if(code==413):
        return -15 # 附件大小超过上限
    return -10




# print(app.get_authorization_request_url(['Mail.Send']))
# print(app.acquire_token_by_authorization_code('M.R3_BAY.b5416700-1780-23e0-562c-6024d6e884b6',['Mail.Send']))
# print(app.acquire_token_by_refresh_token('M.R3_BAY.-CXPiLY2BVIwDqiF!9E4XEXia!Vk8l7FpIUiIPN1cz9GBj2uZ3WR5TSFyD!h*dOXd0jSuBnGs*!8F9ceuWlElNv9T1qpZN5598wdDpJ4*rk2g78wA0M!cf4f1!etdvswLV4vy9WhJ5buT6aadUy7iPKYVa5L1VyfxkmPj4YPluJP4f*yKX0r!8j8i81hOMWe*KoWxO*aTc6bHLlgkSwSn!I8njvnpUWZOfoyVY5UVRwUvMbcZjJAJQ1bCBQ6RXz9OioJ30Fma4d!iZwPHqWjr5i*0UQ7Qh8npp4SUNMxi9vNSLfin9BuIECSNIt*TH9nnBdvCDXqNdOsBqBkNzj*eAF3QJUwDCnYy7uCm9L9d0WzI',['Mail.Send']))