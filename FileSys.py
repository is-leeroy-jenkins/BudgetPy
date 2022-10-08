import io
from datetime import datetime, date
import os
import zipfile as zp
import openpyxl as xl
from openpyxl import Workbook
from Booger import Error, ErrorDialog
from openpyxl.chart import ( AreaChart, AreaChart3D, BarChart, BarChart3D,
                             Reference, Series, PieChart,  PieChart3D,
                             ProjectedPieChart, LineChart, LineChart3D )
from openpyxl.chart.series import DataPoint
from openpyxl.styles import ( NamedStyle, PatternFill, Border, Side,
                              Protection, Font, Fill, Color,
                              GradientFill, Alignment )
from openpyxl.formatting import Rule
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.comments import Comment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import units
from Static import Source, Provider, SQL, Model, EXT
import enum
import sys
from sys import exc_info

# Path( filepath )
class Path( ):
    ''' Path( filename ) initializes the
    Path class providing selectedpath information of getsubfolders
    used in the application'''
    __name = None
    __input = None
    __ext = None
    __currdir = None
    __report = None
    __drive = None
    __pathsep = None
    __extsep = None
    __drivesep = None
    __parentdirectory = None

    @property
    def name( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ):
            self.__input = value

    @property
    def path( self ):
        if isinstance( self.__input, str ) and self.__input != '':
            return self.__input

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and value != '':
            self.__input = value

    @property
    def drive( self ):
        if isinstance( self.__drive, str ) and self.__drive != '':
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if isinstance( value, str ):
            self.__drive = os.path.splitdrive( value )[ 0 ]

    @property
    def extension( self ):
        if  isinstance( self.__ext, str ):
            return str( self.__ext )

    @extension.setter
    def extension( self, value ):
        if  isinstance( value, str ):
            self.__ext = str( value )

    @property
    def currentdirectory( self ):
        if os.path.exists( self.__currdir ):
            return self.__currdir

    @currentdirectory.setter
    def currentdirectory( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if os.path.exists( value ):
            os.chdir( value )
            self.__currdir = value

    @property
    def parentdirectory( self ):
        if isinstance( self.__parentdirectory, str ) and self.__parentdirectory != '':
            return self.__parentdirectory

    @parentdirectory.setter
    def parentdirectory( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if isinstance( value, str ):
            self.__parentdirectory = value

    @property
    def pathseparator( self ):
        if isinstance( self.__pathsep, str ):
            return self.__pathsep

    @pathseparator.setter
    def pathseparator( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if isinstance( value, str ):
            self.__pathsep = value

    @property
    def driveseparator( self ):
        if isinstance( self.__drivesep, str ):
            return self.__drivesep

    @driveseparator.setter
    def driveseparator( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if isinstance( value, str ):
            self.__drivesep = value

    @property
    def extensionseparator( self ):
        if isinstance( self.__extsep, str ):
            return self.__extsep

    @extensionseparator.setter
    def extensionseparator( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if isinstance( value, str ):
            self.__extsep = value

    def __init__( self, filepath ):
        self.__input = filepath if isinstance( filepath, str ) else None
        self.__name = os.path.split( filepath )[ 1 ] if isinstance( filepath, str ) else None
        self.__currdir = os.getcwd( )
        self.__ext = os.path.splitext( filepath )[ 1 ] if isinstance( filepath, str ) else None
        self.__parentdirectory = os.path.split( filepath )[ 0 ]
        self.__report = r'etc\templates\report\Excel.xlsx'
        self.__pathsep = os.path.sep
        self.__extsep = os.extsep
        self.__drivesep = ':\\'
        self.__drive = os.path.splitdrive( filepath )[ 0 ] if os.path.ismount( filepath ) \
            else os.path.splitdrive( os.path.join( self.__currdir, filepath ) )[ 0 ]

    def __str__( self ):
       if self.__input is not None:
           return str( self.__input )

    def exists( self ):
        '''Method returning a boolean value indicating whether or not the
        internal 'self.__input' exists'''
        try:
            if os.path.exists( self.__input ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'exists( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isfolder( self ):
        '''Method returning boolean value indicating whether
        or not self.__input is a folder'''
        try:
            if os.path.isdir( self.__input ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'isfolder( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isfile( self ):
        '''Method returning boolean value indicating whether
        or not self.__input is a file'''
        try:
            if os.path.isfile( self.__input ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'isfile( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isabsolute( self ):
        '''Method to determine if the input path is an
        absolute file path'''
        try:
            if isinstance( self.__input, str ) and self.__input != '':
                if os.path.isabs( self.__input ) == True:
                    return True
                elif os.path.isabs( self.__input ) == False:
                    return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'isabsolute( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isrelative( self ):
        '''Method to determine if the input path is an
        relative file path'''
        try:
            if isinstance( self.__input, str ) and self.__input != '':
                if os.path.isabs( self.__input ) == True:
                    return False
                elif os.path.isabs( self.__input ) == False:
                    return True
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'isrelative( self )'
            err = ErrorDialog( exc )
            err.show( )

    def verify( self, other ):
        '''Method returns a boolean value indicating if
        the external path 'other' exists'''
        try:
            if os.path.exists( other ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'verify( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getextension( self, other ):
        '''Returns string representing the file extension of 'other' '''
        try:
            if isinstance( other, str ) and os.path.exists( other ):
                return  os.path.splitext( other )[ 1 ]
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'getextension( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getreportpath( self, ext = EXT.XLSX ):
        '''Method returns string representing the relative path
        to the report template
        '''
        try:
            if isinstance( self.__report, str ):
                return self.__report
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'getreportpath( self )'
            err = ErrorDialog( exc )
            err.show( )

    def join( self, first, second ):
        ''' Method concatenates the path provided by the argument 'first'
        to the path provided by argument 'second' '''
        try:
            if os.path.exists( first ) and os.path.exists( second ):
                return os.path.join( first, second )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'join( self, first, second )'
            err = ErrorDialog( exc )
            err.show( )


# File( filepath )
class File( Path ):
    '''File( selectedpath ) initializes the
     File Class providing file information for
     getsubfolders used in the application'''
    __absolute = None
    __name = None
    __input = None
    __size = None
    __extension = None
    __directory = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __currdir = None
    __contents = [ ]

    @property
    def name( self ):
        '''Get the title property'''
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, value ):
        '''Set the title property'''
        if os.path.exists( value ):
            self.__name = os.path.basename( value )

    @property
    def path( self ):
        if isinstance( self.__input, str ) and self.__input != '':
            return self.__input

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and value != '':
            self.__input = value

    @property
    def absolute( self ):
        if isinstance( self.__absolute, str ) and self.__absolute != '':
            return self.__absolute

    @absolute.setter
    def absolute( self, value ):
        if isinstance( value, str ) and value != '':
            self.__absolute = value

    @property
    def size( self ):
        if isinstance( self.__size, int ):
            return self.__size

    @size.setter
    def size( self, value ):
        if isinstance( value, int ):
            self.__size = value

    @property
    def directory( self ):
        if self.__directory is not None:
            return self.__directory

    @directory.setter
    def directory( self, value ):
        if os.path.isdir( value ):
            self.__directory = str( os.path.dirname( value ) )

    @property
    def extension( self ):
        if isinstance( self.__extension, str ) and self.__extension != '':
            return self.__extension

    @extension.setter
    def extension( self, value ):
        if isinstance( value, str ) and value != '':
            self.__extension = value

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if os.path.ismount( value ):
            self.__drive = str( value )

    @property
    def modified( self ):
        if isinstance( self.__modified, datetime ):
            return self.__modified

    @modified.setter
    def modified( self, value ):
        if isinstance( value, float ):
            self.__modified = value

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @accessed.setter
    def accessed( self, value ):
        if isinstance( value, float ):
            self.__accessed = value

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    @created.setter
    def created( self, value ):
        if isinstance( value, float ):
            self.__created = value

    @property
    def current( self ):
        if os.path.exists( self.__currdir ):
            return str( self.__currdir )

    @current.setter
    def current( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if os.path.exists( value ) and os.path.isdir( value ):
            os.chdir( value )
            self.__currdir = value

    def __init__( self, filepath = None ):
        super( ).__init__( filepath )
        self.__absolute = filepath if os.path.isabs( filepath ) else os.getcwd( ) +'\\' + filepath
        self.__input = filepath if not os.path.isabs( filepath ) else os.path.relpath( filepath )
        self.__name = os.path.basename( filepath )
        self.__size = os.path.getsize( filepath )
        self.__directory = os.path.dirname( filepath )
        self.__extension = list( os.path.splitext( filepath ) )[ 1 ]
        self.__created = os.path.getctime( filepath )
        self.__accessed = os.path.getatime( filepath )
        self.__modified = os.path.getmtime( filepath )
        self.__currdir = os.getcwd( )
        self.__drive = super( ).drive

    def __str__( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    def exists( self ):
        if isinstance( self.__path, str ) and os.path.exists( self.__path ):
            return True
        else:
            return False

    def rename( self, other ):
        '''Renames the currentdirectory file to 'other' '''
        try:
            if isinstance( other, str ) and not other == '':
                src = os.path.abspath( self.__path )
                dst = os.path.join( self.directory, other )
                os.rename( src, dst )
                return dst
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'rename( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def move( self, destination ):
        '''renames currentdirectory file'''
        try:
            if os.path.isdir( destination ):
                return os.path.join( self.__name, destination )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'move( self, destination )'
            err = ErrorDialog( exc )
            err.show( )

    def create( self, other, lines = None ):
        ''' creates and returns 'selectedpath' file '''
        try:
            if isinstance( other, str ):
                newfile = open( other, 'r+' )
                if isinstance( lines, list ) and len( lines ) > 0:
                    for line in lines:
                        newfile.write( line )

                    newfile.flush( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'create( self, other, lines = None )'
            err = ErrorDialog( exc )
            err.show( )

    def verify( self, other ):
        '''determines if an external file exists'''
        try:
            if other is not None:
                return os.path.exists( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'verify( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def delete( self, other ):
        ''' deletes file at 'self.__selecteditem'   '''
        try:
            if os.path.isfile( other ):
                os.remove( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'delete( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getsize( self, other ):
        '''gets the size of another file'''
        try:
            if self.__path is not None and os.path.isfile( other ):
                return os.path.getsize( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'getsize( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getdrive( self, other ):
        '''gets the drive of another file'''
        try:
            if os.path.exists( other ):
                return str( list( os.path.splitdrive( other ) )[ 0 ] )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'getdrive( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getextension( self, other ):
        ''' gets and returns extension of 'selectedpath' 'file' '''
        try:
            if other is not None and os.path.isfile( other ):
                return str( list( os.path.splitext( other ) )[ 1 ] )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'getextension( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def readlines( self, other ):
        '''reads all lines in 'other' into a list
            then returns the list '''
        try:
            if os.path.isfile( other ):
                file = open( other, 'r' )
                contents = file.readlines( )
                file.close( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'realines( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def readall( self, other ):
        '''reads a single line from the file into a string
            then returns the string'''
        try:
            contents = ''
            if os.path.isfile( other ):
                file = open( other, 'r' )
                contents = file.read( )
                file.close( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'readall( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def writelines( self, lines = None ):
        ''' writes the contents of 'lines' to self.__contents '''
        try:
            if isinstance( lines, list ):
                path = os.path.relpath( self.__path )
                contents = open( path, 'a' )
                for line in lines:
                    contents.write( line )
                contents.flush( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'writelines( self, lines = None )'
            err = ErrorDialog( exc )
            err.show( )

    def writeall( self, other ):
        ''' writes the contents of 'lines' to self.__contents '''
        try:
            contents = [ ]
            lines = [ ]
            if os.path.isfile( other ):
                path = os.path.relpath( self.__path )
                contents = open( path, 'a' )
                lines = open( other, 'r' )
                for line in lines.readlines( ):
                    contents.write( line )
                contents.flush( )
                lines.close( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'File'
            exc.method = 'writeall( self, other )'
            err = ErrorDialog( exc )
            err.show( )


# Folder( dirpath )
class Folder( ):
    '''Folder( selectedpath ) initializes the
     Folder Class providing file directory information'''
    __absolute = None
    __relative = None
    __path = None
    __name = None
    __parent = None
    __dir = None
    __drive = None
    __current = None

    @property
    def name( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if os.path.exists( self.__path ):
            return str( list( os.path.split( self.__path ) )[ 1 ] )

    @name.setter
    def name( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ):
            self.__path = value

    @property
    def directory( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @directory.setter
    def directory( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if os.path.isdir( value ):
            self.__name = value

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, value ):
        if os.path.exists( value ):
            self.__path = str( value )

    @property
    def absolute( self ):
        if isinstance( self.__absolute, str ) and self.__absolute != '':
            return self.__absolute

    @absolute.setter
    def absolute( self, value ):
        if os.path.exists( value ) and os.path.isabs( value ):
            self.__absolute = value

    @property
    def relative( self ):
        if isinstance( self.__relative, str ) and self.__relative != '':
            return self.__relative

    @relative.setter
    def relative( self, value ):
        if isinstance( self.__relative, str ) and not os.path.isabs( value ):
            self.__relative = value

    @property
    def parent( self ):
        if self.__parent is not None:
            return self.__parent

    @parent.setter
    def parent( self, value ):
        if os.path.isdir( value ):
            self.__parent = str( value )

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if os.path.ismount( value ):
            self.__drive = str( value )

    @property
    def current( self ):
        if self.__current is not None:
            return self.__current

    @current.setter
    def current( self, value ):
        if os.path.exists( value ):
            os.chdir( value )

    def __init__( self, dirpath ):
        self.__current = os.getcwd( )
        self.__path = dirpath
        self.__name = os.path.basename( dirpath )
        self.__parent = os.path.dirname( dirpath )
        self.__absolute = self.__path if os.path.isabs( dirpath ) else None
        self.__relative = self.__path if not os.path.isabs( dirpath ) \
            else f'{ os.getcwd( ) }\\{ self.__name }'

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def getfiles( self ):
        '''Iterates subfolders in the base directory
        and returns a list of subfile paths'''
        try:
            current = self.__current
            abspath = self.__absolute
            filenames = [ ]
            for i in os.listdir( abspath ):
                path = os.path.join( abspath, i )
                if os.path.isfile( path ):
                    filenames.append( path )
            return filenames
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'getfiles( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getsubfiles( self ):
        '''Iterates getsubfolders in the base directory'''
        try:
            current = self.__current
            abspath = self.__absolute
            filenames = [ ]
            for i in os.walk( abspath ):
                dirpath = i[ 0 ]
                if len( i[ 1 ] ) > 0:
                    for name in i[ 1 ]:
                        path = os.path.join( dirpath, name )
                        filenames.append( path )
            return filenames
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'getsubfolders( self )'
            err = ErrorDialog( exc )
            err.show( )

        return filenames

    def getsubfolders( self ):
        '''Iterates getsubfolders in the base directory'''
        try:
            current = self.__current
            abspath = self.__absolute
            filenames = [ ]
            for i in os.walk( abspath ):
                if len( i[ 1 ] ) > 0:
                    for file in i[ 1 ]:
                        path = os.path.join( abspath, file )
                        if os.path.isdir( path ):
                            filenames.append( path )
            return filenames
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'getsubfolders( self )'
            err = ErrorDialog( exc )
            err.show( )

        return filenames

    def rename( self, new_name ):
        '''renames currentdirectory file'''
        try:
            if self.__name is not None and isinstance( new_name, str ):
                return os.rename( self.__name, new_name )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'rename( self, new_name )'
            err = ErrorDialog( exc )
            err.show( )

    def move( self, destination ):
        '''renames currentdirectory file'''
        try:
            if not destination == '' and not os.path.exists( destination ):
                return os.path.join( self.__name, destination )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'move( self, destination )'
            err = ErrorDialog( exc )
            err.show( )

    def exists( self, other ):
        '''determines if the base file exists'''
        try:
            if not other == '' and os.path.isdir( other ):
                return True
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'exists( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def create( self, other ):
        try:
            if other is not None:
                os.mkdir( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'create( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def delete( self, other ):
        ''' deletes 'selectedpath' directory '''
        try:
            if other is not None and os.path.isdir( other ):
                os.rmdir( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'delete( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getsize( self, other ):
        ''' gets and returns size of 'selectedpath' '''
        try:
            if other is not None and os.path.isdir( other ):
                return os.path.getsize( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = ''
            err = ErrorDialog( exc )
            err.show( )

    def getdrive( self, other ):
        ''' gets and returns parent directory of 'selectedpath' '''
        try:
            if other is not None and os.path.isdir( other ):
                return os.path.splitdrive( other )[ 0 ]
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'getdrive( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def iterate( self ):
        '''iterates getsubfolders in the base directory'''
        try:
            for i in os.walk( self.__path ):
                yield i
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'iterate( self )'
            err = ErrorDialog( exc )
            err.show( )


# Message( sender, receiver, body, subject, copy )
class Message( ):
    '''Message( frm, to, body, subject ) initializes
    class providing email behavior '''
    __sender = None
    __receiver = None
    __subject = None
    __body = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if self.__sender is not None:
            return self.__sender

    @sender.setter
    def sender( self, value ):
        ''' Set the sender's email address '''
        if value is not None:
            self.__sender = str( value )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__receiver is not None:
            return [ self.__receiver, ]

    @receiver.setter
    def receiver( self, value ):
        ''' Sets the receiver's email address '''
        if value is not None:
            self.__receiver = str( value )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__receiver = str( value )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__body is not None:
            return self.__body

    @body.setter
    def body( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__receiver = str( value )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, value ):
        ''' Sets the address's to send copies  '''
        if value is not None:
            self.__others = list( value )

    def __init__( self, sender, receiver, body, subject, copy = '' ):
        self.__sender = sender if isinstance( sender, str ) and sender != '' else None
        self.__receiver = receiver if isinstance( receiver, str ) and receiver != '' else None
        self.__body = body if isinstance( body, str ) and body != '' else None
        self.__others = copy if isinstance( copy, list ) and len( copy ) > 0 else None
        self.__subject = subject if isinstance( subject, str ) and subject != '' else None

    def __str__( self ):
        if isinstance( self.__body, str ) and self.__body != '':
            return self.__body


# Emai( sender, receiver, body, subject, copy )
class Email( Message ):
    '''Email( frm, to, body, subject ) initializes
    class providing email behavior '''

    def __init__( self, sender, receiver, body, subject, copy = '' ):
        super( ).__init__( sender, receiver, body, subject, copy )
        self.__sender = super( ).sender
        self.__receiver = super( ).receiver
        self.__body = super( ).body
        self.__others = super( ).copy
        self.__subject = super( ).subject


# MessageBuilder(  )
class MessageBuilder( ):
    ''' Helper class for generating email messages '''
    __from = None
    __to = None
    __subject = None
    __body = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if isinstance( self.__from, str ) and self.__from != '':
            return self.__from

    @sender.setter
    def sender( self, value ):
        ''' Set the sender's email address '''
        if isinstance( value, str ) and value != '':
            self.__from = value

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if isinstance( self.__to, str ) and self.__to != '':
            return self.__to

    @receiver.setter
    def receiver( self, value ):
        ''' Sets the receiver's email address '''
        if isinstance( value, str ) and value != '':
            self.__to = value

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if isinstance( self.__subject, str ) and self.__subject != '':
            return self.__subject

    @subject.setter
    def subject( self, value ):
        ''' Sets the email's subject line '''
        if isinstance( value, str ) and value != '':
            self.__subject = value

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if isinstance( self.__body, str ) and self.__body != '':
            return self.__body

    @body.setter
    def body( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__to = str( value )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if isinstance( self.__others, list ):
            return self.__others

    @copy.setter
    def copy( self, value ):
        ''' Sets the address's to send copies  '''
        if value is not None:
            self.__others = list( value )

    def __init__( self, sender = '', receiver = '', body = '', copy = '', subject = ''):
        self.__from = sender if isinstance( sender, str ) and sender != '' else None
        self.__to = receiver if isinstance( receiver, str ) and receiver != '' else None
        self.__body = body if isinstance( body, str ) and body != '' else None
        self.__others = copy if isinstance( copy, str ) and copy != '' else None
        self.__subject = subject if isinstance( subject, str ) and subject != '' else None

    def __str__( self ):
        if self.__body is not None:
            return self.__body


# Document( )
class Document( ):
    '''Excel( selectedpath ) class provides
    the spreadsheet for Budget Py reports '''
    __path = None
    __name = None
    __title = None

    @property
    def path( self ):
        ''' Get the title of the workbook '''
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and value != '':
            self.__path = value

    @property
    def name( self ):
        ''' Get the title of the workbook '''
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None and len( value ) > 0:
            self.__name = str( value )

    def __init__( self, fullpath ):
        self.__path = fullpath if isinstance( fullpath, str ) else None
        self.__name = os.path.split( fullpath )[ 1 ] if isinstance( fullpath, str ) else None
        self.__title = self.__name
        self.__workbook = Workbook( )
        self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

    def __str__( self ):
        if self.__path is not None:
            return self.__path


# Excel( fullpath )
class Excel( ):
    '''Excel( selectedpath ) class provides
    the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __title = None

    @property
    def path( self ):
        ''' Get the title of the workbook '''
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and value != '':
            self.__path = value

    @property
    def name( self ):
        ''' Get the title of the workbook '''
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None and len( value ) > 0:
            self.__name = str( value )

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if isinstance( self.__workbook, Workbook ):
            return self.__workbook

    @workbook.setter
    def workbook( self, value ):
        ''' Gets the report template '''
        if isinstance( value, Workbook ):
            self.__workbook = value

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if isinstance( self.__workbook, Workbook ):
            return self.__workbook.active

    @worksheet.setter
    def worksheet( self, value ):
        ''' Gets the workbooks worksheet '''
        if isinstance( value, Workbook ):
            self.__name = value.active

    def __init__( self, fullpath ):
        self.__path = fullpath if isinstance( fullpath, str ) else None
        self.__name = os.path.split( fullpath )[ 1 ] if isinstance( fullpath, str ) else None
        self.__title = self.__name
        self.__workbook = Workbook( )
        self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def save( self ):
        try:
            if isinstance( self.__workbook, Workbook ):
                self.__workbook.save( self.__path )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Excel'
            exc.method = 'save( self )'
            err = ErrorDialog( exc )
            err.show( )


# ExcelReport( title, rows = 46, cols = 12 )
class ExcelReport( ):
    '''ExcelReport( title ) class provides
    the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __rows = None
    __columns = None
    __dimensions = None

    @property
    def name( self ):
        ''' Get the title of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None and len( value ) > 0:
            self.__name = str( value )

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if isinstance( value, int ) and value > 0:
            self.__rows = value

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, int ) and value > 0:
            self.__columns = value

    @property
    def dimensions( self ):
        if self.__dimensions is not None:
            return self.__dimensions

    @dimensions.setter
    def dimensions( self, value ):
        if isinstance( value, tuple ) and len( value ) <= 2:
            self.__dimensions = value

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = xl.open( self.__path )
            return self.__workbook

    @workbook.setter
    def workbook( self, value ):
        ''' Gets the report template '''
        if value is not None and os.path.exists( value ):
            self.__workbook = xl.open( value )

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__worksheet is not None:
            return self.__worksheet

    @worksheet.setter
    def worksheet( self, value ):
        ''' Gets the workbooks worksheet '''
        if self.__workbook is not None and value is not None:
            self.__workbook.worksheets.clear( )
            self.__worksheet = self.__workbook.create_sheet( title = value, index = 1 )

    def __init__( self, name, rows = 46, cols = 12 ):
        self.__path = r'etc/templates/report/Excel.xlsx'
        self.__name = name if isinstance( name, str ) and name != '' else None
        self.__rows = rows if isinstance( rows, int ) and rows > -1 else None
        self.__columns = cols if isinstance( cols, int ) and cols > -1 else None
        self.__dimensions = (self.__rows, self.__columns)


# ZipFile( selectedpath )
class ZipFile( ):
    __infile = None
    __name = None
    __filepath = None
    __extension = None
    __zippath = None
    __zipextension = None

    @property
    def path( self ):
        if not self.__filepath == '':
            return self.__filepath

    @path.setter
    def path( self, value ):
        if os.path.exists( value ) and os.path.isfile( value ):
            self.__filepath = value

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, value ):
        if not value == '':
            self.__name = value

    def __init__( self, filepath ):
        self.__infile = filepath if isinstance( filepath, str ) and filepath != '' else None
        self.__zipextension = '.zip'
        self.__filepath = filepath if os.path.isfile( filepath ) else None
        self.__extension = os.path.splitext( filepath )
        self.__zippath = self.__filepath.replace( self.__extension, self.__zipextension )
        self.__name = os.path.basename( filepath )

    def create( self ):
        ''' Creates zip file'''
        try:
            if not self.__filepath == '':
                zp.ZipFile( self.__zippath, 'w' ).write( self.__filepath, self.__name )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'ZipFile'
            exc.method = 'create( self )'
            err = ErrorDialog( exc )
            err.show( )


    def unzip( self ):
        ''' Extracts zip file contents '''
        try:
            if os.path.exists( self.__zippath ):
                file = zp.ZipFile( self.__zippath )
                file.extractall( self.__zippath )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'ZipFile'
            exc.method = 'unzip( self )'
            err = ErrorDialog( exc )
            err.show( )
