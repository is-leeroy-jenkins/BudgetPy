'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                FileSys.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="FileSys.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2023  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    FileSys.py
  </summary>
  ******************************************************************************************
  '''
import os
import zipfile as zp
from openpyxl import Workbook
from Booger import Error, ErrorDialog
from Static import EXT

class Path( ):
	'''
	Constructor: Path( filename: str )

	Purpose:  Class representing a path'''
	__name = None
	__input = None
	__extension = None
	__currentdirectory = None
	__report = None
	__drive = None
	__pathseparator = None
	__extensionseparator = None
	__driveseparator = None
	__parentdirectory = None

	@property
	def input( self ) -> str:
		if self.__input is not None:
			return self.__input

	@input.setter
	def input( self, value: str ):
		if value is not None:
			self.__input = value

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if value is not None:
			self.__input = value

	@property
	def drive( self ) -> str:
		if self.__drive is not None:
			return self.__drive

	@drive.setter
	def drive( self, value: str ):
		if value is not None:
			self.__drive = os.path.splitdrive( value )[ 0 ]

	@property
	def extension( self ) -> str:
		if self.__extension is not None:
			return self.__extension

	@extension.setter
	def extension( self, value: str ):
		if value is not None:
			self.__extension = str( value )

	@property
	def current_directory( self ) -> str:
		if self.__currentdirectory is not None:
			return self.__currentdirectory

	@current_directory.setter
	def current_directory( self, value: str ):
		if os.path.exists( value ):
			os.chdir( value )
			self.__currentdirectory = value

	@property
	def parent_directory( self ) -> str:
		if self.__parentdirectory is not None:
			return self.__parentdirectory

	@parent_directory.setter
	def parent_directory( self, value: str ):
		if value is not None:
			self.__parentdirectory = value

	@property
	def path_separator( self ) -> str:
		if self.__pathseparator is not None:
			return self.__pathseparator

	@path_separator.setter
	def path_separator( self, value: str ):
		if value is not None:
			self.__pathseparator = value

	@property
	def drive_separator( self ) -> str:
		if self.__driveseparator is not None:
			return self.__driveseparator

	@drive_separator.setter
	def drive_separator( self, value: str ):
		if value is not None:
			self.__driveseparator = value

	@property
	def extension_separator( self ) -> str:
		if self.__extensionseparator is not None:
			return self.__extensionseparator

	@extension_separator.setter
	def extension_separator( self, value: str ):
		if value is not None:
			self.__extensionseparator = value

	def __init__( self, filepath: str ):
		self.__input = filepath
		self.__name = os.path.split( filepath )[ 1 ]
		self.__currentdirectory = os.getcwd( )
		self.__extension = os.path.splitext( filepath )[ 1 ]
		self.__parentdirectory = os.path.split( filepath )[ 0 ]
		self.__report = r'etc\templates\report\Excel.xlsx'
		self.__pathseparator = os.path.sep
		self.__extensionseparator = os.extsep
		self.__driveseparator = ':\\'
		self.__drive = os.path.splitdrive( filepath )[ 0 ]

	def __str__( self ) -> str:
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
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'exists( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_folder( self ) -> bool:
		'''Method returning boolean value indicating if is a folder'''
		try:
			if os.path.isdir( self.__input ):
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_folder( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_file( self ) -> bool:
		'''Method returning boolean value indicating if is a file'''
		try:
			if os.path.isfile( self.__input ):
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_file( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_absolute( self ) -> bool:
		'''Method to determine if the input path is an
		absolute path file'''
		try:
			if isinstance( self.__input, str ) and self.__input != '':
				if os.path.isabs( self.__input ):
					return True
				elif not os.path.isabs( self.__input ):
					return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_absolute_path( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_relative( self ) -> bool:
		'''Method to determine if the input path is a
		relative_path file path'''
		try:
			if isinstance( self.__input, str ) and self.__input != '':
				if os.path.isabs( self.__input ):
					return False
				elif not os.path.isabs( self.__input ):
					return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_relative_path( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def verify( self, other: str ) -> bool:
		'''Method returns a boolean value indicating if
		the external path 'other' exists'''
		try:
			if os.path.exists( other ):
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'verify( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_reportpath( self, ext: EXT = EXT.XLSX ) -> str:
		'''Method returns string representing the relative_path path
		to the report template
		'''
		try:
			if isinstance( self.__report, str ):
				return self.__report
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'get_report_path( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def join( self, first: str, second: str ) -> str:
		''' Method concatenates the path provided by the argument 'first'
		to the path provided by argument 'second' '''
		try:
			if os.path.exists( first ) and os.path.exists( second ):
				return os.path.join( first, second )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'join( self, first, second )'
			_err = ErrorDialog( _exc )
			_err.show( )

class File( Path ):
	'''
	Constructor: File( path: str )

	Purpose: Class providing file information
	 '''
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
	__currentdirectory = None
	__contents = [ ]

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if os.path.exists( value ):
			self.__name = os.path.basename( value )

	@property
	def path( self ) -> str:
		if self.__buffer is not None:
			return self.__buffer

	@path.setter
	def path( self, value: str ):
		if value is not None:
			self.__buffer = value

	@property
	def size( self ) -> int:
		if self.__size is not None:
			return self.__size

	@size.setter
	def size( self, value: int ):
		if value is not None:
			self.__size = value

	@property
	def directory( self ) -> str:
		if self.__directory is not None:
			return self.__directory

	@directory.setter
	def directory( self, value: str ):
		if os.path.isdir( value ):
			self.__directory = os.path.dirname( value )

	@property
	def extension( self ) -> str:
		if self.__extension is not None:
			return self.__extension

	@extension.setter
	def extension( self, value: str ):
		if isinstance( value, str ) and value != '':
			self.__extension = value

	@property
	def drive( self ) -> str:
		if self.__drive is not None:
			return self.__drive

	@drive.setter
	def drive( self, value: str ):
		if os.path.ismount( value ):
			self.__drive = str( value )

	@property
	def modified( self ) -> float:
		if self.__modified is not None:
			return self.__modified

	@modified.setter
	def modified( self, value: float ):
		if isinstance( value, float ):
			self.__modified = value

	@property
	def accessed( self ) -> float:
		if self.__accessed is not None:
			return self.__accessed

	@accessed.setter
	def accessed( self, value: float ):
		if value is not None:
			self.__accessed = value

	@property
	def created( self ) -> float:
		if self.__created is not None:
			return self.__created

	@created.setter
	def created( self, value: float ):
		if value is not None:
			self.__created = value

	def __init__( self, path: str = None ):
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

	def __str__( self ) -> str:
		if self.__path is not None:
			return self.__path

	def exists( self ) -> bool:
		if os.path.exists( self.__path ):
			return True
		else:
			return False

	def rename( self, other: str ) -> str:
		'''Renames the current_directory file to 'other' '''
		try:
			if isinstance( other, str ) and not other == '':
				_src = os.path.abspath( self.__path )
				_dest = os.path.join( self.directory, other )
				os.rename( _src, _dest )
				return _dest
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'rename( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def move( self, destination: str ) -> str:
		'''renames current_directory file'''
		try:
			if os.path.isdir( destination ):
				return os.path.join( self.__name, destination )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'move( self, destination )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def create( self, other: str, lines: list[ str ] = None ):
		''' creates and returns 'selected_path' file '''
		try:
			if other is not None:
				_file = open( other, 'r+' )
				if isinstance( lines, list ) and len( lines ) > 0:
					for line in lines:
						_file.write( line )

					_file.flush( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'create( self, other, lines = None )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def verify( self, other: str ) -> bool:
		'''determines if an external file exists'''
		try:
			if other is not None:
				return os.path.exists( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'verify( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def delete( self, other: str ):
		''' deletes file at 'self.__selecteditem'   '''
		try:
			if os.path.isfile( other ):
				os.remove( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'delete( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def readlines( self, other: str ):
		'''reads all lines in 'other' into a list
			then returns the list '''
		try:
			if os.path.isfile( other ):
				_file = open( other, 'r' )
				_contents = _file.readlines( )
				_file.close( )
				return _contents
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'realines( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def readall( self, other: str ):
		'''reads a single line from the _file into a string
			then returns the string'''
		try:
			_contents = ''
			if os.path.isfile( other ):
				_file = open( other, 'r' )
				_contents = _file.read( )
				_file.close( )
				return _contents
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'readall( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def writelines( self, lines: list[ str ] = None ):
		''' writes the _contents of 'lines' to self.__contents '''
		try:
			if isinstance( lines, list ):
				_path = os.path.relpath( self.__path )
				_contents = open( _path, 'a' )
				for line in lines:
					_contents.write( line )
				_contents.flush( )
				return _contents
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'writelines( self, lines = None )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def writeall( self, other: str ):
		''' writes the contents of '_lines' to self.__contents '''
		try:
			_contents = [ ]
			_lines = [ ]
			if os.path.isfile( other ):
				_path = os.path.relpath( self.__path )
				_contents = open( _path, 'a' )
				_lines = open( other, 'r' )
				for line in _lines.readlines( ):
					_contents.write( line )
				_contents.flush( )
				_lines.close( )
				return _contents
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'writeall( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Folder( Path ):
	'''
	Constructor: Folder( filepath: str )

	Purpose: Class providing file directory information
	'''
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
	def name( self ) -> str:
		if self.__path is not None:
			return self.__path

	@name.setter
	def name( self, value: str ):
		if value is not None:
			self.__path = value

	@property
	def directory( self ) -> str:
		if self.__path is not None:
			return self.__path

	@directory.setter
	def directory( self, value: str ):
		if value is not None:
			self.__name = value

	@property
	def path( self ) -> str:
		if self.__path is not None:
			return self.__path

	@path.setter
	def path( self, value: str ):
		if value is not None:
			self.__path = value

	@property
	def absolute_path( self ) -> str:
		if self.__absolutepath is not None:
			return self.__absolutepath

	@absolute_path.setter
	def absolute_path( self, value: str ):
		if value is not None:
			self.__absolutepath = value

	@property
	def relative_path( self ) -> str:
		if self.__relativepath is not None:
			return self.__relativepath

	@relative_path.setter
	def relative_path( self, value: str ):
		if self.__relativepath is not None:
			self.__relativepath = value

	@property
	def parent( self ) -> str:
		if self.__parent is not None:
			return self.__parent

	@parent.setter
	def parent( self, value: str ):
		if value is not None:
			self.__parent = value

	@property
	def drive( self ) -> str:
		if self.__drive is not None:
			return self.__drive

	@drive.setter
	def drive( self, value: str ):
		if value is not None:
			self.__drive = value

	@property
	def size( self ) -> int:
		if self.__size is not None:
			return self.__size

	@size.setter
	def size( self, value: int ):
		if value is not None:
			self.__size = value

	@property
	def current( self ) -> str:
		if self.__current is not None:
			return self.__current

	@current.setter
	def current( self, value: str ):
		if value is not None:
			os.chdir( value )
			self.__current = os.getcwd( )

	def __init__( self, filepath: str ):
		super( ).__init__( filepath )
		self.__size = os.path.getsize( filepath )
		self.__drive = super( ).drive
		self.__current = os.getcwd( )
		self.__path = super( ).input
		self.__name = os.path.basename( filepath )
		self.__parent = os.path.dirname( filepath )
		self.__absolutepath = os.path.abspath( filepath )
		self.__relativepath = f'{os.getcwd( )}\\{os.path.basename( filepath )}'

	def __str__( self ) -> str:
		if self.__path is not None:
			return self.__path

	def get_files( self ) -> list:
		'''Iterates subfolders in the base directory
		and returns a list of subfile paths'''
		try:
			_names = [ ]
			for i in os.listdir( self.__absolutepath ):
				_path = os.path.join( self.__absolutepath, i )
				if os.path.isfile( _path ):
					_names.append( _path )
			return _names
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'get_files( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_subfiles( self ) -> list:
		'''Iterates get_subfolders in the base directory'''
		try:
			_current = self.__current
			_abspath = self.__absolutepath
			_names = [ ]
			for i in os.walk( _abspath ):
				_dirpath = i[ 0 ]
				if len( i[ 1 ] ) > 0:
					for name in i[ 1 ]:
						path = os.path.join( _dirpath, name )
						_names.append( path )
			return _names
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'get_subfolders( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_subfolders( self ) -> list:
		'''Iterates get_subfolders in the base directory'''
		try:
			_names = [ ]
			for i in os.walk( self.__absolutepath ):
				if len( i[ 1 ] ) > 0:
					for file in i[ 1 ]:
						_path = os.path.join( self.__absolutepath, file )
						if os.path.isdir( _path ):
							_names.append( _path )
			return _names
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'get_subfolders( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def rename( self, name: str ):
		'''renames current_directory file'''
		try:
			if self.__name is not None:
				return os.rename( self.__name, name )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'rename( self, name )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def move( self, destination: str ):
		'''renames current_directory file'''
		try:
			if destination is not None and os.path.exists( destination ):
				return os.path.join( self.__name, destination )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'move( self, destination )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def exists( self ) -> bool:
		'''determines if the base file exists'''
		try:
			if self.__path is not None and os.path.isdir( self.__path ):
				return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'exists( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def create( self, other: str ):
		try:
			if other is not None:
				os.mkdir( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'create( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def delete( self, other: str ):
		''' deletes 'selected_path' directory '''
		try:
			if other is not None and os.path.isdir( other ):
				os.rmdir( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'delete( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def iterate( self ) -> iter:
		'''iterates subfolders in the base directory'''
		try:
			for i in os.walk( self.__path ):
				yield i
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'iterate( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Message( ):
	'''
	Constructor: Message( sender: str, receiver: str,
	              body: str, subject: str, copy: str = '')

	Purpose: Class providing email behavior
	'''
	__sender = None
	__receiver = None
	__subject = None
	__body = None
	__others = None

	@property
	def sender( self ) -> str:
		if self.__sender is not None:
			return self.__sender

	@sender.setter
	def sender( self, value: str ):
		if value is not None:
			self.__sender = value

	@property
	def receiver( self ) -> list[ str ]:
		if self.__receiver is not None:
			return [ self.__receiver, ]

	@receiver.setter
	def receiver( self, value: list[ str ] ):
		if value is not None:
			self.__receiver = value

	@property
	def subject( self ) -> str:
		if self.__subject is not None:
			return self.__subject

	@subject.setter
	def subject( self, value: str ):
		if value is not None:
			self.__receiver = value

	@property
	def body( self ) -> str:
		if self.__body is not None:
			return self.__body

	@body.setter
	def body( self, value: str ):
		if value is not None:
			self.__receiver = value

	@property
	def copy( self ) -> str:
		if self.__others is not None:
			return self.__others

	@copy.setter
	def copy( self, value: list ):
		if value is not None:
			self.__others = value

	def __init__( self, sender: str, receiver: str,
	              body: str, subject: str, copy: str = '' ):
		self.__sender = sender
		self.__receiver = receiver
		self.__body = body
		self.__others = copy
		self.__subject = subject

	def __str__( self ) -> str:
		if self.__body is not None:
			return self.__body

class Email( Message ):
	'''
	Constructor:  Emai( sender: str, receiver: str, body: str,
				  subject: str, copy: str = '' )

	Purpose: Class providing email behavior '''

	def __init__( self, sender: str, receiver: str, body: str,
	              subject: str, copy: str = '' ):
		super( ).__init__( sender, receiver, body, subject, copy )
		self.__sender = super( ).sender
		self.__receiver = super( ).receiver
		self.__body = super( ).body
		self.__others = super( ).copy
		self.__subject = super( ).subject

class MessageBuilder( ):
	'''
	Constructor: MessageBuilder( sender: str = '', receiver: str = '',
	              body: str = '', copy: str = '', subject: str = '' )

	Purpose:  Helper class for generating email messages
	'''
	__sender = None
	__receiver = None
	__subject = None
	__body = None
	__others = None

	@property
	def sender( self ) -> str:
		if self.__sender is not None:
			return self.__sender

	@sender.setter
	def sender( self, value: str ):
		if value is not None:
			self.__sender = value

	@property
	def receiver( self ) -> str:
		if self.__receiver is not None:
			return self.__receiver

	@receiver.setter
	def receiver( self, value: str ):
		if value is not None:
			self.__receiver = value

	@property
	def subject( self ) -> str:
		if self.__subject is not None:
			return self.__subject

	@subject.setter
	def subject( self, value: str ):
		if value is not None:
			self.__subject = value

	@property
	def body( self ) -> str:
		if self.__body is not None:
			return self.__body

	@body.setter
	def body( self, value: str ):
		if value is not None:
			self.__body = value

	@property
	def copy( self ) -> str:
		if self.__others is not None:
			return self.__others

	@copy.setter
	def copy( self, value: str ):
		if value is not None:
			self.__others = value

	def __init__( self, sender: str = '', receiver: str = '',
	              body: str = '', copy: str = '', subject: str = '' ):
		self.__sender = sender
		self.__receiver = receiver
		self.__body = body
		self.__others = copy
		self.__subject = subject

	def __str__( self ) -> str:
		if self.__body is not None:
			return self.__body

class Document( File ):
	'''
	Constructor:  Document( path: str )

	Purpose:  Class provides
	the spreadsheet for Budget Py reports
	'''
	__title = None

	def __init__( self, path: str ):
		super( ).__init__( path )
		self.__path = path
		self.__name = os.path.split( path )[ 1 ]
		self.__title = os.path.split( path )[ 1 ]
		self.__workbook = Workbook( )
		self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

	def __str__( self ) -> str:
		if self.__path is not None:
			return self.__path

class Excel( ):
	'''
	Constructor: Excel( path: str )

	Purpose: Class provides the spreadsheet for reports '''
	__path = None
	__workbook = None
	__worksheet = None
	__name = None
	__title = None

	@property
	def path( self ) -> str:
		if self.__path is not None and self.__path != '':
			return self.__path

	@path.setter
	def path( self, value: str ):
		if value is not None:
			self.__path = value

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if value is not None:
			self.__name = value

	@property
	def workbook( self ) -> Workbook:
		if self.__workbook is not None:
			return self.__workbook

	@workbook.setter
	def workbook( self, value: Workbook ):
		if value is not None:
			self.__workbook = value

	@property
	def worksheet( self ) -> str:
		if self.__workbook is not None:
			return self.__workbook.active

	@worksheet.setter
	def worksheet( self, value: Workbook ):
		if value is not None:
			self.__name = value.active

	def __init__( self, path: str ):
		self.__path = path
		self.__name = os.path.split( path )[ 1 ]
		self.__title = os.path.split( path )[ 1 ]
		self.__workbook = Workbook( )
		self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

	def __str__( self ) -> str:
		if self.__path is not None:
			return self.__path

	def save( self ):
		try:
			self.__workbook.save( self.__path )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Excel'
			_exc.method = 'save( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ExcelReport( Excel ):
	'''
	Constructor:  ExcelReport( name: str, rows: int = 46, cols: int = 12 ).

	Purpose:  Class providing spreadsheet for reports '''
	__rows = None
	__columns = None
	__dimensions = None

	@property
	def rows( self ) -> int:
		if self.__rows is not None:
			return self.__rows

	@rows.setter
	def rows( self, value: int ):
		if value is not None:
			self.__rows = value

	@property
	def columns( self ) -> int:
		if self.__columns is not None:
			return self.__columns

	@columns.setter
	def columns( self, value: int ):
		if value is not None:
			self.__columns = value

	@property
	def dimensions( self ) -> (int, int):
		if self.__dimensions is not None:
			return self.__dimensions

	@dimensions.setter
	def dimensions( self, value: (int, int) ):
		if value is not None:
			self.__dimensions = value

	def __init__( self, name: str, rows: int = 46, cols: int = 12 ):
		super( ).__init__( name )
		self.__path = r'etc/templates/report/Excel.xlsx'
		self.__name = name
		self.__rows = rows
		self.__columns = cols
		self.__dimensions = (self.__rows, self.__columns)

class ZipFile( ):
	'''
	Constructor:  ZipFile( path: str )

	Purpose:  Class defines object providing zip file functionality
	'''
	__infile = None
	__name = None
	__filepath = None
	__extension = None
	__zippath = None
	__zipextension = None

	@property
	def path( self ) -> str:
		if self.__filepath is not None:
			return self.__filepath

	@path.setter
	def path( self, value: str ):
		if value is not None:
			self.__filepath = value

	@property
	def name( self ) -> str:
		if not self.__name == '':
			return self.__name

	@name.setter
	def name( self, value: str ):
		if not value == '':
			self.__name = value

	def __init__( self, path: str ):
		self.__infile = path
		self.__zipextension = '.zip'
		self.__filepath = path
		self.__extension = os.path.splitext( path )[ 1 ]
		self.__zippath = self.__filepath.replace( self.__extension, self.__zipextension )
		self.__name = os.path.basename( path )

	def create( self ):
		''' Creates zip file'''
		try:
			if not self.__filepath == '':
				zp.ZipFile( self.__zippath, 'w' ).write( self.__filepath, self.__name )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'ZipFile'
			_exc.method = 'create( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def unzip( self ):
		''' Extracts zip _file contents '''
		try:
			if os.path.exists( self.__zippath ):
				_file = zp.ZipFile( self.__zippath )
				_file.extractall( self.__zippath )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'ZipFile'
			_exc.method = 'unzip( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
