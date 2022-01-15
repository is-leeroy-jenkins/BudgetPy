import os
import datetime as dt

class BudgetFolder():
    '''Defines the BudgetFolder Class'''
    # pseudo-private backing fields
    __base = None
    __name = None
    __path = None
    __size = None
    __parent = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __current = None

    @property
    def base( self ):
        if self.__base is not None:
            return self.__base

    @base.setter
    def base( self, path ):
        if path is not None:
            self.__base = str( path )

    @property
    def name( self ):
        '''Returns string representing the name of the path 'base' '''
        if os.path.exists( self.__base ):
            return str( list( os.path.split( self.__base ) )[ 1 ] )

    @name.setter
    def name( self, path ):
        '''Returns string representing the name of the path 'base' '''
        if path is not None:
            self.__path = str( list( os.path.split( self.__base ) )[ 1 ] )

    @property
    def path( self ):
        if os.path.isdir( self.__path ):
            return str( self.__path )

    @path.setter
    def path( self, base ):
        if os.path.exists( base ):
            self.__path = str( base )

    @property
    def size( self ):
        if self.__base is not None:
            return float( self.__size )

    @size.setter
    def size( self, num ):
        if num is not None:
            self.__size = float( num )

    @property
    def parent( self ):
        if self.__parent is not None:
            return self.__parent

    @parent.setter
    def parent( self, path ):
        if os.path.isdir( path ):
            self.__parent = str( path )

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, path ):
        if os.path.ismount( path ):
            self.__drive = str( path )

    @property
    def modified( self ):
        if self.__modified is not None:
            return self.__modified

    @modified.setter
    def modified( self, yr, mo = 1, dy = 1 ):
        if dt.date( yr, mo, dy ):
            self.__modified = dt.date( yr, mo, dy )

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @accessed.setter
    def accessed( self, yr, mo = 1, dy = 1 ):
        if dt.date( yr, mo, dy ):
            self.__accessed = dt.date( yr, mo, dy )

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    @created.setter
    def created( self, yr, mo = 1, dy = 1 ):
        if dt.date( yr, mo, dy ):
            self.__created = dt.date( yr, mo, dy )

    @property
    def current( self ):
        if self.__current is not None:
            return self.__current

    @current.setter
    def current( self, path ):
        if os.path.exists( path ):
            os.chdir( path )

    # Constructor
    def __init__( self, base ):
        self.__base = base
        self.__name = str( os.path.basename( base ) )
        self.__path = str( os.path.abspath( base ) )
        self.__size = int( os.path.getsize( base ) )
        self.__created = float( os.path.getctime( base ) )
        self.__accessed = float( os.path.getatime( base ) )
        self.__modified = float( os.path.getmtime( base ) )
        self.__parent = str( os.path.dirname( base ) )

    def rename( self, new_name ):
        '''renames current file'''
        if self.__name is not None and new_name is not None:
            return os.rename( self.__name, new_name )

    def move( self, destination ):
        '''renames current file'''
        if self.__name is not None and destination is not None:
            return os.path.join( self.__name, destination )

    def exists( self, other ):
        '''determines if the base file exists'''
        if other is not None and os.path.isdir( other ):
            return True

    def create( self, other ):
        if other is not None:
            os.mkdir( other )

    def delete( self, other ):
        ''' deletes 'path' directory '''
        if other is not None and os.path.isdir( other ):
            os.rmdir( other )

    def get_size( self, other ):
        ''' gets and returns size of 'path' '''
        if other is not None and os.path.isdir( other ):
            return os.path.getsize( other )

    def get_drive( self, other ):
        ''' gets and returns parent directory of 'path' '''
        if other is not None and os.path.isdir( other ):
            return os.path.splitdrive( other )[ 0 ]

