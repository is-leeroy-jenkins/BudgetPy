class Objective():
    '''Defines the Objective Class'''
    __code = None
    __name = None
    __data = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'code' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'code': self.__code }

    def __str__( self ):
        return self.__code



