import pandas as pd

class SqlServerReference():
    '''Class representing the budget execution reference models'''
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
    def source( self, src ):
        if src is not None:
            self.__source = str( src )

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
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\mssql\referencemodels\References.mdf'
        self.__data = pd.DataFrame
