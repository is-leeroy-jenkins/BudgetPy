class Fund():
    '''Defines the Fund Class'''
    _code = ''
    _name = ''
    _title = ''

    def __init__( self, code, name='' ):
        self._code = code
        self._name = name