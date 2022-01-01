import os
import datetime as dt
import sqlite3 as sl
import pandas as pd
import pyodbc as db
import openpyxl as xl

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

    def is_file( self, other ):
        if os.path.isfile( other ):
            return True

    def is_folder( self, other ):
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
        if os.path.exists( first ) \
                and os.path.exists( second ):
            return os.path.join( first, second )

    def __init__( self, filepath ):
        self.__base = str( filepath )
        self.__path = self.__base
        self.__ext = os.path.split( self.__path )
        self.__report = r'etc\templates\report\ReportBase.xlsx'

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

class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __and = None
    __where = None
    __or = None
    __criteria = None
    __cmd = None
    __sql = None

    @property
    def AND( self ):
        if self.__and is not None:
            return self.__and

    @property
    def WHERE( self ):
        if self.__where is not None:
            return self.__where

    @property
    def command( self ):
        if self.__cmd is not None:
            return str( self.__sql[ self.__cmd ] )

    @command.setter
    def command( self, cmd ):
        if cmd is not None and cmd in self.__sql:
            self.__cmd = str( self.__sql[ cmd ] )

    def create( self, pairs ):
        ''' builds criteria from dictionary of name value pairs'''
        if isinstance( pairs, dict ):
            self.__criteria = pairs

    def __init__( self, cmd = 'SELECT' ):
        self.__and = ' AND '
        self.__where = ' WHERE '
        self.__cmd = str( cmd )
        self.__sql = [ 'SELECT', 'INSERT', 'UPDATE',
                       'DELETE', 'CREATE', 'ALTER',
                       'DROP', 'DETACH' ]

class DataRow():
    '''Defines the DataRow Class'''
    __source = None
    __names = None
    __items = None
    __data = None
    __values = None
    __id = None
    __record = None

    @property
    def index( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @index.setter
    def index( self, ordinal ):
        if isinstance( ordinal, int ):
            self.__id = ordinal

    @property
    def data( self ):
        if self.__data is not None:
            return dict( self.__data )

    @data.setter
    def data( self, items ):
        if isinstance( items, dict ):
            self.__items = items

    @property
    def items( self ):
        if isinstance( self.__items, tuple ):
            return self.__items

    @items.setter
    def items( self, data ):
        if isinstance( data, tuple ):
            self.__items = data

    @property
    def names( self ):
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, data ):
        if isinstance( data, dict ):
            self.__names = data.keys()

    @property
    def values( self ):
        if self.__values is not None:
            return list( self.__values )

    @values.setter
    def values( self, items ):
        if isinstance( items, list ):
            self.__values = items

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, row ):
        if isinstance( row, sl.Row ):
            self.__source = row

    def __init__( self, items = None ):
        self.__source = sl.Row
        self.__items = tuple( items )
        self.__id = int( items[ 0 ] )
        self.__names = list( self.__items.keys() )
        self.__values = self.__items.values()

    def __str__( self ):
        return 'Row ID: ' + str( self.__id )

class DataColumn():
    '''Defines the DataColumn Class'''
    __base = None
    __source = None
    __row = None
    __name = None
    __value = None
    __type = None
    __caption = None
    __id = None
    __table = None
    __data = None

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )

    @property
    def value( self ):
        if self.__value is not None:
            return self.__value

    @value.setter
    def value( self, value ):
        if value is not None:
            self.__value = value

    @property
    def type( self ):
        if self.__type is not None:
            return self.__type
        else:
            return 'NS'

    @type.setter
    def type( self, typ ):
        if typ is not None:
            self.__type = str( type( typ ) )

    @property
    def caption( self ):
        if self.__caption is not None:
            return self.__caption

    @caption.setter
    def caption( self, text ):
        if text is not None:
            self.__caption = str( text )

    @property
    def ordinal( self ):
        if self.__id > -1:
            return self.__id

    @ordinal.setter
    def ordinal( self, index ):
        if isinstance( index, int ):
            self.__id = index

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, name ):
        if name is not None:
            self.__table = str( name )

    @property
    def row( self ):
        if self.__row is not None:
            return self.__row

    @row.setter
    def row( self, items ):
        if isinstance( items, dict ):
            self.__base = items
            self.__row = self.__base

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, table ):
        if table is not None:
            self.__source = str( table )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def isnumeric( self ):
        if not isinstance( self.__value, str ):
            return True

    @property
    def istext( self ):
        if isinstance( self.__value, str ):
            return True

    def __init__( self, name, value ):
        self.__name = str( name )
        self.__value = value
        self.__base = { self.__name: self.__value }
        self.__data = { 'ordinal': self.__id, 'name': self.__name,
                        'caption': self.__caption, 'value': self.__value,
                        'datatype': self.__type, 'table': self.__table }

    def __str__( self ):
        return self.__name

class DataTable( pd.DataFrame ):
    '''Defines the DataTable Class'''
    __base = None
    __name = None
    __data = None
    __columns = None
    __records = None

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dataframe ):
        if isinstance( dataframe, pd.DataFrame ):
            self.__data = pd.DataFrame( dataframe )

    @property
    def schema( self ):
        if self.__columns is not None:
            return self.__columns

    @schema.setter
    def schema( self, columns ):
        if isinstance( columns, dict ):
            self.__columns = pd.Series( columns ).index

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    def __init__( self, name ):
        super().__init__()
        self.__base = str( name )
        self.__name = self.__base
        self.__data = pd.DataFrame( self.__name )
        self.__columns = self.__data.columns
        self.__rows = self.__data.items

    def __str__( self ):
        if self.__name is not None:
            return self.__name

class Source():
    '''Provides iterator for the Budget Execution table tables '''
    __data = None
    __reference = None

    @property
    def data( self ):
        ''' Property used to store table names in a list '''
        if self.__data is not None:
            return self.__data

    @property
    def reference( self ):
        ''' Property used to store table names in a list '''
        if self.__reference is not None:
            return self.__reference

    def __init__( self ):
        self.__data = [ 'Allocations', 'ApplicationTables', 'CarryoverEstimates',
                        'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                        'Deobligations', 'Defactos', 'DocumentControlNumbers', 'HeadquartersAuthority',
                        'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                        'ObjectClassOutlays', 'CarryoverOutlays', 'UnobligatedBalances',
                        'QueryDefinitions',  'RegionalAuthority', 'SpendingRates', 'GrowthRates',
                        'ReimbursableAgreements', 'ReimbursableFunds',
                        'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations',
                        'BudgetControls', 'AppropriationDocuments', 'BudgetDocuments',
                        'Apportionments', 'BudgetOutlays', 'SF133',
                        'Reprogrammings', 'SiteActivity', 'SiteProjectCodes',
                        'StatusOfFunds', 'Supplementals', 'Transfers',
                        'TravelObligations' ]
        self.__reference = [ 'Accounts', 'ActivityCodes',
                        'AllowanceHolders', 'Appropriations', 'BudgetObjectClasses',
                        'CostAreas', 'CPIC', 'Divisions',
                        'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                        'FiscalYears', 'FiscalYearsBackUp', 'Funds',
                        'Goals', 'GsPayScale', 'Images',
                        'Messages', 'NationalPrograms', 'Objectives',
                        'Organizations', 'ProgramAreas', 'ProgramDescriptions',
                        'ProgramProjects', 'Projects', 'Providers',
                        'ReferenceTables', 'ResourcePlanningOffices', 'ResponsibilityCenters',
                        'SchemaTypes', 'Sources' ]

    def __iter__( self ):
        if len( self.__data ) > 0:
            for i in self.__data:
                yield i

class DataModel():
    ''' Defines object used to provide the path to data model databases '''
    __accesspath = None
    __sqlitepath = None

    @property
    def accesspath( self ):
        if self.__accesspath is not None:
            return str( self.__accesspath )

    @property
    def sqlitepath( self ):
        if self.__sqlitepath is not None:
            return str( self.__sqlitepath )

    def __init__( self ):
        self.__accesspath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\access\datamodels\Data.accdb'
        self.__sqlitepath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\sqlite\datamodels\Data.db'

class ReferenceModel():
    '''Defines object used to provide paths to the reference model databases '''
    __accesspath = None
    __sqlitepath = None

    @property
    def accesspath( self ):
        if self.__accesspath is not None:
            return str( self.__accesspath )

    @accesspath.setter
    def accesspath( self, path ):
        if os.path.exists( path ):
            self.__accesspath = str( path )

    @property
    def sqlitepath( self ):
        if self.__sqlitepath is not None:
            return str( self.__sqlitepath )

    @sqlitepath.setter
    def sqlitepath( self, path ):
        if os.path.exists( path ):
            self.__sqlitepath = str( path )

    def __init__( self ):
        self.__accesspath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\access\referencemodels\References.accdb'
        self.__sqlitepath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\sqlite\referencemodels\References.db'

class AccessData():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __data = None
    __source = None
    __query = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, table ):
        if table is not None:
            self.__source = str( table )

    @property
    def connstring( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstring.setter
    def connstring( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data = dframe

    def connect( self ):
        if self.__dbpath is not None:
            db.connect( self.__dbpath, timeout = 3,
            attrs_before = dict() )

    def __init__( self, table = None ):
        self.__source = table
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy\db' \
            r'\access\datamodels\Data.accdb;'
        self.__data = pd.DataFrame

class AccessReference():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __data = None
    __source = None
    __query = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstring( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstring.setter
    def connstring( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data[ 0: ] = dframe

    def __init__( self, table = None ):
        self.__source = table
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy\db\access' \
            r'\referencemodels\References.accdb;'
        self.__data = pd.DataFrame

    def connect( self ):
        if self.__dbpath is not None:
            db.connect( self.__dbpath, timeout = 3,
                attrs_before = dict() )

class SQLiteData():
    '''Builds the budget execution data classes'''
    __source = None
    __dbpath = None
    __data = None
    __query = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstring( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstring.setter
    def connstring( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if isinstance( self.__data, pd.DataFrame ):
            return self.__data

    @data.setter
    def data( self, dframe ):
        if isinstance( dframe, pd.DataFrame ):
            self.__data = dframe

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlite\datamodels\\Data.db'
        self.__data = pd.DataFrame

class SQLiteReference():
    '''Class representing the budget execution reference models'''
    __source = None
    __dbpath = None
    __data = None
    __query = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, src ):
        if src is not None:
            self.__source = str( src )

    @property
    def connstring( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstring.setter
    def connstring( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
            r'\db\sqlite\referencemodels\References.db'
        self.__data = pd.DataFrame

class EmailBuilder():
    ''' Helper class for generating email messages '''
    __from = None
    __to = None
    __subject = None
    __message = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if self.__from is not None:
            return self.__from

    @sender.setter
    def sender( self, frm ):
        ''' Set the sender's email address '''
        if frm is not None:
            self.__from = str( frm )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__to is not None:
            return self.__to

    @receiver.setter
    def receiver( self, rec ):
        ''' Sets the receiver's email address '''
        if rec is not None:
            self.__to = str( rec )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, sub ):
        ''' Sets the email's subject line '''
        if sub is not None:
            self.__to = str( sub )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__message is not None:
            return self.__message

    @body.setter
    def body( self, msg ):
        ''' Sets the email's subject line '''
        if msg is not None:
            self.__to = str( msg )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, copy ):
        ''' Sets the address's to send copies  '''
        if copy is not None:
            self.__others = list( copy )

    def __init__( self, frm = None, to = None,
                  body = None, sub = None, copy = None ):
        self.__from = str( frm )
        self.__to = str( to )
        self.__message = str( body )
        self.__others = list( copy )
        self.__subject = str( sub )

    def __str__( self ):
        if self.__message is not None:
            return self.__message

class ExcelFile():
    ''' Provides the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __rows = None
    __columns = None
    __dimensions = None

    @property
    def name( self ):
        ''' Get the name of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, filename ):
        if filename is not None and len( filename ) > 0:
            self.__name = str( filename )

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, count ):
        if isinstance( count, int ) and count > 0:
            self.__rows = count

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, count ):
        if isinstance( count, int ) and count > 0:
            self.__columns = count

    @property
    def dimensions( self ):
        if self.__dimensions is not None:
            return self.__dimensions

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = xl.open( self.__path )
            return self.__workbook

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__workbook is not None:
            self.__worksheet = self.__workbook.active
            return self.__worksheet

    def __init__( self, name, rows = None,
                  cols = None ):
        self.__path = r'etc\templates\report\ReportBase.xlsx'
        self.__name = str( name )
        self.__rows = int( rows )
        self.__columns = int( cols )
        self.__dimensions = (self.__rows, self.__columns)
