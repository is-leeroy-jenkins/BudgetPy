class Appropriation():
    '''Defines the Appropriation Class'''
    _code = ''
    _name = ''

    def __init__( self, code, name = '' ):
        self._code = code
        self._name = name