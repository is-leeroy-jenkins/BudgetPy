import os
import pandas as pd
import pyodbc as access
import sqlite3

class BudgetFile():
    '''Defines the BudgetFile Class'''
    __base = None
    __name = None
    __path = None
    __size = None
    __extension = None
    __parent_folder = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __current = None

    @property
    def base( self ):
        return self.__base

    @property
    def name( self ):
        return os.path.basename( self.__base )

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @property
    def size( self ):
        if self.__parent_folder is not None:
            return self.__size

    @property
    def extension( self ):
        if self.__extension is not None:
            return self.__extension

    @property
    def parent_folder( self ):
        if self.__parent_folder is not None:
            return self.__parent_folder

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
        self.__parent_folder = os.path.dirname( base )

    def get_current_directory( self ):
        '''gets the current directory'''
        self.__current = os.getcwd()
        return self.__current

    def rename( self, new_name ):
        '''renames current file'''
        return os.rename( self.__name, new_name )

    def move( self, destination_path ):
        '''renames current file'''
        return os.path.join( self.__name, destination_path )

    def exists( self ):
        '''determines if the base file exists'''
        if os.path.isfile( self.__base ):
            return True

    def get_drive( self ):
        '''get the file's drive'''
        return list(os.path.splitdrive( self.__path ))[0]

    def verify( self, other_filepath ):
        '''determines if an external file exists'''
        if other_filepath != '':
            return os.path.exists( other_filepath )

    def get_size( self ):
        '''gets the size of the base file'''
        return os.path.getsize( self.__name )

class BudgetFolder():
    '''Defines the BudgetFolder Class'''
    # pseudo-private backing fields
    __base = None
    __name = None
    __path = None
    __size = None
    __parent_folder = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __current = None

    @property
    def base( self ):
        return self.__base

    @property
    def name( self ):
        return os.path.basename( self.__base )

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @property
    def size( self ):
        if self.__parent_folder is not None:
            return self.__size

    @property
    def parent_folder( self ):
        if self.__parent_folder is not None:
            return self.__parent_folder

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
        self.__parent_folder = os.path.dirname( base )

    def get_current_directory( self ):
        '''gets the current directory'''
        self.__current = os.getcwd()
        return self.__current

    def rename( self, new_name ):
        '''renames current file'''
        return os.rename( self.__name, new_name )

    def move( self, destination_path ):
        '''renames current file'''
        return os.path.join( self.__name, destination_path )

    def exists( self ):
        '''determines if the base file exists'''
        if os.path.isdir( self.__base ):
            return True

    def get_drive( self ):
        '''get the file's drive'''
        return list(os.path.splitdrive( self.__path ))[0]

    def verify( self, other_path ):
        '''determines if an external file exists'''
        if other_path != '':
            return os.path.isdir( other_path )

    def get_size( self ):
        '''gets the size of the base file'''
        return os.path.getsize( self.__name )

class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __sql = ''
    __and = ''
    __where = ''
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
        self.__criteria = name_value_pairs

    def __init__( self ):
        self.__and = ' AND '
        self.__where = ' WHERE '

class DataRow():
    '''Defines the DataRow Class'''
    __items = { }
    __value = None
    __values = []
    __columns = pd.Series
    __id = -1

    @property
    def items( self ):
        return self.__items

    @property
    def columns( self ):
        return self.__columns

    @property
    def values( self ):
        return self.__values

    @property
    def id( self ):
        return self.__id

    @property
    def value( self ):
        return self.__value

    def __init__( self, items ):
        self.__items = dict( items )
        self.__columns = dict.fromkeys( self.__items )
        self.__values = list( self.__items.values() )
        self.__id = self.__values[ 0 ]
        self.__value = self.__items.setdefault( 'Amount', 0 )

    def __str__( self ):
        return self.__id + ' ' + self.__value

class DataColumn():
    '''Defines the DataColumn Class'''
    __name = None
    __type = None
    __caption = None
    __ordinal = -1
    __table = None
    __row = None
    __source = None
    __data = { }

    @property
    def name( self ):
        return self.__name

    @property
    def type( self ):
        return self.__type

    @property
    def caption( self ):
        return self.__caption

    @property
    def ordinal( self ):
        return self.__ordinal

    @property
    def table( self ):
        return self.__table

    @property
    def row( self ):
        return self.__row

    @property
    def source( self ):
        return self.__source

    @property
    def data( self ):
        return self.__data

    @property
    def is_numeric( self ):
        if not isinstance( str, self.__type ):
            return True

    @property
    def is_text( self ):
        if isinstance( str, self.__type ):
            return True

    def __init__( self, name, data_type = None,
                  source = None, caption = None):
        self.__name = name
        self.__type = data_type
        self.__caption = caption
        self.__data = { 'name': self.__name, 'type': self.__type, 'caption': self.__caption }
        self.__source = source
        self.__table = self.__source

    def __str__(self):
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

    def __init__( self, name, sql = ''  ):
        self.__name = name
        self.__query = sql

    def __str__(self):
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
        self.__connection = sqlite3.connect( 'Data.db' )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {0}', table )

class SQLiteReferenceBuilder():
    '''Builds the budget execution reference models'''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connection = sqlite3.connect( 'References.db' )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )