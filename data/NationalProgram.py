class NationalProgram():
    '''Defines the NationalProgram Class'''
    _code = ''
    _name = ''
    _rpio = ''
    _title = ''

    def __init__(self, code, name=''):
        self._code = code
        self._name = name