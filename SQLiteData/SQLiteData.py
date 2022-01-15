import sqlite3 as sl
import pandas as pd

class SQLiteData():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __connstr = None
    __data = None
    __source = None
    __query = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstr( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if isinstance( self.__data, pd.DataFrame ):
            return self.__data

    @data.setter
    def data( self, dframe ):
        if isinstance( dframe, pd.DataFrame ):
            self.__data = dframe

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\\sqlite\\datamodels\Data.db'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def get_connection( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr )

