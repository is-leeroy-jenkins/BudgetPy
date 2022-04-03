import sqlite3 as sl
import pandas as pd
import pyodbc as db
import os


class Source( ):
    '''Source( tablename  ) provides list of Budget Execution
    tables across two databases ( data and references ) '''
    __data = []
    __references = []
    __table = None

    @property
    def data( self ):
        ''' Property used to store tablename names in a list '''
        if self.__data is not None:
            return list( self.__data ) 

    @property
    def references( self ):
        ''' Property used to store tablename names in a list '''
        if self.__references is not None:
            return list( self.__references ) 

    @property
    def table( self ):
        if self.__table is not None and self.__table != '':
            return self.__table

    @table.setter
    def table( self, name ):
        if isinstance( name, str ) and name in self.__data:
            self.__table = name
        elif name in self.__references:
            self.__table = name
        else:
            self.__table = None

    def is_data( self ):
        if self.__table is not None and self.__table in self.__data:
            return True
        else:
            return False

    def is_reference( self ):
        if self.__table is not None and self.__table in self.__references:
            return True
        else:
            return False

    def __str__( self ):
        if isinstance( self.__table, str ) and self.__table != '':
            return self.__table

    def __init__( self, tablename ):
        '''Constructor for the Source class providing
       a list of tables in the data database and/or
        reference database'''
        self.__data = ['Allocations', 'ApplicationTables', 'CarryoverEstimates',
                       'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                       'Deobligations', 'Defactos', 'DocumentControlNumbers',
                       'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                       'ObjectClassOutlays', 'CarryoverOutlays', 'UnobligatedAuthority',
                       'QueryDefinitions', 'RegionalAuthority', 'SpendingRates',
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
                       'AdministrativeRequests', 'OpenCommitments', 'Expenditures',
                       'UnliquidatedObligations']

        self.__references = ['Accounts', 'ActivityCodes', 'AllowanceHolders',
                             'Appropriations', 'BudgetObjectClasses',
                             'CostAreas', 'CPIC', 'Divisions',
                             'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                             'FiscalYears', 'FiscalYearsBackUp', 'Funds',
                             'Goals', 'GsPayScale', 'Images',
                             'Messages', 'NationalPrograms', 'Objectives',
                             'Organizations', 'ProgramAreas', 'ProgramDescriptions',
                             'ProgramProjects', 'Projects', 'Providers',
                             'ReferenceTables', 'ResourcePlanningOffices', 'ResponsibilityCenters',
                             'SchemaTypes', 'Sources']
        self.__table = tablename


class Provider( ):
    '''Provider( name  ) class that
    provides the data providers used to identify
    the type of database ( access, sqlite, sqlserver, or sqlce ) '''
    __access = None
    __sqlite = None
    __sqlce = None
    __mssql = None
    __excel = None
    __name = None
    __baseprovider = None
    __list = None

    @property
    def access( self ):
        ''' Property used to identify
        access provider '''
        if self.__access is not None:
            return self.__access

    @property
    def sqlite( self ):
        ''' Property used to identify
         sqlite provider '''
        if self.__sqlite is not None:
            return self.__sqlite

    @property
    def sqlserver( self ):
        ''' Property used to identify
         sql server provider '''
        if self.__mssql is not None:
            return self.__mssql

    @property
    def sqlce( self ):
        ''' Property used to identify sqlserver
         compact provider '''
        if self.__sqlce is not None:
            return self.__sqlce

    @property
    def excel( self ):
        ''' Property used to identify excel provider '''
        if self.__excel is not None:
            return self.__excel

    @property
    def extension( self ):
        if self.__name is not None and self.__name != '':
            if self.__name == 'Access':
                return '.accdb'
            elif self.__name == 'SqlCe':
                return '.sdf'
            elif self.__name == 'SQLite':
                return '.db'
            elif self.__name == 'SqlServer':
                return '.mdf'
            elif self.__name == 'Excel':
                return '.xlsx'
            else:
                return '.db'

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, base ):
        if isinstance( base, str ) and base != '':
            if base in self.__list:
                self.__name = base
            else:
                self.__name = 'SQLite'

    @property
    def path( self ):
        if self.__name == 'Access':
            dp = DataPath( 'Access' ) 
            return dp.access
        elif self.__name == 'SQLite':
            dp = DataPath( 'SQLite' ) 
            return dp.sqlite
        elif self.__name == 'SqlServer':
            dp = DataPath( 'SqlServer' ) 
            return dp.sqlserver

    def setbyname( self, name ):
        if isinstance( name, str ) and name != '':
            if name == 'SQLite':
                self.__name = name
                self.__baseprovider = self.__sqlite
            elif name == 'Access':
                self.__name = name
                self.__baseprovider = self.__access
            elif name == 'SqlServer':
                self.__name = name
                self.__baseprovider = self.__mssql
            elif name == 'SqlCe':
                self.__name = name
                self.__baseprovider = self.__sqlce
            elif name == 'Excel':
                self.__name = name
                self.__baseprovider = self.__excel
            else:
                self.__name = 'SQLite'
                self.__baseprovider = self.__sqlite

    def __str__( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    def __init__( self, name ):
        self.__access = 'Access'
        self.__sqlite = 'SQLite'
        self.__sqlce = 'SqlCe'
        self.__mssql = 'SqlServer'
        self.__excel = 'Excel'
        self.__list = ['Access', 'Sqlite', 'SqlCe', 'SqlServer', 'Excel']
        self.setbyname( name ) 


class CommandType( ):
    '''CommandType( cmd  ) defines the types of sql commands
    used to query the database'''
    __select = None
    __insert = None
    __update = None
    __delete = None
    __droptable = None
    __dropview = None
    __createtable = None
    __createview = None
    __altertable = None
    __altercolumn = None
    __list = None
    __type = None

    @property
    def select( self ):
        if self.__select is not None:
            return self.__select

    @property
    def insert( self ):
        if self.__insert is not None:
            return self.__insert

    @property
    def update( self ):
        if self.__update is not None:
            return self.__update

    @property
    def createtable( self ):
        if self.__createtable is not None:
            return self.__createtable

    @property
    def createview( self ):
        if self.__createview is not None:
            return self.__createview

    @property
    def droptable( self ):
        if self.__droptable is not None:
            return self.__droptable

    @property
    def dropview( self ):
        if self.__dropview is not None:
            return self.__dropview

    @property
    def delete( self ):
        if self.__delete is not None:
            return self.__delete

    @property
    def altertable( self ):
        if self.__altertable is not None:
            return self.__altertable

    @property
    def altercolumn( self ):
        if self.__altercolumn is not None:
            return self.__altercolumn

    def setbyname( self, cmd ):
        '''Function to set the type of sql command that
        will be used to query the database'''
        if cmd in self.__list and str( cmd ) .upper( ) == 'SELECT':
            self.__type = self.__select
        elif str( cmd ) .upper( ) == 'INSERT':
            self.__type = self.__insert
        elif str( cmd ) .upper( ) == 'DELETE':
            self.__type = self.__delete
        elif str( cmd ) .upper( ) == 'DROP TABLE':
            self.__type = self.__droptable
        elif str( cmd ) .upper( ) == 'DROP VIEW':
            self.__type = self.__dropview
        elif str( cmd ) .upper( ) == 'UPDATE':
            self.__type = self.__update
        elif str( cmd ) .upper( ) == 'CREATE TABLE':
            self.__type = self.__createtable
        elif str( cmd ) .upper( ) == 'CREATE VIEW':
            self.__type = self.__createview
        elif str( cmd ) .upper( ) == 'ALTER TABLE':
            self.__type = self.__altertable
        elif str( cmd ) .upper( ) == 'ALTER COLUMN':
            self.__type = self.__altercolumn
        else:
            self.__type = self.__select

    def __str__( self ):
        if self.__type is not None:
            return str( self.__type ) 

    def __init__( self, cmd ):
        '''constructor for the CommandType class'''
        self.__select = 'SELECT'
        self.__insert = 'INSERT'
        self.__update = 'UPDATE'
        self.__delete = 'DELETE'
        self.__createtable = 'CREATE TABLE'
        self.__createview = 'CREATE VIEW'
        self.__droptable = 'DROP TABLE'
        self.__dropview = 'DROP VIEW'
        self.__altercolumn = 'ALTER COLUMN'
        self.__altertable = 'ALTER TABLE'
        self.__list = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP TABLE', 'DROP VIEW',
                       'CREATE TABLE', 'CREATE VIEW', 'ALTER COLUMN', 'ALTER TABLE']
        self.setbyname( cmd ) 


class DataPath( ):
    '''DataPath( name  ) provides path information
    related to the data model databases '''
    __accesspath = None
    __sqlitepath = None
    __mssqlpath = None
    __sqlcepath = None
    __abspath = None
    __relpath = None
    __basepath = None

    @property
    def access( self ):
        if self.__accesspath is not None:
            return str( self.__accesspath ) 

    @access.setter
    def access( self, path ):
        if path is not None:
            self.__accesspath = str( path ) 

    @property
    def sqlite( self ):
        if self.__sqlitepath is not None:
            return str( self.__sqlitepath ) 

    @sqlite.setter
    def sqlite( self, path ):
        if path is not None:
            self.__sqlitepath = str( path ) 

    @property
    def sqlserver( self ):
        if self.__mssqlpath is not None:
            return str( self.__mssqlpath ) 

    @sqlserver.setter
    def sqlserver( self, path ):
        if os.path.exists( path ):
            self.__mssqlpath = path

    @property
    def sqlce( self ):
        if isinstance( self.__sqlcepath, str ) and os.path.exists( self.__sqlcepath ):
            return str( self.__sqlcepath ) 

    @sqlce.setter
    def sqlce( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            self.__sqlcepath = str( path ) 

    def setbyextension( self, ext ):
        if isinstance( ext, str ) and ext != '':
            if ext == '.db':
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif ext == '.accdb':
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif ext == '.mdf':
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif ext == '.sdf':
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__relpath = r'db\sqlite\datamodels\Data.db'

    def setbyname( self, name ):
        if isinstance( name, str ) and name != '':
            if name == 'SQLite':
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif name == 'Access':
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif name == 'SqlServer':
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif name == 'SqlCe':
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sdf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__relpath = r'db\sqlite\datamodels\Data.db'

    def setbyprovider( self, pvdr ):
        if isinstance( pvdr, Provider ) and pvdr is not None:
            if pvdr.extension == '.db':
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif pvdr.extension == '.accdb':
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif pvdr.extension == '.mdf':
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif pvdr.extension == '.sdf':
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sdf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__relpath = r'db\sqlite\datamodels\Data.db'

    def setbypath( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            if path == self.__sqlitepath:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif path == self.__accesspath:
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif path == self.__mssqlpath:
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif path == self.__sqlcepath:
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sdf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__relpath = r'db\sqlite\datamodels\Data.db'

    @sqlserver.setter
    def sqlserver( self, path ):
        if path is not None:
            self.__mssqlpath = str( path ) 

    def __str__( self ):
        if os.path.exists( self.__basepath ):
            return self.__basepath

    def __init__( self, name ):
        self.__accesspath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\access\datamodels\Data.accdb'
        self.__sqlitepath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\sqlite\datamodels\Data.db'
        self.__mssqlpath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\mssql\datamodels\Data.mdf'
        self.__sqlcepath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\sqlce\datamodels\Data.sdf'
        self.setbyname( name ) 


class ReferencePath( ):
    '''ReferencePath( name  ) provides path information
    related to the references model databases '''
    __accesspath = None
    __sqlitepath = None
    __mssqlpath = None
    __sqlcepath = None
    __abspath = None
    __relpath = None
    __basepath = None

    @property
    def access( self ):
        if self.__accesspath is not None:
            return str( self.__accesspath ) 

    @access.setter
    def access( self, path ):
        if os.path.exists( path ):
            self.__accesspath = str( path ) 

    @property
    def sqlite( self ):
        if self.__sqlitepath is not None:
            return str( self.__sqlitepath ) 

    @sqlite.setter
    def sqlite( self, path ):
        if os.path.exists( path ):
            self.__sqlitepath = str( path ) 

    @property
    def sqlserver( self ):
        if self.__mssqlpath is not None:
            return str( self.__mssqlpath ) 

    @sqlserver.setter
    def sqlserver( self, path ):
        if os.path.exists( path ):
            self.__mssqlpath = path

    @property
    def sqlce( self ):
        if isinstance( self.__sqlcepath, str ) and os.path.exists( self.__sqlcepath ):
            return str( self.__sqlcepath ) 

    @sqlce.setter
    def sqlce( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            self.__sqlcepath = str( path ) 

    def setbyextension( self, ext ):
        if isinstance( ext, str ) and ext != '':
            if ext == '.db':
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif ext == '.accdb':
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif ext == '.mdf':
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif ext == '.sdf':
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'

    def setbyname( self, name ):
        if isinstance( name, str ) and name != '':
            if name == 'SQLite':
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif name == 'Access':
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif name == 'SqlServer':
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif name == 'SqlCe':
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sdf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'

    def setbyprovider( self, pvdr ):
        if isinstance( pvdr, Provider ) and pvdr is not None:
            if pvdr.extension == '.db':
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'
            elif pvdr.extension == '.accdb':
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'db\access\datamodels\Data.accdb'
            elif pvdr.extension == '.mdf':
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\mssql\datamodels\Data.mdf'
            elif pvdr.extension == '.sdf':
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\sqlce\datamodels\Data.sdf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'db\sqlite\datamodels\Data.db'

    def setbypath( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            if path == self.__sqlitepath:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'\db\access\referencemodels\References.db'
            elif path == self.__accesspath:
                self.__basepath = self.__accesspath
                self.__abspath = self.__accesspath
                self.__relpath = r'\db\access\referencemodels\References.accdb'
            elif path == self.__mssqlpath:
                self.__basepath = self.__mssqlpath
                self.__abspath = self.__mssqlpath
                self.__relpath = r'\db\access\referencemodels\References.mdf'
            elif path == self.__sqlcepath:
                self.__basepath = self.__sqlcepath
                self.__abspath = self.__sqlcepath
                self.__relpath = r'\db\access\referencemodels\References.sdf'
            else:
                self.__basepath = self.__sqlitepath
                self.__abspath = self.__sqlitepath
                self.__abspath = r'\db\access\referencemodels\References.db'

    def __str__( self ):
        if os.path.exists( self.__basepath ):
            return self.__basepath

    def __init__( self, name ):
        self.__accesspath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\access\referencemodels\References.accdb'
        self.__sqlitepath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\sqlite\referencemodels\References.db'
        self.__mssqlpath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\mssql\referencemodels\References.mdf'
        self.__sqlcepath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\sqlce\referencemodels\References.sdf'
        self.setbyname( name ) 


class CriteriaBuilder( ):
    '''CriteriaBuilder( cmd, names, values  ) provides the
     predicate name value pairs for sql queries'''
    __predicate = None
    __names = None
    __values = None
    __cmd = None

    @property
    def command( self ):
        if self.__cmd is not None:
            return self.__cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__cmd = cmd

    @property
    def names( self ):
        ''' builds criteria from name value namevaluepairs'''
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, keys ):
        ''' builds criteria from name value namevaluepairs'''
        if keys is not None and isinstance( keys, list ):
            self.__names = keys

    @property
    def values( self ):
        ''' builds criteria from name value namevaluepairs'''
        if isinstance( self.__values, list ):
            return self.__values

    @values.setter
    def values( self, vals  ):
        ''' builds criteria from name value namevaluepairs'''
        if vals is not None and isinstance( vals, list ):
            self.__values = vals

    @property
    def predicate( self  ):
        if self.__names is not None and self.__values is not None:
            for name in self.__names:
                for value in self.__values:
                    self.__predicate += f'{name} = {value} AND'
            self.__predicate.rstrip( ' AND' ) 
            return str( self.__predicate ) 

    @predicate.setter
    def predicate( self, kvp ):
        if isinstance( kvp, dict ):
            for name in kvp.keys( ):
                for value in kvp.values( ):
                    self.__predicate += f'{name} = {value} AND'
            self.__predicate.rstrip( ' AND' ) 

    def create( self, names, values ):
        if isinstance( names, list ) and isinstance( values, list ):
            criteria = ''
            for name in names:
                for value in values:
                    criteria += f'{name} = {value} AND'
                criteria.rstrip( ' AND'  ) 

    def equimap( self, this, that  ):
        if this is not None and that is not None:
            return f'{this} = {that}'

    def inequimap( self, this, that ):
        if this is not None and that is not None:
            return f'{this} != {that}'


    def lessmap( self, this, that ):
        if this is not None and that is not None:
            return f'{this} < {that}'

    def greatermap( self, this, that ):
        if this is not None and that is not None:
            return f'{this} > {that}'

    def lessequimap( self, this, that ):
        if this is not None and that is not None:
            return f'{this} <= {that}'

    def greaterequimap( self, this, that ):
        if this is not None and that is not None:
            return f'{this} >= {that}'

    def likemap( self, this, that ):
        if this is not None and that is not None:
            return f'{this} LIKE {that}'

    def __init__( self, cmd, names, values ):
        self.__names = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, list ) else None
        self.__cmd = cmd if isinstance( cmd, CommandType ) else CommandType( 'SELECT' ) 
        self.__predicate = ''


class SqlStatement( ):
    '''SqlStatement( pvdr, cmd, src, path  ) Class represents
     the sql queries used in the application'''
    __provider = None
    __command = None
    __path = None
    __source = None
    __table = None

    @property
    def provider( self ):
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, pdr ):
        if isinstance( pdr, Provider ):
            self.__provider = pdr
        else:
            sqlite = Provider( 'SQLite' ) 
            self.__provider = sqlite

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd
        else:
            command = CommandType( 'SELECT' ) 
            self.__command = command

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, Source ):
            self.__source = src
        else:
            source = Source( 'Allocations' ) 
            self.__source = source

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, name ):
        if name is not None and name != '':
            self.__table = name

    @property
    def sqlpath( self ):
        if self.__path is not None:
            return self.__path

    @sqlpath.setter
    def sqlpath( self, path ):
        if isinstance( path, DataPath ):
            self.__path = path
        else:
            model = DataPath( 'SQLite'  ) 
            self.__path = model

    def __init__( self, pvdr, cmd, src, path ):
        self.__provider = pvdr if isinstance( pvdr, Provider  ) else Provider( 'SQLite'  ) 
        self.__command = cmd if isinstance( cmd, CommandType  ) else CommandType( 'SELECT'  ) 
        self.__source = src if isinstance( src, Source  ) else Source( 'Allocations'  ) 
        self.__table = self.__source.table
        self.__path = path if isinstance( path, DataPath  ) else DataPath( 'SQLite'  ) 


class DataRow( sl.Row ):
    '''Defines the DataRow Class'''
    __source = None
    __names = None
    __items = None
    __data = None
    __values = None
    __id = None

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
            self.__names = data.keys( ) 

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

    def __init__( self, items=None ):
        super( ) .__init__( items ) 
        self.__source = sl.Row( ) 
        self.__items = dict( items ) 
        self.__id = int( items[0] ) 
        self.__names = list( self.__items.keys( ) ) 
        self.__values = self.__items.values( ) 

    def __str__( self ):
        return 'Row ID: ' + str( self.__id ) 


class DataColumn( ):
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
        self.__base = {self.__name: self.__value}
        self.__data = {'ordinal': self.__id, 'name': self.__name,
                       'caption': self.__caption, 'value': self.__value,
                       'datatype': self.__type, 'tablename': self.__table}

    def __str__( self ):
        return self.__name


class DataTable( pd.DataFrame ):
    '''Defines the DataTable Class'''
    __base = None
    __name = None
    __data = None
    __columns = None

    @property
    def name( self ):
        if isinstance( self.__name, str ):
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
            self.__columns = pd.Series( columns ) .index

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, items ):
        if isinstance( items, list ):
            self.__rows = items

    def __init__( self, name ):
        super( ) .__init__( ) 
        self.__base = str( name ) 
        self.__name = self.__base
        self.__data = pd.DataFrame( self.__name ) 
        self.__rows = [tuple( r ) for r in self.__data[0:]]
        self.__columns = self.__data.columns

    def __str__( self ):
        if self.__name is not None:
            return self.__name


class AccessData( ):
    '''AccessData( tablename  ) class
      represents the budget execution
      data model classes'''
    __dbpath = None
    __driver = None
    __connstr = None
    __data = None
    __source = None
    __table = None
    __command = None

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
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, Source ):
            self.__source = src

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
            return iter( self.__data[0:] ) 

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

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def connect( self ):
        if not self.__connstr == '':
            return db.connect( self.__connstr ) 

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = tablename
        self.__driver = r'DRIVER={Microsoft Access Driver ( *.mdb, *.accdb ) }'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db' \
                        r'\access\datamodels\Data.accdb;'
        self.__connstr = f'{self.__driver};{self.__dbpath};{self.__source};'
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' ) 


class AccessReference( ):
    '''AccessReference( tablename  ) class represents
    the budget execution data classes'''
    __dbpath = None
    __driver = None
    __connstr = None
    __data = None
    __source = None
    __table = None
    __command = None

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

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = self.__source.table
        self.__driver = r'DRIVER={Microsoft Access Driver ( *.mdb, *.accdb ) };'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db\access' \
                        r'\referencemodels\References.accdb;'
        self.__connstr = f'{self.__driver} {self.__dbpath}'
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' ) 

    def connect( self ):
        if self.__connstr is not None:
            return db.connect( self.__connstr ) 


class SQLiteData( ):
    '''SQLiteData( tablename  ) class represents
     the budget execution data classes'''
    __dbpath = None
    __driver = None
    __connstr = None
    __data = None
    __source = None
    __table = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath ) 

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path ) 

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver ) 

    @driver.setter
    def driver( self, driver ):
        if isinstance( driver, str ) and driver != '':
            self.__driver = str( driver ) 

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
        if not self.__dbpath == '':
            return self.__dbpath

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

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def connect( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr ) 

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = tablename
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlite\datamodels\Data.db'
        self.__driver = r'DBMS: SQLite ( ver. 3.36.0 ) Case sensitivity: plain=mixed, ' \
                        'delimited=mixed Driver: SQLite JDBC ( ver. 3.36.0.3, JDBC2.1 ) Ping: 15 ms'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' ) 


class SQLiteReference( ):
    '''The SQLiteReference( tablename  ) Class
    represents the budget execution
    references models'''
    __source = None
    __dbpath = None
    __driver = None
    __connstr = None
    __data = None
    __table = None
    __command = None

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
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver ) 

    @driver.setter
    def driver( self, driver ):
        if isinstance( driver, str ) and driver != '':
            self.__driver = str( driver ) 

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[0:] ) 

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def connect( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr ) 

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = tablename
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlite\referencemodels\References.db'
        self.__driver = r'DBMS: SQLite ( ver. 3.36.0 ) Case sensitivity: plain=mixed, ' \
                        r'delimited=mixed Driver: SQLite JDBC ( ver. 3.36.0.3, JDBC2.1 ) Ping: 15 ms'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' ) 


class SqlServerData( ):
    '''Builds the budget execution data classes'''
    __server = None
    __driver = None
    __source = None
    __table = None
    __dbpath = None
    __data = None
    __connstr = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath ) 

    @path.setter
    def path( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            self.__dbpath = path

    @property
    def server( self ):
        if self.__server is not None:
            return str( self.__server ) 

    @server.setter
    def server( self, path ):
        if isinstance( path, str ):
            self.__server = path

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver ) 

    @driver.setter
    def driver( self, drvr ):
        if isinstance( drvr, str ):
            self.__server = drvr

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source ) 

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source ) 

    @property
    def connectionstring( self ):
        if not self.__connstr == '':
            return self.__connstr

    @connectionstring.setter
    def connectionstring( self, conn ):
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

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = self.__source.table
        self.__server = r'( LocalDB ) \MSSQLLocalDB'
        self.__driver = r'{SQL Server Native Client 11.0}'
        self.__command = CommandType( 'SELECT' ) 
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\mssql\datamodels\Data.mdf'
        self.__connstr = f'DRIVER={self.__driver};SERVER={self.__server};DATABASE={self.__dbpath}'
        self.__data = pd.DataFrame


class SqlServerReference( ):
    '''SqlServerReference( tablename  ) Class
    represents the budget execution references models'''
    __source = None
    __table = None
    __dbpath = None
    __data = None
    __connstr = None
    __command = None
    __server = None
    __driver = None

    @property
    def server( self ):
        if self.__server is not None:
            return str( self.__server ) 

    @server.setter
    def server( self, path ):
        if isinstance( path, str ):
            self.__server = path

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver ) 

    @driver.setter
    def driver( self, drvr ):
        if isinstance( drvr, str ):
            self.__server = drvr

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath ) 

    @path.setter
    def path( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            self.__dbpath = path

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
        if not self.__connstr == '':
            return self.__connstr

    @connstring.setter
    def connstring( self, conn ):
        if isinstance( conn, str ) and os.path.exists( conn ):
            self.__connstr = conn

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[0:] ) 

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = self.__source.table
        self.__server = r'( LocalDB ) \MSSQLLocalDB'
        self.__driver = r'{SQL Server Native Client 11.0}'
        self.__command = CommandType( 'SELECT' ) 
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\mssql\referencemodels\References.mdf'
        self.__connstr = f'DRIVER={self.__driver};SERVER={self.__server};DATABASE={self.__dbpath}'
        self.__data = pd.DataFrame


class SqlCeData( ):
    '''Builds the budget execution data classes'''
    __server = None
    __driver = None
    __source = None
    __table = None
    __dbpath = None
    __data = None
    __connstr = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath ) 

    @path.setter
    def path( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            self.__dbpath = path

    @property
    def server( self ):
        if self.__server is not None:
            return str( self.__server ) 

    @server.setter
    def server( self, path ):
        if isinstance( path, str ):
            self.__server = path

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver ) 

    @driver.setter
    def driver( self, drvr ):
        if isinstance( drvr, str ):
            self.__server = drvr

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source ) 

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source ) 

    @property
    def connectionstring( self ):
        if not self.__connstr == '':
            return self.__connstr

    @connectionstring.setter
    def connectionstring( self, conn ):
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

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = self.__source.table
        self.__server = r'( LocalDB ) \MSSQLLocalDB'
        self.__driver = r'{SQL Server Native Client 11.0}'
        self.__command = CommandType( 'SELECT' ) 
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlce\datamodels\Data.sdf'
        self.__connstr = f'DRIVER={self.__driver};SERVER={self.__server};DATABASE={self.__dbpath}'
        self.__data = pd.DataFrame


class SqlCeReference( ):
    '''Class representing the budget execution references models'''
    __source = None
    __table = None
    __dbpath = None
    __data = None
    __connstr = None
    __command = None
    __server = None
    __driver = None

    @property
    def server( self ):
        if self.__server is not None:
            return str( self.__server ) 

    @server.setter
    def server( self, path ):
        if isinstance( path, str ):
            self.__server = path

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver ) 

    @driver.setter
    def driver( self, drvr ):
        if isinstance( drvr, str ):
            self.__server = drvr

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath ) 

    @path.setter
    def path( self, path ):
        if isinstance( path, str ) and os.path.exists( path ):
            self.__dbpath = path

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
        if not self.__connstr == '':
            return self.__connstr

    @connstring.setter
    def connstring( self, conn ):
        if isinstance( conn, str ) and os.path.exists( conn ):
            self.__connstr = conn

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[0:] ) 

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __init__( self, tablename ):
        self.__source = Source( tablename ) 
        self.__table = self.__source.table
        self.__server = r'( LocalDB ) \MSSQLLocalDB'
        self.__driver = r'{SQL Server Native Client 11.0}'
        self.__command = CommandType( 'SELECT' ) 
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlce\referencemodels\References.sdf'
        self.__connstr = f'DRIVER={self.__driver};SERVER={self.__server};DATABASE={self.__dbpath}'
        self.__data = pd.DataFrame
