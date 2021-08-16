class AllowanceHolder():
    '''Defines the AllowanceHolder Class'''
    _code = None
    _name = None

    def __init__( self, code, name = '' ):
        self._code = code
        self._name = name