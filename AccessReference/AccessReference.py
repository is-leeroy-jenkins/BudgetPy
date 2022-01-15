import pandas as pd
import pyodbc as db

class AccessReference():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __driver = None
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
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data[ 0: ] = dframe

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver )

    @driver.setter
    def driver( self, name ):
        if name is not None:
            self.__driver = name

    def __init__( self, table = None ):
        self.__source = table
        self.__driver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db\access' \
            r'\referencemodels\References.accdb;'
        self.__connstr = f'{ self.__driver } { self.__dbpath }'
        self.__data = pd.DataFrame

    def get_connection( self ):
        if self.__connstr is not None:
            return db.connect( self.__connstr )



