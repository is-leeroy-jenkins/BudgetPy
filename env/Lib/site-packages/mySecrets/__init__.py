from .exceptions import NotHexError,NotJtc64Error,InputError,InvalidCiphertextError,VersionNotSupportError,PasswordWrongError
from .hash import getHash
from .crypt import encrypt,decrypt
from .jtc64 import hexToStr,toHex,hexToJtc64,strToJtc64,jtc64ToHex,jtc64ToStr


__all__=[
    'NotHexError','NotJtc64Error','InputError','InvalidCiphertextError','VersionNotSupportError','PasswordWrongError',
    'getHash',
    'encrypt','decrypt',
    'hexToStr','toHex','hexToJtc64','strToJtc64','jtc64ToHex','jtc64ToStr'
]


__version__='1.0.4'
__license__='GPL-2.0 License'
__author__='Tiancheng Jiao'
__github__='https://github.com/jtc1246/mySecrets'
__author_email__='jtc1246@outlook.com'
__description__='Very secure hash and symmetrical encryption'