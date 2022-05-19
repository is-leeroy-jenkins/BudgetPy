'''
jtc64 类似于 base64, 但是在处理多余位数时需要的位数更少, 同时使用的符号更易辨别
base64 是每6位变4位, jtc64是每3位变2位; base64 多2位和多4位都需要额外的4个字符, jtc64多1位只需1个字符, 多2位只需2个字符
正常情况使用 0~9, a~z, A~Z, @, #
在多2位的情况下要使用 $, %, &, =
'''

from .exceptions import *
import codecs
chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#'
dic1={}
for i in range(0,64):
    dic1[chars[i]]=i
hexs='0123456789abcdef'
dic2={}
for i in range(0,16):
    dic2[hexs[i]]=i
syms='$%&='
dic3={'$':0,'%':1,'&':2,'=':3}




def hexToStr(text:str):
    return codecs.decode(text,'hex').decode('utf-8')

def toHex(text:str):
    text=text.encode('utf-8')
    return codecs.encode(text,'hex').decode('utf-8')



def hexToJtc64(text:str):
    try:
        l=len(text)
        n=l//3
        r=l-n*3
        text2=''
        for i in range(0,n):
            num=dic2[text[3*i]]*256+dic2[text[3*i+1]]*16+dic2[text[3*i+2]]
            s1=num//64
            s2=num%64
            text2=text2+chars[s1]+chars[s2]
        if(r==0):
            return text2
        if(r==1):
            tmp=dic2[text[-1]]
            return text2+text[-1]
        num2=dic2[text[3*n]]*16+dic2[text[3*n+1]]
        text2=text2+chars[num2//4]+syms[num2%4]
        return text2
    except:
        raise NotHexError



def strToJtc64(text:str):
    text=toHex(text)
    return hexToJtc64(text)


def jtc64ToHex(text:str):
    try:
        if(text==''):
            return ''
        type=0
        main=text
        if(len(text)%2==1):
            type=1
            main=text[:-1]
        if(text[-1] in ['$','%','&','=']):
            type=2
            main=text[:-2]
        n=len(main)//2
        text2=''
        for i in range(0,n):
            num=dic1[text[2*i]]*64+dic1[text[2*i+1]]
            text2=text2+hexs[num//256]+hexs[(num%256)//16]+hexs[num%16]
        if(type==0):
            return text2
        if(type==1):
            tmp=dic2[text[-1]]
            return text2+text[-1]
        num2=dic1[text[2*n]]*4+dic3[text[2*n+1]]
        text2=text2+hexs[num2//16]+hexs[num2%16]
        return text2
    except:
        raise NotJtc64Error


def jtc64ToStr(text:str):
    return hexToStr(jtc64ToHex(text))

