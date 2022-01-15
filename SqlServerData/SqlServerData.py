import pandas as pd

class SqlServerData():
    '''Builds the budget execution data classes'''
    __source = None
    __dbpath = None
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
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstring( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstring.setter
    def connstring( self, conn ):
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

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\mssql\datamodels\Data.mdf'
        self.__data = pd.DataFrame

