class Activity():
    '''Defines the Activity Class'''
    __code = ''
    __name = ''

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code
