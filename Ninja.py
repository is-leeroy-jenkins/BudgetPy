import sqlite3 as sl
import pandas as pd
import pyodbc as db

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
            return  self.__cmd

    @command.setter
    def command( self, cmd ):
        if cmd is not None and cmd in self.__sql:
            self.__cmd = str( self.__sql[ cmd ] )

    @property
    def pairs( self ):
        ''' builds criteria from name value pairs'''
        if isinstance( self.__criteria, dict ):
            return self.__criteria

    @pairs.setter
    def pairs( self, nvpairs ):
        ''' builds criteria from name value pairs'''
        if isinstance( nvpairs, dict ):
            self.__criteria = nvpairs

    def __init__( self, cmd = 'SELECT' ):
        self.__and = ' AND '
        self.__where = ' WHERE '
        self.__cmd = cmd
        self.__sql = [ 'SELECT', 'INSERT', 'UPDATE', 'CREATE',
                       'ALTER', 'DROP', 'DETACH' ]

class DataRow( sl.Row ):
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

    def __init__( self, items = None  ):
        super().__init__( items )
        self.__source = sl.Row()
        self.__items = dict( items )
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
    __data = [ ]
    __references = [ ]

    @property
    def data( self ):
        ''' Property used to store table names in a list '''
        if self.__data is not None:
            return iter( self.__data )

    @property
    def references( self ):
        ''' Property used to store table names in a list '''
        if self.__references is not None:
            return iter( self.__references )

    def __init__( self ):
        self.__data = [ 'Allocations', 'ApplicationTables', 'CarryoverEstimates',
                        'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                        'Deobligations', 'Defactos', 'DocumentControlNumbers',
                        'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                        'ObjectClassOutlays', 'CarryoverOutlays', 'UnobligatedAuthority',
                        'QueryDefinitions',  'RegionalAuthority', 'SpendingRates',
                        'GrowthRates', 'ReimbursableAgreements', 'ReimbursableFunds',
                        'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations',
                        'BudgetControls', 'AppropriationDocuments', 'BudgetDocuments',
                        'Apportionments', 'BudgetOutlays', 'BudgetResourceExecution',
                        'Reprogrammings', 'SiteActivity', 'SiteProjectCodes',
                        'StatusOfFunds', 'Supplementals', 'Transfers',
                        'HeadquartersAuthority', 'TravelObligations', 'StatusOfAppropriations',
                        'StatusOfJobsActFunding', 'StatusOfSupplementalFunding', 'SuperfundSites',
                        'PayrollAuthority', 'TransTypes', 'ProgramFinancingSchedule',
                        'PayrollRequests', 'CarryoverRequests', 'CompassLevels',
                        'AdministrativeRequests']
        self.__references = [ 'Accounts', 'ActivityCodes',
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

class AccessData():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __driver = None
    __connstr = None
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
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data = dframe.items

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver )

    @driver.setter
    def driver( self, name ):
        if name is not None:
            self.__driver = name

    def get_connection( self ):
        if self.__connstr is not None:
            return db.connect( self.__connstr )

    def __init__( self, table = None ):
        self.__source = table
        self.__driver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db' \
            r'\access\datamodels\Data.accdb;'
        self.__connstr = f'{ self.__driver } { self.__dbpath }'
        self.__data = pd.DataFrame

class AccessReference():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __driver = None
    __connstr = None
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
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data = dframe.items

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver )

    @driver.setter
    def driver( self, name ):
        if name is not None:
            self.__driver = name

    def __init__( self, table = None ):
        self.__source = table
        self.__driver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db\access' \
            r'\referencemodels\References.accdb;'
        self.__connstr = f'{ self.__driver } { self.__dbpath }'
        self.__data = pd.DataFrame

    def get_connection( self ):
        if self.__connstr is not None:
            return db.connect( self.__connstr )

class SQLiteData():
    '''Builds the budget execution data classes'''
    __dbpath = None
    __connstr = None
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
    def connstr( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @connstr.setter
    def connstr( self, conn ):
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

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\\sqlite\\datamodels\Data.db'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def get_connection( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr )

class SQLiteReference():
    '''Class representing the budget execution references models'''
    __source = None
    __dbpath = None
    __connstr = None
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
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

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
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
        self.__data = [ ]

    def get_connection( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr )

class SqlServerData():
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
            r'\db\mssql\datamodels\Data.mdf'
        self.__data = pd.DataFrame

class SqlServerReference():
    '''Class representing the budget execution references models'''
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
            r'\db\mssql\referencemodels\References.mdf'
        self.__data = pd.DataFrame
