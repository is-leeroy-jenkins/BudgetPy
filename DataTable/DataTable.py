import pandas as pd

class DataTable( pd.DataFrame ):
    '''Defines the DataTable Class'''
    __base = None
    __name = None
    __data = None
    __columns = None
    __records = None

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dataframe ):
        if isinstance( dataframe, pd.DataFrame ):
            self.__data = pd.DataFrame( dataframe )

    @property
    def schema( self ):
        if self.__columns is not None:
            return self.__columns

    @schema.setter
    def schema( self, columns ):
        if isinstance( columns, dict ):
            self.__columns = pd.Series( columns ).index

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    def __init__( self, name ):
        super().__init__()
        self.__base = str( name )
        self.__name = self.__base
        self.__data = pd.DataFrame( self.__name )
        self.__columns = self.__data.columns
        self.__rows = self.__data.items

    def __str__( self ):
        if self.__name is not None:
            return self.__name


