import pandas as pd

class WorkCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

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

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code
