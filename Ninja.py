import sqlite3 as sl
import pandas
from pandas import DataFrame, Index, MultiIndex, Series
from pandas import read_sql as sqlreader
import pyodbc as db
import os
from collections import namedtuple as ntuple
from Static import Source, Provider, SQL, ParamStyle

# DataConfig( source, provider )
class DataConfig( ):
    '''DataConfig( source, provider  ) provides list of Budget Execution
    tables across two databases ( values and references ) '''
    __data = [ ]
    __references = [ ]
    __source = None
    __provider = None
    __accessdriver = None
    __accessdatapath = None
    __accessreferencepath = None
    __sqldriver = None
    __sqldatapath = None
    __sqlreferencepath = None
    __sqlitedatapath = None
    __sqlitereferencepath = None
    __sqlitedriver = None
    __table = None
    __name = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def provider( self ):
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if isinstance( value, Provider ):
            self.__provider = value

    @property
    def table( self ):
        if isinstance( self.__table, str ) and self.__table != '':
            return self.__table

    @table.setter
    def table( self, value ):
        if isinstance( value, str ) and value in self.__data:
            self.__table = value
        elif value in self.__references:
            self.__table = value
        else:
            self.__table = None

    def __init__( self, source, provider ):
        '''Constructor for the DataConfig class providing
        values value details'''
        self.__provider = provider if isinstance( provider, Provider ) else Provider.SQLite
        self.__source = source if isinstance( source, Source ) else None
        self.__table = source.name
        self.__sqlitedatapath = r'C:\Users\teppler\source\repos\BudgetPy' \
                            r'\db\sqlite\datamodels\Data.db'
        self.__sqlitereferencepath = r'C:\Users\teppler\source\repos\BudgetPy' \
                            r'\db\sqlite\referencemodels\References.db'
        self.__accessdriver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
        self.__accessdatapath = r'C:\\Users\teppler\source\repos\BudgetPy' \
                            r'\db\access\datamodels\Data.accdb'
        self.__accessreferencepath = r'C:\\Users\teppler\source\repos\BudgetPy' \
                            r'\db\access\referencemodels\References.accdb'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
        self.__sqldatapath = r'C:\Users\teppler\source\repos\BudgetPy' \
                           r'\db\mssql\datamodels\Data.mdf'
        self.__sqlreferencepath = r'C:\Users\teppler\source\repos\BudgetPy' \
                           r'\db\mssql\referencemodels\References.mdf'
        self.__data = [ 'Allocations', 'Actuals', 'ApplicationTables', 'Apportionments', 'AppropriationDocuments',
                       'BudgetaryResourceExecution', 'BudgetControls', 'BudgetDocuments', 'BudgetOutlays',
                       'CarryoverEstimates', 'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                       'Deobligations', 'Defactos', 'DocumentControlNumbers',
                       'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                       'ObjectClassOutlays', 'CarryoverOutlays',
                       'QueryDefinitions', 'RegionalAuthority', 'SpendingRates',
                       'GrowthRates', 'ReimbursableAgreements', 'ReimbursableFunds',
                       'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations' 
                       'Reprogrammings', 'SiteActivity', 'SiteProjectCodes', 'SpecialAccounts',
                       'StatusOfFunds', 'Supplementals', 'Transfers', 'HumanResourceOrganizations'
                       'HeadquartersAuthority', 'TravelObligations', 'StatusOfAppropriations',
                       'StatusOfJobsActFunding', 'StatusOfSupplementalFunding', 'SuperfundSites',
                       'PayrollAuthority', 'TransTypes', 'ProgramFinancingSchedule',
                       'PayrollRequests', 'CarryoverRequests', 'CompassLevels',
                       'AdministrativeRequests', 'OpenCommitments', 'Expenditures',
                       'UnliquidatedObligations', 'UnobligatedAuthority' ]
        self.__references = [ 'Accounts', 'ActivityCodes', 'AllowanceHolders',
                             'Appropriations', 'BudgetObjectClasses',
                             'CostAreas', 'CPIC', 'Divisions',
                             'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                             'FiscalYears', 'FiscalYearsBackUp', 'Funds',
                             'FundSymbols', 'Goals', 'GsPayScales', 'Images',
                             'Messages', 'NationalPrograms', 'Objectives',
                             'Organizations', 'ProgramAreas', 'ProgramDescriptions',
                             'ProgramProjects', 'Projects', 'Providers', 'RegionalOffices'
                             'ReferenceTables', 'ResourcePlanningOffices', 'ResponsibilityCenters',
                             'SchemaTypes', 'StateOrganizations', 'Sources' ]

    def __str__( self ):
        if isinstance( self.__table, str ) :
            return self.__table

    def isdatamodel( self ):
        '''Returns the boolean value 'True' if the
        source is a memeber of datamodels else 'False' '''
        if self.__table != '' and self.__table in self.__data:
            return True
        else:
            return False

    def isreferencemodel( self ):
        '''Returns boolean value 'True' if the
        source is a memeber of the reference models else 'False' '''
        if self.__table is not None  \
                and self.__table in self.__references:
            return True
        else:
            return False

    def getdriver( self ):
        if self.__provider.name == Provider.SQLite.name:
            return self.getpath( )
        elif self.__provider.name == Provider.Access.name:
            return self.__accessdriver
        elif self.__provider.name == Provider.SqlServer.name:
            return self.__sqldriver
        else:
            return self.__sqlitedriver

    def getpath( self ):
        if self.__provider == Provider.SQLite and self.isreferencemodel( ):
            return self.__sqlitereferencepath
        elif self.__provider == Provider.SQLite and self.isdatamodel( ):
            return self.__sqlitedatapath
        elif self.__provider == Provider.Access and self.isdatamodel( ):
            return self.__accessdatapath
        elif self.__provider == Provider.Access and self.isreferencemodel( ):
            return self.__accessreferencepath
        elif self.__provider == Provider.SqlServer and self.isdatamodel( ):
            return self.__sqldatapath
        elif self.__provider == Provider.SqlServer and self.isreferencemodel( ):
            return self.__sqlreferencepath
        else:
            return self.__sqlitedatapath

    def getconnectionstring( self ):
        path = self.getpath()
        if self.__provider.name == Provider.Access.name:
            return self.getdriver() + path
        elif self.__provider.name == Provider.SqlServer.name:
            return r'DRIVER={ODBC Driver 17 for SQL Server};Server=.\SQLExpress;' \
                          + f'AttachDBFileName={ path }' \
                          + f'DATABASE={ path }Trusted_Connection=yes;'
        else:
            return f'{ path } '


# DataConnection( dataconfig )
class DataConnection(  ):
    '''DataConnection( dataconfig ) initializes
    object used to connect to the databases'''
    __configuration = None
    __provider = None
    __source = None
    __driver = None
    __path = None
    __connectionstring = None
    __connection = None

    @property
    def configuration( self ):
        if isinstance( self.__configuration, DataConfig ):
            return self.__configuration

    @configuration.setter
    def configuration( self, value ):
        if isinstance( value, DataModeel ):
            self.__configuration = value

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def provider( self ):
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if isinstance( value, Provider ):
            self.__provider = value

    @property
    def driver( self ):
        if isinstance( self.__driver, str):
            return self.__driver

    @driver.setter
    def driver( self, value ):
        if value is not None:
            self.__driver = value

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ):
            self.__path = value

    @property
    def connectionstring( self ):
        if isinstance( self.__connectionstring, str ) and self.__connectionstring != '':
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, value ):
        if isinstance( value, str ) and value != '':
            self.__connectionstring = value

    def __init__( self, dataconfig ):
        self.__configuration = dataconfig if isinstance( dataconfig, DataConfig ) else None
        self.__source = dataconfig.source
        self.__provider = dataconfig.provider
        self.__path = dataconfig.getpath( )
        self.__driver = dataconfig.getdriver()
        self.__dsn = dataconfig.source.name + ';'
        self.__connectionstring = dataconfig.getconnectionstring( )

    def connect( self ):
            if self.__provider.name == Provider.Access.name:
                return db.connect( self.__connectionstring )
            elif self.__provider.name == Provider.SqlServer.name:
                return db.connect( self.__connectionstring )
            else:
                return sl.connect( self.__connectionstring )

    def disconnect( self ):
        if self.__connection is not None:
            self.__connection.flush( )
            self.__connection.close( )
            self.__connection = None


# SqlConfig( names, values )
class SqlConfig( ):
    '''SqlConfig( names, values ) provides database
    interaction behavior'''
    __command = None
    __names = None
    __values = None
    __paramstyle = None
    __kvp = None

    @property
    def command( self ):
        if isinstance( self.__command, SQL ):
            return self.__command

    @command.setter
    def command( self, value ):
        if isinstance( value, SQL ):
            self.__command = value

    @property
    def names( self ):
        ''' builds crit from provider index namevaluepairs'''
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, value ):
        ''' builds crit from provider index namevaluepairs'''
        if value is not None and isinstance( value, list ):
            self.__names = value

    @property
    def values( self ):
        ''' builds crit from provider index namevaluepairs'''
        if isinstance( self.__values, tuple ):
            return self.__values

    @values.setter
    def values( self, value ):
        ''' builds crit from provider index namevaluepairs'''
        if isinstance( value, tuple ):
            self.__values = value

    @property
    def paramstyle( self ):
        ''' Property representing the DBI paramstyle'''
        if isinstance( self.__paramstyle, ParamStyle ):
            return self.__paramstyle

    @values.setter
    def paramstyle( self, value ):
        ''' Property representing the DBI paramstyle attribute'''
        if isinstance( value, ParamStyle ):
            self.__paramstyle = value
        else:
            self.__paramstyle = ParamStyle.qmark

    @property
    def keyvaluepairs( self ):
        if isinstance( self.__kvp, dict ):
            return self.__kvp

    @keyvaluepairs.setter
    def keyvaluepairs( self, value ):
        if isinstance( value, dict ):
            self.__kvp = value

    def __init__( self, command = SQL.SELECTALL, names = None, values = None, params  = None ):
        self.__command = command if isinstance( command, SQL ) else SQL.SELECTALL
        self.__names = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__paramstyle = params if isinstance( params, ParamStyle ) else ParamStyle.qmark
        self.__kvp = dict( zip( names,  list( values ) ) )

    def kvpdump( self ):
        '''dump( ) returns string of 'values = index AND' pairs'''
        if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
            pairs = ''
            criteria = ''
            kvp = zip( self.__names, self.__values )
            for k, v in kvp:
                pairs += f'{ k } = \'{ v }\' AND '
            criteria = pairs.rstrip( ' AND ' )
            return criteria

    def wheredump( self ):
        '''wheredump( ) returns a string
        using list arguments names and values'''
        if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
            pairs = ''
            criteria = ''
            for k, v in zip( self.__names, self.__values ):
                pairs += f'{ k } = \'{ v }\' AND '
            criteria = 'WHERE ' + pairs.rstrip( ' AND ' )
            return criteria

    def setdump( self ):
        '''setdump( ) returns a string
        using list arguments names and values'''
        if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
            pairs = ''
            criteria = ''
            for k, v in zip( self.__names, self.__values ):
                pairs += f'{ k } = \'{ v }\', '
            criteria = 'SET ' + pairs.rstrip( ', ' )
            return criteria

    def columndump( self ):
        '''columndump( ) returns a string of columns
        used in select and insert statements from list self.__names'''
        if isinstance( self.__names, list ):
            cols = ''
            columns = ''
            for n in self.__names:
                cols += f'{ n }, '
            columns = '(' + cols.rstrip( ', ' ) + ')'
            return columns

    def valuedump( self ):
        '''valuedump( ) returns a string of values
        used in select statements from list self.__names'''
        if isinstance( self.__values, tuple ):
            vals = ''
            values = ''
            for v in self.__values:
                vals += f'{ v }, '
            values = 'VALUES (' + vals.rstrip( ', ' ) + ')'
            return values


# SqlStatement( dataconfig,  sqlconfig )
class SqlStatement( ):
    '''SqlStatement( dataconfig, sqlconfig ) Class
    represents the values models used in the SQLite database'''
    __command = None
    __sqlconfig = None
    __dataconfig = None
    __source = None
    __provider = None
    __table = None
    __names = None
    __columnnames = None
    __values = None
    __columnvalues = None
    __commandtext = None

    @property
    def provider( self ):
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if isinstance( value, Provider ):
            self.__provider = value
        else:
            self.__provider = Database( 'SQLite' )

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ):
            self.__path = value

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, value ):
        if isinstance( value, SQL ):
            self.__command = value
        else:
            command = SQL( 'SELECT' )
            self.__command = command

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, value ):
        if isinstance( value, str ) and value != '':
            self.__table = value

    @property
    def names( self ):
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, value ):
        if isinstance( value, list ):
            self.__names = value

    @property
    def values( self ):
        if isinstance( self.__values, tuple ):
            return self.__values

    @values.setter
    def values( self, value ):
        if isinstance( value, tuple ):
            self.__values = value

    def __init__( self, dataconfig, sqlconfig ):
        self.__sqlconfig = sqlconfig if isinstance( sqlconfig, SqlConfig ) else None
        self.__dataconfig = dataconfig if isinstance( dataconfig, DataConfig ) else None
        self.__command = sqlconfig.command
        self.__provider = dataconfig.provider
        self.__source = dataconfig.source
        self.__table = dataconfig.table
        self.__names = sqlconfig.names
        self.__values = sqlconfig.values

    def __str__( self ):
        if isinstance( self.__commandtext, str ):
            return self.__commandtext

    def getcommandtext( self ):
        if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
            if self.__command == SQL.SELECTALL:
                self.__commandtext = f'SELECT * FROM { self.__table }' \
                                     + f' { self.__sqlconfig.wheredump( ) };'
                return self.__commandtext
            elif self.__command == SQL.SELECT:
                self.__commandtext = f'SELECT ' + self.__sqlconfig.columndump( ) \
                                     + f' FROM { self.__table }' \
                                     + f' { self.__sqlconfig.wheredump( ) };'
                return self.__commandtext
            elif self.__command == SQL.INSERT:
                self.__commandtext = f'INSERT INTO { self.__table } ' \
                                     + f'{ self.__sqlconfig.columndump( ) } ' \
                                     + f'{ self.__sqlconfig.valuedump( ) };'
                return self.__commandtext
            elif self.__command == SQL.UPDATE:
                self.__commandtext = f'UPDATE { self.__table } ' \
                                     + f'{ self.__sqlconfig.setdump( ) } ' \
                                     + f'{ self.__sqlconfig.valuedump( ) };'
                return self.__commandtext
            elif self.__command == SQL.DELETE:
                self.__commandtext = f'DELETE FROM { self.__table } '\
                                     + f'{ self.__sqlconfig.wheredump( ) };'
                return self.__commandtext
        else:
            if not isinstance( self.__names, list ) or not isinstance( self.__values, tuple ):
                if self.__command == SQL.SELECTALL:
                    self.__commandtext = f'SELECT * FROM { self.__table };'
                    return self.__commandtext
            elif self.__command == 'DELETE':
                self.__commandtext = f'DELETE FROM { self.__table };'


# Badger( connection, sqlstatement )
class Badger( ):
    '''Base class for database interaction'''
    __connection = None
    __sqlstatement = None
    __command = None
    __source = None
    __provider = None
    __path = None
    __connectionstring = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def provider( self ):
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if isinstance( value, Provider ):
            self.__provider = value
        else:
            self.__provider = Database( 'SQLite' )

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ):
            self.__path = value

    @property
    def connection( self ):
        if isinstance( self.__connection, DataConnection ):
            return self.__connection

    @connection.setter
    def connection( self, value ):
        if isinstance( value, DataConnection ):
            self.__connection = value

    @property
    def sqlstatement( self ):
        if isinstance( self.__sqlstatement, SqlStatement ):
            return self.__sqlstatement

    @sqlstatement.setter
    def sqlstatement( self, value ):
        if isinstance( value, SqlStatement ):
            self.__sqlstatement = value

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = SQL( 'SELECT' )
            return cmd

    @command.setter
    def command( self, value ):
        if isinstance( value, SQL ):
            self.__command = value

    @property
    def connectionstring( self ):
        if isinstance( self.__connectionstring, str ):
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, value ):
        if isinstance( value, str ):
            self.__connectionstring = str( value )

    def __init__( self, connection, sqlstatement ):
        self.__connection = connection if isinstance( connection, DataConnection ) else None
        self.__sqlstatement = sqlstatement if isinstance( sqlstatement, SqlStatement ) else None
        self.__source = connection.source
        self.__provider = connection.provider
        self.__command = sqlstatement.command
        self.__path = connection.path
        self.__connectionstring = connection.connectionstring


# SQLiteQuery( connection, sqlstatement )
class SQLiteQuery( Badger ):
    '''SQLiteQuery( value, sqlconfig ) represents
     the budget execution values classes'''
    __driver = None
    __table = None
    __dsn = None
    __query = None
    __data = None
    __frame = None

    @property
    def driver( self ):
        if isinstance( self.__driver, str ):
            return self.__driver

    @driver.setter
    def driver( self, value ):
        if isinstance( value, str ):
            self.__driver = value

    @property
    def data( self ):
        if isinstance( self.__data, ntuple ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, ntuple ):
            self.__data = value

    @property
    def frame( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @data.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def query( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    @query.setter
    def query( self, value ):
        if isinstance( value, str ) and value != '':
            self.__query = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement)
        self.__table = connection.source.name
        self.__driver = connection.driver
        self.__query = sqlstatement.getcommandtext()

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def getdata( self ):
        src = super( ).source
        pro = super( ).provider
        sql = super( ).sqlstatement
        n = sql.names
        v = sql.values
        db = DataConfig( src, pro )
        cmd = SqlConfig( names = n, values = v )
        dcnx = DataConnection( db )
        sql = SqlStatement( db, cmd )
        sqlite = dcnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data

    def getframe( self ):
        src = super( ).source
        pro = super( ).provider
        query = f'SELECT * FROM { src.name }'
        db = DataConfig( src, pro )
        dcnx = DataConnection( db )
        sqlite = dcnx.connect( )
        self.__frame = sqlreader( query, sqlite )
        sqlite.close( )
        return self.__frame


# AccessQuery( connection, sqlstatement )
class AccessQuery( Badger ):
    '''AccessQuery( value, sqlconfig ) class
      represents the budget execution
      values model classes in the MS Access database'''
    __query = None
    __driver = None
    __dsn = None
    __data = None
    __table = None

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def driver( self ):
        if isinstance( self.__driver, str ):
            return self.__driver

    @driver.setter
    def driver( self, value ):
        if value is not None:
            self.__driver = value

    @property
    def query( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    @query.setter
    def query( self, value ):
        if isinstance( value, str ) and value != '':
            self.__query = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement)
        self.__query = sqlstatement.getcommandtext( )
        self.__table = connection.source.name
        self.__driver = r'DRIVER={Microsoft Access Driver( *.mdb, *.accdb )};'
        self.__data = [ ]

    def __str__( self ):
        if isinstance( self.__source, DataConfig ):
            return self.__source.name

    def getdata( self ):
        src = super().source
        pro = super().provider
        sql = super().sqlstatement
        n = sql.names
        v = sql.values
        db = DataConfig( src, pro )
        cmd = SqlConfig( names = n, values = v )
        dcnx = DataConnection( db )
        sql = SqlStatement( db, cmd )
        sqlite = dcnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data

    def getframe( self ):
        src = super( ).source
        pro = super( ).provider
        query = f'SELECT * FROM { src.name }'
        db = DataConfig( src, pro )
        dcnx = DataConnection( db )
        access = dcnx.connect( )
        self.__frame = sqlreader( query, access )
        access.close( )
        return self.__frame


# SqlServerQuery( connection, sqlstatement )
class SqlServerQuery( Badger ):
    '''SqlServerQuery( value, sqlconfig ) object
    represents the values models in the MS SQL Server
    database'''
    __query = None
    __server = None
    __driver = None
    __dsn = None
    __table = None
    __data = None

    @property
    def server( self ):
        if isinstance( self.__server, str ):
            return self.__server

    @server.setter
    def server( self, value ):
        if isinstance( value, str ):
            self.__server = value

    @property
    def driver( self ):
        if isinstance( self.__driver, str ):
            return self.__driver

    @driver.setter
    def driver( self, value ):
        if isinstance( value, str ):
            self.__driver = value

    @property
    def data( self ):
        if isinstance( self.__data, ntuple ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, ntuple ):
            self.__data = value

    @property
    def query( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    @query.setter
    def query( self, value ):
        if isinstance( value, str ) and value != '':
            self.__query = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement)
        self.__query = sqlstatement.getcommandtext()
        self.__table = connection.source.name
        self.__server = r'(LocalDB)\MSSQLLocalDB;'
        self.__driver = r'{SQL Server Native Client 11.0};'

    def __str__( self ):
        if isinstance( self.__source, DataConfig ):
            return self.__source.name

    def getdata( self ):
        src = super( ).source
        pro = super( ).provider
        sql = super( ).sqlstatement
        n = sql.names
        v = sql.values
        db = DataConfig( src, pro )
        cmd = SqlConfig( names = n, values = v )
        dcnx = DataConnection( db )
        sql = SqlStatement( db, cmd )
        sqlite = dcnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# QueryBuilder( source, provider, command,  names, values )
class QueryBuilder( ):
    '''QueryBuilder class generates queries used as the input arguement
    for the DataFactory class. Class contructor initializes object with optional
    arguments ( source: Source, provider: Provider, command: DataCommand,
    names: list, values: tuple )'''
    __names = None
    __values = None
    __command = None
    __source = None
    __provider = None
    __dbconfig = None
    __sqlconfig = None
    __connection = None
    __sqlstatement = None
    __query = None
    __data = None

    @property
    def names( self ):
        '''Provides list of value names'''
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, value ):
        '''Sets the list of value names'''
        if isinstance( value, list ):
            self.__names = value

    @property
    def values( self ):
        '''Provides tuple of value values'''
        if isinstance( self.__values, tuple ):
            return self.__values

    @values.setter
    def values( self, value ):
        '''Sets tuple of value values'''
        if isinstance( value, tuple ):
            self.__values = value

    @property
    def provider( self ):
        '''Gets the provider'''
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, value ):
        '''Sets the provider'''
        if isinstance( value, Provider ):
            self.__provider = value

    @property
    def command( self ):
        '''Gets an instance of the DataCommand object'''
        if isinstance( self.__command, SQL ):
            return self.__command

    @command.setter
    def command( self, value ):
        '''Set the command property to a DataCommand instance'''
        if isinstance( value, SQL ):
            self.__command = value
        else:
            command = SQL( 'SELECT' )
            self.__command = command

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def dataconfiguration( self ):
        if isinstance( self.__dbconfig, DataConfig ):
            return self.__dbconfig

    @dataconfiguration.setter
    def dataconfiguration( self, value ):
        if isinstance( value, DataConfig ):
            self.__dbconfig = value

    @property
    def sqlconfiguration( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlconfig, SqlConfig ):
            return self.__sqlconfig

    @sqlconfiguration.setter
    def sqlconfiguration( self, value ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( value, SqlConfig ):
            self.__sqlconfig = value

    @property
    def query( self ):
        '''Gets an instance of the DataCommand object'''
        if isinstance( self.__query, str ):
            return self.__query

    @query.setter
    def query( self, value ):
        '''Set the command property to a DataCommand instance'''
        if isinstance( value, str ):
            self.__query = value

    def __init__( self, source = None, provider = Provider.SQLite,
                  command = SQL.SELECTALL, names = None, values = None ):
        self.__name = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__command = command if isinstance( command, SQL ) else None
        self.__source = source if isinstance( source, Source ) else None
        self.__provider = provider if isinstance( provider, Provider ) else None
        self.__dbconfig = DataConfig( self.__source, self.__provider )
        self.__connection = DataConnection( self.__dbconfig )
        self.__sqlconfig = SqlConfig( self.__command, self.__names, self.__values )
        self.__sqlstatement = SqlStatement( self.__dbconfig, self.__sqlconfig )
        self.__query = self.__sqlstatement.getcommandtext( )


# DataFactory( provider, source, command, names, values )
class DataFactory( ):
    '''DataFactory class creates factory method providing
    application data. Constructor creates object using
    optional arguments ( provider: Provider, source: Source,
    command: DataCommand, names: list, values: tuple ) '''
    __names = None
    __values = None
    __command = None
    __source = None
    __provider = None
    __dbconfig = None
    __sqlconfig = None
    __connection = None
    __sqlstatement = None
    __query = None
    __data = None

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, DataConfig ):
            self.__source = value
        else:
            self.__source = DataConfig( 'StatusOfFunds' )

    @property
    def provider( self ):
        '''Gets the provider'''
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, value ):
        '''Sets the provider'''
        if isinstance( value, Provider ):
            self.__provider = value
        else:
            self.__provider = Provider.SQLite

    @property
    def command( self ):
        '''Gets an instance of the DataCommand object'''
        if isinstance( self.__command, SQL ):
            return self.__command

    @command.setter
    def command( self, value ):
        '''Set the command property to a DataCommand instance'''
        if isinstance( value, SQL ):
            self.__command = value
        else:
            command = SQL( 'SELECT' )
            self.__command = command

    @property
    def names( self ):
        '''Provides list of value names'''
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, value ):
        '''Sets the list of value names'''
        if isinstance( value, list ):
            self.__names = value

    @property
    def values( self ):
        '''Provides tuple of value values'''
        if isinstance( self.__values, tuple ):
            return self.__values

    @values.setter
    def values( self, value ):
        '''Sets tuple of value values'''
        if isinstance( value, tuple ):
            self.__values = value

    @property
    def dataconfiguration( self ):
        if isinstance( self.__dbconfig, DataConfig ):
            return self.__dbconfig

    @dataconfiguration.setter
    def dataconfiguration( self, value ):
        if isinstance( value, DataConfig ):
            self.__dbconfig = value

    @property
    def sqlconfiguration( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlconfig, SqlConfig ):
            return self.__sqlconfig

    @sqlconfiguration.setter
    def sqlconfiguration( self, value ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( value, SqlConfig ):
            self.__sqlconfig = value

    def __init__( self, source, provider, command = SQL.SELECTALL,
                  names = None, values = None ):
        self.__source = source if isinstance( source, Source ) else None
        self.__provider = provider if isinstance( provider, Provider ) else None
        self.__command = command if isinstance( command, SQL ) else SQL.SELECTALL
        self.__name = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__dbconfig = DataConfig( self.__source, self.__provider )
        self.__connection = DataConnection( self.__dbconfig )
        self.__sqlconfig = SqlConfig( self.__command, self.__names, self.__values )
        self.__sqlstatement = SqlStatement( self.__dbconfig, self.__sqlconfig )

    def create( self ):
        if self.__provider == Provider.SQLite:
            sqlite = SQLiteQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in sqlite.getdata( ) ]
            return self.__data
        elif self.__provider == Provider.Access:
            access = AccessQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in access.getdata( ) ]
            return self.__data
        elif self.__provider == Provider.SqlServer:
            sqlserver = SqlServerQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in sqlserver.getdata( ) ]
            return self.__data
        else:
            sqlite = SQLiteQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in sqlite.getdata( ) ]
            return self.__data


# DataSchema( name, datatype )
class DataSchema( ):
    '''Provides the name and data types used by the
    DataColumn class.  Contructor uses opetional
    arguments ( name: str, datatype: type, source: Source )'''
    __name = None
    __coltype = None
    __source = None
    __ordinal = None

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def datatype( self ):
        if isinstance( self.__type, object ):
            return self.__type

    @datatype.setter
    def datatype( self, value ):
        if isinstance( value, object ):
            self.__type = value

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def ordinal( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @ordinal.setter
    def ordinal( self, value ):
        if isinstance( value, int ):
            self.__id = value

    def __init__( self, name = '', datatype = None ):
        self.__name = name if isinstance( name, str ) and name != '' else November
        self.__coltype = datatype if isinstance( datatype, object ) else None


# DataColumn( name, datatype, value, series  )
class DataColumn(  ):
    '''Defines the DataColumn Class providing schema information.
    Constructor uses optional arguments ( name: str, datatype: type,
     value: object, series: DataSeries )'''
    __series = None
    __row = None
    __name = None
    __value = None
    __label = None
    __id = None
    __type = None
    __caption = None
    __id = None
    __table = None
    __frame = None

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def value( self ):
        if isinstance( self.__value, object ):
            return self.__value

    @value.setter
    def value( self, value ):
        if isinstance( value, object ):
            self.__value = value

    @property
    def datatype( self ):
        if isinstance( self.__type, object ):
            return self.__type

    @datatype.setter
    def datatype( self, value ):
        if isinstance( value, object ):
            self.__type = value

    @property
    def caption( self ):
        if isinstance( self.__caption, str ) and self.__caption != '':
            return self.__caption

    @caption.setter
    def caption( self, value ):
        if isinstance( value, str ) and value != '':
            self.__caption = value

    @property
    def ordinal( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @ordinal.setter
    def ordinal( self, value ):
        if isinstance( value, int ):
            self.__id = value

    @property
    def id( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__id = value

    @property
    def table( self ):
        if isinstance( self.__table, DataTable ):
            return self.__table

    @table.setter
    def table( self, value ):
        if isinstance( value, DataTable ):
            self.__table = value

    @property
    def row( self ):
        if isinstance( self.__row, DataRow ):
            return self.__row

    @row.setter
    def row( self, value ):
        if isinstance( value, DataRow ):
            self.__series = value
            self.__row = self.__series

    @property
    def frame( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @data.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    def __init__( self, name = None, datatype = None,
                  value = None, series = None, source = None ):
        self.__name = name if isinstance( name, str ) and name != '' else None
        self.__label = name
        self.__caption = name
        self.__type = datatype if isinstance( datatype, type ) else None
        self.__value = value if isinstance( value, object ) else None
        self.__series = series if isinstance( series, pd.Series ) else None
        self.__id = series.index.get_loc( name )
        self.__ordinal = self.__id
        self.__source = source if isinstance( source, Source ) else None
        self.__table = source.name if isinstance( source, Source ) else None
        self.__frame = None

    def __str__( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    def isnumeric( self ):
        if not isinstance( self.__value, str ):
            return True
        else:
            return False

    def istext( self ):
        if isinstance( self.__value, str ):
            return True
        else:
            return False

    def getdata( self ):
        src = self.__source
        name = self.__name
        pro = Provider.SQLite
        query = f'SELECT * FROM { src.name }'
        db = DataConfig( src, pro )
        dcnx = DataConnection( db )
        sqlite = dcnx.connect( )
        self.__frame = sqlreader( query, sqlite )
        data = [ i for i in self.__frame ]
        sqlite.close( )
        return data

    def getframe( self ):
        src = self.__source
        name = self.__name
        pro = Provider.SQLite
        query = f'SELECT * FROM { src.name }'
        db = DataConfig( src, pro )
        dcnx = DataConnection( db )
        sqlite = dcnx.connect( )
        self.__frame = sqlreader( query, sqlite )
        frame = DataFrame( self.__frame )
        sqlite.close( )
        return frame


# DataRow( names, values, source )
class DataRow( ):
    '''Defines the DataRow Class with optional arguments
    ( names: list, values: list, source: Source )'''
    __source = None
    __names = None
    __items = None
    __data = None
    __values = None
    __key = None
    __id = None

    @property
    def id( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__id = value

    @property
    def key( self ):
        if isinstance( self.__key, str ) and self.__key != '':
            return self.__key

    @key.setter
    def key( self, value ):
        if isinstance( value, int ) and value != '':
            self.__key = value

    @property
    def data( self ):
        if isinstance( self.__data, list ) and len( self.__data ) > 0:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__data = value

    @property
    def items( self ):
        if isinstance( self.__items, tuple ):
            return self.__items

    @items.setter
    def items( self, value ):
        if isinstance( value, tuple ):
            self.__items = value

    @property
    def names( self ):
        if isinstance( self.__names, list ) and len( self.__names ) > 0:
            return self.__names

    @names.setter
    def names( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__names = value

    @property
    def values( self ):
        if isinstance( self.__values, list ) and len( self.__values ) > 0:
            return self.__values

    @values.setter
    def values( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__values = value

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    def __init__( self, names = None, values = None, source = None ):
        self.__source = source if isinstance( source, Source ) else None
        self.__names = names if isinstance( names, list ) else None
        self.__values = value if isinstance( values, list ) else None
        self.__items = zip( names, values )
        self.__key = str( self.__names[ 0 ] ) if isinstance( self.__names, list ) else None
        self.__id = int( self.__values[ 0 ] ) if isinstance( self.__values, list ) else None

    def __str__( self ):
        if isinstance( self.__id, int ) and self.__id > -1:
            return 'Row ID: ' + str( self.__id )


# DataTable( columns, rows, source, dataframe )
class DataTable( ):
    '''Defines the DataTable Class with optional arguments
    ( columns: list( str ), rows: list( tuple ), source: Source,
     dataframe: DataFrame )'''
    __name = None
    __data = None
    __frame = None
    __rows = None
    __columns = None
    __schema = None
    __source = None

    @property
    def name( self ):
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = str( value )

    @property
    def data( self ):
        if isinstance( self.__rows, list( tuple ) ):
            return self.__rows

    @data.setter
    def data( self, value ):
        if isinstance( value, list( tuple ) ):
            self.__rows = value

    @property
    def frame( self ):
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @frame.setter
    def frame( self, value ):
        if isinstance( value, pd.DataFrame ):
            self.__frame = value

    @property
    def schema( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @schema.setter
    def schema( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    @property
    def rows( self ):
        if isinstance( self.__rows, list ) and len( self.__rows ) > 0:
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if isinstance( value, list ):
            self.__rows = value

    @property
    def columns( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    def __init__( self, columns = None, rows = None,
                  source = None,  dataframe = None ):
        self.__frame = dataframe if isinstance( dataframe, pd.DataFrame ) else None
        self.__name = name if isinstance( name, str ) and name != '' else None
        self.__rows = [ tuple( r ) for r in dataframe.items ]
        self.__data = self.__rows
        self.__columns = [ str( c ) for c in columns ] if isinstance( columns, list ) else None
        self.__schema = [ DataColumn( c ) for c in columns ] if isinstance( columns, list ) else None

    def __str__( self ):
        if self.__name is not None:
            return self.__name


# BudgetData( src )
class BudgetData( ):
    '''Class representing pandas DataFrame'''
    __source = None
    __name = None
    __path = None
    __connection = None
    __sql = None
    __data = None
    __frame = None
    __columns = None
    __index = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def name( self ):
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = str( value )

    @property
    def data( self ):
        if isinstance( self.__data, list( tuple ) ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list( tuple ) ):
            self.__data = value

    @property
    def query( self ):
        if isinstance( self.__sql, str ) and self.__sql != '':
            return self.__sql

    @query.setter
    def query( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sql = value

    @property
    def columns( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    @property
    def index( self ):
        if isinstance( self.__index, pd.DataFrame.id ):
            return self.__index

    @index.setter
    def index( self, value ):
        if isinstance( value, pd.DataFrame.id ):
            self.__index = value

    @property
    def frame( self ):
        if isinstance( self.__data, DataFrame ):
            return self.__data

    @frame.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    def __init__( self, src ):
        self.__source = src if isinstance( src, Source ) else None
        self.__name = src.name if isinstance( src, Source ) else None
        self.__path = DataConfig( src, Provider.SQLite ).getpath( )
        self.__sql = f'SELECT * FROM { src.name };'

    def getframe( self ):
        path = self.__path
        src = self.__source
        table = src.name
        conn = sl.connect( path )
        sql = f'SELECT * FROM { table };'
        frame = sqlreader( sql, conn )
        return frame
