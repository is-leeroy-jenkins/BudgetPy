import sqlite3 as sl
import pandas as pd

class SQLiteReference():
    '''Class representing the budget execution reference models'''
    __source = None
    __dbpath = None
    __connstr = None
    __data = None
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
    def source( self, src ):
        if src is not None:
            self.__source = str( src )

    @property
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\sqlite\referencemodels\References.db'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
        self.__data = [ ]

    def get_connection( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr )


