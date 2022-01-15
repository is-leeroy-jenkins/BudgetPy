import datetime as dt
import os

class BudgetFile():
    '''Defines the BudgetFile Class'''
    __base = None
    __name = None
    __path = None
    __size = None
    __extension = None
    __directory = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __current = None
    __content = [ ]

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
        if os.path.isdir( self.__name ):
            return str( os.path.dirname( self.__path ) )

    @name.setter
    def name( self, path ):
        if os.path.exists( path ):
            self.__name = str( os.path.basename( path ) )

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
    def directory( self ):
        if self.__directory is not None:
            return self.__directory

    @directory.setter
    def directory( self, path ):
        if os.path.isdir( path ):
            self.__directory = str( os.path.dirname( path ) )

    @property
    def extension( self ):
        if self.__extension is not None:
            return self.__extension

    @extension.setter
    def extension( self, ext ):
        if ext is not None:
            self.__extension = str( ext )

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
        self.__base = str( base )
        self.__path = self.__base
        self.__name = os.path.basename( base )
        self.__size = os.path.getsize( base )
        self.__directory = str( os.path.dirname( self.__path ) )
        self.__extension = str( list( os.path.splitext( base ) )[ 1 ] )
        self.__created = os.path.getctime( base )
        self.__accessed = os.path.getatime( base )
        self.__modified = os.path.getmtime( base )
        self.__current = os.getcwd()
        self.__drive = str( list( os.path.splitdrive( self.__path ) )[ 0 ] )
        self.__content = list()

    def rename( self, other ):
        '''renames current file'''
        if self.__base is not None and self.__name is not None:
            return os.rename( self.__name, other )

    def move( self, destination ):
        '''renames current file'''
        if self.__base is not None and os.path.exists( self.__base ):
            return os.path.join( self.__name, destination )

    def create( self, other ):
        ''' creates and returns 'path' file '''
        if other is not None:
            os.mkdir( other )

    def exists( self, other ):
        '''determines if an external file exists'''
        if other is not None:
            return os.path.exists( other )

    def delete( self, other ):
        ''' deletes file at 'self.__path'   '''
        if other is not None and os.path.isfile( other ):
            os.remove( other )

    def getsize( self, other ):
        '''gets the size of another file'''
        if self.__base is not None and os.path.exists( other ):
            return os.path.getsize( other )

    def getdrive( self, other ):
        '''gets the drive of another file'''
        if os.path.exists( other ):
            return str( list( os.path.splitdrive( other ) )[ 0 ] )

    def getextension( self, other ):
        ''' gets and returns extension of 'path' 'file' '''
        if other is not None and os.path.isfile( other ):
            return str( list( os.path.splitext( other ) )[ 1 ] )

    def readlines( self, other ):
        '''reads all lines in 'path' into a list
            then returns the list '''
        lines = [ ]
        count = len( self.__content )
        if other is not None and os.path.isfile( other ):
            file = open( other, 'r' )
            for line in file.readlines():
                lines.append( line )
            self.__content.append( lines )
        if len( lines ) > 0 and len( self.__content ) > count:
            return lines

    def readline( self, other ):
        '''reads a single line from the file into a string
            then returns the string'''
        count = len( self.__content )
        if other is not None and os.path.isfile( other ):
            line = open( self.__path, 'r' ).readline()
            self.__content.append( line )
            if len( self.__content ) > count:
                return line

    def writelines( self, lines = None ):
        ''' writes the contents of 'lines' to self.__content '''
        if os.path.isfile( self.__path ) and isinstance( lines, list ):
            for line in lines:
                self.__content.append( open( self.__path, 'w' ).write( line ) )
