import base64,time,json,datetime
from datetime import timezone

def base64ToBin(base64Str:str):
    text=base64Str
    text=text.encode('utf-8')
    d=base64.b64decode(text)
    return d

def base64ToStr(base64Str:str):
    text=base64Str
    text=text.encode('utf-8')
    d=base64.b64decode(text)
    return d.decode('utf-8')




def binToBase64(bin:bytes):
    e=base64.b64encode(bin)
    return e.decode('utf-8')


def strToBase64(text:str):
    return binToBase64(text.encode('utf-8'))


def getTime():
    t=time.time()
    t=int(1000*t)
    return t

def toJson(Text):
    text=Text
    i=0
    while text[0]==' ' or text[0]=='\n':
        text=text[1:]
    if text[0]=='[':
        text='{"1":'+text+'}'
        i=1
    text=json.loads(text,strict=False)
    if i==1:
        text=text['1']
    return text


# 格式示例: "2022-01-17 10:00:00", 输入为零时区时间, 输出为 Unix 毫秒
def toUnix(timeStr:str):
    dt=datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
    t=int(1000*dt.timestamp())
    return t


