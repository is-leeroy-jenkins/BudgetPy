import sqlite3 as sqlite
import pandas
import string
from pandas import DataFrame, Index, MultiIndex, Series
from pandas import read_sql as sqlreader
import pyodbc as db
import os
from collections import namedtuple as ntuple
from Static import Source, Provider, SQL, ParamStyle
from Booger import Error, ErrorDialog
import enum

class Pascal( ):
    __input = None
    __output = None

    @property
    def input( self ):
        if isinstance( self.__input, str ) and self.__input != '':
            return self.__input

    @input.setter
    def input( self, value ):
        if isinstance( value, str ) and value != '':
            self.__input = value

    @property
    def output( self ):
        if isinstance( self.__output, str ) and self.__output != '':
            return self.__output

    @output.setter
    def output( self, value ):
        if isinstance( value, str ) and value != self.__input:
            self.__output = value

    def __init__( self, input = None ):
        self.__input = input if isinstance( input, str ) and input != '' else None

    def __str__( self ):
        if isinstance( self.__output, str ) and self.__output != '':
            return self.__output

    def split( self ):
        '''takes the string provided as an input argument
         and formats it into pascal case'''
        try:
            if isinstance( self.__input, str ) and self.__input.count( ' ' ) == 0:
                input = list( self.__input )
                rtnstr = ''
                outstr = ''
                cnt = len( input )

                for i in range( cnt ):
                    char = input[ i ]
                    if i <= 1 and char.islower( ):
                        outstr += f'{char}'
                    elif i <= 1 and char.isupper( ):
                        outstr += f'{char}'
                    elif i > 1 and char.islower( ):
                        outstr += f'{char}'
                    elif i > 1 and char.isupper( ):
                        outstr += f' {char}'

                if len( outstr ) < 5:
                    rtnstr = outstr.replace( ' ', '' )
                else:
                    rtnstr = outstr.replace( 'Ah', 'AH' ).replace( 'Boc', 'BOC' ).replace( 'Rpio', 'RPIO' ).replace(
                        'Rc', 'RC' ).replace( 'Prc', 'PRC' ).replace( 'Id', 'ID' ).replace( 'Omb', 'OMB' ).replace(
                        'Npm', 'NPM' ).replace( 'Foc', 'FOC' ).replace( 'Org', 'ORG' ).replace( ' THE ',
                                                                                                ' The ' ).replace(
                        ' OR ', ' Or ' ).replace( ' AND ', ' And ' ).replace( 'BUT ', ' But ' ).replace( ' OF ',
                                                                                                         ' Of ' )

                self.__output = rtnstr
                return self.__output
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'Pascal'
            exc.method = 'split( self )'
            err = ErrorDialog( exc )
            err.show( )

    def join( self ):
        '''removes ' ' from strings previously formatted into pascal casing with split( self ) '''
        try:
            if isinstance( self.__input, str ) and self.__input.count( ' ' ) > 0:
                input = list( self.__input )
                outlist = list( )
                outstr = ''

                for char in input:
                    if char != ' ':
                        outlist.append( char )

                for o in outlist:
                    outstr += f'{o}'

                self.__output = outstr.replace( 'AH', 'Ah' ).replace( 'BOC', 'Boc' ).replace( 'RPIO', 'Rpio' ).replace(
                    'RC', 'Rc' ).replace( 'PRC', 'Prc' ).replace( 'ID', 'Id' ).replace( 'OMB', 'Omb' ).replace( 'NPM',
                                                                                                                'Npm'
                                                                                                                ).replace(
                    'FOC', 'Foc' ).replace( 'ORG', 'Org' ).replace( 'THE', 'The' ).replace( 'OR', 'Or' ).replace( 'AND',
                                                                                                                  'And' ).replace(
                    'BUT', 'But' ).replace( 'OF', 'Of' )

                return self.__output
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'Pascal'
            exc.method = 'join( self )'
            err = ErrorDialog( exc )
            err.show( )


class SqlPath( ):
    '''class providing relative paths to the folders containing sql files and
    driver paths used in the application'''
    __accessdriver = None
    __accessdata = None
    __accessreference = None
    __sqlitedriver = None
    __sqlitedata = None
    __sqlitereference = None
    __sqldriver = None
    __sqldata = None
    __sqlreference = None

    @property
    def sqlitedriver( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__sqlitedriver, str ):
            return self.__sqlitedriver

    @sqlitedriver.setter
    def sqlitedriver( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitedriver = value

    @property
    def sqlitedata( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__sqlitedata, str ):
            return self.__sqlitedata

    @sqlitedata.setter
    def sqlitedata( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitedata = value

    @property
    def sqlitereference( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__sqlitereference, str ):
            return self.__sqlitereference

    @sqlitereference.setter
    def sqlitereference( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitereference = value

    @property
    def accessdriver( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__accessdriver, str ):
            return self.__accessdriver

    @accessdriver.setter
    def accessdriver( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__accessdriver = value

    @property
    def accessdata( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__accessdata, str ):
            return self.__accessdata

    @accessdata.setter
    def accessdata( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__accessdata = value

    @property
    def accessreference( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__accessreference, str ):
            return self.__accessreference

    @accessreference.setter
    def accessreference( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__accessreference = value

    @property
    def sqldriver( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__sqldriver, str ):
            return self.__sqldriver

    @sqlitedriver.setter
    def sqldriver( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqldriver = value

    @property
    def sqldata( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__sqldata, str ):
            return self.__sqldata

    @sqldata.setter
    def sqldata( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqldata = value

    @property
    def sqlreference( self ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( self.__sqlreference, str ):
            return self.__sqlreference

    @sqlreference.setter
    def sqlreference( self, value ):
        '''Returns string representing the title of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlreference = value

    def __init__( self ):
        self.__sqlitedriver = 'sqlite3'
        self.__sqlitedata =  r'db\sqlite\datamodels\sql'
        self.__sqlitereference = r'db\sqlite\referencemodels\sql'
        self.__accessdriver = r'DRIVER={Microsoft ACCDB Driver (*.mdb, *.accdb)};DBQ='
        self.__accessdata = r'db\access\datamodels\sql'
        self.__accessreference = r'db\access\referencemodels\sql'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
        self.__sqldata = r'db\mssql\datamodels\sql'
        self.__sqlreference = r'db\mssql\referencemodels\sql'


# SqlFile( source, provider, command )
class SqlFile( ):
    '''Class providing access to sql sub-folders in the application provided
    optional arguements source, provider, and command'''
    __data = None
    __reference = None
    __command = None
    __source = None
    __provider = None

    @property
    def provider( self ):
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if isinstance( value, Provider ):
            self.__provider = value

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def command( self ):
        if isinstance( self.__command, SQL ):
            return self.__command

    @command.setter
    def command( self, value ):
        if isinstance( value, SQL ):
            self.__command = value

    def __init__( self, source = None, provider = None,
                  command = None ):
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
        self.__command = command if isinstance( command, SQL ) else SQL.SELECTALL
        self.__source = source if isinstance( source, Source ) else Source.StatusOfFunds
        self.__provider = provider if isinstance( provider, Provider ) else Provider.SQLite

    def getpath( self ):
        '''Method returning a string representing
         the absolute path to the SQL file used to execute the
         command 'self.__commandtype' against the table given by the
         member self.__source depending on the member self.__provider'''
        try:
            sqlpath = SqlPath( )
            data = self.__data
            references = self.__references
            provider = self.__provider.name
            source = self.__source.name
            command = self.__command.name
            current = os.getcwd( )
            path = ''
            if provider == 'SQLite' and source in data:
                path = f'{ sqlpath.sqlitedata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'SQLite' and source in references:
                path = f'{ sqlpath.sqlitereference }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'ACCDB' and source in data:
                path = f'{ sqlpath.accessdata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'ACCDB' and source in references:
                path = f'{ sqlpath.accessreference }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'SqlServer' and source in data:
                path = f'{ sqlpath.sqldata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'SqlServer' and source in references:
                path = f'{ sqlpath.sqlreference }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            else:
                path = f'{ sqlpath.sqlitedata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlFile'
            exc.method = 'getpath( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getdirectory( self ):
        '''Method creates and returns a string representing
        the parent directory where the SQL file resides'''
        try:
            sqlpath = SqlPath( )
            data = self.__data
            reference = self.__references
            source = self.__source.name
            provider = self.__provider.name
            command = self.__command.name
            current = os.getcwd( )
            folder = ''
            if provider == 'SQLite' and source in data:
                folder = f'{ sqlpath.sqlitedata }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'SQLite' and source in references:
                folder = f'{ sqlpath.sqlitereference }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'ACCDB' and source in data:
                folder = f'{ sqlpath.accessdata }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'ACCDB' and source in references:
                folder = f'{ sqlpath.accessreference }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'SqlServer' and source in data:
                folder = f'{ sqlpath.sqldata }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'SqlServer' and source in references:
                folder = f'{ sqlpath.sqlreference }\\{ command }'
                return os.path.join( current, folder )
            else:
                folder = f'{ sqlpath.sqlitedata }\\{ command }'
                return os.path.join( current, folder )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlFile'
            exc.method = 'getdirectory( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getquery( self ):
        '''Method reads the given '.sql' file and returns
        a string representing the text used the sql query'''
        try:
            source = self.__source.name
            paths = self.getpath( )
            folder = self.getdirectory( )
            sql = ''
            for name in os.listdir( folder ):
                if name.endswith( '.sql' ) and os.path.splitext( name )[ 0 ] == source:
                    path = os.path.join( folder, name )
                    query = open( path )
                    sql = query.read( )
                    return sql
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlFile'
            exc.method = 'getquery( self, other )'
            err = ErrorDialog( exc )
            err.show( )


# DbConfig( source, provider )
class DbConfig( ):
    '''DbConfig( source, provider  ) provides list of Budget Execution
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

    def __init__( self, source, provider = Provider.SQLite ):
        '''Constructor for the DbConfig class providing
        values value details'''
        self.__provider = provider if isinstance( provider, Provider ) else None
        self.__source = source if isinstance( source, Source ) else None
        self.__table = source.name
        self.__sqlitedatapath = os.getcwd( ) + r'\db\sqlite\datamodels\Data.db'
        self.__sqlitereferencepath = os.getcwd( ) + r'\db\sqlite\referencemodels\References.db'
        self.__accessdriver = r'DRIVER={ Microsoft ACCDB Driver (*.mdb, *.accdb) };DBQ='
        self.__accessdatapath = os.getcwd( ) + r'\db\access\datamodels\Data.accdb'
        self.__accessreferencepath = os.getcwd( ) + r'\db\access\referencemodels\References.accdb'
        self.__sqldriver = r'DRIVER={ ODBC Driver 17 for SQL Server };SERVER=.\SQLExpress;'
        self.__sqldatapath = os.getcwd( ) + r'\db\mssql\datamodels\Data.mdf'
        self.__sqlreferencepath = os.getcwd( ) + r'\db\mssql\referencemodels\References.mdf'
        self.__data = [ 'Allocations', 'Actuals', 'ApplicationTables', 'AppropriationDocuments', 'BudgetControls',
                        'BudgetDocuments', 'CarryoverEstimates', 'CarryoverSurvey', 'Changes',
                        'CongressionalReprogrammings', 'Deobligations', 'Defactos', 'DocumentControlNumbers',
                        'Obligations', 'OperatingPlans', 'OperatingPlanUpdates', 'QueryDefinitions',
                        'RegionalAuthority', 'ReimbursableAgreements', 'ReimbursableFunds', 'ReimbursableSurvey',
                        'Reports', 'StatusOfAppropriations'
                                   'Reprogrammings', 'SiteActivity', 'SiteProjectCodes', 'SpecialAccounts',
                        'StatusOfFunds', 'Supplementals', 'Transfers', 'HumanResourceOrganizations'
                                                                       'HeadquartersAuthority', 'TravelObligations',
                        'StatusOfAppropriations', 'StatusOfJobsActFunding', 'StatusOfSupplementalFunding',
                        'SuperfundSites', 'PayrollAuthority', 'TransTypes', 'PayrollRequests', 'CarryoverRequests',
                        'CompassLevels', 'AdministrativeRequests', 'OpenCommitments', 'Expenditures',
                        'UnliquidatedObligations', 'UnobligatedBalances' ]
        self.__references = [ 'Accounts', 'ActivityCodes', 'AllowanceHolders', 'Appropriations', 'Apportionments',
                              'BudgetObjectClasses', 'BudgetOutlays', 'BudgetaryResourceExecution', 'CostAreas', 'CPIC',
                              'CarryoverOutlays', 'Divisions', 'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                              'FiscalYears', 'FiscalYearsBackUp', 'Funds', 'FundSymbols', 'Goals', 'GsPayScales',
                              'GrowthRates', 'Images', 'Messages', 'NationalPrograms', 'Objectives',
                              'ProgramFinancingSchedule', 'ObjectClassOutlays', 'Organizations', 'ProgramAreas',
                              'ProgramDescriptions', 'ProgramProjects', 'Projects', 'Providers', 'RegionalOffices'
                                                                                                 'ReferenceTables',
                              'ResourcePlanningOffices', 'ResponsibilityCenters', 'SchemaTypes', 'StateOrganizations',
                              'Sources', 'SpendingRates' ]

    def __str__( self ):
        if isinstance( self.__table, str ):
            return self.__table

    def isdatamodel( self ):
        '''Returns the boolean value 'True' if the
        source is a memeber of datamodels else 'False' '''
        try:
            if self.__table != '' and self.__table in self.__data:
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'DbConfig'
            exc.method = 'isdatamodel( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isreferencemodel( self ):
        '''Returns boolean value 'True' if the
        source is a memeber of the reference models else 'False' '''
        try:
            if self.__table is not None and self.__table in self.__references:
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'DbConfig'
            exc.method = 'isreference( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getdriver( self ):
        try:
            if self.__provider.name == Provider.SQLite.name:
                return self.getpath( )
            elif self.__provider.name == Provider.Access.name:
                return self.__accessdriver
            elif self.__provider.name == Provider.SqlServer.name:
                return self.__sqldriver
            else:
                return self.__sqlitedriver
        except Exception as e:
            exc = Error( e )
            exc.cause = 'DbConfig Class'
            exc.method = 'getdriver( self )'
            error = ErrorDialog( exc )
            error.show( )

    def getpath( self ):
        try:
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
        except Exception as e:
            exc = Error( e )
            exc.cause = 'DbConfig Class'
            exc.method = 'getpath( self )'
            error = ErrorDialog( exc )
            error.show( )

    def getconnectionstring( self ):
        try:
            path = self.getpath( )
            if self.__provider.name == Provider.Access.name:
                return self.getdriver( ) + path
            elif self.__provider.name == Provider.SqlServer.name:
                return r'DRIVER={ ODBC Driver 17 for SQL Server };Server=.\SQLExpress;' + f'AttachDBFileName={path}' \
                       + f'DATABASE={path}Trusted_Connection=yes;'
            else:
                return f'{path} '
        except Exception as e:
            exc = Error( e )
            exc.cause = 'DbConfig Class'
            exc.method = 'getconnectionstring( self )'
            error = ErrorDialog( exc )
            error.show( )


# Connection( source, provider = Provider.SQLite )
class Connection( DbConfig ):
    '''Connection( source, provider = Provider.SQLite ) initializes
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
        if isinstance( self.__configuration, DbConfig ):
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
        if isinstance( self.__driver, str ):
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

    def __init__( self, source, provider = Provider.SQLite ):
        super( ).__init__( source, provider )
        self.__source = source
        self.__provider = provider
        self.__path = super( ).getpath( )
        self.__driver = super( ).getdriver( )
        self.__dsn = source.name + ';'
        self.__connectionstring = super( ).getconnectionstring( )

    def connect( self ):
        try:
            if self.__provider.name == Provider.Access.name:
                return db.connect( self.__connectionstring )
            elif self.__provider.name == Provider.SqlServer.name:
                return db.connect( self.__connectionstring )
            else:
                return sqlite.connect( self.__connectionstring )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'Connection'
            exc.method = 'connect( self )'
            err = ErrorDialog( exc )
            err.show( )

    def disconnect( self ):
        try:
            if self.__connection is not None:
                self.__connection.flush( )
                self.__connection.close( )
                self.__connection = None
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'Connection'
            exc.method = 'disconnect( self )'
            err = ErrorDialog( exc )
            err.show( )


# SqlConfig( commandtype, names, values, style )
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

    def __init__( self, command = SQL.SELECTALL, names = [ ], values = ( ), style = None ):
        self.__command = command if isinstance( command, SQL ) else SQL.SELECTALL
        self.__names = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__paramstyle = style if isinstance( style, ParamStyle ) else ParamStyle.qmark
        self.__kvp = dict( zip( names, list( values ) ) ) if isinstance( names, list ) and isinstance( values,
                                                                                                       tuple ) else None

    def kvpdump( self ):
        '''dump( ) returns string of 'values = index AND' pairs'''
        try:
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                pairs = ''
                criteria = ''
                kvp = zip( self.__names, self.__values )
                for k, v in kvp:
                    pairs += f'{k} = \'{v}\' AND '
                criteria = pairs.rstrip( ' AND ' )
                return criteria
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'kvpdump( self )'
            err = ErrorDialog( exc )
            err.show( )

    def wheredump( self ):
        '''wheredump( ) returns a string
        using list arguments names and values'''
        try:
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                pairs = ''
                criteria = ''
                for k, v in zip( self.__names, self.__values ):
                    pairs += f'{k} = \'{v}\' AND '
                criteria = 'WHERE ' + pairs.rstrip( ' AND ' )
                return criteria
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'wheredump( self )'
            err = ErrorDialog( exc )
            err.show( )

    def setdump( self ):
        '''setdump( ) returns a string
        using list arguments names and values'''
        try:
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                pairs = ''
                criteria = ''
                for k, v in zip( self.__names, self.__values ):
                    pairs += f'{k} = \'{v}\', '
                criteria = 'SET ' + pairs.rstrip( ', ' )
                return criteria
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'setdump( self )'
            err = ErrorDialog( exc )
            err.show( )

    def columndump( self ):
        '''columndump( ) returns a string of columns
        used in select and insert statements from list self.__names'''
        try:
            if isinstance( self.__names, list ):
                cols = ''
                columns = ''
                for n in self.__names:
                    cols += f'{n}, '
                columns = '(' + cols.rstrip( ', ' ) + ')'
                return columns
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'columndump( self )'
            err = ErrorDialog( exc )
            err.show( )

    def valuedump( self ):
        '''valuedump( ) returns a string of values
        used in select statements from list self.__names'''
        try:
            if isinstance( self.__values, tuple ):
                vals = ''
                values = ''
                for v in self.__values:
                    vals += f'{v}, '
                values = 'VALUES (' + vals.rstrip( ', ' ) + ')'
                return values
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'valuedump( self )'
            err = ErrorDialog( exc )
            err.show( )


# SqlStatement( dbconfig,  sqlconfig )
class SqlStatement( ):
    '''SqlStatement( dataconfig, sqlconfig ) Class
    represents the values models used in the SQLite database'''
    __commandtype = None
    __sqlconfig = None
    __dataconfig = None
    __source = None
    __provider = None
    __table = None
    __names = None
    __values = None
    __commandtext = None

    @property
    def dataconfig( self ):
        if isinstance( self.__dataconfig, DbConfig ):
            return self.__dataconfig

    @dataconfig.setter
    def dataconfig( self, value ):
        if isinstance( value, DbConfig ):
            self.__dataconfig = value

    @property
    def sqlconfig( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlconfig, SqlConfig ):
            return self.__sqlconfig

    @sqlconfig.setter
    def sqlconfig( self, value ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( value, SqlConfig ):
            self.__sqlconfig = value

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

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ):
            self.__path = value

    @property
    def commandtype( self ):
        if isinstance( self.__commandtype, SQL ):
            return self.__commandtype

    @commandtype.setter
    def commandtype( self, value ):
        if isinstance( value, SQL ):
            self.__commandtype = value
        else:
            command = SQL( 'SELECT' )
            self.__commandtype = command

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

    @property
    def commandtext( self ):
        if isinstance( self.__commandtext, str ) and self.__commandtext != '':
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value ):
        if isinstance( value, str ) and value != '':
            self.__commandtext = value

    def __init__( self, dataconfig, sqlconfig ):
        self.__sqlconfig = sqlconfig if isinstance( sqlconfig, SqlConfig ) else None
        self.__dataconfig = dataconfig if isinstance( dataconfig, DbConfig ) else None
        self.__commandtype = sqlconfig.command
        self.__provider = dataconfig.provider
        self.__source = dataconfig.source
        self.__table = dataconfig.table
        self.__names = sqlconfig.names
        self.__values = sqlconfig.values

    def __str__( self ):
        if isinstance( self.__commandtext, str ) and self.__commandtext != '':
            return self.__commandtext

    def getquery( self ):
        try:
            table = self.__table
            columns = self.__sqlconfig.columndump( )
            values = self.__sqlconfig.valuedump( )
            predicate = self.__sqlconfig.wheredump( )
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                if self.__commandtype == SQL.SELECTALL:
                    if len( self.__names ) == 0:
                        self.__commandtext = f'SELECT * FROM {table}'
                        return self.__commandtext
                    if len( self.__names ) > 0:
                        self.__commandtext = f'SELECT ' + columns + f'FROM {table}' + f' {predicate}'
                        return self.__commandtext
                elif self.__commandtype == SQL.SELECT:
                    if len( self.__names ) == 0:
                        self.__commandtext = f'SELECT * FROM {table}'
                        return self.__commandtext
                    if len( self.__names ) > 0:
                        self.__commandtext = f'SELECT ' + columns + f' FROM {table}' + f' {predicate}'
                        return self.__commandtext
                elif self.__commandtype == SQL.INSERT:
                    self.__commandtext = f'INSERT INTO {table} ' + f'{columns} ' + f'{values}'
                    return self.__commandtext
                elif self.__commandtype == SQL.UPDATE:
                    self.__commandtext = f'UPDATE {table} ' + f'{self.__sqlconfig.setdump( )} ' + f'{values}'
                    return self.__commandtext
                elif self.__commandtype == SQL.DELETE:
                    self.__commandtext = f'DELETE FROM {table} ' + f'{predicate}'
                    return self.__commandtext
            else:
                if isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__commandtype == SQL.SELECT:
                        cols = columns.lstrip( '(' ).rstrip( ')' )
                        self.__commandtext = f'SELECT {cols} FROM {table}'
                        return self.__commandtext
                elif not isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__commandtype == SQL.SELECTALL:
                        self.__commandtext = f'SELECT * FROM {table}'
                        return self.__commandtext
                elif self.__commandtype == 'DELETE':
                    self.__commandtext = f'DELETE FROM {table}'
                    return self.__commandtext
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlStatement'
            exc.method = 'getcommandtext( self )'
            err = ErrorDialog( exc )
            err.show( )


# Query( connection, sqlstatement )
class Query( ):
    '''Base class for database interaction'''
    __connection = None
    __sqlstatement = None
    __sqlconfig = None
    __dbconfig = None
    __commandtype = None
    __source = None
    __table = None
    __provider = None
    __names = None
    __values = None
    __path = None
    __connectionstring = None
    __commandtext = None

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
        if isinstance( self.__connection, Connection ):
            return self.__connection

    @connection.setter
    def connection( self, value ):
        if isinstance( value, Connection ):
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
    def commandtype( self ):
        if self.__commandtype is not None:
            return self.__commandtype
        if self.__commandtype is None:
            cmd = SQL( 'SELECT' )
            return cmd

    @commandtype.setter
    def commandtype( self, value ):
        if isinstance( value, SQL ):
            self.__commandtype = value

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

    @property
    def commandtext( self ):
        if isinstance( self.__commandtext, str ) and self.__commandtext != '':
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value ):
        if isinstance( value, str ) and value != '':
            self.__commandtext = value

    @property
    def connectionstring( self ):
        if isinstance( self.__connectionstring, str ):
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, value ):
        if isinstance( value, str ):
            self.__connectionstring = str( value )

    def __init__( self, connection, sqlstatement ):
        self.__connection = connection if isinstance( connection, Connection ) else None
        self.__sqlstatement = sqlstatement if isinstance( sqlstatement, SqlStatement ) else None
        self.__dbconfig = connection.configuration
        self.__sqlconfig = sqlstatement.sqlconfig
        self.__source = connection.source
        self.__provider = connection.provider
        self.__commandtype = sqlstatement.commandtype
        self.__path = connection.path
        self.__connectionstring = connection.connectionstring

    def __str__( self ):
        if isinstance( self.__commandtext, str ) and self.__commandtext != '':
            return self.__commandtext

    def getquery( self ):
        try:
            table = self.__table
            columns = self.__sqlconfig.columndump( )
            values = self.__sqlconfig.valuedump( )
            predicate = self.__sqlconfig.wheredump( )
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                if self.__commandtype == SQL.SELECTALL:
                    if len( self.__names ) == 0:
                        self.__commandtext = f'SELECT * FROM {table}'
                        return self.__commandtext
                    if len( self.__names ) > 0:
                        self.__commandtext = f'SELECT ' + columns + f'FROM {table}' + f' {predicate}'
                        return self.__commandtext
                elif self.__commandtype == SQL.SELECT:
                    if len( self.__names ) == 0:
                        self.__commandtext = f'SELECT * FROM {table}'
                        return self.__commandtext
                    if len( self.__names ) > 0:
                        self.__commandtext = f'SELECT ' + columns + f' FROM {table}' + f' {predicate}'
                        return self.__commandtext
                elif self.__commandtype == SQL.INSERT:
                    self.__commandtext = f'INSERT INTO {table} ' + f'{columns} ' + f'{values}'
                    return self.__commandtext
                elif self.__commandtype == SQL.UPDATE:
                    self.__commandtext = f'UPDATE {table} ' + f'{self.__sqlconfig.setdump( )} ' + f'{values}'
                    return self.__commandtext
                elif self.__commandtype == SQL.DELETE:
                    self.__commandtext = f'DELETE FROM {table} ' + f'{predicate}'
                    return self.__commandtext
            else:
                if isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__commandtype == SQL.SELECT:
                        cols = columns.lstrip( '(' ).rstrip( ')' )
                        self.__commandtext = f'SELECT {cols} FROM {table}'
                        return self.__commandtext
                elif not isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__commandtype == SQL.SELECTALL:
                        self.__commandtext = f'SELECT * FROM {table}'
                        return self.__commandtext
                elif self.__commandtype == 'DELETE':
                    self.__commandtext = f'DELETE FROM {table}'
                    return self.__commandtext
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlStatement'
            exc.method = 'getcommandtext( self )'
            err = ErrorDialog( exc )
            err.show( )


# SQLiteData( connection, sqlstatement )
class SQLiteData( Query ):
    '''SQLiteData( value, sqlconfig ) represents
     the budget execution values classes'''
    __source = None
    __provider = None
    __connection = None
    __sqlstatement = None
    __driver = None
    __table = None
    __dsn = None
    __query = None
    __data = None
    __frame = None
    __columns = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = Source

    @property
    def connection( self ):
        if isinstance( self.__connection, Connection ):
            return self.__connection

    @connection.setter
    def connection( self, value ):
        if isinstance( value, Connection ):
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
    def commandtext( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    @commandtext.setter
    def commandtext( self, value ):
        if isinstance( value, str ) and value != '':
            self.__query = value

    @property
    def columns( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement )
        self.__provider = Provider.SQLite
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sqlstatement
        self.__source = super( ).source
        self.__table = super( ).source.name
        self.__driver = super( ).connection.driver
        self.__query = super( ).sqlstatement.getquery( )

    def __str__( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    def createtable( self ):
        try:
            query = self.__query
            sqlite = self.__connection.connect( )
            cursor = sqlite.cursor( )
            data = cursor.execute( query )
            self.__columns = [ i[ 0 ] for i in cursor.description ]
            self.__data = [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SQLiteData'
            exc.method = 'createtable( self )'
            err = ErrorDialog( exc )
            err.show( )

    def createframe( self ):
        try:
            query = f'SELECT * FROM {self.__source.name}'
            connection = self.__connection.connect( )
            self.__frame = sqlreader( query, connection )
            connection.close( )
            return self.__frame
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SQLiteData'
            exc.method = 'createframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# AccessData( connection, sqlstatement )
class AccessData( Query ):
    '''AccessData( value, sqlconfig ) class
      represents the budget execution
      values model classes in the MS ACCDB database'''
    __source = None
    __provider = None
    __connection = None
    __sqlstatement = None
    __query = None
    __driver = None
    __dsn = None
    __data = None
    __table = None
    __columns = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = Source

    @property
    def connection( self ):
        if isinstance( self.__connection, Connection ):
            return self.__connection

    @connection.setter
    def connection( self, value ):
        if isinstance( value, Connection ):
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
    def commandtext( self ):
        if isinstance( self.__query, str ):
            return self.__query

    @commandtext.setter
    def commandtext( self, value ):
        if isinstance( value, str ):
            self.__query = value

    @property
    def columns( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement )
        self.__source = super( ).source
        self.__provider = Provider.Access
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sqlstatement
        self.__query = sqlstatement.getquery( )
        self.__table = connection.source.name
        self.__driver = r'DRIVER={ Microsoft ACCDB Driver( *.mdb, *.accdb ) };'
        self.__data = [ ]

    def __str__( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    def createtable( self ):
        try:
            query = self.__query
            access = self.__connection.connect( )
            cursor = access.cursor( )
            data = cursor.execute( query )
            self.__columns = [ i[ 0 ] for i in cursor.description ]
            self.__data = [ i for i in data.fetchall( ) ]
            cursor.close( )
            access.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'AccessData'
            exc.method = 'createtable( self )'
            err = ErrorDialog( exc )
            err.show( )

    def createframe( self ):
        try:
            query = self.__query
            connection = self.__connection.connect( )
            self.__frame = sqlreader( query, connection )
            connection.close( )
            return self.__frame
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'AccessData'
            exc.method = 'createframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# SqlServerData( connection, sqlstatement )
class SqlServerData( Query ):
    '''SqlServerData( value, sqlconfig ) object
    represents the values models in the MS SQL Server
    database'''
    __source = None
    __provider = None
    __connection = None
    __sqlstatement = None
    __query = None
    __server = None
    __driver = None
    __dsn = None
    __table = None
    __columns = None
    __data = None

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = Source

    @property
    def connection( self ):
        if isinstance( self.__connection, Connection ):
            return self.__connection

    @connection.setter
    def connection( self, value ):
        if isinstance( value, Connection ):
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
    def commandtext( self ):
        if isinstance( self.__query, str ):
            return self.__query

    @commandtext.setter
    def commandtext( self, value ):
        if isinstance( value, str ):
            self.__query = value

    @property
    def columns( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement )
        self.__provider = Provider.SqlServer
        self.__connection = connection
        self.__source = connection.source
        self.__sqlstatement = sqlstatement
        self.__query = sqlstatement.getquery( )
        self.__table = connection.source.name
        self.__server = r'(LocalDB)\MSSQLLocalDB;'
        self.__driver = r'{ SQL Server Native Client 11.0 };'

    def __str__( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    def createtable( self ):
        try:
            query = self.__query
            conection = self.__connection.connect( )
            cursor = conection.cursor( )
            data = cursor.execute( query )
            self.__columns = [ i[ 0 ] for i in cursor.description ]
            self.__data = [ i for i in data.fetchall( ) ]
            cursor.close( )
            conection.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlServerData'
            exc.method = 'createtable( self )'
            err = ErrorDialog( exc )
            err.show( )

    def createframe( self ):
        try:
            query = f'SELECT * FROM {self.__table}'
            connection = self.__connection.connect( )
            self.__frame = sqlreader( query, connection )
            connection.close( )
            return self.__frame
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlServerData'
            exc.method = 'createframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# DataBuilder( provider, source, command, names, values )
class DataBuilder( ):
    '''DataBuilder class provides methods that access
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
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

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
    def dbconfig( self ):
        if isinstance( self.__dbconfig, DbConfig ):
            return self.__dbconfig

    @dbconfig.setter
    def dbconfig( self, value ):
        if isinstance( value, DbConfig ):
            self.__dbconfig = value

    @property
    def sqlconfig( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlconfig, SqlConfig ):
            return self.__sqlconfig

    @sqlconfig.setter
    def sqlconfig( self, value ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( value, SqlConfig ):
            self.__sqlconfig = value

    def __init__( self, source, provider = Provider.SQLite, command = SQL.SELECTALL, names = None, values = None ):
        self.__source = source if isinstance( source, Source ) else None
        self.__provider = provider
        self.__command = command
        self.__name = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__dbconfig = DbConfig( self.__source, self.__provider )
        self.__connection = Connection( self.__dbconfig )
        self.__sqlconfig = SqlConfig( self.__command, self.__names, self.__values )
        self.__sqlstatement = SqlStatement( self.__dbconfig, self.__sqlconfig )

    def createtable( self ):
        try:
            if self.__provider == Provider.SQLite:
                sqlite = SQLiteData( self.__connection, self.__sqlstatement )
                self.__data = [ tuple( i ) for i in sqlite.getdata( ) ]
                return self.__data
            elif self.__provider == Provider.Access:
                access = AccessData( self.__connection, self.__sqlstatement )
                self.__data = [ tuple( i ) for i in access.getdata( ) ]
                return self.__data
            elif self.__provider == Provider.SqlServer:
                sqlserver = SqlServerData( self.__connection, self.__sqlstatement )
                self.__data = [ tuple( i ) for i in sqlserver.getdata( ) ]
                return self.__data
            else:
                sqlite = SQLiteData( self.__connection, self.__sqlstatement )
                self.__data = [ tuple( i ) for i in sqlite.getdata( ) ]
                return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'DataBuilder'
            exc.method = 'createtable( self )'
            error = ErrorDialog( exc )
            error.show( )


# DataColumn( name, type, value, series  )
class DataColumn( ):
    '''Defines the DataColumn Class providing schema information.
    Constructor uses optional arguments ( name: str, type: type,
     value: object, series: DataSeries )'''
    __series = None
    __row = None
    __name = None
    __value = None
    __label = None
    __id = None
    __type = None
    __caption = None
    __table = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__id = value

    @property
    def name( self ):
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ):
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
    def type( self ):
        if isinstance( self.__type, object ):
            return self.__type

    @type.setter
    def type( self, value ):
        if isinstance( value, object ):
            self.__type = value

    @property
    def ordinal( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @ordinal.setter
    def ordinal( self, value ):
        if isinstance( value, int ):
            self.__id = value

    @property
    def caption( self ):
        if isinstance( self.__caption, str ):
            return self.__caption

    @caption.setter
    def caption( self, value ):
        if isinstance( value, str ):
            self.__caption = value

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

    @frame.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    def __init__( self, name = '', datatype = None, value = None ):
        self.__name = name if isinstance( name, str ) else None
        self.__label = name
        self.__caption = name
        self.__type = datatype if isinstance( datatype, type ) else None
        self.__value = value if isinstance( value, object ) else None

    def __str__( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    def isnumeric( self ):
        '''Method used to return a boolean value indicating whether
        the data column contains numeric data'''
        try:
            if not isinstance( self.__value, str ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'DataColumn'
            exc.method = 'isnumeric( self )'
            err = ErrorDialog( exc )
            err.show( )

    def istext( self ):
        '''Method used to return a boolean value indicating
        whether the data column contains text data'''
        try:
            if isinstance( self.__value, str ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'DataColumn'
            exc.method = 'istext( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    __index = None

    @property
    def id( self ):
        if isinstance( self.__index, int ):
            return self.__index

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__index = value

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

    def __init__( self, names = [ ], values = ( ), source = None ):
        self.__source = source if isinstance( source, Source ) else None
        self.__names = names if isinstance( names, list ) else None
        self.__values = value if isinstance( values, tuple ) else None
        self.__items = zip( names, list( values ) )
        self.__key = str( self.__names[ 0 ] ) if isinstance( self.__names, list ) else None
        self.__index = int( self.__values[ 0 ] ) if isinstance( self.__values, tuple ) else None

    def __str__( self ):
        if isinstance( self.__index, int ) and self.__index > -1:
            return 'Row ID: ' + str( self.__index )


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
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @frame.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
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

    def __init__( self, columns = None, rows = None, source = None, dataframe = None ):
        self.__frame = dataframe if isinstance( dataframe, DataFrame ) else None
        self.__name = name if isinstance( name, str ) and name != '' else None
        self.__rows = [ tuple( r ) for r in dataframe.items ]
        self.__data = self.__rows
        self.__columns = [ str( c ) for c in columns ] if isinstance( columns, list ) else None
        self.__schema = [ DataColumn( c ) for c in columns ] if isinstance( columns, list ) else None

    def __str__( self ):
        if self.__name is not None:
            return self.__name


# BudgetData( source )
class BudgetData( ):
    '''Class containing factory method for providing
    pandas dataframes based on the Source argument 'source' '''
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
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def path( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and value != '':
            self.__path = value

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
        if isinstance( self.__sql, str ):
            return self.__sql

    @query.setter
    def query( self, value ):
        if isinstance( value, str ):
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
        if isinstance( self.__index, DataFrame.id ):
            return self.__index

    @index.setter
    def index( self, value ):
        if isinstance( value, DataFrame.id ):
            self.__index = value

    @property
    def frame( self ):
        if isinstance( self.__data, DataFrame ):
            return self.__data

    @frame.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    def __init__( self, source ):
        self.__source = source if isinstance( source, Source ) else None
        self.__name = source.name
        self.__path = DbConfig( source, Provider.SQLite ).getpath( )
        self.__sql = f'SELECT * FROM {source.name};'

    def getframe( self ):
        '''Facotry method that returns a pandas DataFrame object
        based on the Source input arguement 'source' given to the constructor'''
        try:
            path = self.__path
            src = self.__source
            table = self.__name
            conn = sqlite.connect( path )
            sql = f'SELECT * FROM {table};'
            frame = sqlreader( sql, conn )
            return frame
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'BudgetData'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )
