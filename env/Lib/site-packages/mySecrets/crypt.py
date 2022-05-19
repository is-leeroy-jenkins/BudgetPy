from .hash import *
from .jtc64 import *
from secrets import randbelow as rb
import time



def getDiff(s1:str,s2:str): # s1-s2
    global nums,digit
    s3=''
    for i in range(0,len(s1)):
        s3=s3+digit[(16+nums[s1[i]]-nums[s2[i]])%16]
    return s3




def encrypt(text:str,key:str):
    if(text==''):
        raise InputError
    key=getHash(key)
    ran=getHash(getHash(text)+str(rb(2**32))+str(rb(2**32))+str(time.time())+str(rb(2**32))+str(rb(2**32)))[0:32]
    text=toHex(text)
    text=text+getHash(text)[0:16]
    l=len(text)
    n=0
    if(l%64==0):
        n=l//64
    else:
        n=l//64+1
    secret=''
    for i in range(0,n):
        secret=secret+getHash(str(i)+ran+key)
    secret=secret[0:l]
    text2=getSum(secret,text)
    text2=ran+text2
    text2=getHash(text2)[0:16]+text2+'0' # 最后的 0 是模式, 以后可能会加入新的加密模式, 便于兼容前面加密的结果
    return hexToJtc64(text2)
    
    




def decrypt(text:str,key:str):
    key=getHash(key)
    if(text==''):
        raise InvalidCiphertextError
    try:
        text=jtc64ToHex(text)
    except:
        raise InvalidCiphertextError
    if(text[-1]!='0'):
        raise VersionNotSupportError
    text=text[:-1]
    if(len(text)<=64):
        raise InvalidCiphertextError
    check1=text[0:16]
    if(getHash(text[16:])[0:16]!=check1):
        raise InvalidCiphertextError
    ran=text[16:48]
    text=text[48:]
    l=len(text)
    n=0
    if(l%64==0):
        n=l//64
    else:
        n=l//64+1
    secret=''
    for i in range(0,n):
        secret=secret+getHash(str(i)+ran+key)
    secret=secret[0:l]
    text2=getDiff(text,secret)
    if(getHash(text2[0:-16])[0:16]!=text2[-16:]):
        raise PasswordWrongError
    return hexToStr(text2[0:-16])


