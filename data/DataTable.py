import pandas as pd

class DataTable():
    '''Defines the DataTable Class'''
    __name = None
    __data = { }
    __rows = pd.DataFrame
    __columns = pd.Series
    __schema = { }
    __query = None

    @property
    def name( self ):
        return self.__name

    @property
    def data( self ):
        return self.__data

    def __init__( self, name, sql = ''  ):
        self.__name = name
        self.__query = sql

    def __str__(self):
        return self.__name

    def get_sql( self ):
        return self.__query

    def get_source( self ):
        return self.__name

    def get_datarows( self ):
        return self.__rows

    def get_datacolumns( self ):
        return self.__columns

    def get_schema( self ):
        return self.__schema