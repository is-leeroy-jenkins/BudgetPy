import time,json,urllib3

def getTime():
    t = time.time()
    t = int(1000 * t)
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


def testInternet():
    http1=urllib3.PoolManager()
    try:
        r=http1.request("GET",'https://apple.com',timeout=2,retries=False)
    except:
        return -1
    return 0


