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
        if self.__input is not None:
            return self.__input

    @input.setter
    def input( self, value ):
        if value != '':
            self.__input = value

    @property
    def output( self ):
        """

        @return:
        """
        if self.__output is not None and self.__output != '':
            return self.__output

    @output.setter
    def output( self, value ):
        if value is not None and value != self.__input:
            self.__output = value

    def __init__( self, buffer = None ):
        self.__input = buffer if buffer is not None and buffer != '' else None

    def __str__( self ):
        if self.__output is not None and self.__output != '':
            return self.__output

    def split( self ):
        '''takes the string provided as an inbuffer argument
         and formats it into pascal case
         @return: '''
        try:
            if self.__input != '' and self.__input.count( ' ' ) == 0:
                inbuffer = list( self.__input )
                rtnstr = ''
                outstr = ''
                cnt = len( inbuffer )

                for i in range( cnt ):
                    char = inbuffer[ i ]
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
                inbuffer = list( self.__input )
                outlist = list( )
                outstr = ''

                for char in inbuffer:
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
    '''class providing relative_path paths to the folders containing sql files and
    driver paths used in the application'''
    __accessdriver = None
    __accessdata = None
    __sqlitedriver = None
    __sqlitedata = None
    __sqldriver = None
    __sqldata = None

    @property
    def sqlite_driver( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__sqlitedriver is not None:
            return self.__sqlitedriver

    @sqlite_driver.setter
    def sqlite_driver( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value != '':
            self.__sqlitedriver = value

    @property
    def sqlite_data( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__sqlitedata is not None:
            return self.__sqlitedata

    @sqlite_data.setter
    def sqlite_data( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value != '':
            self.__sqlitedata = value

    @property
    def access_driver( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__accessdriver is not None:
            return self.__accessdriver

    @access_driver.setter
    def access_driver( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value != '':
            self.__accessdriver = value

    @property
    def access_data( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__accessdata is not None:
            return self.__accessdata

    @access_data.setter
    def access_data( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value != '':
            self.__accessdata = value

    @property
    def sql_driver( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__sqldriver is not None:
            return self.__sqldriver

    @sql_driver.setter
    def sql_driver( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value != '':
            self.__sqldriver = value

    @property
    def sql_data( self ):
        '''Returns string representing the title of the selected_path 'base' '''
        if self.__sqldata is not None:
            return self.__sqldata

    @sql_data.setter
    def sql_data( self, value ):
        '''Returns string representing the title of the selected_path 'base' '''
        if value != '':
            self.__sqldata = value

    def __init__( self ):
        self.__sqlitedriver = 'sqlite3'
        self.__sqlitedata = r'db\sqlite\datamodels\sql'
        self.__accessdriver = r'DRIVER={Microsoft ACCDB Driver (*.mdb, *.accdb)};DBQ='
        self.__accessdata = r'db\access\datamodels\sql'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
        self.__sqldata = r'db\mssql\datamodels\sql'

# SqlFile( source = None, provider = None, command = None  )
class SqlFile( ):
    '''Class providing access to sql sub-folders in the application provided
    optional arguments source, provider, and command'''
    __data = None
    __command = None
    __source = None
    __provider = None

    @property
    def provider( self ):
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if value is not None:
            self.__provider = value

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value ):
        if value is not None:
            self.__source = value

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, value ):
        if value is not None:
            self.__command = value

    @property
    def filepath( self ):
        '''Method returning a string representing
         the absolute_path path to the SQL file used to execute the
         command 'self.__cmdtype' against the table given by the
         member self.__source depending on the member self.__provider'''
        try:
            sqlpath = SqlPath( )
            data = self.__data
            provider = self.__provider.name
            source = self.__source.name
            command = self.__command.name
            current = os.getcwd( )
            path = ''
            if provider == 'SQLite' and source in data:
                path = f'{sqlpath.sqlite_data}\\{command}\\{source}.sql'
                return os.path.join( current, path )
            elif provider == 'ACCDB' and source in data:
                path = f'{sqlpath.access_data}\\{command}\\{source}.sql'
                return os.path.join( current, path )
            elif provider == 'SqlServer' and source in data:
                path = f'{sqlpath.sql_data}\\{command}\\{source}.sql'
                return os.path.join( current, path )
            else:
                path = f'{sqlpath.sqlite_data}\\{command}\\{source}.sql'
                return os.path.join( current, path )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlFile'
            exc.method = 'filepath( self )'
            err = ErrorDialog( exc )
            err.show( )

    @property
    def directory( self ):
        '''Method creates and returns a string representing
        the parent directory where the SQL file resides'''
        try:
            sqlpath = SqlPath( )
            data = self.__data
            source = self.__source.name
            provider = self.__provider.name
            command = self.__command.name
            current = os.getcwd( )
            folder = ''
            if provider == 'SQLite' and source in data:
                folder = f'{sqlpath.sqlite_data}\\{command}'
                return os.path.join( current, folder )
            elif provider == 'ACCDB' and source in data:
                folder = f'{sqlpath.access_data}\\{command}'
                return os.path.join( current, folder )
            elif provider == 'SqlServer' and source in data:
                folder = f'{sqlpath.sql_data}\\{command}'
                return os.path.join( current, folder )
            else:
                folder = f'{sqlpath.sqlite_data}\\{command}'
                return os.path.join( current, folder )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlFile'
            exc.method = 'directory( self )'
            err = ErrorDialog( exc )
            err.show( )

    @property
    def query( self ):
        '''Method reads the given '.sql' file and returns
        a string representing the text used the sql query'''
        try:
            source = self.__source.name
            paths = self.filepath
            folder = self.directory
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
            exc.method = 'query( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def __init__( self, source = None, provider = None,
                  command = None ):
        self.__data = [ 'Actual', 'AdministrativeRequests', 'Allocation',
                        'AmericanRescuePlan', 'AnnualCarryoverEstimates', 'AnnualCarryoverSurvey',
                        'AnnualReimbursableEstimates', 'AnnualReimbursableSurvey', 'ApplicationTable',
                        'AppropriationAvailableBalance', 'AppropriationDocument', 'AppropriationLevelAuthority',
                        'BudgetDocument', 'CarryoverApportionments', 'CarryoverRequests',
                        'Changes', 'CompassLevel', 'CompassOutlays',
                        'CongressionalReprogrammings', 'Contacts', 'Defactos',
                        'DeobligationActivity', 'Deobligations', 'DocumentControlNumber',
                        'Earmarks', 'Expenditure', 'PayPeriods',
                        'PayrollActivity', 'PayrollAuthority', 'PayrollCostCode',
                        'PayrollRequests', 'PRC', 'ProjectCostCodes',
                        'QueryDefinitions', 'RegionalAuthority', 'ReimbursableAgreement',
                        'ReimbursableFunds', 'Reports', 'Reprogrammings',
                        'GrossAuthority', 'GrossUtilization', 'HeadquartersAuthority',
                        'HumanResourceOrganization', 'JobsActCarryoverEstimates', 'MonthlyLedgerAccountBalances',
                        'NetAuthority', 'ObligationActivity', 'Obligation',
                        'OpenCommitment', 'SiteActivity', 'SiteProjectCode',
                        'SpecialAccount', 'StateGrantObligation', 'StatusOfAppropriations',
                        'StatusOfBudgetaryResources', 'StatusOfEarmarks', 'StatusOfFunds',
                        'StatusOfJobsActFunding', 'StatusOfSupplementalFunding', 'SuperfundSite',
                        'SupplementalCarryoverEstimates', 'SupplementalReimburseableEstimates', 'TransferActivity',
                        'Transfer', 'UnliquidatedObligation', 'UnobligatedBalance',
                        'AccountingEvents', 'Account', 'ActivityCode',
                        'AllowanceHolder', 'ApportionmentData', 'Appropriation',
                        'BudgetaryResourceExecution', 'BudgetControl', 'BudgetObjectClass',
                        'BudgetOutlay', 'CapitalPlanningInvestmentCodes', 'CarryoverOutlay',
                        'CongressionalControl', 'CostAreas', 'DataRuleDescriptions',
                        'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                        'FiscalYears', 'FiscalYearsBackUp', 'FundCategories',
                        'Fund', 'FundSymbols', 'GeneralLedgerAccount',
                        'Goal', 'GrowthRate', 'GsPayScales',
                        'HeadquartersOffice', 'Images', 'InfrastructureAccounts',
                        'Messages', 'MonthlyOutlay', 'NationalProgram',
                        'ObjectClassOutlay', 'Objective', 'OperatingPlan',
                        'OperatingPlanUpdates', 'Organization', 'ProgramArea',
                        'ProgramFinancingSchedule', 'ProgramProjectDescriptions', 'ProgramProject',
                        'Project', 'Providers', 'PublicLaw',
                        'RecoveryAct', 'ReferenceTables', 'RegionalOffice',
                        'ResourcePlanningOffice', 'Resources', 'ResponsibilityCenter',
                        'SchemaTypes', 'SpendingRate', 'StateOrganization',
                        'SubAppropriation', 'TransType', 'UnobligatedAuthority',
                        'URL', 'WorkCode' ]
        self.__command = command if command is not None else SQL.SELECTALL
        self.__source = source if source is not None else Source.StatusOfFunds
        self.__provider = provider if provider is not None else Provider.SQLite

# DbConfig( source, provider = Provider.SQLite )
class DbConfig( ):
    '''DbConfig( source, provider = Provider. SQLite ) provides list of Budget Execution
    tables across two databases ( values and references ) '''
    __source = None
    __provider = None
    __data = [ ]
    __accessdriver = None
    __accesspath = None
    __sqldriver = None
    __sqlpath = None
    __sqlitepath = None
    __sqlitedriver = None
    __table = None
    __name = None

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value ):
        if value is not None:
            self.__source = value

    @property
    def provider( self ):
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if value is not None:
            self.__provider = value

    @property
    def table( self ):
        if self.__table is not None and self.__table != '':
            return self.__table

    @table.setter
    def table( self, value ):
        if value != '':
            self.__table = value

    def __init__( self, source, provider = Provider.SQLite ):
        '''Constructor for the DbConfig class providing
        values value details'''
        self.__provider = provider
        self.__source = source
        self.__table = source.name
        self.__sqlitepath = os.getcwd( ) + r'\db\sqlite\datamodels\Data.db'
        self.__accessdriver = r'DRIVER={ Microsoft ACCDB Driver (*.mdb, *.accdb) };DBQ='
        self.__accesspath = os.getcwd( ) + r'\db\access\datamodels\Data.accdb'
        self.__sqldriver = r'DRIVER={ ODBC Driver 17 for SQL Server };SERVER=.\SQLExpress;'
        self.__sqlpath = os.getcwd( ) + r'\db\mssql\datamodels\Data.mdf'
        self.__data = [ 'Actual', 'AdministrativeRequests', 'Allocation',
                        'AmericanRescuePlan', 'AnnualCarryoverEstimates', 'AnnualCarryoverSurvey',
                        'AnnualReimbursableEstimates', 'AnnualReimbursableSurvey', 'ApplicationTable',
                        'AppropriationAvailableBalance', 'AppropriationDocument', 'AppropriationLevelAuthority',
                        'BudgetDocument', 'CarryoverApportionments', 'CarryoverRequests',
                        'Changes', 'CompassLevel', 'CompassOutlays',
                        'CongressionalReprogrammings', 'Contacts', 'Defactos',
                        'DeobligationActivity', 'Deobligations', 'DocumentControlNumber',
                        'Earmarks', 'Expenditure', 'PayPeriods',
                        'PayrollActivity', 'PayrollAuthority', 'PayrollCostCode',
                        'PayrollRequests', 'PRC', 'ProjectCostCodes',
                        'QueryDefinitions', 'RegionalAuthority', 'ReimbursableAgreement',
                        'ReimbursableFunds', 'Reports', 'Reprogrammings',
                        'GrossAuthority', 'GrossUtilization', 'HeadquartersAuthority',
                        'HumanResourceOrganization', 'JobsActCarryoverEstimates', 'MonthlyLedgerAccountBalances',
                        'NetAuthority', 'ObligationActivity', 'Obligation',
                        'OpenCommitment', 'SiteActivity', 'SiteProjectCode',
                        'SpecialAccount', 'StateGrantObligation', 'StatusOfAppropriations',
                        'StatusOfBudgetaryResources', 'StatusOfEarmarks', 'StatusOfFunds',
                        'StatusOfJobsActFunding', 'StatusOfSupplementalFunding', 'SuperfundSite',
                        'SupplementalCarryoverEstimates', 'SupplementalReimburseableEstimates', 'TransferActivity',
                        'Transfer', 'UnliquidatedObligation', 'UnobligatedBalance',
                        'AccountingEvents', 'Account', 'ActivityCode',
                        'AllowanceHolder', 'ApportionmentData', 'Appropriation',
                        'BudgetaryResourceExecution', 'BudgetControl', 'BudgetObjectClass',
                        'BudgetOutlay', 'CapitalPlanningInvestmentCodes', 'CarryoverOutlay',
                        'CongressionalControl', 'CostAreas', 'DataRuleDescriptions',
                        'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                        'FiscalYears', 'FiscalYearsBackUp', 'FundCategories',
                        'Fund', 'FundSymbols', 'GeneralLedgerAccount',
                        'Goal', 'GrowthRate', 'GsPayScales',
                        'HeadquartersOffice', 'Images', 'InfrastructureAccounts',
                        'Messages', 'MonthlyOutlay', 'NationalProgram',
                        'ObjectClassOutlay', 'Objective', 'OperatingPlan',
                        'OperatingPlanUpdates', 'Organization', 'ProgramArea',
                        'ProgramFinancingSchedule', 'ProgramProjectDescriptions', 'ProgramProject',
                        'Project', 'Providers', 'PublicLaw',
                        'RecoveryAct', 'ReferenceTables', 'RegionalOffice',
                        'ResourcePlanningOffice', 'Resources', 'ResponsibilityCenter',
                        'SchemaTypes', 'SpendingRate', 'StateOrganization',
                        'SubAppropriation', 'TransType', 'UnobligatedAuthority',
                        'URL', 'WorkCode' ]

    def __str__( self ):
        if isinstance( self.__table, str ):
            return self.__table

    def get_driver( self ):
        try:
            if self.__provider.name == 'SQLite':
                return self.get_path( )
            elif self.__provider.name == 'Access':
                return self.__accessdriver
            elif self.__provider.name == 'SqlServer':
                return self.__sqldriver
            else:
                return self.__sqlitedriver
        except Exception as e:
            exc = Error( e )
            exc.cause = 'DbConfig Class'
            exc.method = 'get_driver( self )'
            error = ErrorDialog( exc )
            error.show( )

    def get_path( self ):
        try:
            if self.__provider.name == 'SQLite':
                return self.__sqlitepath
            elif self.__provider.name == 'Access':
                return self.__accesspath
            elif self.__provider.name == 'SqlServer':
                return self.__sqlpath
            else:
                return self.__sqlitepath
        except Exception as e:
            exc = Error( e )
            exc.cause = 'DbConfig Class'
            exc.method = 'filepath( self )'
            error = ErrorDialog( exc )
            error.show( )

    def get_connectionstring( self ):
        try:
            path = self.get_path( )
            if self.__provider.name == Provider.Access.name:
                return self.get_driver( ) + path
            elif self.__provider.name == Provider.SqlServer.name:
                return r'DRIVER={ ODBC Driver 17 for SQL Server };Server=.\SQLExpress;' + f'AttachDBFileName={path}' \
                       + f'DATABASE={path}Trusted_Connection=yes;'
            else:
                return f'{path} '
        except Exception as e:
            exc = Error( e )
            exc.cause = 'DbConfig Class'
            exc.method = 'get_connectionstring( self )'
            error = ErrorDialog( exc )
            error.show( )

# Connection( source, provider = Provider.SQLite )
class Connection( DbConfig ):
    '''Connection( source, provider = Provider.SQLite ) initializes
    object used to connect to the databases'''
    __driver = None
    __path = None
    __connectionstring = None

    @property
    def driver( self ):
        if self.__driver is not None:
            return self.__driver

    @driver.setter
    def driver( self, value ):
        if value != '':
            self.__driver = value

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, value ):
        if value != '':
            self.__path = value

    @property
    def connection_string( self ):
        if self.__connectionstring is not None \
                and self.__connectionstring != '':
            return self.__connectionstring

    @connection_string.setter
    def connection_string( self, value ):
        if value != '':
            self.__connectionstring = value

    def __init__( self, source, provider = Provider.SQLite ):
        super( ).__init__( source, provider )
        self.__source = super( ).source
        self.__provider = super( ).provider
        self.__path = super( ).get_path( )
        self.__driver = super( ).get_driver( )
        self.__dsn = super( ).table + ';' if provider == Provider.SQLite else None
        self.__connectionstring = super( ).get_connectionstring( )

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

# SqlConfig( command = SQL.SELECTALL, names = [ ], values = ( ), style = None )
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
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, value ):
        if value != '':
            self.__command = value

    @property
    def names( self ):
        ''' builds crit from provider index namevaluepairs'''
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, value ):
        ''' builds crit from provider index namevaluepairs'''
        if value is not None:
            self.__names = value

    @property
    def values( self ):
        ''' builds crit from provider index namevaluepairs'''
        if self.__values is not None:
            return self.__values

    @values.setter
    def values( self, value ):
        ''' builds crit from provider index namevaluepairs'''
        if value is not None:
            self.__values = value

    @property
    def paramstyle( self ):
        ''' Property representing the DBI param_style'''
        if self.__paramstyle is not None:
            return self.__paramstyle

    @paramstyle.setter
    def paramstyle( self, value ):
        ''' Property representing the DBI param_style attribute'''
        if value is not None:
            self.__paramstyle = value
        else:
            self.__paramstyle = ParamStyle.qmark

    @property
    def key_value_pairs( self ):
        if self.__kvp is not None:
            return self.__kvp

    @key_value_pairs.setter
    def key_value_pairs( self, value ):
        if value is not None:
            self.__kvp = value

    def __init__( self, command = SQL.SELECTALL, names = ( ), values = ( ), style = None ):
        self.__command = command
        self.__names = names if names is not None else [ ]
        self.__values = values if values is not None else ( )
        self.__paramstyle = style if style is not None else ParamStyle.qmark
        self.__kvp = dict( zip( names, list( values ) ) ) \
            if isinstance( names, list ) and isinstance( values, tuple ) else None

    def dump_kvp( self ) -> str:
        '''dump( ) returns string of 'values = index AND' pairs
        @return:
        '''
        try:
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                pairs = ''
                kvp = zip( self.__names, self.__values )
                for k, v in kvp:
                    pairs += f'{k} = \'{v}\' AND '
                criteria = pairs.rstrip( ' AND ' )
                return criteria
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'dump_kvp( self )'
            err = ErrorDialog( exc )
            err.show( )

    def dump_where( self ) -> str:
        '''dump_where( ) returns a string
        using list arguments names and values
        @return: '''
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
            exc.method = 'dump_where( self )'
            err = ErrorDialog( exc )
            err.show( )

    def dump_set( self ) -> str:
        '''dump_set( ) returns a string
        using list arguments names and values
        @return: '''
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
            exc.method = 'dump_set( self )'
            err = ErrorDialog( exc )
            err.show( )

    def dump_columns( self ) -> str:
        '''dump_columns( ) returns a string of columns
        used in select and insert statements from list self.__names
        @return: '''
        try:
            if self.__names is not None:
                cols = ''
                for n in self.__names:
                    cols += f'{n}, '
                columns = '(' + cols.rstrip( ', ' ) + ')'
                return columns
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'dump_columns( self )'
            err = ErrorDialog( exc )
            err.show( )

    def dump_values( self ) -> str:
        '''dump_values( ) returns a string of values
        used in select statements from list self.__names
        @return: '''
        try:
            if self.__values is not None:
                vals = ''
                for v in self.__values:
                    vals += f'{v}, '
                values = 'VALUES (' + vals.rstrip( ', ' ) + ')'
                return values
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlConfig'
            exc.method = 'dump_values( self )'
            err = ErrorDialog( exc )
            err.show( )

# SqlStatement( db_config,  sqlcfg )
class SqlStatement( ):
    '''SqlStatement( dbcfg, sqlcfg ) Class
    represents the values models used in the SQLite database'''
    __cmdtyp = None
    __sqlcfg = None
    __dbcfg = None
    __source = None
    __provider = None
    __table = None
    __names = None
    __values = None
    __text = None

    @property
    def data_config( self ):
        if isinstance( self.__dbcfg, DbConfig ):
            return self.__dbcfg

    @data_config.setter
    def data_config( self, value ):
        if isinstance( value, DbConfig ):
            self.__dbcfg = value

    @property
    def sql_config( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlcfg, SqlConfig ):
            return self.__sqlcfg

    @sql_config.setter
    def sql_config( self, value ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( value, SqlConfig ):
            self.__sqlcfg = value

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
        if value is not None:
            self.__provider = value

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, value ):
        if value is not None:
            self.__path = value

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, value ):
        if value != '':
            self.__table = value

    @property
    def names( self ):
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, value ):
        if value is not None:
            self.__names = value

    @property
    def values( self ):
        if self.__values is not None:
            return self.__values

    @values.setter
    def values( self, value ):
        if value is not None:
            self.__values = value

    @property
    def command_text( self ):
        if self.__text is not None:
            return self.__text

    @command_text.setter
    def command_text( self, value ):
        if value != '':
            self.__text = value

    @property
    def command_type( self ):
        if self.__cmdtyp is not None:
            return self.__cmdtyp

    @command_type.setter
    def command_type( self, value ):
        if value is not None:
            self.__cmdtyp = value
        else:
            command = SQL( 'SELECT' )
            self.__cmdtyp = command

    def __init__( self, dbcfg, sqlcfg ):
        self.__dbcfg = dbcfg
        self.__sqlcfg = sqlcfg
        self.__cmdtyp = sqlcfg.command
        self.__provider = dbcfg.provider
        self.__source = dbcfg.source
        self.__table = dbcfg.table
        self.__names = sqlcfg.names
        self.__values = sqlcfg.values
        self.__text = self.get_query( )

    def __str__( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    def get_query( self ) -> str:
        try:
            table = self.__table
            columns = self.__sqlcfg.dump_columns( )
            values = self.__sqlcfg.dump_values( )
            predicate = self.__sqlcfg.dump_where( )
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                if self.__cmdtyp == SQL.SELECTALL:
                    if len( self.__names ) == 0:
                        self.__text = f'SELECT * FROM {table}'
                        return self.__text
                    if len( self.__names ) > 0:
                        self.__text = f'SELECT ' + columns + f'FROM {table}' + f' {predicate}'
                        return self.__text
                elif self.__cmdtyp == SQL.SELECT:
                    if len( self.__names ) == 0:
                        self.__text = f'SELECT * FROM {table}'
                        return self.__text
                    if len( self.__names ) > 0:
                        self.__text = f'SELECT ' + columns + f' FROM {table}' + f' {predicate}'
                        return self.__text
                elif self.__cmdtyp == SQL.INSERT:
                    self.__text = f'INSERT INTO {table} ' + f'{columns} ' + f'{values}'
                    return self.__text
                elif self.__cmdtyp == SQL.UPDATE:
                    self.__text = f'UPDATE {table} ' + f'{self.__sqlcfg.dump_set( )} ' + f'{values}'
                    return self.__text
                elif self.__cmdtyp == SQL.DELETE:
                    self.__text = f'DELETE FROM {table} ' + f' {predicate}'
                    return self.__text
            else:
                if isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__cmdtyp == SQL.SELECT:
                        cols = columns.lstrip( '(' ).rstrip( ')' )
                        self.__text = f'SELECT {cols} FROM {table}'
                        return self.__text
                elif not isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__cmdtyp == SQL.SELECTALL:
                        self.__text = f'SELECT * FROM {table}'
                        return self.__text
                elif self.__cmdtyp == 'DELETE':
                    self.__text = f'DELETE FROM {table}'
                    return self.__text
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlStatement'
            exc.method = 'getcommandtext( self )'
            err = ErrorDialog( exc )
            err.show( )

# Query( connection, sql_statement )
class Query( ):
    '''Base class for database interaction'''
    __cnx = None
    __sql = None
    __sqlcfg = None
    __cmdtype = None
    __source = None
    __table = None
    __provider = None
    __names = None
    __values = None
    __path = None
    __connectionstring = None
    __text = None

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
            self.__provider = Provider.SQLite

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
        if isinstance( self.__cnx, Connection ):
            return self.__cnx

    @connection.setter
    def connection( self, value ):
        if isinstance( value, Connection ):
            self.__cnx = value

    @property
    def sql_statement( self ):
        if isinstance( self.__sql, SqlStatement ):
            return self.__sql

    @sql_statement.setter
    def sql_statement( self, value ):
        if isinstance( value, SqlStatement ):
            self.__sql = value

    @property
    def command_type( self ):
        if self.__cmdtype is not None:
            return self.__cmdtype
        if self.__cmdtype is None:
            cmd = SQL( 'SELECT' )
            return cmd

    @command_type.setter
    def command_type( self, value ):
        if isinstance( value, SQL ):
            self.__cmdtype = value

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, value ):
        if value != '':
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
    def command_text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @command_text.setter
    def command_text( self, value ):
        if value != '':
            self.__text = value

    @property
    def connection_string( self ):
        if isinstance( self.__connectionstring, str ):
            return self.__connectionstring

    @connection_string.setter
    def connection_string( self, value ):
        if isinstance( value, str ):
            self.__connectionstring = str( value )

    def __init__( self, connection, sqlstatement ):
        self.__cnx = connection if isinstance( connection, Connection ) else None
        self.__sql = sqlstatement if isinstance( sqlstatement, SqlStatement ) else None
        self.__sqlcfg = sqlstatement.sql_config
        self.__source = connection.source
        self.__provider = connection.provider
        self.__cmdtype = sqlstatement.command_type
        self.__path = connection.path
        self.__connectionstring = connection.connection_string
        self.__text = sqlstatement.get_query( )

    def __str__( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    def get_query( self ):
        try:
            table = self.__table
            columns = self.__sqlcfg.dump_columns( )
            values = self.__sqlcfg.dump_values( )
            predicate = self.__sqlcfg.dump_where( )
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                if self.__cmdtype == SQL.SELECTALL:
                    if len( self.__names ) == 0:
                        self.__text = f'SELECT * FROM { table }'
                        return self.__text
                    if len( self.__names ) > 0:
                        self.__text = f'SELECT ' + columns + f'FROM { table }' + f' { predicate }'
                        return self.__text
                elif self.__cmdtype == SQL.SELECT:
                    if len( self.__names ) == 0:
                        self.__text = f'SELECT * FROM { table }'
                        return self.__text
                    if len( self.__names ) > 0:
                        self.__text = f'SELECT ' + columns + f' FROM { table }' + f' { predicate }'
                        return self.__text
                elif self.__cmdtype == SQL.INSERT:
                    self.__text = f'INSERT INTO {table} ' + f'{ columns } ' + f'{ values }'
                    return self.__text
                elif self.__cmdtype == SQL.UPDATE:
                    self.__text = f'UPDATE {table} ' + f'{ self.__sqlcfg.dump_set( ) } ' + f'{ values }'
                    return self.__text
                elif self.__cmdtype == SQL.DELETE:
                    self.__text = f'DELETE FROM { table } ' + f'{ predicate }'
                    return self.__text
            else:
                if isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__cmdtype == SQL.SELECT:
                        cols = columns.lstrip( '(' ).rstrip( ')' )
                        self.__text = f'SELECT { cols } FROM { table }'
                        return self.__text
                elif not isinstance( self.__names, list ) and not isinstance( self.__values, tuple ):
                    if self.__cmdtype == SQL.SELECTALL:
                        self.__text = f'SELECT * FROM { table }'
                        return self.__text
                elif self.__cmdtype == 'DELETE':
                    self.__text = f'DELETE FROM { table }'
                    return self.__text
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlStatement'
            exc.method = 'query( self )'
            err = ErrorDialog( exc )
            err.show( )

# SQLiteData( connection, sql_statement )
class SQLiteData( Query ):
    '''SQLiteData( value, sqlcfg ) represents
     the budget execution values classes'''
    __driver = None
    __dsn = None
    __query = None
    __data = None
    __frame = None
    __columns = None

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
        if isinstance( self.__data, tuple ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, tuple ):
            self.__data = value

    @property
    def frame( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @frame.setter
    def frame( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

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
        self.__sqlstatement = super( ).sql_statement
        self.__source = super( ).source
        self.__table = super( ).source.name
        self.__driver = super( ).connection.driver
        self.__query = super( ).sql_statement.get_query( )

    def __str__( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    def create_table( self ) -> list[ tuple ]:
        try:
            query = self.__query
            sqlite = self.__connection.connect( )
            cursor = sqlite.cursor( )
            data = cursor.execute( query )
            self.__columns = [ i[ 0 ] for i in cursor.description ]
            self.__data = [ tuple( i ) for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SQLiteData'
            exc.method = 'create_table( self )'
            err = ErrorDialog( exc )
            err.show( )

    def create_frame( self ) -> DataFrame:
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
            exc.method = 'create_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# AccessData( connection, sql_statement )
class AccessData( Query ):
    '''AccessData( value, sqlcfg ) class
      represents the budget execution
      values model classes in the MS ACCDB database'''
    __query = None
    __driver = None
    __dsn = None
    __data = None
    __columns = None

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
    def columns( self ):
        if isinstance( self.__columns, list ) and len( self.__columns ) > 0:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, list ):
            self.__columns = value

    @property
    def query( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    @query.setter
    def query( self, value ):
        if value != '':
            self.__query = value

    def __init__( self, connection, sqlstatement ):
        super( ).__init__( connection, sqlstatement )
        self.__source = super( ).source
        self.__provider = Provider.Access
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sql_statement
        self.__query = sqlstatement.query
        self.__table = super( ).table
        self.__driver = r'DRIVER={ Microsoft ACCDB Driver( *.mdb, *.accdb ) };'
        self.__data = [ ]

    def __str__( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    def create_table( self ) -> list[ tuple ]:
        try:
            query = self.__query
            access = self.__connection.connect( )
            cursor = access.cursor( )
            data = cursor.execute( query )
            self.__columns = [ i[ 0 ] for i in cursor.description ]
            self.__data = [ tuple( i ) for i in data.fetchall( ) ]
            cursor.close( )
            access.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'AccessData'
            exc.method = 'create_table( self )'
            err = ErrorDialog( exc )
            err.show( )

    def create_frame( self ) -> DataFrame:
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
            exc.method = 'create_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# SqlData( connection, sql_statement )
class SqlData( Query ):
    '''SqlData( value, sqlcfg ) object
    represents the values models in the MS SQL Server
    database'''
    __query = None
    __server = None
    __driver = None
    __dsn = None
    __columns = None
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
        if isinstance( self.__data, tuple ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, tuple ):
            self.__data = value

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
        self.__query = sqlstatement.query
        self.__table = connection.source.name
        self.__server = r'(LocalDB)\MSSQLLocalDB;'
        self.__driver = r'{ SQL Server Native Client 11.0 };'

    def __str__( self ):
        if isinstance( self.__query, str ) and self.__query != '':
            return self.__query

    def create_table( self ) -> list[ tuple ]:
        try:
            query = self.__query
            connection = self.__connection.connect( )
            cursor = connection.cursor( )
            data = cursor.execute( query )
            self.__columns = [ i[ 0 ] for i in cursor.description ]
            self.__data = [ tuple( i ) for i in data.fetchall( ) ]
            cursor.close( )
            connection.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlData'
            exc.method = 'create_table( self )'
            err = ErrorDialog( exc )
            err.show( )

    def create_frame( self ) -> DataFrame:
        try:
            query = f'SELECT * FROM {self.__table}'
            connection = self.__connection.connect( )
            self.__frame = sqlreader( query, connection )
            connection.close( )
            return self.__frame
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'SqlData'
            exc.method = 'create_frame( self )'
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
    __commandtype = None
    __source = None
    __provider = None
    __dbconfig = None
    __sqlcfg = None
    __cnx = None
    __sql = None
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
        if isinstance( self.__commandtype, SQL ):
            return self.__commandtype

    @command.setter
    def command( self, value ):
        '''Set the command property to a DataCommand instance'''
        if isinstance( value, SQL ):
            self.__commandtype = value

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
    def data_config( self ):
        if isinstance( self.__dbconfig, DbConfig ):
            return self.__dbconfig

    @data_config.setter
    def data_config( self, value ):
        if isinstance( value, DbConfig ):
            self.__dbconfig = value

    @property
    def sql_config( self ):
        '''Gets instance of the SqlConfig class'''
        if isinstance( self.__sqlcfg, SqlConfig ):
            return self.__sqlcfg

    @sql_config.setter
    def sql_config( self, value ):
        '''Sets property to an instance of the SqlConfig class'''
        if isinstance( value, SqlConfig ):
            self.__sqlcfg = value

    def __init__( self, source, provider = Provider.SQLite,
                  command = SQL.SELECTALL, names = None, values = None ):
        self.__source = source if isinstance( source, Source ) else None
        self.__provider = provider
        self.__commandtype = command
        self.__name = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__dbconfig = DbConfig( self.__source, self.__provider )
        self.__cnx = Connection( source )
        self.__sqlcfg = SqlConfig( self.__commandtype, self.__names, self.__values )
        self.__sql = SqlStatement( self.__dbconfig, self.__sqlcfg )

    def create_table( self ) -> list[ tuple ]:
        try:
            if self.__provider == Provider.SQLite:
                sqlite = SQLiteData( self.__cnx, self.__sql )
                self.__data = [ tuple( i ) for i in sqlite.getdata( ) ]
                return self.__data
            elif self.__provider == Provider.Access:
                access = AccessData( self.__cnx, self.__sql )
                self.__data = [ tuple( i ) for i in access.getdata( ) ]
                return self.__data
            elif self.__provider == Provider.SqlServer:
                sqlserver = SqlData( self.__cnx, self.__sql )
                self.__data = [ tuple( i ) for i in sqlserver.getdata( ) ]
                return self.__data
            else:
                sqlite = SQLiteData( self.__cnx, self.__sql )
                self.__data = [ tuple( i ) for i in sqlite.getdata( ) ]
                return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Ninja'
            exc.cause = 'DataBuilder'
            exc.method = 'create_table( self )'
            error = ErrorDialog( exc )
            error.show( )

# DataColumn( name = '', datatype = None, value = None  )
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

    def is_numeric( self ):
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
            exc.method = 'is_numeric( self )'
            err = ErrorDialog( exc )
            err.show( )

    def is_text( self ):
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
            exc.method = 'is_text( self )'
            err = ErrorDialog( exc )
            err.show( )

# DataRow( names = None, values = ( ), source = None)
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

    def __init__( self, names = None, values = ( ), source = None ):
        self.__source = source if isinstance( source, Source ) else None
        self.__names = names if isinstance( names, list ) else None
        self.__values = values if isinstance( values, tuple ) else None
        self.__items = zip( names, list( values ) )
        self.__key = str( self.__names[ 0 ] ) if isinstance( self.__names, list ) else None
        self.__index = int( self.__values[ 0 ] ) if isinstance( self.__values, tuple ) else None

    def __str__( self ):
        if isinstance( self.__index, int ) and self.__index > -1:
            return 'Row ID: ' + str( self.__index )

# DataTable( columns = None, rows = None, source = None, dataframe = None  )
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
        if isinstance( self.__rows, tuple ):
            return self.__rows

    @data.setter
    def data( self, value ):
        if isinstance( value, tuple ):
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
        self.__name = source.name if isinstance( source, Source ) and source.name != '' else None
        self.__rows = [ tuple( r ) for r in dataframe.iterrows( ) ]
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
        if value != '':
            self.__name = value

    @property
    def path( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    @path.setter
    def path( self, value ):
        if value != '':
            self.__path = value

    @property
    def data( self ):
        if isinstance( self.__data, tuple ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, tuple ):
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
        self.__path = DbConfig( source, Provider.SQLite ).get_path( )
        self.__sql = f'SELECT * FROM {source.name};'

    def get_frame( self ):
        '''Factory method that returns a pandas DataFrame object
        based on the Source buffer arguement 'source' given to the constructor'''
        try:
            path = self.__path
            src = self.__source
            table = src.name
            conn = sqlite.connect( path )
            sql = f'SELECT * FROM {table};'
            frame = sqlreader( sql, conn )
            return frame
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'BudgetData'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )
