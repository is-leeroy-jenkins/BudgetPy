class FinanceObjectClass():
    '''Defines the FinanceObjectClass Class'''
    _code = ''
    _name = ''

    def __init__( self, code, name = '' ):
        self._code = code
        self._name = name