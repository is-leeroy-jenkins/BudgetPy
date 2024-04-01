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
import shutil as sh
from datetime import datetime
from Booger import Error, ErrorDialog

class Path( ):
	'''

	Constructor: Path( filepath: str )

	Purpose:  Class representing a path

	'''
	__name: str=None
	__input: str=None
	__fileextension: str=None
	__currentdirectory: str=None
	__template: str=None
	__drive: str=None
	__pathseparator: str=None
	__extensionseparator: str=None
	__driveseparator: str=None
	__parentdirectory: str=None

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
			self.__name = value

	@property
	def file_extension( self ) -> str:
		if self.__fileextension is not None:
			return self.__fileextension

	@file_extension.setter
	def file_extension( self, value: str ):
		if value is not None:
			self.__fileextension = value

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
	def drive( self ):
		if self.__drive is not None:
			return self.__drive

	@drive.setter
	def drive( self, value: str  ):
		if value is not None:
			self.__drive = value

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

	@property
	def template_path( self ):
		if self.__template is not None:
			return self.__template

	@template_path.setter
	def template_path( self, value: str ):
		if value is not None:
			self.__template = value

	def __init__( self, filepath: str ):
		self.__input = filepath
		self.__name = os.path.split( filepath )[ 1 ]
		self.__currentdirectory = os.getcwd( )
		self.__fileextension = os.path.splitext( filepath )[ 1 ]
		self.__parentdirectory = os.path.split( filepath )[ 0 ]
		self.__template = r'etc\templates\report\Report.xlsx'
		self.__pathseparator = os.path.sep
		self.__extensionseparator = os.extsep
		self.__driveseparator = ':\\'
		self.__drive = os.path.splitdrive( filepath )[ 0 ]

	def __str__( self ) -> str:
		if self.__input is not None:
			return str( self.__input )

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'input', 'name', 'current_directory', 'extension',
		         'parent_directory', 'path_separator', 'drive',
		         'drive_separator', 'extension_separator', 'template_path',
		         'exists', 'is_folder', 'is_file', 'is_absolute',
		         'is_relative', 'verify', 'join', 'copy_tree' ]

	def exists( self ) -> bool:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if not os.path.exists( self.__input ):
				_msg = "The object 'self' does not exist or is None!"
				raise Exception( _msg )
			else:
				return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'exists( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_folder( self ) -> bool:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if self.__input is None:
				_msg = "The 'input' is None!"
				raise Exception( _msg )
			if os.path.isdir( self.__input ) == False:
				return False
			else:
				return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_folder( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_file( self ) -> bool:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if self.__input is None:
				_msg = "The 'input' is None!"
				raise Exception( _msg )
			elif os.path.isfile( self.__input ) == False:
				return False
			else:
				return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_file( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_absolute( self ) -> bool:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if not os.path.isabs( self.__input ):
				_msg = "The object 'self' is not a file!"
				raise Exception( _msg )
			else:
				return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_absolute_path( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_relative( self ) -> bool:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if not os.path.isabs( self.__input ):
				_msg = "The object 'self' is not a file!"
				raise Exception( _msg )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'is_relative_path( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def verify( self, other: str ) -> bool:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if not os.path.exists( other ):
				_msg = "The object 'self' is not a path!"
				raise Exception( _msg )
			else:
				return True
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'verify( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def join( self, first: str, second: str ) -> str:
		'''

		Purpose: Joins two paths into one.

		Parameters: 'first: str' representing the first path
		that is joined to the second path 'second: str'.

		Returns: a single string representing a path

		'''

		try:
			if not os.path.exists( first ) or not os.path.exists( second ):
				_msg = "The arguement 'first' or 'second' is not a file!"
				raise Exception( _msg )
			else:
				return os.path.join( first, second )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Path'
			_exc.method = 'join( self, first, second )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def copy_tree( self, destination: str ):
		'''

		Purpose:

		Copies directory tree to 'destination'

		Parameters:

		destination: str

		Returns:

		Void

		'''
		if destination is None:
			_msg = "The argument 'destination' is None"
			raise Exception( _msg )
		else:
			sh.copytree( self.__input, destination )

	def create_link( self, path: str, name: str ) -> str:
		'''

		Purpose:

			creates a symbolic link of 'path' the name 'name'

		Parameters:

			path: str, name: str

		Returns:

			str

		'''
		if path is None:
			_msg = "The argument 'path' is None"
			raise Exception( _msg )
		elif name is None:
			_msg = "The argument 'name' is None"
			raise Exception( _msg )
		else:
			os.link( path, name )

	def read_link( self, path: str ) -> str:
		'''

		Purpose:

			reads a symbolic link of 'path'

		Parameters:

			path: str, name: str

		Returns:

			str

		'''
		if path is None:
			_msg = "The argument 'path' is None"
			raise Exception( _msg )
		else:
			os.readlink( path )

class File( Path ):
	'''
	Constructor: File( path: str )

	Purpose: Class providing file information
	 '''
	__absolutepath: str=None
	__relativepath: str=None
	__size: int = None
	__created: datetime = None
	__modified: datetime = None
	__accessed: datetime = None
	__contents: list = [ ]

	@property
	def absolute_path( self ) -> str:
		'''
		Gets the absolute path
		'''
		if self.__absolutepath is not None:
			return self.__absolutepath

	@absolute_path.setter
	def absolute_path( self, value: str ):
		'''
		Sets the absolute path
		'''
		if value is not None:
			self.__absolutepath = value

	@property
	def relative_path( self ) -> str:
		'''
		Gets the relative path
		'''
		if self.__relativepath is not None:
			return self.__relativepath

	@relative_path.setter
	def relative_path( self, value: str ):
		'''
		Sets the relative path
		'''
		if value is not None:
			self.__relativepath = value

	@property
	def path( self ) -> str:
		if self.__input is not None:
			return self.__input

	@path.setter
	def path( self, value: str ):
		if value is not None:
			self.__input = value

	@property
	def size( self ) -> int:
		if self.__size is not None:
			return self.__size

	@size.setter
	def size( self, value: int ):
		if value is not None:
			self.__size = value

	@property
	def modified( self ) -> datetime:
		if self.__modified is not None:
			return self.__modified

	@modified.setter
	def modified( self, value: datetime ):
		if value is not None:
			self.__modified = value

	@property
	def accessed( self ) -> datetime:
		if self.__accessed is not None:
			return self.__accessed

	@accessed.setter
	def accessed( self, value: datetime ):
		if value is not None:
			self.__accessed = value

	@property
	def created( self ) -> datetime:
		if self.__created is not None:
			return self.__created

	@created.setter
	def created( self, value: datetime ):
		if value is not None:
			self.__created = value

	def __init__( self, path: str=None ):
		super( ).__init__( path )
		self.__input = super( ).input
		self.__absolutepath = os.path.abspath( path )
		self.__relativepath = os.path.relpath( path )
		self.__name = os.path.basename( path )
		self.__size = os.path.getsize( path )
		self.__extension = super( ).file_extension
		self.__created = os.path.getctime( path )
		self.__accessed = os.path.getatime( path )
		self.__modified = os.path.getmtime( path )

	def __str__( self ) -> str:
		if self.__path is not None:
			return self.__path

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'name', 'current_directory', 'extension',
		         'parent_directory', 'path_separator', 'drive',
		         'drive_separator', 'extension_separator', 'template_path',
		         'exists', 'is_folder', 'is_file', 'is_absolute',
		         'is_relative', 'verify', 'join', 'copy_tree',
		         'absolute_path', 'relative_path', 'path',
		         'name', 'size', 'extension', 'created',
		         'accessed', 'modified', 'rename', 'move',
		         'create', 'delete', 'get_lines', 'readlines', 'readall',
		         'iterlines', 'writelines', 'writeall' ]

	def rename( self, other: str ) -> str:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			if other is None:
				_msg = " The argument 'other' has not been specified!"
				raise Exception( _msg )
			else:
				_src = os.path.abspath( self.__path )
				_dest = os.path.join( self.directory, other )
				os.rename( _src, _dest )
				return _dest
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'rename( self, other: str )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def move( self, destination: str ) -> str:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_msg = " The 'path' is not a file or the argument " \
			        "'destination' has not been specified!"
			if os.path.isfile( self.__input ) == false or destination is None:
				raise Exception( _msg )
			else:
				return os.path.join( self.__name, destination )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'move( self, destination )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def create( self, other: str, lines: list[ str ]=None ):
		''' creates and returns 'selected_path' file '''
		try:
			_msg = " The argument 'other' has not been specified!"
			if other is None:
				raise Exception( _msg )
			else:
				_file = open( other, 'r+' )
				if len( lines ) > 0:
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

	def delete( self, other: str ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if other is None or not os.path.isfile( other ):
				_msg = " The argument 'other' has not been specified " \
				       "or does not exist!"
				raise Exception( _msg )
			else:
				os.remove( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'delete( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_lines( self ) -> list[ str ]:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		_lines = list( )
		try:
			if os.path.isfile( self.__input ) == False:
				_msg = "The 'path' is not a file!"
				raise Exception( _msg )
			else:
				file = open( self.__input )
				for i in file.readlines( ):
					_lines.append( i )
				return _lines
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'get_lines( )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def delete( self, other: str ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if other is None or os.path.isfile( self.__input ) == False:
				_msg = "The argument 'other' has not been " \
				       "specified or does not exist!"
				raise Exception( _msg )
			else:
				os.remove( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'delete( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def iterlines( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			if os.path.isfile( self.__input ) == False:
				_msg = "The 'path' is not a file!"
				raise Exception( _msg )
			else:
				file = open( self.__input )
				for i in file.readlines( ):
					yield i
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'iterlines( )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def readlines( self ) -> list[ str ]:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_contents = list( )
			if os.path.isfile( self.__input ) == False:
				_msg = "The 'path' is not a file!"
				raise Exception( _msg )
			else:
				_file = open( self.__input )
				for i in _file.readlines( ):
					_contents.append( i )
				_file.close( )
				return _contents
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'File'
			_exc.method = 'readlines( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def readall( self ) -> str:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_contents = ''
			if os.path.isfile( self.__input ) == False:
				_msg = "The 'path' is not a file!"
				raise Exception( _msg )
			else:
				_file = open( self.__input )
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

	def writelines( self, lines: list[ str ] ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if lines is None or os.path.isfile( self.__input ) == False:
				_msg = "The 'lines' is None or 'path' is not a file!"
				raise Exception( _msg )
			else:
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
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			_contents = [ ]
			_lines = [ ]
			if other is None or os.path.isfile( self.__input ) == False:
				_msg = "The argument 'other' has not been specified " \
					"or the 'path' is not a file!"
				raise Exception( _msg )
			else:
				_path = os.path.relpath( self.__input )
				_contents = open( _path, 'a' )
				_lines = open( other )
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
	__absolutepath: str=None
	__relativepath: str=None
	__size: int=None

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if value is not None:
			self.__name = value

	@property
	def path( self ) -> str:
		if self.__input is not None:
			return self.__input

	@path.setter
	def path( self, value: str ):
		if value is not None:
			self.__input = value

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
	def size( self ) -> int:
		if self.__size is not None:
			return self.__size

	@size.setter
	def size( self, value: int ):
		if value is not None:
			self.__size = value

	def __init__( self, filepath: str ):
		super( ).__init__( filepath )
		self.__input = super( ).input
		self.__name = super( ).name
		self.__size = os.path.getsize( filepath )
		self.__absolutepath = os.path.abspath( filepath )
		self.__relativepath = f'{os.getcwd( )}\\{os.path.basename( filepath )}'

	def __str__( self ) -> str:
		if self.__input is not None:
			return self.__input

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'name', 'current_directory', 'extension',
		         'parent_directory', 'path_separator', 'drive',
		         'drive_separator', 'extension_separator', 'template_path',
		         'exists', 'is_folder', 'is_file', 'is_absolute',
		         'is_relative', 'verify', 'join', 'copy_tree',
		         'absolute_path', 'relative_path', 'path',
		         'name', 'size', 'get_files', 'get_subfiles',
		         'get_subfolders', 'rename', 'move', 'create',
		         'delete', 'iterate' ]

	def get_files( self ) -> list[ str ]:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_names = [ ]
			_msg = "The object 'self' is not a directory!"
			if not os.path.isdir( self.__input ):
				raise Exception( _msg )
			else:
				for i in os.listdir( self.__input ):
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

	def get_subfiles( self ) -> list[ str ]:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_names = [ ]
			_msg = "The input path 'input' is not a directory!"
			if not os.path.isdir( self.__input ):
				raise Exception( _msg )
			else:
				for i in os.walk( self.__input ):
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

	def get_subfolders( self ) -> list[ str ]:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_names = [ ]
			if not os.path.isdir( self.__input ):
				_msg = "The object 'self' is not a directory!"
				raise Exception( _msg )
			else:
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
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if name is None:
				_msg = "The argument 'name' has not been specified!"
				raise Exception( _msg )
			else:
				return os.rename( self.__name, name )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'rename( self, name )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def move( self, destination: str ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if destination is None:
				_msg = "The 'destination' has not been specified!"
				raise Exception( _msg )
			else:
				return os.path.join( self.__name, destination )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'move( self, destination )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def create( self, other: str ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if other is None:
				_msg = "The argument 'other' has not been specified!"
				raise Exception( _msg )
			else:
				os.mkdir( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'create( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def delete( self, other: str ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if other is None:
				_msg = "The argument 'other' has not been specified!"
				raise Exception( _msg )
			else:
				os.rmdir( other )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Folder'
			_exc.method = 'delete( self, other )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def iterate( self ) -> iter:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if not os.path.isdir( self.__input ):
				_msg = " 'self' is not a directory!"
				raise Exception( _msg )
			else:
				for i in os.walk( self.__input ):
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
	__sender: str=None
	__receiver: str=None
	__subject: str=None
	__body: str=None
	__others: list[ str ]=None

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
	def body( self ) -> list[ str ]:
		if self.__body is not None:
			return self.__body

	@body.setter
	def body( self, value: list[ str ] ):
		if value is not None:
			self.__receiver = value

	@property
	def copy( self ) -> list[ str ]:
		if self.__others is not None:
			return self.__others

	@copy.setter
	def copy( self, value: list[ str ] ):
		if value is not None:
			self.__others = value

	def __init__( self, sender: str, receiver: str, body: list[ str ],
	              subject: str, copy: list[ str ]=None ):
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

	def __init__( self, sender: str, receiver: str, body: list[ str ],
	              subject: str, copy: list[ str ]=None ):
		super( ).__init__( sender, receiver, body, subject, copy )
		self.__sender = super( ).sender
		self.__receiver = super( ).receiver
		self.__body = super( ).body
		self.__others = super( ).copy
		self.__subject = super( ).subject

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'sender', 'receiver', 'subject',
		         'body', 'copy' ]

class Excel( ):
	'''

	Constructor: Excel( path: str )

	Purpose: Class provides the spreadsheet for reports

	'''
	__templatepath: str=None
	__externalpath: str=None
	__workbook: Workbook=None
	__worksheet: Workbook=None
	__name: str=None
	__title: str=None

	@property
	def template_path( self ) -> str:
		if self.__templatepath is not None:
			return self.__templatepath

	@template_path.setter
	def template_path( self, value: str ):
		if value is not None:
			self.__templatepath = value

	@property
	def external_path( self ) -> str:
		if self.__externalpath is not None:
			return self.__externalpath

	@external_path.setter
	def external_path( self, value: str ):
		if value is not None:
			self.__externalpath = value

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if value is not None:
			self.__name = value

	@property
	def title( self ) -> str:
		if self.__title is not None:
			return self.__title

	@title.setter
	def title( self, value: str ):
		if value is not None:
			self.__title = value

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

	def __init__( self, path: str=None ):
		self.__templatepath = r'etc/templates/report/Excel.xlsx'
		self.__externalpath = path
		self.__name = os.path.split( path )[ 1 ]
		self.__title = self.__name.split( '.' )[ 0 ]
		self.__workbook = Workbook( )
		self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

	def __str__( self ) -> str:
		if self.__externalpath is not None:
			return self.__externalpath

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'internal_path', 'external_path', 'name',
		         'title', 'workbook', 'worksheet', 'save' ]

	def save( self ):
		'''

		Purpose:

		Parameters:

		Returns:

		'''
		try:
			self.__workbook.save( self.__externalpath )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'Excel'
			_exc.method = 'save( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ExcelReport( Excel ):
	'''

	Constructor:  ExcelReport( path: str, rows: int = 46, cols: int = 12 ).

	Purpose:  Class providing spreadsheet for reports

	'''
	__rows: int=None
	__columns: int=None
	__dimensions: ( int, int )=None

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
	def dimensions( self, value: ( int, int ) ):
		if value is not None:
			self.__dimensions = value

	def __init__( self, path: str=None, rows: int=46, cols: int=12 ):
		super( ).__init__( path )
		self.__internal = super( ).internal
		self.__path = super( ).path
		self.__name = super( ).name
		self.__rows = rows
		self.__columns = cols
		self.__dimensions = ( rows, cols )
		self.__title = super( ).title
		self.__workbook = super( ).workbook
		self.__worksheet = super( ).worksheet

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'rows', 'columns', 'dimensions' ]

class ZipFile( ):
	'''

	Constructor:  ZipFile( path: str )

	Purpose:  Class defines object providing zip file functionality

	'''
	__input: str=None
	__filename: str=None
	__filepath: str=None
	__fileextension: str=None
	__zippath: str=None
	__zipname: str=None
	__zipextension: str=None

	@property
	def file_path( self ) -> str:
		if self.__filepath is not None:
			return self.__filepath

	@file_path.setter
	def file_path( self, value: str ):
		if value is not None:
			self.__filepath = value

	@property
	def file_name( self ) -> str:
		if not self.__filename == '':
			return self.__filename

	@file_name.setter
	def file_name( self, value: str ):
		if not value == '':
			self.__filename = value

	@property
	def file_extension( self ):
		if self.__fileextension is not None:
			return self.__fileextension
	@file_extension.setter
	def file_extension( self, value: str ):
		if value is not None:
			self.__fileextension = value

	@property
	def zip_path( self ):
		if self.__zippath is not None:
			return self.__zippath

	@zip_path.setter
	def zip_path( self, value: str ):
		if value is not None:
			self.__zippath = value

	@property
	def zip_name( self ):
		if self.__zipname is not None:
			return self.__zipname

	@zip_name.setter
	def zip_name( self, value: str ):
		if value is not None:
			self.__zipname = value

	@property
	def zip_extension( self ):
		if self.__zipextension is not None:
			return self.__zipextension

	@zip_extension.setter
	def zip_extension( self, value: str ):
		if value is not None:
			self.__zipextension = value

	def __init__( self, path: str ):
		self.__input = path
		self.__zipextension = '.zip'
		self.__filepath = path
		self.__fileextension = os.path.splitext( path )[ 1 ]
		self.__zipname = self.__filename + self.__zipextension
		self.__zippath = self.__filepath.replace( self.__fileextension, self.__zipextension )
		self.__filename = os.path.basename( path )

	def __str__( self ):
		if self.__path is not None:
			return self.__path

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'file_name', 'file_path', 'file_extenstion',
		         'zip_name', 'zip_path', 'zip_extension',
		         'create', 'unzip'  ]

	def create( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if not self.__filepath == '':
				zp.ZipFile( self.__zippath, 'w' ).write( self.__filepath, self.__filename )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'FileSys'
			_exc.cause = 'ZipFile'
			_exc.method = 'create( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def unzip( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''

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
