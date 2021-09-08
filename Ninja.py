import os
import sqlite3
import pandas as pd
import pyodbc as access

class BudgetPath():
    '''Defines the BudgetPath class'''
    __base = None
    __path = None
    __ext = None
    __access_datamodels = r'db\access\datamodels\Data.accdb'
    __access_data_sql = r'db\access\datamodels\sql'
    __access_referencemodels = r'db\access\referencemodels\References.accdb'
    __access_reference_sql = r'db\access\referencemodels\sql'
    __sqlite_datamodels = r'db\sqlite\datamodels\Data.db'
    __sqlite_data_sql = r'db\sqlite\datamodels\sql'
    __sqlite_referencemodels = r'db\sqlite\referencemodels\Reference.accdb'
    __sqlite_reference_sql = r'db\sqlite\referencemodels\sql'
    __sqlserver_datamodels = r''
    __sqlserver_referencemodels = r''
    __sqlserver_data_sql = r''
    __sqlserver_reference_sql = r''
    __excelreport = r'etc\templates\report\ReportBase.xlsx'
    __excelbudget = r'etc\templates\budget\BudgetBase.xlsx'

    @property
    def base( self ):
        if self.__base is not None:
            return self.__base

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @property
    def exists( self ):
        if os.path.exists( self.__path ):
            return True

    @property
    def access_datamodels( self ):
        if os.path.exists( self.__access_datamodels ):
            return self.__access_datamodels

    @property
    def access_referencemodels( self ):
        if os.path.exists( self.__access_referencemodels ):
            return self.__access_referencemodels

    @property
    def sqlite_datamodels( self ):
        if os.path.exists( self.__sqlite_datamodels ):
            return self.__sqlite_referencemodels

    @property
    def sqlite_referencemodels( self ):
        if os.path.exists( self.__sqlite_referencemodels ):
            return self.__sqlite_referencemodels

    @property
    def isfolder( self ):
        if os.path.exists( self.__path ) and os.path.isdir( self.__path ):
            return True

    @property
    def isfile( self ):
        if os.path.exists( self.__path ) and os.path.isfile( self.__path ):
            return True

    @property
    def extension( self ):
        if self.__path is not None:
            return os.path.split( self.__path )

    def __init__( self, filepath ):
        self.__base = str( filepath )
        self.__path = self.__base

class BudgetFile():
    '''Defines the BudgetFile Class'''
    __base = None
    __name = None
    __path = None
    __size = None
    __extension = None
    __parentfolder = None
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

    @property
    def name( self ):
        if os.path.isdir( self.__name ):
            return os.path.dirname( self.__path )

    @property
    def path( self ):
        if os.path.isdir( self.__path ):
            return self.__path

    @property
    def size( self ):
        if self.__parentfolder is not None:
            return self.__size

    @property
    def extension( self ):
        if self.__extension is not None:
            return self.__extension

    @property
    def parentfolder( self ):
        if self.__parentfolder is not None:
            return self.__parentfolder

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @property
    def modified( self ):
        if self.__modified is not None:
            return self.__modified

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    @property
    def currentdirectory( self ):
        if self.__current is not None:
            return self.__current

    # Constructor
    def __init__( self, base ):
        self.__base = str( base )
        self.__name = os.path.basename( base )
        self.__path = os.path.abspath( base )
        self.__size = os.path.getsize( base )
        self.__directory = os.path.dirname( self.__path )
        self.__extension = str( list( os.path.splitext( base ) )[ 1 ] )
        self.__created = os.path.getctime( base )
        self.__accessed = os.path.getatime( base )
        self.__modified = os.path.getmtime( base )
        self.__parentfolder = str( list( os.path.dirname( base ) )[ 0 ] )
        self.__current = os.getcwd()
        self.__drive = str(list( os.path.splitdrive( self.__path ) )[ 0 ] )
        self.__content = list()

    def rename( self, filename ):
        '''renames current file'''
        if self.__base is not None and self.__name is not None:
            return os.rename( self.__name, filename )

    def move( self, destination ):
        '''renames current file'''
        if self.__base is not None and os.path.exists( self.__base ):
            return os.path.join( self.__name, destination )

    def create( self, other ):
        ''' creates and returns 'path' file '''
        if other is not None:
            os.mkfifo( other )

    def exists( self, path ):
        '''determines if an external file exists'''
        if path is not None:
            return os.path.exists( path )

    def delete( self, path ):
        ''' deletes file at 'self.__path'   '''
        if path is not None and os.path.isfile( path ):
            os.remove( path )

    def getsize( self, path ):
        '''gets the size of another file'''
        if self.__base is not None and os.path.exists( path ):
            return os.path.getsize( path )

    def getdrive( self, path ):
        '''gets the drive of another file'''
        if self.__base is not None and os.path.exists( path ):
            return list( os.path.splitdrive( path ) )[ 0 ]

    def getextension( self, path ):
        ''' gets and returns extension of 'path' 'file' '''
        if path is not None and os.path.isfile( path ):
            return list( os.path.splitext( path ) )[ 1 ]

    def readlines( self, other ):
        '''reads all lines in 'path' into a list
            then returns the list '''
        lines = [ ]
        count = len( self.__content )
        if other is not None and os.path.isfile( other ):
            for line in open( other, 'r' ):
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

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @property
    def size( self ):
        if self.__parent is not None:
            return self.__size

    @property
    def currentdirectory( self ):
        if self.__current is not None:
            return self.__current

    @property
    def parentfolder( self ):
        if self.__parent is not None:
            return self.__parent

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @property
    def modified( self ):
        if self.__modified is not None:
            return self.__modified

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    # Constructor
    def __init__( self, base ):
        self.__base = base
        self.__name = os.path.basename( base )
        self.__path = os.path.abspath( base )
        self.__size = os.path.getsize( base )
        self.__extension = list( os.path.splitext( base ) )[ 1 ]
        self.__created = os.path.getctime( base )
        self.__accessed = os.path.getatime( base )
        self.__modified = os.path.getmtime( base )
        self.__parent = os.path.dirname( base )

    def rename( self, new_name ):
        '''renames current file'''
        if self.__name is not None and new_name is not None:
            return os.rename( self.__name, new_name )

    def move( self, destination ):
        '''renames current file'''
        if self.__name is not None and destination is not None:
            return os.path.join( self.__name, destination )

    def exists( self, path ):
        '''determines if the base file exists'''
        if path is not None and os.path.isdir( path ):
            return True

    def create( self, path ):
        if path is not None:
            os.mkdir( path )

    def delete( self, path ):
        ''' deletes 'path' directory '''
        if path is not None and os.path.isdir( path ):
            os.rmdir( path )

    def getsize( self, path ):
        ''' gets and returns size of 'path' '''
        if path is not None and os.path.isdir( path ):
            return os.path.getsize( path )

    def getdrive( self, path ):
        ''' gets and returns parent directory of 'path' '''
        if path is not None and os.path.isdir( path ):
            return os.path.splitdrive( path )[ 0 ]

class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __sql = None
    __and = None
    __where = None
    __database = None
    __datatable = None
    __criteria = None
    __command = [ 'SELECT', 'INSERT', 'UPDATE',
                  'DELETE', 'CREATE', 'ALTER',
                  'DROP', 'DETACH' ]

    @property
    def AND( self ):
        if self.__and is not None:
            return self.__and

    @property
    def WHERE( self ):
        if self.__where is not None:
            return self.__where

    @property
    def criteria( self ):
        if self.__criteria is not None:
            return self.__criteria

    @criteria.setter
    def criteria( self, namevaluepairs  ):
        if namevaluepairs is not None:
            self.__criteria = dict( namevaluepairs )

    def __init__( self ):
        self.__and = ' AND '
        self.__where = ' WHERE '


class DataRow():
    '''Defines the DataRow Class'''
    __base = None
    __source = None
    __name = None
    __items = None
    __date = None
    __value = None
    __values = [ ]
    __columns = pd.Series
    __id = -1

    @property
    def data( self ):
        if self.__items is not None:
            return self.__items.items()

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns.keys()

    @property
    def values( self ):
        if self.__values is not None:
            return self.__values

    @property
    def index( self ):
        if self.__id is not None and isinstance( self.__id, int ):
            return self.__id

    @property
    def value( self ):
        if self.__values is not None:
            return self.__value

    def __init__( self, base, source = None,
                  items = None ):
        self.__base = base
        self.__source = source
        self.__items = dict( items )
        self.__data = self.__items
        self.__columns = dict.fromkeys( self.__items )
        self.__values = list( self.__items.values() )
        self.__id = int( self.__values[ 0 ] )
        self.__value = self.__items.setdefault( 'Amount', 0 )

    def __str__( self ):
        return 'Row ID: ' + str( self.__id )

class DataColumn():
    '''Defines the DataColumn Class'''
    __base = None
    __source = None
    __row = None
    __name = None
    __type = None
    __caption = None
    __ordinal = -1
    __table = None
    __data = { }

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def type( self ):
        if self.__type is not None:
            return self.__type
        else:
            return 'NS'

    @property
    def caption( self ):
        if self.__caption is not None:
            return self.__caption

    @property
    def ordinal( self ):
        if self.__ordinal > -1:
            return self.__ordinal
        else:
            return -1

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table
        else:
            return 'NS'

    @property
    def row( self ):
        if self.__row is not None:
            return self.__row
        else:
            return 'NS'

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source
        else:
            return 'NS'

    @property
    def data( self ):
        return self.__data

    @property
    def isnumeric( self ):
        if not isinstance( str, type( self.__type ) ):
            return True

    @property
    def istext( self ):
        if isinstance( str, type( self.__type ) ):
            return True

    def __init__( self, name, datatype = None,
                  caption = None, source = None, ordinal = None):
        self.__name = name
        self.__type = datatype
        self.__caption = caption
        self.__source = source
        self.__ordinal = int( ordinal )
        self.__table = self.__source
        self.__data = { 'ordinal': self.__ordinal, 'name': self.__name,
                        'caption': self.__caption, 'datatype': self.__type,
                        'table': self.__table }

    def __str__( self ):
        return self.__name

class DataTable():
    '''Defines the DataTable Class'''
    __base = None
    __source = None
    __name = None
    __data = None
    __schema = None
    __query = None

    @property
    def name( self ):
        return self.__name

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def schema( self ):
        if self.__schema is not None:
            return self.__schema

    @property
    def rows( self ):
        if self.__source is not None:
            return self.__source.iterrows()

    def __init__( self, name, sql = None ):
        self.__name = name
        self.__base = self.__name
        self.__source = pd.DataFrame( self.__base )
        self.__data = self.__source[ 0: ].iterrows()
        self.__schema = self.__source.columns.names
        self.__query = str( sql )

    def __str__( self ):
        return self.__name

    def getsql( self ):
        if self.__query is not None:
            return self.__query

class AccessDataBuilder():
    '''Builds the budget execution data classes'''
    __connector = None
    __connection = None
    __cursor = None
    __data = None
    __budget = None
    __sqlpath = None

    def __init__( self ):
        self.__connector = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=db\access\datamodels\Data.accdb;')
        self.__connection = access.connect( self.__connector,
            timeout = 3, attrs_before = dict() )
        self.__budget = BudgetPath
        self.__sqlpath = self.__budget.sqlite_datamodels
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data is None:
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )

class AccessReferenceBuilder():
    '''Builds the budget execution data classes'''
    __connector = None
    __connection = None
    __cursor = None
    __data = None
    __budget = BudgetPath
    __sqlpath = None

    def __init__( self ):
        self.__connector = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=db\access\referencemodels\References.accdb;')
        self.__connection = access.connect( self.__connector,
            timeout = 3, attrs_before = dict() )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {0}', table )

class SQLiteDataBuilder():
    '''Builds the budget execution data classes'''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connection = sqlite3.connect( r'db\sqlite\datamodels\Data.db' )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )

class SQLiteReferenceBuilder():
    '''Builds the budget execution reference models'''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connection = sqlite3.connect( r'db\sqlite\referencemodels\References.db' )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )
