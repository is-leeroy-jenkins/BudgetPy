class Account():
    '''defines the Account Code class'''
    __code = ''
    __name = None
    __goal = ''
    __objective = ''
    __npm = ''
    __program_project = ''

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if not self.__name == '':
            return self.__code
        else:
            return 'NS'

    @property
    def goal( self ):
        if not self.__goal == '':
            return self.__goal
        else:
            return 'NS'

    @property
    def npm( self ):
        if not self.__npm == '':
            return self.__npm
        else:
            return 'NS'

    @property
    def program_project( self ):
        if not self.__program_project == '':
            return self.__program_project
        else:
            return 'NS'

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name
        self.__goal = list( code )[ 0 ]
        self.__objective = list( code )[ 1:3 ]
        self.__npm = list( code )[ 3 ]
        self.__program_project = list( code )[ 4:6 ]

    def __str__( self ):
        if not self.__code == '':
            return self.__code
