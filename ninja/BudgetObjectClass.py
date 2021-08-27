class BudgetObjectClass():
    '''Defines the BudgetObjectClass Class'''
    _code = ''
    _name = ''

    @property
    def code( self ):
        if not self._code == '':
            return self._code

    @property
    def name( self ):
        if not self._name == '':
            return self._name

    def __init__( self, code, name = '' ):
        self._code = code
        self._name = name