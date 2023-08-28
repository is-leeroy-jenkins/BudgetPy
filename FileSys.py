from datetime import datetime
import os
import zipfile as zp
import openpyxl as xl
from openpyxl import Workbook
from Booger import Error, ErrorDialog
from Static import EXT

# Path( path )
class Path( ):
    ''' Path( file_name ) initializes the
    Path class providing selected_path information of get_subfolders
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
    def input( self ):
        '''Get the input string'''
        if self.__input is not None:
            return self.__input

    @input.setter
    def input( self, value: str ):
        '''Sets the input string'''
        if value is not None:
            self.__input = value

    @property
    def name( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value: str ):
        '''Returns string representing the title of the selected_path 'base' '''
        if isinstance( value, str ):
            self.__input = value

    @property
    def path( self ):
        if self.__input is not None:
            return self.__input

    @path.setter
    def path( self, value: str ):
        if value is not None:
            self.__input = value

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, value: str ):
        if value is not None:
            self.__drive = os.path.splitdrive( value )[ 0 ]

    @property
    def extension( self ):
        if  self.__ext is not None:
            return self.__ext

    @extension.setter
    def extension( self, value: str ):
        if  value is not None:
            self.__ext = str( value )

    @property
    def current_directory( self ):
        if self.__currdir is not None:
            return self.__currdir

    @current_directory.setter
    def current_directory( self, value: str ):
        '''Set the current_directory directory to 'selected_path' '''
        if os.path.exists( value ):
            os.chdir( value )
            self.__currdir = value

    @property
    def parent_directory( self ):
        if self.__parentdirectory is not None:
            return self.__parentdirectory

    @parent_directory.setter
    def parent_directory( self, value: str ):
        '''Set the current_directory directory to 'selected_path' '''
        if value is not None:
            self.__parentdirectory = value

    @property
    def path_separator( self ):
        if self.__pathsep is not None:
            return self.__pathsep

    @path_separator.setter
    def path_separator( self, value: str ):
        '''Set the current_directory directory to 'selected_path' '''
        if value is not None:
            self.__pathsep = value

    @property
    def drive_separator( self ):
        if self.__drivesep is not None:
            return self.__drivesep

    @drive_separator.setter
    def drive_separator( self, value: str ):
        '''Set the current_directory directory to 'selected_path' '''
        if value is not None:
            self.__drivesep = value

    @property
    def extension_separator( self ):
        if self.__extsep is not None:
            return self.__extsep

    @extension_separator.setter
    def extension_separator( self, value: str ):
        '''Set the current_directory directory to 'selected_path' '''
        if value is not None:
            self.__extsep = value

    def __init__( self, filepath: str ):
        self.__input = filepath
        self.__name = os.path.split( filepath )[ 1 ]
        self.__currdir = os.getcwd( )
        self.__ext = os.path.splitext( filepath )[ 1 ]
        self.__parentdirectory = os.path.split( filepath )[ 0 ]
        self.__report = r'etc\templates\report\Excel.xlsx'
        self.__pathsep = os.path.sep
        self.__extsep = os.extsep
        self.__drivesep = ':\\'
        self.__drive = os.path.splitdrive( filepath )[ 0 ]

    def __str__( self ):
       if self.__input is not None:
           return str( self.__input )

    def exists( self ) -> bool:
        '''Method returning a boolean value indicating whether the
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

    def is_folder( self ) -> bool:
        '''Method returning boolean value indicating whether         self.__input is a folder'''
        try:
            if os.path.isdir( self.__input ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'is_folder( self )'
            err = ErrorDialog( exc )
            err.show( )

    def is_file( self ) -> bool:
        '''Method returning boolean value indicating whether         self.__input is a file'''
        try:
            if os.path.isfile( self.__input ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'is_file( self )'
            err = ErrorDialog( exc )
            err.show( )

    def is_absolute( self ) -> bool:
        '''Method to determine if the input path is an
        absolute_path file path'''
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
            exc.method = 'is_absolute_path( self )'
            err = ErrorDialog( exc )
            err.show( )

    def is_relative( self ) -> bool:
        '''Method to determine if the input path is a
        relative_path file path'''
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
            exc.method = 'is_relative_path( self )'
            err = ErrorDialog( exc )
            err.show( )

    def verify( self, other: str ) -> bool:
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

    def get_reportpath( self, ext = EXT.XLSX ) -> str:
        '''Method returns string representing the relative_path path
        to the report template
        '''
        try:
            if isinstance( self.__report, str ):
                return self.__report
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Path'
            exc.method = 'get_report_path( self )'
            err = ErrorDialog( exc )
            err.show( )

    def join( self, first: str, second: str ) -> str:
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

# File( path )
class File( Path ):
    '''File( selected_path ) initializes the
     File Class providing file information for
     get_subfolders used in the application'''
    __absolute = None
    __name = None
    __path = None
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
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        '''Set the title property'''
        if os.path.exists( value ):
            self.__name = os.path.basename( value )

    @property
    def path( self ):
        if self.__buffer is not None:
            return self.__buffer

    @path.setter
    def path( self, value ):
        if value is not None:
            self.__buffer = value

    @property
    def size( self ):
        if self.__size is not None:
            return self.__size

    @size.setter
    def size( self, value ):
        if value is not None:
            self.__size = value

    @property
    def directory( self ):
        if self.__directory is not None:
            return self.__directory

    @directory.setter
    def directory( self, value ):
        if os.path.isdir( value ):
            self.__directory = os.path.dirname( value )

    @property
    def extension( self ):
        if self.__extension is not None:
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

    def __init__( self, path = None ):
        super( ).__init__( path )
        self.__path = super( ).input
        self.__name = os.path.basename( path )
        self.__size = os.path.getsize( path )
        self.__directory = os.path.dirname( path )
        self.__extension = list( os.path.splitext( path ) )[ 1 ]
        self.__created = os.path.getctime( path )
        self.__accessed = os.path.getatime( path )
        self.__modified = os.path.getmtime( path )
        self.__drive = super( ).drive

    def __str__( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    def exists( self ):
        if os.path.exists( self.__path ):
            return True
        else:
            return False

    def rename( self, other ):
        '''Renames the current_directory file to 'other' '''
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
        '''renames current_directory file'''
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
        ''' creates and returns 'selected_path' file '''
        try:
            if other is not None:
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

# Folder( path )
class Folder( Path ):
    '''Folder( selected_path ) initializes the
     Folder Class providing file directory information'''
    __absolutepath = None
    __relativepath = None
    __path = None
    __name = None
    __parent = None
    __dir = None
    __drive = None
    __current = None
    __size = None

    @property
    def name( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__path is not None:
            return self.__path

    @name.setter
    def name( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value is not None:
            self.__path = value

    @property
    def directory( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__path is not None:
            return self.__path

    @directory.setter
    def directory( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value is not None:
            self.__name = value

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, value ):
        if value is not None:
            self.__path = value

    @property
    def absolute_path( self ):
        if self.__absolutepath is not None:
            return self.__absolutepath

    @absolute_path.setter
    def absolute_path( self, value ):
        if value is not None:
            self.__absolutepath = value

    @property
    def relative_path( self ):
        if self.__relativepath is not None:
            return self.__relativepath

    @relative_path.setter
    def relative_path( self, value ):
        if self.__relativepath is not None:
            self.__relativepath = value

    @property
    def parent( self ):
        if self.__parent is not None:
            return self.__parent

    @parent.setter
    def parent( self, value ):
        if value is not None:
            self.__parent = value

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if value is not None:
            self.__drive = value

    @property
    def size( self ):
        if self.__size is not None:
            return self.__size

    @size.setter
    def size( self, value ):
        if value is not None:
            self.__size = value

    @property
    def current( self ):
        if self.__current is not None:
            return self.__current

    @current.setter
    def current( self, value ):
        if value is not None:
            os.chdir( value )
            self.__current = os.getcwd( )

    def __init__( self, path ):
        super( ).__init__( path )
        self.__size = os.path.getsize( path )
        self.__drive = super( ).drive
        self.__current = os.getcwd( )
        self.__path = super().input
        self.__name = os.path.basename( path )
        self.__parent = os.path.dirname( path )
        self.__absolutepath = os.path.abspath( path )
        self.__relativepath = f'{ os.getcwd( ) }\\{ os.path.basename( path ) }'

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def get_files( self ) -> list:
        '''Iterates subfolders in the base directory
        and returns a list of subfile paths'''
        try:
            filenames = [ ]
            for i in os.listdir( self.__absolutepath ):
                path = os.path.join( self.__absolutepath, i )
                if os.path.isfile( path ):
                    filenames.append( path )
            return filenames
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'get_files( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_subfiles( self ) -> list:
        '''Iterates get_subfolders in the base directory'''
        try:
            current = self.__current
            abspath = self.__absolutepath
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
            exc.method = 'get_subfolders( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_subfolders( self ) -> list:
        '''Iterates get_subfolders in the base directory'''
        try:
            filenames = [ ]
            for i in os.walk( self.__absolutepath ):
                if len( i[ 1 ] ) > 0:
                    for file in i[ 1 ]:
                        path = os.path.join( self.__absolutepath, file )
                        if os.path.isdir( path ):
                            filenames.append( path )
            return filenames
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'get_subfolders( self )'
            err = ErrorDialog( exc )
            err.show( )

    def rename( self, name ):
        '''renames current_directory file'''
        try:
            if self.__name is not None and isinstance( name, str ):
                return os.rename( self.__name, name )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'Folder'
            exc.method = 'rename( self, name )'
            err = ErrorDialog( exc )
            err.show( )

    def move( self, destination ):
        '''renames current_directory file'''
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

    def exists( self ) -> bool:
        '''determines if the base file exists'''
        try:
            if os.path.isdir( self.__path ):
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
        ''' deletes 'selected_path' directory '''
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

    def iterate( self ):
        '''iterates subfolders in the base directory'''
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
    def sender( self, value: str ):
        ''' Set the sender's email address '''
        if value is not None:
            self.__sender = value

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__receiver is not None:
            return [ self.__receiver, ]

    @receiver.setter
    def receiver( self, value: str ):
        ''' Sets the receiver's email address '''
        if value is not None:
            self.__receiver = value

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, value: str ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__receiver = value

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__body is not None:
            return self.__body

    @body.setter
    def body( self, value: str ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__receiver = value

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, value: list ):
        ''' Sets the address's to send copies  '''
        if value is not None:
            self.__others = value

    def __init__( self, sender: str, receiver: str, body: str, subject: str, copy = '' ):
        self.__sender = sender
        self.__receiver = receiver
        self.__body = body
        self.__others = copy
        self.__subject = subject

    def __str__( self ):
        if self.__body is not None:
            return self.__body

# Emai( sender, receiver, body, subject, copy )
class Email( Message ):
    '''Email( frm, to, body, subject ) initializes
    class providing email behavior '''

    def __init__( self, sender: str, receiver: str, body: str, subject: str, copy = '' ):
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
        if self.__from is not None:
            return self.__from

    @sender.setter
    def sender( self, value: str ):
        ''' Set the sender's email address '''
        if value is not None:
            self.__from = value

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__to is not None:
            return self.__to

    @receiver.setter
    def receiver( self, value: str ):
        ''' Sets the receiver's email address '''
        if value is not None:
            self.__to = value

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, value: str ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__subject = value

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__body is not None:
            return self.__body

    @body.setter
    def body( self, value: str ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__body = str( value )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, value: list ):
        ''' Sets the address's to send copies  '''
        if value is not None:
            self.__others = value

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
    '''Excel( selected_path ) class provides
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
    def path( self, value: str ):
        if value is not None:
            self.__path = value

    @property
    def name( self ):
        ''' Get the title of the workbook '''
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    def __init__( self, full_path: str ):
        self.__path = full_path
        self.__name = os.path.split( full_path )[ 1 ]
        self.__title = self.__name
        self.__workbook = Workbook( )
        self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

    def __str__( self ):
        if self.__path is not None:
            return self.__path

# Excel( fullpath )
class Excel( ):
    '''Excel( selected_path ) class provides
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
    def workbook( self, value: Workbook ):
        ''' Gets the report template '''
        if value is not None:
            self.__workbook = value

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__workbook is not None:
            return self.__workbook.active

    @worksheet.setter
    def worksheet( self, value: Workbook ):
        ''' Gets the workbooks worksheet '''
        if value is not None:
            self.__name = value.active

    def __init__( self, fullpath: str ):
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
        if value is not None:
            self.__name = str( value )

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if value is not None:
            self.__rows = value

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if value is not None:
            self.__columns = value

    @property
    def dimensions( self ):
        if self.__dimensions is not None:
            return self.__dimensions

    @dimensions.setter
    def dimensions( self, value ):
        if value is not None:
            self.__dimensions = value

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = xl.load_workbook( self.__path )
            return self.__workbook

    @workbook.setter
    def workbook( self, value ):
        ''' Gets the report template '''
        if value is not None:
            self.__workbook = value

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
        self.__name = name
        self.__rows = rows
        self.__columns = cols
        self.__dimensions = (self.__rows, self.__columns)

# ZipFile( path )
class ZipFile( ):
    __infile = None
    __name = None
    __filepath = None
    __extension = None
    __zippath = None
    __zipextension = None

    @property
    def path( self ):
        if self.__filepath is not None:
            return self.__filepath

    @path.setter
    def path( self, value ):
        if value is not None:
            self.__filepath = value

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, value ):
        if not value == '':
            self.__name = value

    def __init__( self, path ):
        self.__infile = path
        self.__zipextension = '.zip'
        self.__filepath = path
        self.__extension = os.path.splitext( path )
        self.__zippath = self.__filepath.replace( self.__extension, self.__zipextension )
        self.__name = os.path.basename( path )

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
