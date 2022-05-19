class NotHexError(Exception):
    def __init__(self):
        Exception.__init__(self,'Input is not in hex format.')


class NotJtc64Error(Exception):
    def __init__(self):
        Exception.__init__(self,'Input is not in jtc64 format.')

class InputError(Exception):
    def __init__(self):
        Exception.__init__(self,'The length of text must be larger than 0.')

class InvalidCiphertextError(Exception):
    def __init__(self):
        Exception.__init__(self,'Invalid Ciphertext. Please check if there is something wrong during transportation.')

class VersionNotSupportError(Exception):
    def __init__(self):
        Exception.__init__(self,'This version cannot decrypt the data encrypted in a new version. Please update this package.')

class PasswordWrongError(Exception):
    def __init__(self):
        Exception.__init__(self,'Password is not correct.')


