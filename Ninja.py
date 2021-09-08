import os
import pandas as pd
import pyodbc as access
import sqlite3
import datetime as dt


class BudgetPath():
    '''Defines the BudgetPath class'''
    __base = None
    __path = None
    __ext = None

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

    def rename( self, new_name ):
        '''renames current file'''
        if self.__base is not None and self.__name is not None:
            return os.rename( self.__name, new_name )

    def move( self, destination_path ):
        '''renames current file'''
        if self.__base is not None and os.path.exists( self.__base ):
            return os.path.join( self.__name, destination_path )

    def exists( self ):
        '''determines if the base file exists'''
        if os.path.isfile( self.__base ):
            return True

    def create( self, other ):
        ''' creates and returns 'other' file '''
        if other is not None:
            os.mkfifo( other )

    def verify( self, other ):
        '''determines if an external file exists'''
        if other is not None and os.path.exists( self.__base ):
            return os.path.exists( other )

    def delete( self ):
        ''' deletes file at 'self.__path'   '''
        if self.__path is not None and os.path.isfile( self.__path ):
            os.remove( self.__path )

    def getsize( self, other ):
        '''gets the size of another file'''
        if self.__base is not None and os.path.exists( other ):
            return os.path.getsize( other )

    def getdrive( self, other ):
        '''gets the drive of another file'''
        if self.__base is not None and os.path.exists( other ):
            return list( os.path.splitdrive( other ) )[ 0 ]

    def getextension( self, other ):
        ''' gets and returns extension of 'other' 'file' '''
        if other is not None and os.path.isfile( other ):
            return list( os.path.splitext( other ) )[ 1 ]

    def readlines( self, other ):
        '''reads all lines in 'other' into a list
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

    def exists( self ):
        '''determines if the base file exists'''
        if os.path.isdir( self.__base ):
            return True

    def verify( self, other ):
        '''determines if an external file exists'''
        if other != '':
            return os.path.isdir( other )

    def create( self, other ):
        if other is not None:
            os.mkdir( other )

    def kill( self, other ):
        ''' deletes 'other' directory '''
        if other is not None and os.path.isdir( other ):
            os.rmdir( other )

    def delete( self ):
        ''' deletes directory at self.__path '''
        if self.__base is not None and os.path.isdir( self.__path ):
            os.rmdir( self.__path )

    def getsize( self, other ):
        ''' gets and returns size of 'other' '''
        if other is not None and os.path.isdir( other ):
            return os.path.getsize( other )

    def getdrive( self, other ):
        ''' gets and returns parent directory of 'other' '''
        if other is not None and os.path.isdir( other ):
            return os.path.splitdrive( other )[ 0 ]

class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __sql = None
    __and = None
    __where = None
    __database = None
    __datatable = None
    __commandtype = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP']
    __criteria = { }

    @property
    def AND( self ):
        return self.__and

    @property
    def WHERE( self ):
        return self.__where

    @property
    def criteria( self ):
        return self.__criteria

    @criteria.setter
    def criteria( self, name_value_pairs = None ):
        self.__criteria = dict( name_value_pairs )

    def __init__( self ):
        self.__and = ' AND '
        self.__where = ' WHERE '

class DataRow():
    '''Defines the DataRow Class'''
    __base = None
    __source = None
    __items = { }
    __value = None
    __values = [ ]
    __columns = pd.Series
    __id = -1

    @property
    def items( self ):
        if self.__items is not None:
            return self.__items

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @property
    def values( self ):
        if self.__values is not None:
            return self.__values

    @property
    def id( self ):
        if self.__id is not None:
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
        self.__columns = dict.fromkeys( self.__items )
        self.__values = list( self.__items.values() )
        self.__id = self.__values[ 0 ]
        self.__value = self.__items.setdefault( 'Amount', 0 )

    def __str__( self ):
        return 'ID: ' + self.__id + ' ' + 'Value: ' + self.__value

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

    def __init__( self, name, data_type = None,
                  caption = None, source = None, ordinal = None ):
        self.__name = name
        self.__type = data_type
        self.__caption = caption
        self.__data = { 'ordinal': self.__ordinal, 'name': self.__name,
                        'caption': self.__caption, 'type': self.__type,
                        'table': self.__table }
        self.__source = source
        self.__ordinal = int( ordinal )
        self.__table = self.__source

    def __str__( self ):
        return self.__name

class DataTable():
    '''Defines the DataTable Class'''
    __name = None
    __data = { }
    __rows = pd.DataFrame
    __columns = pd.Series
    __schema = { }
    __query = None

    @property
    def name( self ):
        return self.__name

    @property
    def data( self ):
        return self.__data

    def __init__( self, name, sql = '' ):
        self.__name = name
        self.__query = sql

    def __str__( self ):
        return self.__name

    def get_sql( self ):
        return self.__query

    def get_source( self ):
        return self.__name

    def get_datarows( self ):
        return self.__rows

    def get_datacolumns( self ):
        return self.__columns

    def get_schema( self ):
        return self.__schema

class AccessDataBuilder():
    '''Builds the budget execution data classes'''
    __connector = ''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connector = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=accdb\Data.accdb;')
        self.__connection = access.connect( self.__connector,
            timeout = 3, attrs_before = dict() )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )

class AccessReferenceBuilder():
    '''Builds the budget execution data classes'''
    __connector = ''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connector = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=accdb\References.accdb;')
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
