class Account():
    '''defines the Account Code class'''
    _code = ''
    _name = ''
    _goal = ''
    _objective = ''
    _npm = ''
    _program_project = ''

    @property
    def code( self ):
        if not self._code == '':
            return self._code
        else:
            return 'NS'

    @property
    def goal( self ):
        if not self._goal == '':
            return self._goal
        else:
            return 'NS'

    @property
    def npm( self ):
        if not self._npm == '':
            return self._npm
        else:
            return 'NS'

    @property
    def program_project( self ):
        if not self._program_project == '':
            return self._program_project
        else:
            return 'NS'

    def __init__( self, code, name = '' ):
        self._code = code
        self._name = name
        self._goal = list( code )[ 0 ]
        self._objective = list( code )[ 1:3 ]
        self._npm = list( code )[ 3 ]
        self._program_project = list( code )[ 4:6 ]
