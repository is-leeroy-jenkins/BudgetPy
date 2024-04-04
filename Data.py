'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Data.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Data.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2024  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at: terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Data.py
  </summary>
  ******************************************************************************************
  '''
import sqlite3 as sqlite
from pandas import DataFrame
from pandas import read_sql as sqlreader
import pyodbc as db
import os
from Static import Source, Provider, SQL, ParamStyle
from Booger import Error, ErrorDialog

class Pascal( ):
    '''

    Constructor:
    Pascal( input: str )

    Purpose:
    Class splits string 'input' argument into Pascal Casing

    '''
    __input: str=None
    __output: str=None

    @property
    def input( self ) -> str:
        if self.__input is not None:
            return self.__input

    @input.setter
    def input( self, value: str ):
        if value is not None:
            self.__input = value

    @property
    def output( self ) -> str:
        if self.__output is not None:
            return self.__output

    @output.setter
    def output( self, value: str ):
        if value is not None and value != self.__input:
            self.__output = value

    def __init__( self, input: str=None ):
        self.__input = input

    def __str__( self ) -> str:
        if self.__output is not None:
            return self.__output

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'input', 'split', 'join' ]

    def split( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__input is not None and self.__input.count( ' ' ) == 0:
                _buffer = [ c for c in self.__input ]
                _retval = ''
                _output = ''
                _count = len( _buffer )

                for i in range( _count ):
                    _char = _buffer[ i ]
                    if i <= 1 and _char.islower( ):
                        _output += f'{_char}'
                    elif i <= 1 and _char.isupper( ):
                        _output += f'{_char}'
                    elif i > 1 and _char.islower( ):
                        _output += f'{_char}'
                    elif i > 1 and _char.isupper( ):
                        _output += f' {_char}'

                if len( _output ) < 5:
                    _retval = _output.replace( ' ', '' )
                else:
                    _retval = _output.replace( 'Ah', 'AH' ).replace( 'Boc', 'BOC' ) \
                        .replace( 'Rpio', 'RPIO' ).replace( 'Rc', 'RC' ) \
                        .replace( 'Prc', 'PRC' ).replace( 'Id', 'ID' ) \
                        .replace( 'Omb', 'OMB' ).replace( 'Npm', 'NPM' ) \
                        .replace( 'Foc', 'FOC' ).replace( 'Org', 'ORG' ) \
                        .replace( ' THE ', ' The ' ).replace( ' OR ', ' Or ' ) \
                        .replace( ' AND ', ' And ' ).replace( 'BUT ', ' But ' ) \
                        .replace( ' OF ', ' Of ' )

                self.__output = _retval
                return self.__output
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'Pascal'
            _exc.method = 'split( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def join( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__input is not None and self.__input.count( ' ' ) > 0:
                _buffer = [ c for c in self.__input ]
                _output = list( )
                _retval = ''

                for char in _buffer:
                    if char != ' ':
                        _output.append( char )

                for o in _output:
                    _retval += f'{o}'

                self.__output = _retval.replace( 'AH', 'Ah' ).replace( 'BOC', 'Boc' ) \
                    .replace( 'RPIO', 'Rpio' ).replace( 'RC', 'Rc' ) \
                    .replace( 'PRC', 'Prc' ).replace( 'ID', 'Id' ) \
                    .replace( 'OMB', 'Omb' ).replace( 'NPM', 'Npm' ) \
                    .replace( 'FOC', 'Foc' ).replace( 'ORG', 'Org' ) \
                    .replace( 'THE', 'The' ).replace( 'OR', 'Or' ) \
                    .replace( 'AND', 'And' ).replace( 'BUT', 'But' ) \
                    .replace( 'OF', 'Of' )

                return self.__output
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'Pascal'
            _exc.method = 'join( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SqlPath( ):
    '''

    Constructor:
    SqlPath( )

    Purpose:
    Class providing relative_path paths to the
    folders containing sqlstatement files and driverinfo
    paths used in the application

    '''
    __accessdriver: str=None
    __accesspath: str=None
    __sqlitedriver: str=None
    __sqlitepath: str=None
    __sqldriver: str=None
    __sqldatabase: str=None

    @property
    def sqlite_driver( self ) -> str:
        if self.__sqlitedriver is not None:
            return self.__sqlitedriver

    @sqlite_driver.setter
    def sqlite_driver( self, value: str ):
        if value is not None:
            self.__sqlitedriver = value

    @property
    def sqlite_database( self ) -> str:
        if self.__sqlitepath is not None:
            return self.__sqlitepath

    @sqlite_database.setter
    def sqlite_database( self, value: str ):
        if value is not None:
            self.__sqlitepath = value

    @property
    def access_driver( self ) -> str:
        if self.__accessdriver is not None:
            return self.__accessdriver

    @access_driver.setter
    def access_driver( self, value: str ):
        if value is not None:
            self.__accessdriver = value

    @property
    def access_database( self ) -> str:
        if self.__accesspath is not None:
            return self.__accesspath

    @access_database.setter
    def access_database( self, value: str ):
        if value is not None:
            self.__accesspath = value

    @property
    def sqlserver_driver( self ) -> str:
        if self.__sqldriver is not None:
            return self.__sqldriver

    @sqlserver_driver.setter
    def sqlserver_driver( self, value: str ):
        if value is not None:
            self.__sqldriver = value

    @property
    def sqlserver_database( self ) -> str:
        if self.__sqldatabase is not None:
            return self.__sqldatabase

    @sqlserver_database.setter
    def sqlserver_database( self, value: str ):
        if value is not None:
            self.__sqldatabase = value

    def __init__( self ):
        self.__sqlitedriver = 'sqlite3'
        self.__sqlitepath = r'db\sqlite\datamodels\sql'
        self.__accessdriver = r'DRIVER={Microsoft ACCDB Driver (*.mdb, *.accdb)};DBQ='
        self.__accesspath = r'db\access\datamodels\sql'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
        self.__sqldatabase = r'db\mssql\datamodels\sql'

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'sqlite_driver', 'sqlite_database',
                 'access_driver', 'access_database',
                 'sqlserver_driver', 'sqlserver_database' ]

class SqlFile( ):
    '''

    Constructor:
    SqlFile( source: Source = None, provider: Provider  = Provider.SQLite,
            command: SQL=SQL.SELECTALL )

    Purpuse:
    Class providing access to sqlstatement sub-folders in the application provided
    optional arguments source, provider, and command.

    '''
    __data: list[ str ]=None
    __commandtype: str=None
    __source: Source=None
    __provider: Provider=None

    @property
    def provider( self ) -> Provider:
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value: Provider ):
        if value is not None:
            self.__provider = value

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    @property
    def command( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

    @command.setter
    def command( self, value: SQL ):
        if value is not None:
            self.__commandtype = value

    def __init__( self, source: Source = None, provider: Provider = Provider.SQLite,
                  commandtype: SQL=SQL.SELECTALL ):
        self.__data = [ 'Actuals',
                        'AdjustedTrialBalances'
                        'AdministrativeRequests',
                        'Allocations',
                        'AmericanRescuePlanCarryoverEstimates',
                        'AnnualCarryoverEstimates',
                        'AnnualReimbursableEstimates',
                        'ApportionmentData',
                        'AppropriationAvailableBalances',
                        'AppropriationDocuments',
                        'AppropriationLevelAuthority',
                        'BudgetaryResourceExecution',
                        'BudgetAuthorityAndOutlays',
                        'BudgetDocuments',
                        'CarryoverApportionments',
                        'CarryoverRequests',
                        'Changes',
                        'CompassLevels',
                        'CongressionalProjects',
                        'Contacts',
                        'CombinedSchedules',
                        'Defactos',
                        'Deobligations',
                        'DocumentControlNumbers',
                        'Earmarks',
                        'Expenditures',
                        'HeadquartersAuthority',
                        'InflationReductionActCarryoverEstimates',
                        'JobsActCarryoverEstimates',
                        'LedgerAccounts',
                        'MainAccounts',
                        'MonthlyActuals',
                        'MonthlyLedgerAccountBalances',
                        'MonthlyOutlays',
                        'ObligationActivity',
                        'Obligations',
                        'OpenCommitments',
                        'OperatingPlans',
                        'Outlays',
                        'Partitions'
                        'PayrollAuthority',
                        'PayrollRequests',
                        'PRC',
                        'QueryDefinitions',
                        'RecoveryAct',
                        'RegionalAuthority',
                        'ReimbursableAgreements',
                        'ReimbursableFunds',
                        'Reports',
                        'Reprogrammings',
                        'StatusOfSuperfundSites',
                        'SpecialAccounts',
                        'SpendingDocuments',
                        'SpendingRates',
                        'StateGrantObligations',
                        'StatusOfAmericanRescuePlanFunds',
                        'StatusOfAppropriations',
                        'StatusOfBudgetaryResources',
                        'StatusOfEarmarks',
                        'StatusOfFunds',
                        'StatusOfInflationReductionActFunds',
                        'StatusOfJobsActFunds',
                        'StatusOfSupplementalFunds',
                        'StatusOfSuperfundSites',
                        'StatusOfSpecialAccountFunds',
                        'SupplementalCarryoverEstimates',
                        'TransferActivity',
                        'Transfers',
                        'UnliquidatedObligations',
                        'UnobligatedBalances',
                        'AccountingEvents',
                        'Accounts',
                        'ActivityCodes',
                        'AllowanceHolders',
                        'ApplicationTables',
                        'Appropriations',
                        'BudgetControls',
                        'BudgetObjectClasses',
                        'CapitalPlanningInvestmentCodes',
                        'ColumnSchema',
                        'CompassErrors',
                        'CongressionalControls',
                        'CostAreas',
                        'DataRuleDescriptions',
                        'Documents',
                        'EarmarkCodes',
                        'FederalHolidays',
                        'FinanceObjectClasses',
                        'FiscalYears',
                        'FundCategories',
                        'Funds',
                        'FundSymbols',
                        'Goals',
                        'GsPayScales',
                        'HeadquartersOffices',
                        'Images',
                        'Messages',
                        'MainAccounts',
                        'NationalPrograms',
                        'Objectives',
                        'Organizations',
                        'Partitions',
                        'PayPeriods',
                        'ProgramAreas',
                        'ProgramProjectDescriptions',
                        'ProgramProjects',
                        'Projects',
                        'Providers',
                        'PublicLaws',
                        'ReconciliationLines',
                        'ReferenceTables',
                        'RegionalOffices',
                        'ReportingLines',
                        'ResourcePlanningOffices',
                        'Resources',
                        'ResponsibilityCenters',
                        'SchemaTypes',
                        'StateOrganizations',
                        'SubAppropriations',
                        'TransTypes',
                        'TreasurySybmols',
                        'URL' ]
        self.__commandtype = commandtype
        self.__source = source
        self.__provider = provider

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'source', 'provider', 'command', 'get_file_path',
                 'get_folder_path', 'get_command_text' ]

    def get_file_path( self ) -> str:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _sqlpath = SqlPath( )
            _data = self.__data
            _provider = self.__provider.name
            _tablename = self.__source.name
            _command = self.__commandtype.name
            _current = os.getcwd( )
            _filepath = ''
            if _provider == 'SQLite' and _tablename in _data:
                _filepath = f'{_sqlpath.sqlite_database}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _filepath )
            elif _provider == 'ACCDB' and _tablename in _data:
                _filepath = f'{_sqlpath.access_database}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _filepath )
            elif _provider == 'SqlServer' and _tablename in _data:
                _filepath = f'{_sqlpath.sqlserver_database}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _filepath )
            else:
                _filepath = f'{_sqlpath.sqlite_database}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _filepath )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlFile'
            _exc.method = 'get_file_path( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_folder_path( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _sqlpath = SqlPath( )
            _data = self.__data
            _source = self.__source.name
            _provider = self.__provider.name
            _command = self.__commandtype.name
            _current = os.getcwd( )
            _folder = ''
            if _provider == 'SQLite' and _source in _data:
                _folder = f'{_sqlpath.sqlite_database}\\{_command}'
                return os.path.join( _current, _folder )
            elif _provider == 'ACCDB' and _source in _data:
                _folder = f'{_sqlpath.access_database}\\{_command}'
                return os.path.join( _current, _folder )
            elif _provider == 'SqlServer' and _source in _data:
                _folder = f'{_sqlpath.sqlserver_database}\\{_command}'
                return os.path.join( _current, _folder )
            else:
                _folder = f'{_sqlpath.sqlite_database}\\{_command}'
                return os.path.join( _current, _folder )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlFile'
            _exc.method = 'get_folder_path( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_command_text( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _source = self.__source.name
            _paths = self.get_file_path( )
            _folder = self.get_folder_path( )
            _sql = ''
            for name in os.listdir( _folder ):
                if name.endswith( '.sql' ) and os.path.splitext( name )[ 0 ] == _source:
                    _path = os.path.join( _folder, name )
                    _query = open( _path )
                    _sql = _query.read( )
                    return _sql
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlFile'
            _exc.method = 'get_command_text( self, other )'
            _err = ErrorDialog( _exc )
            _err.show( )

class DbConfig( ):
    '''

    Constructor:
        DbConfig( source: Source, provider: Provider = Provider.SQLite )

    Purpose:
        Class provides list of Budget Execution tables across two databases

    '''
    __source: Source=None
    __provider: Provider=None
    __data: list[ str ]=None
    __accessdriver: str=None
    __accesspath: str=None
    __sqldriver: str=None
    __sqlpath: str=None
    __sqlitepath: str=None
    __sqlitedriver: str=None
    __tablename: str=None

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    @property
    def provider( self ) -> Provider:
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value: Provider ):
        if value is not None:
            self.__provider = value

    @property
    def table_name( self ) -> str:
        '''Gets the'''
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value: str ):
        if value is not None:
            self.__tablename = value

    def __init__( self, source: Source, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = source
        self.__tablename = source.name
        self.__sqlitepath = os.getcwd( ) + r'\db\sqlite\datamodels\Data.db'
        self.__accessdriver = r'DRIVER={ Microsoft Access Driver (*.mdb, *.accdb) };DBQ='
        self.__accesspath = os.getcwd( ) + r'\db\access\datamodels\sql\Data.accdb'
        self.__sqldriver = r'DRIVER={ ODBC Driver 17 for SQL Server };SERVER=.\SQLExpress;'
        self.__sqlpath = os.getcwd( ) + r'\db\mssql\datamodels\Data.mdf'
        self.__data = [ 'Actuals',
                        'AdjustedTrialBalances'
                        'AdministrativeRequests',
                        'Allocations',
                        'AmericanRescuePlanCarryoverEstimates',
                        'AnnualCarryoverEstimates',
                        'AnnualReimbursableEstimates',
                        'ApportionmentData',
                        'AppropriationAvailableBalances',
                        'AppropriationDocuments',
                        'AppropriationLevelAuthority',
                        'BudgetaryResourceExecution',
                        'BudgetAuthorityAndOutlays',
                        'BudgetDocuments',
                        'CarryoverApportionments',
                        'CarryoverRequests',
                        'Changes',
                        'CompassLevels',
                        'CongressionalProjects',
                        'Contacts',
                        'CombinedSchedules',
                        'Defactos',
                        'Deobligations',
                        'DocumentControlNumbers',
                        'Earmarks',
                        'Expenditures',
                        'HeadquartersAuthority',
                        'InflationReductionActCarryoverEstimates',
                        'JobsActCarryoverEstimates',
                        'LedgerAccounts',
                        'MainAccounts',
                        'MonthlyActuals',
                        'MonthlyLedgerAccountBalances',
                        'MonthlyOutlays',
                        'ObligationActivity',
                        'Obligations',
                        'OpenCommitments',
                        'OperatingPlans',
                        'Outlays',
                        'Partitions'
                        'PayrollAuthority',
                        'PayrollRequests',
                        'PRC',
                        'QueryDefinitions',
                        'RecoveryAct',
                        'RegionalAuthority',
                        'ReimbursableAgreements',
                        'ReimbursableFunds',
                        'Reports',
                        'Reprogrammings',
                        'StatusOfSuperfundSites',
                        'SpecialAccounts',
                        'SpendingDocuments',
                        'SpendingRates',
                        'StateGrantObligations',
                        'StatusOfAmericanRescuePlanFunds',
                        'StatusOfAppropriations',
                        'StatusOfBudgetaryResources',
                        'StatusOfEarmarks',
                        'StatusOfFunds',
                        'StatusOfInflationReductionActFunds',
                        'StatusOfJobsActFunds',
                        'StatusOfSupplementalFunds',
                        'StatusOfSuperfundSites',
                        'StatusOfSpecialAccountFunds',
                        'SupplementalCarryoverEstimates',
                        'TransferActivity',
                        'Transfers',
                        'UnliquidatedObligations',
                        'UnobligatedBalances',
                        'AccountingEvents',
                        'Accounts',
                        'ActivityCodes',
                        'AllowanceHolders',
                        'ApplicationTables',
                        'Appropriations',
                        'BudgetControls',
                        'BudgetObjectClasses',
                        'CapitalPlanningInvestmentCodes',
                        'ColumnSchema',
                        'CompassErrors',
                        'CongressionalControls',
                        'CostAreas',
                        'DataRuleDescriptions',
                        'Documents',
                        'EarmarkCodes',
                        'FederalHolidays',
                        'FinanceObjectClasses',
                        'FiscalYears',
                        'FundCategories',
                        'Funds',
                        'FundSymbols',
                        'Goals',
                        'GsPayScales',
                        'HeadquartersOffices',
                        'Images',
                        'Messages',
                        'MainAccounts',
                        'NationalPrograms',
                        'Objectives',
                        'Organizations',
                        'Partitions',
                        'PayPeriods',
                        'ProgramAreas',
                        'ProgramProjectDescriptions',
                        'ProgramProjects',
                        'Projects',
                        'Providers',
                        'PublicLaws',
                        'ReconciliationLines',
                        'ReferenceTables',
                        'RegionalOffices',
                        'ReportingLines',
                        'ResourcePlanningOffices',
                        'Resources',
                        'ResponsibilityCenters',
                        'SchemaTypes',
                        'StateOrganizations',
                        'SubAppropriations',
                        'TransTypes',
                        'TreasurySybmols',
                        'URL' ]

    def __str__( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'source', 'provider', 'table_name', 'get_driver_info',
                 'get_data_path', 'get_connection_string' ]

    def get_driver_info( self ) -> str:
        '''

        Purpose:
            Returns a string defining the driverinfo being used

        Parameters:  None

        Returns:  str

        '''
        try:
            if self.__provider.name == 'SQLite':
                return self.__sqlitepath
            elif self.__provider.name == 'Access':
                return self.__accessdriver
            elif self.__provider.name == 'SqlServer':
                return self.__sqldriver
            else:
                return self.__sqlitedriver
        except Exception as e:
            _exc = Error( e )
            _exc.cause = 'DbConfig Class'
            _exc.method = 'get_driver_info( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

    def get_data_path( self ) -> str:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

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
            _exc = Error( e )
            _exc.cause = 'DbConfig Class'
            _exc.method = 'get_data_path( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

    def get_connection_string( self ) -> str:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _path = self.get_data_path( )
            if self.__provider.name == Provider.Access.name:
                return self.get_driver_info( ) + _path
            elif self.__provider.name == Provider.SqlServer.name:
                return r'DRIVER={ ODBC Driver 17 for SQL Server };Server=.\SQLExpress;' \
                    + f'AttachDBFileName={ _path }' \
                    + f'DATABASE={ _path }Trusted_Connection=yes;'
            else:
                return f'{ _path } '
        except Exception as e:
            _exc = Error( e )
            _exc.cause = 'DbConfig Class'
            _exc.method = 'get_connection_string( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

class Connection( DbConfig ):
    '''

    Constructor:
    Connection( source: Source, provider: Provider = Provider.SQLite )

    Purpose:
    Class providing object used to connect to the databases

    '''
    __driver: str=None
    __datapath: str=None
    __connectionstring: str=None

    @property
    def driver_info( self ) -> str:
        if self.__driver is not None:
            return self.__driver

    @driver_info.setter
    def driver_info( self, value: str ):
        if value is not None:
            self.__driver = value

    @property
    def data_path( self ) -> str:
        if self.__datapath is not None:
            return self.__datapath

    @data_path.setter
    def data_path( self, value: str ):
        if value is not None:
            self.__datapath = value

    @property
    def connection_string( self ) -> str:
        if self.__connectionstring is not None \
                and self.__connectionstring != '':
            return self.__connectionstring

    @connection_string.setter
    def connection_string( self, value: str ):
        if value is not None:
            self.__connectionstring = value

    def __init__( self, source: Source, provider: Provider=Provider.SQLite ):
        super( ).__init__( source, provider )
        self.__source = super( ).source
        self.__provider = super( ).provider
        self.__datapath = super( ).get_data_path( )
        self.__driver = super( ).get_driver_info( )
        self.__dsn = super( ).table_name + ';'
        self.__connectionstring = super( ).get_connection_string( )

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [  'source', 'provider', 'table_name', 'get_driver_info',
                  'get_data_path', 'get_connection_string',
                  'driver_info', 'data_path', 
                  'connection_string', 'connect' ]

    def connect( self ):
        '''
        Purpose:
			Establishes a data connections using the connecdtion
			string.

        Parameters:
        	self

        Returns:
        	None
        '''

        try:
            if self.__provider.name == Provider.Access.name:
                return db.connect( self.__connectionstring )
            elif self.__provider.name == Provider.SqlServer.name:
                return db.connect( self.__connectionstring )
            else:
                return sqlite.connect( self.__connectionstring )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'Connection'
            _exc.method = 'connect( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SqlConfig( ):
    '''

     Constructor:

	     SqlConfig( commandtype: SQL=SQL.SELECTALL, columnnames: list = None,
	                columnvalues: tuple = None, paramstyle: ParamStyle = None )

     Purpose:

	     Class provides database interaction behavior

     '''
    __commandtype: str=None
    __columnnames: str=None
    __columnvalues: str=None
    __paramstyle: str=None
    __criteria: str=None

    @property
    def command_type( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

    @command_type.setter
    def command_type( self, value: SQL ):
        if value is not None:
            self.__commandtype = value

    @property
    def column_names( self ) -> list[ str ]:
        if self.__columnnames is not None:
            return self.__columnnames

    @column_names.setter
    def column_names( self, value: list[ str ] ):
        if value is not None:
            self.__columnnames = value

    @property
    def column_values( self ) -> tuple:
        if self.__columnvalues is not None:
            return self.__columnvalues

    @column_values.setter
    def column_values( self, value: tuple ):
        if value is not None:
            self.__columnvalues = value

    @property
    def parameter_style( self ) -> ParamStyle:
        if self.__paramstyle is not None:
            return self.__paramstyle

    @parameter_style.setter
    def parameter_style( self, value: ParamStyle ):
        if value is not None:
            self.__paramstyle = value
        else:
            self.__paramstyle = ParamStyle.qmark

    @property
    def criteria( self ) -> dict:
        if self.__criteria is not None:
            return self.__criteria

    @criteria.setter
    def criteria( self, value: dict ):
        if value is not None:
            self.__criteria = value

    def __init__( self, commandtype: SQL=SQL.SELECTALL, columnnames: list[ str ]=None,
                  columnvalues: tuple=( ), paramstyle: ParamStyle=None ):
        self.__commandtype = commandtype
        self.__columnnames = columnnames
        self.__columnvalues = columnvalues
        self.__paramstyle = paramstyle
        self.__criteria = dict( zip( columnnames, list( columnvalues ) ) ) \
            if columnnames is not None and columnvalues is not None else None

    def __dir__( self ) -> list[ str ]:
        '''

        Returns a list[ str ] of member names.

        '''
        return [ 'command_type', 'column_names', 'column_values',
                 'parameter_style', 'pair_dump', 'where_dump',
                 'set_dump', 'column_dump', 'value_dump' ]

    def pair_dump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__columnnames is not None and self.__columnvalues is not None:
                _pairs = ''
                _kvp = zip( self.__columnnames, self.__columnvalues )
                for k, v in _kvp:
                    _pairs += f'{k} = \'{v}\' AND '
                _criteria = _pairs.rstrip( ' AND ' )
                return _criteria
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'pair_dump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def where_dump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if isinstance( self.__columnnames, list ) and isinstance( self.__columnvalues, tuple ):
                pairs = ''
                for k, v in zip( self.__columnnames, self.__columnvalues ):
                    pairs += f'{k} = \'{v}\' AND '
                criteria = 'WHERE ' + pairs.rstrip( ' AND ' )
                return criteria
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'where_dump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def set_dump( self ) -> str:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            if self.__columnnames is not None and self.__columnvalues is not None:
                _pairs = ''
                _criteria = ''
                for k, v in zip( self.__columnnames, self.__columnvalues ):
                    _pairs += f'{k} = \'{v}\', '
                _criteria = 'SET ' + _pairs.rstrip( ', ' )
                return _criteria
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'set_dump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def column_dump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__columnnames is not None:
                _colnames = ''
                for n in self.__columnnames:
                    _colnames += f'{n}, '
                _columns = '(' + _colnames.rstrip( ', ' ) + ')'
                return _columns
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'column_dump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def value_dump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__columnvalues is not None:
                _vals = ''
                for v in self.__columnvalues:
                    _vals += f'{v}, '
                _values = 'VALUES (' + _vals.rstrip( ', ' ) + ')'
                return _values
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'value_dump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Command( ):
    '''

    Constructor:

    SqlStatement( dbcfg: DbConfig, sqlcfg: SqlConfig )

    Purpose:

    Class represents the values models used in the SQLite database

    '''
    __type: SQL=None
    __source: Source=None
    __provider: Provider=None
    __tablename: str=None
    __columnnames: str=None
    __columnvalues: str=None
    __criteria: dict=None
    __updates: str=None
    __querytext: str=None

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    @property
    def provider( self ) -> Provider:
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value: Provider ):
        if value is not None:
            self.__provider = value

    @property
    def table_name( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value: str ):
        if value is not None:
            self.__tablename = value

    @property

    def column_names( self ) -> str:
        if self.__columnnames is not None:
            return self.__columnnames

    @column_names.setter
    def column_names( self, value: str ):
        if value is not None:
            self.__columnnames = value

    @property
    def column_values( self ) -> str:
        if self.__columnvalues is not None:
            return self.__columnvalues

    @column_values.setter
    def column_values( self, value: str ):
        if value is not None:
            self.__columnvalues = value

    @property
    def updates( self ) -> str:
        if self.__updates is not None:
            return self.__updates

    @updates.setter
    def updates( self, value: str ):
        if value is not None:
            self.__updates = value

    @property
    def query_text( self ) -> str:
        if self.__querytext is not None:
            return self.__querytext

    @query_text.setter
    def query_text( self, value: str ):
        if value is not None:
            self.__querytext = value

    @property
    def type( self ) -> SQL:
        if self.__type is not None:
            return self.__type

    @type.setter
    def type( self, value: SQL ):
        if value is not None:
            self.__type = value
        else:
            command = SQL( 'SELECT' )
            self.__type = command

    def __init__( self, dbcfg: DbConfig, sqlcfg: SqlConfig ):
        self.__type = sqlcfg.command_type
        self.__provider = dbcfg.provider
        self.__source = dbcfg.source
        self.__tablename = dbcfg.table_name
        self.__columnnames = sqlcfg.column_dump( )
        self.__columnvalues = sqlcfg.value_dump( )
        self.__updates = sqlcfg.set_dump( ) 
        self.__criteria = dict( zip( sqlcfg.column_names, list( sqlcfg.column_values ) ) ) 
        self.__querytext = self.__getquerytext( )

    def __str__( self ) -> str:
        if self.__querytext is not None:
            return self.__querytext

    def __dir__(self) -> list[ str ]:
        '''

        Returns a list[ str ] of member names.

        '''
        return [ 'provider', 'table_name',
                 'command_type', 'column_names', 'values',
                 'updates', 'command_text'  ]

    def __getquerytext( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _table = self.__tablename
            _where = self.__criteria
            _cols = self.__columnnames
            _vals = self.__columnvalues
            if self.__columnnames is not None and _vals is not None:
                if self.__type == SQL.SELECTALL:
                    if len( _where.items( ) ) == 0:
                        return  f'SELECT * FROM {_table}'
                    if len( _where.items( ) ) > 0:
                        return  f'SELECT ' + _cols + f'FROM {_table}' + f' {_where}'
                elif self.__type == SQL.SELECT:
                    if len( _where.items( ) ) == 0:
                        return  f'SELECT * FROM {_table}'
                    if len( _where.items( ) ) > 0:
                        return  f'SELECT ' + _cols + f' FROM {_table}' + f' {_where}'
                elif self.__type == SQL.INSERT and self.__updates is not None:
                    return  f'INSERT INTO {_table} ' + f'{_cols} ' + f'{_vals}'
                elif self.__type == SQL.UPDATE:
                    _set = self.__updates
                    return f'UPDATE {_table} ' + f'{_set} ' + f'{_vals}' + f' {_where}'
                elif self.__type == SQL.DELETE:
                    return f'DELETE FROM {_table} ' + f'{_where}'
            else:
                if self.__columnnames is not None and _vals is None:
                    if self.__type == SQL.SELECT:
                        cols = _cols.lstrip( '(' ).rstrip( ')' )
                        return f'SELECT {cols} FROM {_table}'
                elif self.__columnnames is None and _vals is None:
                    if self.__type == SQL.SELECTALL:
                        return f'SELECT * FROM {_table}'
                elif self.__type == 'DELETE':
                    return f'DELETE FROM {_table}'
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlStatement'
            _exc.method = '__getquerytext( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Query( ):
    '''

    Constructor:

    Query( connection: Connection, sqlstatement: SqlStatement ).

    Purpose:

    Base class for database interaction

    '''
    __connection: Connection=None
    __sqlstatement: Command=None
    __sqlconfig: SqlConfig=None
    __commandtype: SQL=None
    __source: Source=None
    __tablename: str=None
    __provider: Provider=None
    __columnnames: list[ str ]=None
    __columnvalues: tuple=None
    __datapath: str=None
    __connectionstring: str=None
    __commandtext: str=None

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    @property
    def provider( self ) -> Provider:
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value: Provider ):
        if value is not None:
            self.__provider = value
        else:
            self.__provider = Provider.SQLite

    @property
    def data_path( self ) -> str:
        if self.__datapath is not None:
            return self.__datapath

    @data_path.setter
    def data_path( self, value: str ):
        if value is not None:
            self.__datapath = value

    @property
    def connection( self ) -> Connection:
        if self.__connection is not None:
            return self.__connection

    @connection.setter
    def connection( self, value: Connection ):
        if value is not None:
            self.__connection = value

    @property
    def sqlstatement( self ) -> Command:
        if self.__sqlstatement is not None:
            return self.__sqlstatement

    @sqlstatement.setter
    def sqlstatement( self, value: Command ):
        if isinstance( value, Command ):
            self.__sqlstatement = value

    @property
    def command_type( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

        if self.__commandtype is None:
            cmd = SQL( 'SELECT' )
            return cmd

    @command_type.setter
    def command_type( self, value: SQL ):
        if isinstance( value, SQL ):
            self.__commandtype = value

    @property
    def table_name( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value: str ):
        if value is not None:
            self.__tablename = value

    @property
    def column_names( self ) -> list[ str ]:
        if self.__columnnames is not None:
            return self.__columnnames

    @column_names.setter
    def column_names( self, value: list[ str ] ):
        if value is not None:
            self.__columnnames = value

    @property
    def column_values( self ) -> tuple:
        if self.__columnvalues is not None:
            return self.__columnvalues

    @column_values.setter
    def column_values( self, value: tuple ):
        if value is not None:
            self.__columnvalues = value

    @property
    def command_text( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @command_text.setter
    def command_text( self, value: str ):
        if value is not None:
            self.__commandtext = value

    @property
    def connection_string( self ) -> str:
        if self.__connectionstring is not None:
            return self.__connectionstring

    @connection_string.setter
    def connection_string( self, value: str ):
        if value is not None:
            self.__connectionstring = value

    def __init__( self, connection: Connection, sqlstatement: Command ):
        self.__connection = connection
        self.__sqlstatement = sqlstatement
        self.__sqlconfig = SqlConfig( connection.source, connection.provider )
        self.__source = connection.source
        self.__tablename = self.__source.name
        self.__provider = connection.provider
        self.__commandtype = sqlstatement.type
        self.__datapath = connection.path
        self.__connectionstring = connection.connection_string
        self.__columnnames = list( self.__sqlconfig.criteria.keys( ) )
        self.__columnvalues = tuple( self.__sqlconfig.criteria.values( ) )
        self.__commandtext = sqlstatement.query_text

    def __str__( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    def __dir__( self ) -> list[ str ]:
        return [ 'source', 'provider', 'data_path', 'connection', 'sqlstatement',
                 'command_type', 'table_name', 'column_names', 'values',
                 'command_text', 'connection_string' ]

class SQLiteData( Query ):
    '''

    Constructor:

    SQLiteData( connection: Connection, sqlstatement: SqlStatement )

    Purpose:

    Class represents the SQLite data factory

    '''
    __driverinfo: str=None

    @property
    def driver_info( self ) -> str:
        if self.__driverinfo is not None:
            return self.__driverinfo

    @driver_info.setter
    def driver_info( self, value: str ):
        if value is not None:
            self.__driverinfo = value

    def __init__( self, connection: Connection, sqlstatement: Command ):
        super( ).__init__( connection, sqlstatement )
        self.__provider = super( ).provider
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sqlstatement
        self.__source = super( ).source
        self.__tablename = super( ).source.name
        self.__commandtype = super( ).command_type
        self.__datapath = super( ).data_path
        self.__driverinfo = super( ).connection.driver_info
        self.__connectionstring = super().connection_string
        self.__columnnames = super( ).column_names
        self.__values = super( ).column_values
        self.__commandtext = super( ).command_text

    def __str__( self ) -> str:
        if self.__query is not None:
            return self.__query

    def __dir__( self ) -> list[ str ]:
        '''

        Returns a list[ str ] of member names

        '''
        return [ 'source', 'provider', 'datapath', 'connection', 'sqlstatement',
                 'commandtype', 'tablename', 'columnnames', 'values', 'driverinfo',
                 'commandtext', 'connectionstring', 'create_table', 'create_frame' ]

    def create_table( self ) -> list[ db.Row ]:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _query = self.__query
            _conn = self.__connection.connect( )
            _cursor = _conn.cursor( )
            _data = _cursor.execute( _query )
            self.__columns = [ i[ 0 ] for i in _cursor.description ]
            self.__data = [ i for i in _data.fetchall( ) ]
            _cursor.close( )
            _conn.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SQLiteData'
            _exc.method = 'create_table( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def create_frame( self ) -> DataFrame:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _query = f'SELECT * FROM {self.__source.name}'
            _connection = self.__connection.connect( )
            self.__frame = sqlreader( _query, _connection )
            _connection.close( )
            return self.__frame
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SQLiteData'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AccessData( Query ):
    '''

    Constructor:

    AccessData( connection: Connection, sqlstatement: SqlStatement )

    Purpose:

    Class represents the main execution
    values model classes in the MS ACCDB database

    '''
    __driverinfo: str=None
    __dsn: str=None
    __data: list[ str ]=None
    __columnnames = None
    __commandtext: str=None

    @property
    def command_text( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @command_text.setter
    def command_text( self, value: str ):
        if value is not None:
            self.__commandtext = value

    def __init__( self, connection: Connection, sqlstatement: Command ):
        super( ).__init__( connection, sqlstatement )
        self.__source = super( ).source
        self.__provider = Provider.Access
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sqlstatement
        self.__commandtext = sqlstatement.query_text
        self.__driverinfo = r'DRIVER={ Microsoft ACCDB Driver( *.mdb, *.accdb ) };'
        self.__data = [ ]

    def __str__( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    def __dir__( self ) -> list[ str ]:
        '''

        Returns a list[ str ] of member names

        '''
        return [ 'source', 'provider', 'path', 'connection', 'sqlstatement',
                 'command_type', 'table_name', 'column_names', 'values',
                 'command_text', 'connection_string',
                 'frame', 'create_table', 'create_frame' ]

    def create_table( self ) -> list[ db.Row ]:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _query = self.__cooandtext
            _access = self.__connection.connect( )
            _cursor = _access.cursor( )
            _data = _cursor.execute( _query )
            self.__columns = [ i[ 0 ] for i in _cursor.description ]
            self.__data = [ i for i in _data.fetchall( ) ]
            _cursor.close( )
            _access.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'AccessData'
            _exc.method = 'create_table( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def create_frame( self ) -> DataFrame:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _query = self.__cooandtext
            _conn = self.__connection.connect( )
            self.__frame = sqlreader( _query, _conn )
            _conn.close( )
            return self.__frame
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'AccessData'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SqlServerData( Query ):
    '''

     Constructor:

     SqlData( connection: Connection, sqlstatement: SqlStatement )

     Purpose:

     Class providing object represents the
     value models in the MS SQL Server database

     '''
    __serverpath: str=None
    __driverinfo: str=None
    __dsn: str=None
    __data: list[ db.Row ]=None

    @property
    def command_text( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @command_text.setter
    def command_text( self, value: str ):
        if value is not None:
            self.__commandtext = value

    def __init__( self, connection: Connection, sql: Command ):
        super( ).__init__( connection, sql )
        self.__provider = Provider.SqlServer
        self.__connection = super( ).connection
        self.__source = super( ).source
        self.__commandtext = super( ).command_text
        self.__tablename = super( ).table_name
        self.__serverpath = r'(LocalDB)\MSSQLLocalDB;'
        self.__driverinfo = r'{ SQL Server Native Client 11.0 };'

    def __str__( self ) -> str:
        if self.__source is not None:
            return self.__source.name

    def __dir__( self ) -> list[ str ]:
        '''

        Returns a list[ str ] of member names

        '''
        return [ 'source', 'provider', 'path', 'connection', 'sqlstatement',
                 'commandtype', 'tablename', 'columnnames', 'values',
                 'commandtext', 'connectionstring',
                 'frame', 'create_table', 'create_frame' ]

    def create_table( self ) -> list[ db.Row ]:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _query = self.__commandtext
            _connection = self.__connection.connect( )
            _cursor = _connection.cursor( )
            _data = _cursor.execute( _query )
            self.__columns = [ i[ 0 ] for i in _cursor.description ]
            self.__data = [ i for i in _data.fetchall( ) ]
            _cursor.close( )
            _connection.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlServerData'
            _exc.method = 'create_table( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def create_frame( self ) -> DataFrame:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _query = f'SELECT * FROM {self.__table}'
            _connection = self.__connection.connect( )
            self.__frame = sqlreader( _query, _connection )
            _connection.close( )
            return self.__frame
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlServerData'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class BudgetData( ):
    '''

    Constructor:

    BudgetData( source: Source )

    Purpose:

    Class containing factory method for providing
    pandas dataframes.

    '''
    __source: Source=None
    __tablename: str=None
    __path: str=None
    __connection: Connection=None
    __commandtext: str=None

    @property
    def source( self ) -> Source:
        ''' Gets a member of the Source enumeration'''
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        '''Sets a member of the Source enumeration'''
        if value is not None:
            self.__source = value

    @property
    def table_name( self ) -> str:
        '''Get the name of the data source'''
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value: str ):
        '''Sets the name of the data source'''
        if value is not None:
            self.__tablename = value

    @property
    def data_path( self ) -> str:
        '''
        Gets a string  to the data source
        '''
        if self.__path is not None:
            return self.__path

    @data_path.setter
    def data_path( self, value: str ):
        '''
        Sets a string to the data source
        '''
        if value is not None:
            self.__path = value

    @property
    def command_text( self ) -> str:
        '''
        Gets a string representing the SQL command text
        '''
        if self.__commandtext is not None:
            return self.__commandtext

    @command_text.setter
    def command_text( self, value: str ):
        '''
        Sets a string representing the SQL command text
        '''
        if value is not None:
            self.__commandtext = value

    def __init__( self, source: Source ):
        self.__source = source
        self.__tablename = source.name
        self.__path = DbConfig( source ).get_data_path( )
        self.__commandtext = f'SELECT * FROM {source.name};'

    def __dir__( self ) -> list[ str ]:
        '''
        Returns a list[ str ] of member names
        '''
        return [ 'source', 'data_path', 'table_name',
                 'command_text', 'create_frame', 'create_tuples']

    def create_frame( self ) -> DataFrame:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _path = self.__path
            _source = self.__source
            _table = self.__source.name
            _connection = sqlite.connect( _path )
            _sql = f'SELECT * FROM {_table};'
            _frame = sqlreader( _sql, _connection )
            return _frame
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'BudgetData'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def create_tuples( self ) -> list[ tuple ]:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _path = self.__path
            _source = self.__source
            _table = self.__source.name
            _connection = sqlite.connect( _path )
            _sql = f'SELECT * FROM {_table};'
            _frame = sqlreader( _sql, _connection )
            _data = [ tuple( i ) for i in _frame.iterrows( ) ]
            return _data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'BudgetData'
            _exc.method = 'create_tuples( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class DataBuilder( ):
    '''
    Constructor:

    DataBuilder( source: Source, provider = Provider.SQLite,
                  commandtype = SQL.SELECTALL, names: list[ str ]=None,
                  values: tuple = None ).

    Purpose:

    Class provides functionality to access application data.

    '''
    __names: list[ str ]=None
    __values: tuple=None
    __commandtype: SQL=None
    __source: Source=None
    __provider: Provider=None
    __dbconfig: DbConfig=None
    __sqlconfig: SqlConfig=None
    __connection: Connection=None
    __sqlstatement: Command=None
    __commandtext: str=None
    __data: list[ db.Row ]=None

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    @property
    def provider( self ) -> Provider:
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, value: Provider ):
        if value is not None:
            self.__provider = value
        else:
            self.__provider = Provider.SQLite

    @property
    def command( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

    @command.setter
    def command( self, value: SQL ):
        if value is not None:
            self.__commandtype = value

    @property
    def names( self ) -> list[ str ]:
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, value: list[ str ] ):
        if value is not None:
            self.__names = value

    @property
    def values( self ) -> tuple:
        if self.__values is not None:
            return self.__values

    @values.setter
    def values( self, value: tuple ):
        if value is not None:
            self.__values = value

    @property
    def dbconfig( self ) -> DbConfig:
        if self.__dbconfig is not None:
            return self.__dbconfig

    @dbconfig.setter
    def dbconfig( self, value: DbConfig ):
        if value is not None:
            self.__dbconfig = value

    @property
    def sqlconfig( self ) -> SqlConfig:
        if self.__sqlconfig is not None:
            return self.__sqlconfig

    @sqlconfig.setter
    def sqlconfig( self, value: SqlConfig ):
        if value is not None:
            self.__sqlconfig = value

    def __init__( self, source: Source, provider: Provider=Provider.SQLite,
                  commandtype: SQL=SQL.SELECTALL, names: list[ str ]=None,
                  values: tuple=None ):
        self.__source = source
        self.__provider = provider
        self.__commandtype = commandtype
        self.__name = names
        self.__values = values
        self.__dbconfig = DbConfig( source, provider )
        self.__connection = Connection( source )
        self.__sqlconfig = SqlConfig( commandtype, names, values )
        self.__sqlstatement = Command( self.__dbconfig, self.__sqlconfig )

    def create_table( self ) -> list[ db.Row ]:
        try:
            if self.__provider == Provider.SQLite:
                _sqlite = SQLiteData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _sqlite.create_table( ) ]
                return self.__data
            elif self.__provider == Provider.Access:
                _access = AccessData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _access.create_table( ) ]
                return self.__data
            elif self.__provider == Provider.SqlServer:
                _sql = SqlServerData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _sql.create_table( ) ]
                return self.__data
            else:
                _sqlite = SQLiteData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _sqlite.create_table( ) ]
                return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'DataBuilder'
            _exc.method = 'create_table( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

class DataColumn( ):
    '''

    Constructor:

    DataColumn( name: str = '', dtype: type = None, value: object = None )

    Purpose:

    Defines the class providing schema information.

     '''
    __series = None
    __row = None
    __name: str=None
    __value: object=None
    __label: str=None
    __id: int=None
    __type: str=None
    __caption: str=None
    __table: list[ db.Row ]=None
    __frame: DataFrame=None

    @property
    def id( self ) -> int:
        if self.__id is not None:
            return self.__id

    @id.setter
    def id( self, value: int ):
        if value > -1:
            self.__id = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def value( self ) -> object:
        if self.__type is not None:
            return self.__value

    @value.setter
    def value( self, value: object ):
        if value is not None:
            self.__value = value

    @property
    def type( self ) -> type:
        if self.__type is not None:
            return self.__type

    @type.setter
    def type( self, value: type ):
        if value is not None:
            self.__type = value

    @property
    def caption( self ) -> str:
        if isinstance( self.__caption, str ):
            return self.__caption

    @caption.setter
    def caption( self, value: str ):
        if value is not None:
            self.__caption = value

    @property
    def table( self ) -> str:
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__table = value

    @property
    def row( self ) -> object:
        if self.__row is not None:
            return self.__row

    @row.setter
    def row( self, value: object ):
        if value is not None:
            self.__series = value
            self.__row = self.__series

    @property
    def frame( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @frame.setter
    def frame( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    def __init__( self, name: str = '', dtype: type = None, value: object = None ):
        self.__name = name
        self.__label = name
        self.__caption = name
        self.__type = dtype
        self.__value = value

    def __str__( self ) -> str:
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    def is_numeric( self ) -> bool:
        try:
            if self.__value is not None:
                return True
            else:
                return False
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'DataColumn'
            _exc.method = 'is_numeric( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def is_text( self ) -> bool:
        try:
            if self.__value is not None:
                return True
            else:
                return False
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'DataColumn'
            _exc.method = 'is_text( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class DataRow( ):
    '''

    Constructor:

    DataRow( names: list[ str ]=None, values: tuple = ( ), source: Source = None)

    Purpose:

    Defines the class representing rows of data

    '''
    __source: Source=None
    __names = None
    __items = None
    __data = None
    __values = None
    __key = None
    __index = None

    @property
    def id( self ) -> int:
        if self.__index is not None:
            return self.__index

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__index = value

    @property
    def key( self ) -> str:
        if self.__key is not None:
            return self.__key

    @key.setter
    def key( self, value: str ):
        if value is not None:
            self.__key = value

    @property
    def data( self ) -> list[ tuple ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ tuple ] ):
        if value is not None:
            self.__data = value

    @property
    def items( self ) -> zip:
        if self.__items is not None:
            return self.__items

    @items.setter
    def items( self, value: zip ):
        if value is not None:
            self.__items = value

    @property
    def names( self ) -> list[ str ]:
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, value: list[ str ] ):
        if value is not None:
            self.__names = value

    @property
    def values( self ) -> tuple:
        if self.__values is not None:
            return self.__values

    @values.setter
    def values( self, value: tuple ):
        if value is not None:
            self.__values = value

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    def __init__( self, names: list[ str ]=None, values: tuple = ( ),
                  source: Source = None ):
        self.__source = source
        self.__names = names
        self.__values = values
        self.__items = zip( names, list( values ) )
        self.__key = str( self.__names[ 0 ] )
        self.__index = int( self.__values[ 0 ] )

    def __str__( self ) -> str:
        if self.__index is not None:
            return 'Row ID: ' + str( self.__index )

class DataTable( ):
    '''
    Constructor:

    DataTable( columns: list[ str ]=None, rows: list = None,
        source: Source = None, dataframe: DataFrame = None  )

    Purpose:

    Defines the class representing table of data

    '''
    __name = None
    __data = None
    __frame = None
    __rows = None
    __columns = None
    __schema = None
    __source: Source=None

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = str( value )

    @property
    def data( self ) -> list:
        if self.__rows is not None:
            return self.__rows

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__rows = value

    @property
    def frame( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @frame.setter
    def frame( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def schema( self ) -> list[ str ]:
        if self.__columns is not None:
            return self.__columns

    @schema.setter
    def schema( self, value: list[ str ] ):
        if value is not None:
            self.__columns = value

    @property
    def rows( self ) -> list:
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if value is not None:
            self.__rows = value

    @property
    def columns( self ) -> list[ str ]:
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, value: list[ str ] ):
        if value is not None:
            self.__columns = value

    @property
    def source( self ) -> Source:
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if value is not None:
            self.__source = value

    def __init__( self, columns: list[ str ]=None, rows: list = None,
                  source: Source = None, dataframe: DataFrame = None ):
        self.__frame = dataframe
        self.__name = source.name
        self.__rows = [ tuple( r ) for r in dataframe.iterrows( ) ]
        self.__data = self.__rows
        self.__columns = [ str( c ) for c in columns ]
        self.__schema = [ DataColumn( c ) for c in columns ]

    def __str__( self ) -> str:
        if self.__name is not None:
            return self.__name
