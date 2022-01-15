import os

class BudgetPath():
    '''Defines the BudgetPath class'''
    __base = None
    __path = None
    __ext = None
    __report = None

    @property
    def base( self ):
        if self.__base is not None:
            return self.__base

    @base.setter
    def base( self, path ):
        if path is not None and os.path.exists( path ):
            self.__base = str( path )

    @property
    def name( self ):
        '''Returns string representing the name of the path 'base' '''
        if os.path.exists( self.__base ):
            return str( list( os.path.split( self.__base ) )[ 1 ] )

    @name.setter
    def name( self, path ):
        '''Returns string representing the name of the path 'base' '''
        if path is not None and os.path.exists( path ):
            self.__path = str( list( os.path.split( self.__base ) )[ 1 ] )

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, base ):
        if os.path.exists( base ) is not None:
            self.__path = str( base )

    @property
    def exists( self ):
        if os.path.exists( self.__path ):
            return True

    @property
    def isfolder( self ):
        if os.path.isdir( self.__path ):
            return True

    @property
    def isfile( self ):
        if os.path.exists( self.__path ) and os.path.isfile( self.__path ):
            return True

    @property
    def extension( self ):
        if self.__ext is not None:
            return str( self.__ext )

    @extension.setter
    def extension( self, ext ):
        if ext is not None:
            self.__ext = str( ext )

    def verify( self, other ):
        '''Verifies if the parameter 'other' exists'''
        if os.path.exists( other ):
            return True

    def verify_file( self, other ):
        if os.path.isfile( other ):
            return True

    def verify_folder( self, other ):
        if os.path.isdir( other ):
            return True

    def get_extension( self, other ):
        '''Returns string representing the file extension of 'other' '''
        if os.path.exists( other ):
            return list( os.path.splitext( other ) )[ 1 ]

    def get_report( self ):
        if self.__report is not None:
            return self.__report

    def join( self, first, second ):
        ''' Concatenates 'first' to 'second' '''
        if os.path.exists( first ) and os.path.exists( second ):
            return os.path.join( first, second )

    def __init__( self, filepath ):
        self.__base = str( filepath )
        self.__path = self.__base
        self.__ext = os.path.split( self.__path )
        self.__report = r'etc\templates\report\ReportBase.xlsx'


