import collections
import sqlite3 as sl
import pandas as pd
import pyodbc as db
import os
from collections import namedtuple as ntuple
from Static import *
from numpy import ndarray


''' DataConfig( source, provider ) '''
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
    __sqlitedriver = None
    __sqlitedatapath = None
    __sqlitereferencepath = None
    __table = None
    __name = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, Source ):
            self.__source = src

    @property
    def provider( self ):
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, pvdr ):
        if isinstance( pvdr, Provider ):
            self.__provider = pvdr

    @property
    def table( self ):
        if isinstance( self.__table, str ) and self.__table != '':
            return self.__table

    @table.setter
    def table( self, name ):
        if isinstance( name, str ) and name in self.__data:
            self.__table = name
        elif name in self.__references:
            self.__table = name
        else:
            self.__table = None

    def isdata( self ):
        '''Determines if the values source is a memeber of the values models'''
        if self.__table is not None \
                and self.__table in self.__data:
            return True
        else:
            return False

    def isreference( self ):
        '''Determines if the values source is a memeber of the reference models'''
        if self.__table is not None  \
                and self.__table in self.__references:
            return True
        else:
            return False

    def getdriver( self ):
        if isinstance( self.__provider, Provider ) and self.__provider != Provider.NS:
            if self.__provider == Provider.SQLite:
                return self.__sqlitedriver
            elif self.__provider == Provider.Access:
                return self.__accessdriver
            elif self.__provider == Provider.SqlServer:
                return self.__sqldriver
            else:
                return self.__sqlitedriver

    def getpath( self ):
        if self.__provider == Provider.SQLite and self.isreference():
            return self.__sqlitereferencepath
        elif self.__provider == Provider.SQLite and self.isdata():
            return self.__sqlitedatapath
        elif self.__provider == Provider.Access and self.isdata():
            return self.__accessdatapath
        elif self.__provider == Provider.Access and self.isreference():
            return self.__accessreferencepath
        elif self.__provider == Provider.SqlServer and self.isdata():
            return self.__sqldatapath
        elif self.__provider == Provider.SqlServer and self.isreference():
            return self.__sqlreferencepath
        else:
            return self.__sqlitedatapath

    def __init__( self, src, prov ):
        '''Constructor for the DataConfig class providing
        values conn details'''
        self.__data = [ 'Allocations', 'Actuals', 'ApplicationTables', 'Apportionments', 'AppropriationDocuments',
                       'BudgetaryResourceExecution', 'BudgetControls', 'BudgetDocuments', 'BudgetOutlays',
                       'CarryoverEstimates', 'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                       'Deobligations', 'Defactos', 'DocumentControlNumbers',
                       'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                       'ObjectClassOutlays', 'CarryoverOutlays',
                       'QueryDefinitions', 'RegionalAuthority', 'SpendingRates',
                       'GrowthRates', 'ReimbursableAgreements', 'ReimbursableFunds',
                       'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations' 
                       'Reprogrammings', 'SiteActivity', 'SiteProjectCodes',
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
        self.__provider = prov if isinstance( prov, Provider ) else Provider.SQLite
        self.__source = src if isinstance( src, Source ) else None
        self.__table = self.__source.name if isinstance( self.__source, Source ) else None
        self.__sqlitedriver = r'DRIVER=SQLite3 ODBC Driver;'
        self.__sqlitedatapath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\dataconfig\sqlite\datamodels\Data.dataconfig;'
        self.__sqlitereferencepath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\dataconfig\sqlite\referencemodels\References.dataconfig;'
        self.__accessdriver = r'DRIVER={Microsoft Access Driver ( *.mdb, *.accdb ) };'
        self.__accessdatapath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\access\datamodels\Data.accdb;'
        self.__accessreferencepath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\access\referencemodels\References.accdb;'
        self.__sqldatapath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\mssql\datamodels\Data.mdf;'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;'
        self.__sqlreferencepath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\mssql\referencemodels\References.mdf;'

    def __str__( self ):
        if isinstance( self.__table, str ) and self.__table != '':
            return self.__table


''' DataConnection( dataconfig ) '''
class DataConnection(  ):
    '''DataConnection( dataconfig, path = '' ) initializes
    object used to connect to Budget databases'''
    __configuration = None
    __provider = None
    __source = None
    __driver = None
    __dsn = None
    __path = None
    __connectionstring = None
    __connection = None
    __isopen = None

    @property
    def configuration( self ):
        if isinstance( self.__configuration, DataConfig ):
            return self.__configuration

    @configuration.setter
    def configuration( self, cfg ):
        if isinstance( cfg, DataModeel ):
            self.__configuration = cfg

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @property
    def provider( self ):
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @property
    def driver( self ):
        if isinstance( self.__driver, str):
            return self.__driver

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @property
    def connectionstring( self ):
        if isinstance( self.__provider, Provider ) and self.__provider == Provider.SQLite:
            self.__connectionstring = f'Database={ self.__path }'
            return self.__connectionstring
        elif isinstance( self.__provider, Provider ) and self.__provider == Provider.Access:
            self.__connectionstring = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};' \
                                      + f'DBQ={ self.__path }'
            return self.__connectionstring
        elif isinstance( self.__provider, Provider ) and self.__provider == Provider.SqlServer:
            self.__connectionstring = r'DRIVER={ODBC Driver 17 for SQL Server};' \
                                      + f'DATABASE={ self.__path }'
            return self.__connectionstring
        else:
            self.__connectionstring = f'DRIVER=SQLite3 ODBC Driver;SERVER=localhost;' \
                                      + f'Database={self.__path}'
            return self.__connectionstring

    def __init__( self, dataconfig ):
        self.__configuration = dataconfig if isinstance( dataconfig, DataConfig ) else None
        self.__source = dataconfig.source if isinstance( dataconfig.source, Source ) else None
        self.__provider = dataconfig.provider if isinstance( dataconfig.provider, Provider ) else None
        self.__path = self.__configuration.getpath( )
        self.__driver = self.__configuration.getdriver( )
        self.__dsn = self.__source.name + ';'
        self.__connectionstring = 'Provider=' + self.__provider.name + ';' \
                                  + self.__dsn + 'DBQ=' + self.__path

    def open( self ):
            __path = self.__provider.getpath( )
            if self.__provider.name == Provider.SQLite.name:
                self.__connection = sl.connect( __path )
                if isinstance( self.__connection, Connection ):
                    self.__isopen = True
                    return self.__connection
            elif self.__provider.name != Provider.SQLite.name:
                self.__connection = db.connect( self.__connectionstring )
                if isinstance( self.__connection, db.Connection ):
                    self.__isopen = True
                    return self.__connection
            else:
                self.__connection = sl.connect( __path )
                if isinstance( self.__connection, Connection ):
                    self.__isopen = True
                    return self.__connection

    def close( self ):
        if self.__isopen == True:
            self.__connection.close( )
            self.__isopen = False


''' SqlConfig( command, names, values ) '''
class SqlConfig( ):
    '''SqlConfig( command, cols, values, paramstyle  ) provides the
     predicate provider index pairs for sqlconfig queries'''
    __predicate = None
    __names = None
    __values = None
    __command = None
    __paramstyle = None

    @property
    def command( self ):
        if isinstance( self.__command, Command ):
            return self.__command

    @command.setter
    def command( self, cmd: CommandType ):
        if isinstance( cmd, Command ):
            self.__command = cmd

    @property
    def names( self ):
        ''' builds crit from provider index namevaluepairs'''
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, keys: list ):
        ''' builds crit from provider index namevaluepairs'''
        if keys is not None and isinstance( keys, list ):
            self.__names = keys

    @property
    def values( self ):
        ''' builds crit from provider index namevaluepairs'''
        if isinstance( self.__values, tuple ):
            return self.__values

    @values.setter
    def values( self, vals: tuple  ):
        ''' builds crit from provider index namevaluepairs'''
        if isinstance( vals, tuple ):
            self.__values = vals

    @property
    def param( self ):
        ''' Property representing the DBI paramstyle'''
        if isinstance( self.__paramstyle, ParamStyle ):
            return self.__paramstyle

    @values.setter
    def param( self, prms: ParamStyle  ):
        ''' Property representing the DBI paramstyle attribute'''
        if isinstance( prms, ParamStyle ):
            self.__paramstyle = prms
        else:
            self.__paramstyle = ParamStyle.qmark

    @property
    def pairs( self ):
        if isinstance( self.__predicate, dict ):
            return self.__predicate

    @pairs.setter
    def pairs( self, kvp: dict ):
        if isinstance( kvp, dict ):
            map = dict( )
            for k, v in kvp.items( ):
                    map.update( k, v )
            self.__predicate = map

    def __init__( self, command, names, values, params  = None ):
        self.__command = command if isinstance( command, Command ) else Command.SELECTALL
        self.__names = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__paramstyle = params if isinstance( params, ParamStyle ) else ParamStyle.qmark
        self.__predicate = self.__map( )

    def __map( self ):
        '''__map( ) returns dictionary built from
        lists self.__names and self.__values'''
        if isinstance( self.__names, list ) and isinstance( self.__values, list ):
            map = dict( )
            kvp = zip( self.__names, self.__values )
            for k, v in kvp:
                kvp = { k: v }
                map.update( kvp )
            return map

    def pairdump( self ):
        '''dump( ) returns string of 'values = index AND' pairs'''
        if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
            pairs = ''
            criteria = ''
            kvp = zip( self.__names, self.__values )
            for k, v in kvp:
                pairs += f'{ k } = { v } AND '
            criteria = pairs.rstrip( ' AND ' )
            return criteria

    def wheredump( self ):
        '''pairdump( names, values) returns a string
        using list arguments names and values'''
        if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
            pairs = ''
            criteria = ''
            for k, v in zip( self.__names, self.__values ):
                pairs += f'{ k } = { v } AND '
            criteria = 'WHERE ' + pairs.rstrip( ' AND ' )
            return criteria

    def setdump( self ):
        '''setdump( ) returns a string
        using list arguments names and values'''
        if isinstance( self.__names, list ) and isinstance( self.__values, list ):
            pairs = ''
            criteria = ''
            for k, v in zip( self.__names, self.__values ):
                pairs += f'{ k } = { v }, '
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
        if isinstance( self.__values, list ):
            vals = ''
            values = ''
            for v in self.__values:
                vals += f'{ v }, '
            values = '(' + vals.rstrip( ', ' ) + ')'
            return values


''' SqlStatement(  dataconfig,  sqlconfig ) '''
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
    def provider( self, pvr ):
        if isinstance( pvr, Provider  ):
            self.__provider = pvr
        else:
            self.__provider = Database( 'SQLite' )

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, Command ):
            self.__command = cmd
        else:
            command = Command( 'SELECT' ) 
            self.__command = command

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, DataConfig ):
            self.__source = src
        else:
            self.__source = DataConfig( 'StatusOfFunds' )

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, name ):
        if isinstance( name, str ) and name != '':
            self.__table = name

    @property
    def names( self ):
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, cols ):
        if isinstance( cols, list ):
            self.__names = cols

    @property
    def values( self ):
        if isinstance( self.__values, list ):
            return self.__values

    @values.setter
    def values( self, vals ):
        if isinstance( vals, list ):
            self.__values = vals

    def __init__( self, dataconfig, sqlconfig ):
        self.__sqlconfig = sqlconfig if isinstance( sqlconfig, SqlConfig ) else None
        self.__dataconfig = dataconfig if isinstance( dataconfig, DataConfig ) else None
        self.__command = sqlconfig.command
        self.__provider = self.__dataconfig.provider
        self.__source = self.__dataconfig.source
        self.__table = self.__source.name
        self.__names = self.__sqlconfig.names
        self.__values = self.__sqlconfig.values

    def __str__( self ):
        if isinstance( self.__commandtext, str ):
            return self.__commandtext

    def commandtext( self ):
        if self.__command == Command.SELECTALL:
            self.__commandtext = f'SELECT ALL FROM { self.__table }' \
                                 + f'{ self.__sqlconfig.wheredump( ) };'
            return self.__commandtext
        elif self.__command == Command.SELECT:
            self.__commandtext = f'SELECT ' + self.__sqlconfig.columndump( ) \
                                 + f' FROM { self.__table }' \
                                 + f'{ self.__sqlconfig.wheredump( ) };'
            return self.__commandtext
        elif self.__command == 'INSERT':
            self.__commandtext = 'INSERT INTO ' + self.__table \
                                 + f'{ self.__sqlconfig.columndump( ) }' \
                                 + f'VALUES { self.__sqlconfig.valuedump( ) }'
        elif self.__command == 'DELETE':
            self.__commandtext = 'DELETE FROM ' + self.__table \
                                 + f'( { self.__sqlconfig.wheredump( ) };'


''' SQLiteQuery( connection, sqlstatement ) '''
class SQLiteQuery( ):
    '''SQLiteQuery( conn, sqlconfig ) represents
     the budget execution values classes'''
    __connection = None
    __path = None
    __driver = None
    __connectionstring = None
    __data = None
    __sqlstatement = None
    __table = None
    __dsn = None
    __command = None

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, path ):
        if isinstance( path, str ):
            self.__path = path

    @property

    def driver( self ):
        if isinstance( self.__driver, str ):
            return self.__driver

    @driver.setter
    def driver( self, driver ):
        if isinstance( driver, str ):
            self.__driver = driver

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, source ):
        if isinstance( source, Source):
            self.__source = source

    @property
    def connectionstring( self ):
        if isinstance( self.__connectionstring, str ):
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, conn ):
        if isinstance( conn, str ):
            self.__connectionstring = str( conn )

    @property
    def data( self ):
        if isinstance( self.__data, ntuple ):
            return self.__data

    @data.setter
    def data( self, data ):
        if isinstance( data, ntuple ):
            self.__data = data

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = Command( 'SELECT' ) 
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, Command ):
            self.__command = cmd

    def __init__( self, conn: DataConnection, sql: SqlStatement ):
        self.__connection = conn if isinstance( conn, DataConnection ) else None
        self.__sqlstatement = sql if isinstance( sql, SqlStatement ) else None
        self.__table = self.__sqlstatement.source.name
        self.__path = self.__connection.path
        self.__driver = self.__sqlstatement.getdriver( )
        self.__command = self.__sqlstatement.command
        self.__connectionstring = self.__path

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def getdata( self ):
        __query = self.__sqlstatement.commandtext()
        __conn = self.__connection.open()
        __cursor = __conn.execute( __query )
        return __cursor.fetchall()


''' AccessQuery( connection, sqlstatement ) '''
class AccessQuery( ):
    '''AccessQuery( conn, sqlconfig ) class
      represents the budget execution
      values model classes in the MS Access database'''
    __path = None
    __connection = None
    __sqlstatement = None
    __driver = None
    __dsn = None
    __connectionstring = None
    __data = None
    __source = None
    __table = None
    __command = None

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, path ):
        if isinstance( path, str ):
            self.__path = path

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, Source ):
            self.__source = src

    @property
    def connectionstring( self ):
        if isinstance( self.__connectionstring, str ):
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, conn ):
        if isinstance( conn, str ):
            self.__connectionstring = conn

    @property
    def data( self ):
        if isinstance( self.__data, ntuple ):
            return self.__data

    @data.setter
    def data( self, data ):
        if isinstance( data, ntuple ):
            self.__data = data

    @property
    def driver( self ):
        if isinstance( self.__driver, str ):
            return self.__driver

    @driver.setter
    def driver( self, name ):
        if name is not None:
            self.__driver = name

    @property
    def command( self ):
        if isinstance( self.__command, Command ):
            return self.__command

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, Command ):
            self.__command = cmd

    def __init__( self, connection, sqlstatement ):
        self.__connection = connection if isinstance( connection, DataConnection ) else None
        self.__sqlstatement = sqlstatement if isinstance( sqlstatement, SqlStatement ) else None
        self.__source = self.__sqlstatment.source
        self.__table = self.__source.table.name
        self.__driver = r'DRIVER={Microsoft Access Driver( *.mdb, *.accdb )};'
        self.__path = self.__connection.path
        self.__command = self.__sqlstatment.command

    def __str__( self ):
        if isinstance( self.__source, DataConfig ):
            return self.__source.name

    def getdata( self ):
        __query = self.__sqlstatement.commandtext()
        __conn = self.__connection.open()
        __cursor = __conn.execute( __query )
        return __cursor.fetchall()


''' SqlServerQuery( connection, sqlstatement ) '''
class SqlServerQuery( ):
    '''SqlServerQuery( conn, sqlconfig ) object
    represents the values models in the MS SQL Server
    database'''
    __connection = None
    __sqlstatment = None
    __server = None
    __driver = None
    __dsn = None
    __source = None
    __table = None
    __path = None
    __data = None
    __recordset = None
    __connectionstring = None
    __command = None

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return  self.__path

    @path.setter
    def path( self, path ):
        if isinstance( path, str ):
            self.__path = path

    @property
    def server( self ):
        if isinstance( self.__server, str ):
            return self.__server

    @server.setter
    def server( self, path ):
        if isinstance( path, str ):
            self.__server = path

    @property
    def driver( self ):
        if isinstance( self.__driver, str ):
            return self.__driver

    @driver.setter
    def driver( self, drvr ):
        if isinstance( drvr, str ):
            self.__server = drvr

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, source ):
        if isinstance( source, Source ):
            self.__source = source

    @property
    def connectionstring( self ):
        if isinstance( self.__connectionstring, str ):
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, cxstring ):
        if isinstance( cxstring, str ):
            self.__connectionstring = cxstring

    @property
    def connection( self ):
        if isinstance( self.__connection, Connection ):
            return self.__connection

    @connection.setter
    def connection( self, conn ):
        if isinstance( conn, DataConnection ):
            self.__connection = conn

    @property
    def data( self ):
        if isinstance( self.__data, ntuple ):
            return self.__data

    @data.setter
    def data( self, data ):
        if isinstance( data, ntuple ):
            self.__data = data

    @property
    def command( self ):
        if isinstance( self.__command, Command):
            return self.__command

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, Command ):
            self.__command = cmd

    def __init__( self, connection, sqlstatement ):
        self.__connection = connection if isinstance( connection, DataConnection ) else None
        self.__sqlstatment = sqlstatement if isinstance( sqlstatement, SqlStatement ) else None
        self.__source = self.__sqlstatment.source
        self.__table = self.__source.name
        self.__server = r'(LocalDB)\MSSQLLocalDB;'
        self.__driver = r'{SQL Server Native Client 11.0};'
        self.__command = self.__sqlstatment.command
        self.__path = self.__connection.path

    def __str__( self ):
        if isinstance( self.__source, DataConfig ):
            return self.__source.name

    def getdata( self ):
        if isinstance( self.__connection, DataConnection ):
            __connection = self.__connection.open()
            __cursor = __connection.cursor()
            self.__data = __cursor.fetchall
            return self.__data


''' QueryBuilder( source, provider, command,  names, values ) '''
class QueryBuilder( ):
    '''QueryBuilder( source, provider, command, names, values )
    initializes object used as argument for the DataFactory'''
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
        '''Provides list of name names'''
        if isinstance( self.__names, list ):
            return self.__names

    @names.setter
    def names( self, names ):
        '''Sets the list of name names'''
        if isinstance( names, list ):
            self.__names = names

    @property
    def values( self ):
        '''Provides tuple of name values'''
        if isinstance( self.__values, tuple ):
            return self.__values

    @values.setter
    def values( self, values ):
        '''Sets tuple of name values'''
        if isinstance( values, tuple ):
            self.__values = values

    @property
    def provider( self ):
        '''Gets the provider'''
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, pvr ):
        '''Sets the provider'''
        if isinstance( pvr, Provider  ):
            self.__provider = pvr
        else:
            self.__provider = Provider.SQLite

    @property
    def command( self ):
        '''Gets an instance of the DataCommand object'''
        if isinstance( self.__command, Command ):
            return self.__command

    @command.setter
    def command( self, cmd ):
        '''Set the command property to a DataCommand instance'''
        if isinstance( cmd, Command ):
            self.__command = cmd
        else:
            command = Command( 'SELECT' )
            self.__command = command

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, DataConfig ):
            self.__source = src
        else:
            self.__source = DataConfig( 'StatusOfFunds' )

    @property
    def dataconfig( self ):
        if isinstance( self.__dbconfig, DataConfig ):
            return self.__dbconfig

    @dataconfig.setter
    def dataconfig( self, dbconfig ):
        if isinstance( dbconfig, DataConfig ):
            self.__dbconfig = dbconfig

    @property
    def sqlconfig( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlconfig, SqlConfig ):
            return self.__sqlconfig

    @sqlconfig.setter
    def sqlconfig( self, sqlconfig ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( sqlconfig, SqlConfig ):
            self.__sqlconfig = sqlconfig

    def __init__( self, source = None, provider = Provider.SQLite,
                  command = Command.SELECTALL, names = None, values = None ):
        self.__name = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__command = command if isinstance( command, Command ) else None
        self.__source = source if isinstance( source, Source ) else None
        self.__provider = provider if isinstance( provider, Provider ) else None
        self.__dbconfig = DataConfig( self.__source, self.__provider )
        self.__connection = DataConnection( self.__dbconfig )
        self.__sqlconfig = SqlConfig( self.__command, self.__names, self.__values )
        self.__sqlstatement = SqlStatement( self.__dbconfig, self.__sqlconfig )


''' DataFactory( querybuilder ) '''
class DataFactory( ):
    '''DataFactory( QueryBuilder ) object
    provides factory method for source values'''
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
        '''Provides list of name names'''
        if isinstance( self.__names, list ):
            return self.__names

    @property
    def values( self ):
        '''Provides tuple of name values'''
        if isinstance( self.__values, tuple ):
            return self.__values

    @property
    def provider( self ):
        '''Gets the provider'''
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @property
    def command( self ):
        '''Gets an instance of the DataCommand object'''
        if isinstance( self.__command, Command ):
            return self.__command

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @property
    def dataconfig( self ):
        if isinstance( self.__dbconfig, DataConfig ):
            return self.__dbconfig

    @property
    def sqlconfig( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlconfig, SqlConfig ):
            return self.__sqlconfig

    def __init__( self, querybuilder ):
        self.__query = querybuilder if isinstance( querybuilder, QueryBuilder ) else None
        self.__name = querybuilder.names if isinstance( querybuilder.names, list ) else None
        self.__values = querybuilder.values if isinstance( querybuilder.values, tuple ) else None
        self.__command = querybuilder.command if isinstance( querybuilder.command, Command ) else None
        self.__source = querybuilder.source if isinstance( querybuilder.source, Source ) else None
        self.__provider = querybuilder.provider if isinstance( querybuilder.provider, Provider ) else None
        self.__dbconfig = DataConfig( self.__source, self.__provider )
        self.__connection = DataConnection( self.__dbconfig )
        self.__sqlconfig = SqlConfig( self.__command, self.__names, self.__values )
        self.__sqlstatement = SqlStatement( self.__dbconfig, self.__sqlconfig )

    def create( self ):
        if self.__provider == Provider.SQLite:
            __query = SQLiteQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in __query.getdata( ) ]
            return self.__data
        elif self.__provider == Provider.Access:
            __query = AccessQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in __query.getdata( ) ]
            return self.__data
        elif self.__provider == Provider.SqlServer:
            __query = SqlServerQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in __query.getdata( ) ]
            return self.__data
        else:
            __query = SQLiteQuery( self.__connection, self.__sqlstatement )
            self.__data = [ tuple( i ) for i in __query.getdata( ) ]
            return self.__data


''' DataColumn( name,  values ) '''
class DataColumn( pd.Series ):
    '''Defines the DataColumn Class'''
    __series = None
    __source = None
    __row = None
    __name = None
    __values = None
    __labels = None
    __index = None
    __type = None
    __caption = None
    __id = None
    __table = None
    __data = None

    @property
    def name( self ):
        if isinstance( self.__name, pd.Series.name ):
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, pd.Series.name ):
            self.__name = name

    @property
    def values( self ):
        if isinstance( self.__values, ndarray ):
            return self.__values

    @values.setter
    def values( self, values ):
        if isinstance( values, ndarray ):
            self.__values = values

    @property
    def datatype( self ):
        if isinstance( self.__type, pd.Series.dtype ):
            return self.__type
        else:
            return 'NS'

    @datatype.setter
    def datatype( self, typ ):
        if isinstance( typ, pd.Series.dtype ):
            self.__type = typ

    @property
    def caption( self ):
        if isinstance( self.__caption, str ) and self.__caption != '':
            return self.__caption

    @caption.setter
    def caption( self, text ):
        if isinstance( text, str ) and text != '':
            self.__caption = text

    @property
    def ordinal( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @ordinal.setter
    def ordinal( self, index ):
        if isinstance( index, int ):
            self.__id = index

    @property
    def index( self ):
        if isinstance( self.__index, pd.Series.index ):
            return self.__index

    @index.setter
    def index( self, index ):
        if isinstance( index, pd.Series.index ):
            self.__index = index

    @property
    def table( self ):
        if isinstance( self.__table, DataTable ):
            return self.__table

    @table.setter
    def table( self, name ):
        if isinstance( name, DataTable ):
            self.__table = name

    @property
    def row( self ):
        if isinstance( self.__row, DataRow ):
            return self.__row

    @row.setter
    def row( self, items ):
        if isinstance( items, DataRow ):
            self.__series = items
            self.__row = self.__series

    @property
    def source( self ):
        if isinstance( self.__source, DataSource ):
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, DataSource ):
            self.__source = src

    @property
    def data( self ):
        if isinstance( self.__series, pd.Series ):
            return self.__data

    @property
    def isnumeric( self ):
        if not isinstance( self.__values, str ):
            return True

    @property
    def istext( self ):
        if isinstance( self.__values, str ):
            return True

    def __init__( self, name, values ):
        super( ).__init__( self, values )
        self.__name = name if isinstance( name, str ) and name != '' else None
        self.__values = values if isinstance( values, list ) else None
        self.__series = pd.Series( self.__values )
        self.__index = self.__series.index if isinstance( self.__series, pd.Series ) else None

    def __str__( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name


''' DataRow( source, items, names ) '''
class DataRow( sl.Row ):
    '''Defines the DataRow Class'''
    __source = None
    __names = None
    __items = None
    __data = None
    __values = None
    __id = None

    @property
    def id( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @index.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__id = id

    @property
    def data( self ):
        if isinstance( self.__data, pd.DataFrame ):
            return dict( self.__data )

    @data.setter
    def data( self, data ):
        if isinstance( data, pd.Dd.DataFrame ):
            self.__data = data

    @property
    def items( self ):
        if isinstance( self.__items, tuple ):
            return self.__items

    @items.setter
    def items( self, items ):
        if isinstance( items, tuple ):
            self.__items = items

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
        if isinstance( self.__values, list ):
            return list( self.__values )

    @values.setter
    def values( self, values ):
        if isinstance( values, pd.DataFrame.values ):
            self.__values = values

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, Source ):
            self.__source = src

    def __init__( self, source, items = ( ), names = None ):
        super( ) .__init__( self, items )
        self.__source = source if isinstance( source, Source ) else None
        self.__items = items if isinstance( items, tuple ) else ( )
        self.__names = names if isinstance( names, list ) else [ ]
        self.__values = list( self.__items )
        self.__id = int( self.__values[ 0 ] )

    def __str__( self ):
        return 'Row ID: ' + str( self.__id )


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
        super( ).__init__( )
        self.__base = str( name )
        self.__name = self.__base
        self.__data = pd.DataFrame( self.__name )
        self.__rows = [tuple( r ) for r in self.__data[0:]]
        self.__columns = self.__data.columns

    def __str__( self ):
        if self.__name is not None:
            return self.__name

