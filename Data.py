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
     Copyright ©  2023  Terry Eppler

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
    __input = None
    __output = None

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

    def __init__( self, buffer: str = None ):
        self.__input = buffer

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
    folders containing sqlstatement files and driverinfo paths used in the application
    '''
    __accessdriver = None
    __accesspath = None
    __sqlitedriver = None
    __sqlitepath = None
    __sqldriver = None
    __sqldatabase = None

    @property
    def sqlitedriver( self ) -> str:
        if self.__sqlitedriver is not None:
            return self.__sqlitedriver

    @sqlitedriver.setter
    def sqlitedriver( self, value: str ):
        if value is not None:
            self.__sqlitedriver = value

    @property
    def sqlitedatabase( self ) -> str:
        if self.__sqlitepath is not None:
            return self.__sqlitepath

    @sqlitedatabase.setter
    def sqlitedatabase( self, value: str ):
        if value is not None:
            self.__sqlitepath = value

    @property
    def accessdriver( self ) -> str:
        if self.__accessdriver is not None:
            return self.__accessdriver

    @accessdriver.setter
    def accessdriver( self, value: str ):
        if value is not None:
            self.__accessdriver = value

    @property
    def accessdatabase( self ) -> str:
        if self.__accesspath is not None:
            return self.__accesspath

    @accessdatabase.setter
    def accessdatabase( self, value: str ):
        if value is not None:
            self.__accesspath = value

    @property
    def sqldriver( self ) -> str:
        if self.__sqldriver is not None:
            return self.__sqldriver

    @sqldriver.setter
    def sqldriver( self, value: str ):
        if value is not None:
            self.__sqldriver = value

    @property
    def sqldatabase( self ) -> str:
        if self.__sqldatabase is not None:
            return self.__sqldatabase

    @sqldatabase.setter
    def sqldatabase( self, value: str ):
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
        return [ 'sqlitedriver', 'sqlitedatabase',
                 'accessdriver', 'accessdatabase' ]

class SqlFile( ):
    '''
    Constructor:
    SqlFile( src: Source = None, pvdr: Provider  = Provider.SQLite,
            command_type: SQL = SQL.SELECTALL )

    Purpuse:
    Class providing access to sqlstatement sub-folders in the application provided
    optional arguments src, pvdr, and command_type
    '''
    __data = None
    __command = None
    __source = None
    __provider = None

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
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, value: SQL ):
        if value is not None:
            self.__command = value

    def __init__( self, source: Source = None, provider: Provider = Provider.SQLite,
                  command: SQL = SQL.SELECTALL ):
        self.__data = [ 'AccountingEvents',
                        'Accounts',
                        'ActivityCodes',
                        'Actuals',
                        'AdministrativeRequests',
                        'Allocations',
                        'AllowanceHolders',
                        'AmericanRescuePlanCarryoverEstimates',
                        'AnnualCarryoverEstimates',
                        'AnnualReimbursableEstimates',
                        'ApplicationTables',
                        'ApportionmentData',
                        'AppropriationAvailableBalances',
                        'AppropriationDocuments',
                        'AppropriationLevelAuthority',
                        'Appropriations',
                        'BudgetaryResourceExecution',
                        'BudgetControls',
                        'BudgetDocuments',
                        'BudgetObjectClasses',
                        'CapitalPlanningInvestmentCodes',
                        'CarryoverApportionments',
                        'CarryoverRequests',
                        'Changes',
                        'ColumnSchema',
                        'CompassLevels',
                        'CongressionalControls',
                        'Contacts',
                        'CostAreas',
                        'CongressionalProjects',
                        'DataRuleDescriptions',
                        'Defactos',
                        'Deobligations',
                        'DocumentControlNumbers',
                        'Documents',
                        'Earmarks',
                        'Expenditures',
                        'FederalHolidays',
                        'FinanceObjectClasses',
                        'FiscalYears',
                        'FundCategories',
                        'Funds',
                        'FundSymbols',
                        'GeneralLedgerAccounts',
                        'Goals',
                        'GsPayScales',
                        'HeadquartersAuthority',
                        'HeadquartersOffices',
                        'Images',
                        'InflationReductionActCarryoverEstimates',
                        'JobsActCarryoverEstimates',
                        'MainAccounts',
                        'Messages',
                        'MonthlyActuals',
                        'MonthlyLedgerAccountBalances',
                        'MonthlyOutlays',
                        'NationalPrograms',
                        'Objectives',
                        'ObligationActivity',
                        'Obligations',
                        'OpenCommitments',
                        'OperatingPlans',
                        'Organizations',
                        'Outlays',
                        'Partitions',
                        'PayPeriods',
                        'PayrollAuthority',
                        'PayrollCostCodes',
                        'PayrollRequests',
                        'PRC',
                        'ProgramAreas',
                        'ProgramProjectDescriptions',
                        'ProgramProjects',
                        'Projects',
                        'Providers',
                        'PublicLaws',
                        'QueryDefinitions',
                        'ReconcilliationLines',
                        'RecoveryAct',
                        'ReferenceTables',
                        'RegionalAuthority',
                        'RegionalOffices',
                        'ReimbursableAgreements',
                        'ReimbursableFunds',
                        'Reports',
                        'ReportingLines',
                        'ResourcePlanningOffices',
                        'Resources',
                        'ResponsibilityCenters',
                        'SchemaTypes',
                        'SpendingDocuments',
                        'SpendingRates',
                        'StateGrantObligations',
                        'StateOrganizations',
                        'StatusOfAmericanRescuePlanFunds',
                        'StatusOfAppropriations',
                        'StatusOfBudgetaryResources',
                        'StatusOfEarmarks',
                        'StatusOfFunds',
                        'StatusOfInflationReductionActFunds',
                        'StatusOfJobsActFunds',
                        'StatusOfSupplementalFunds',
                        'SubAppropriations',
                        'StatusOfSuperfundSites',
                        'StatusOfSpecialAccountFunds',
                        'SupplementalCarryoverEstimates',
                        'SupplementalOutlayEstimates',
                        'TransferActivity',
                        'Transfers',
                        'TransTypes',
                        'TreasurySymbols',
                        'UnliquidatedObligations',
                        'UnobligatedBalances',
                        'URL' ]
        self.__command = command
        self.__source = source
        self.__provider = provider

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'source', 'provider', 'command', 'getfilepath',
                 'getfolderpath', 'getcommandtext' ]

    def getfilepath( self ) -> str:
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
            _command = self.__command.name
            _current = os.getcwd( )
            _path = ''
            if _provider == 'SQLite' and _tablename in _data:
                _path = f'{_sqlpath.sqlitedatabase}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _path )
            elif _provider == 'ACCDB' and _tablename in _data:
                _path = f'{_sqlpath.accessdatabase}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _path )
            elif _provider == 'SqlServer' and _tablename in _data:
                _path = f'{_sqlpath.sqldatabase}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _path )
            else:
                _path = f'{_sqlpath.sqlitedatabase}\\{_command}\\{_tablename}.sql'
                return os.path.join( _current, _path )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlFile'
            _exc.method = 'getfilepath( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def getfolderpath( self ) -> str:
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
            _command = self.__command.name
            _current = os.getcwd( )
            _folder = ''
            if _provider == 'SQLite' and _source in _data:
                _folder = f'{_sqlpath.sqlitedatabase}\\{_command}'
                return os.path.join( _current, _folder )
            elif _provider == 'ACCDB' and _source in _data:
                _folder = f'{_sqlpath.accessdatabase}\\{_command}'
                return os.path.join( _current, _folder )
            elif _provider == 'SqlServer' and _source in _data:
                _folder = f'{_sqlpath.sqldatabase}\\{_command}'
                return os.path.join( _current, _folder )
            else:
                _folder = f'{_sqlpath.sqlitedatabase}\\{_command}'
                return os.path.join( _current, _folder )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlFile'
            _exc.method = 'directory( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def getcommandtext( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _source = self.__source.name
            _paths = self.get_datapath( )
            _folder = self.getfolderpath( )
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
            _exc.method = '_query( self, other )'
            _err = ErrorDialog( _exc )
            _err.show( )

class DbConfig( ):
    '''
    Constructor:
    DbConfig( source: Source, pvdr: Provider = Provider.SQLite )

    Purpose:
    Class provides list of Budget Execution tables across two databases
    '''
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
    def tablename( self ) -> str:
        '''Gets the'''
        if self.__table is not None:
            return self.__table

    @tablename.setter
    def tablename( self, value: str ):
        if value is not None:
            self.__table = value

    def __init__( self, source: Source, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = source
        self.__table = source.name
        self.__sqlitepath = os.getcwd( ) + r'\db\sqlite\datamodels\Data.db'
        self.__accessdriver = r'DRIVER={ Microsoft Access Driver (*.mdb, *.accdb) };DBQ='
        self.__accesspath = os.getcwd( ) + r'\db\access\datamodels\sql\Data.accdb'
        self.__sqldriver = r'DRIVER={ ODBC Driver 17 for SQL Server };SERVER=.\SQLExpress;'
        self.__sqlpath = os.getcwd( ) + r'\db\mssql\datamodels\Data.mdf'
        self.__data = [ 'Actuals',
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
        if isinstance( self.__table, str ):
            return self.__table

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'source', 'provider', 'tablename',
                 'getdriverinfo', 'getdatapath', 'getconnectionstring' ]

    def getdriverinfo( self ) -> str:
        '''
        Purpose: Returns a string defining the driverinfo being used

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
            _exc.method = 'getdriverinfo( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

    def getdatapath( self ) -> str:
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
            _exc.method = 'getdatapath( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

    def getconnectionstring( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _path = self.getdatapath( )
            if self.__provider.name == Provider.Access.name:
                return self.getdriverinfo( ) + _path
            elif self.__provider.name == Provider.SqlServer.name:
                return r'DRIVER={ ODBC Driver 17 for SQL Server };Server=.\SQLExpress;' \
                    + f'AttachDBFileName={ _path }' \
                    + f'DATABASE={ _path }Trusted_Connection=yes;'
            else:
                return f'{ _path } '
        except Exception as e:
            _exc = Error( e )
            _exc.cause = 'DbConfig Class'
            _exc.method = 'getconnectionstring( self )'
            _error = ErrorDialog( _exc )
            _error.show( )

class Connection( DbConfig ):
    '''

    Constructor:
    Connection( source: Source, provider: Provider = Provider.SQLite )

    Purpose:
    Class providing object used to connect to the databases

    '''
    __driver = None
    __datapath = None
    __connectionstring = None

    @property
    def driverinfo( self ) -> str:
        if self.__driver is not None:
            return self.__driver

    @driverinfo.setter
    def driverinfo( self, value: str ):
        if value is not None:
            self.__driver = value

    @property
    def datapath( self ) -> str:
        if self.__datapath is not None:
            return self.__datapath

    @datapath.setter
    def datapath( self, value: str ):
        if value is not None:
            self.__datapath = value

    @property
    def connectionstring( self ) -> str:
        if self.__connectionstring is not None \
                and self.__connectionstring != '':
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, value: str ):
        if value is not None:
            self.__connectionstring = value

    def __init__( self, src: Source, provider: Provider = Provider.SQLite ):
        super( ).__init__( src, provider )
        self.__source = super( ).source
        self.__provider = super( ).provider
        self.__datapath = super( ).getdatapath( )
        self.__driver = super( ).getdriverinfo( )
        self.__dsn = super( ).tablename + ';'
        self.__connectionstring = super( ).getconnectionstring( )

    def __dir__( self ) -> list[ str ]:
        '''
        Retunes a list[ str ] of member names.
        '''
        return [ 'driverinfo', 'datapath', 'connectionstring', 'connect' ]

    def connect( self ):
        '''
        Purpose:

        Parameters:

        Returns:
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

     SqlConfig( command: SQL = SQL.SELECTALL, names: list = None,
                values: tuple = None, style: ParamStyle = None )

     Purpose:

     Class provides database interaction behavior

     '''
    __commandtype = None
    __names = None
    __values = None
    __paramstyle = None
    __criteria = None

    @property
    def commandtype( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

    @commandtype.setter
    def commandtype( self, value: SQL ):
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
    def paramstyle( self ) -> ParamStyle:
        if self.__paramstyle is not None:
            return self.__paramstyle

    @paramstyle.setter
    def paramstyle( self, value: ParamStyle ):
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

    def __init__( self, command: SQL = SQL.SELECTALL, names: list = None,
                  values: tuple = ( ), style: ParamStyle = None ):
        self.__commandtype = command
        self.__names = names
        self.__values = values
        self.__paramstyle = style
        self.__criteria = dict( zip( names, list( values ) ) ) \
            if isinstance( names, list ) and isinstance( values, tuple ) else None

    def __dir__(self) -> list[ str ]:
        '''

        Returns a list[ str ] of member names.

        '''
        return [ 'commandtype', 'names', 'values',
                 'paramstyle', 'pairdump', 'wheredump',
                 'setdump', 'columndump', 'valuedump' ]

    def pairdump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__names is not None and self.__values is not None:
                _pairs = ''
                _kvp = zip( self.__names, self.__values )
                for k, v in _kvp:
                    _pairs += f'{k} = \'{v}\' AND '
                _criteria = _pairs.rstrip( ' AND ' )
                return _criteria
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'pairdump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def wheredump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if isinstance( self.__names, list ) and isinstance( self.__values, tuple ):
                pairs = ''
                for k, v in zip( self.__names, self.__values ):
                    pairs += f'{k} = \'{v}\' AND '
                criteria = 'WHERE ' + pairs.rstrip( ' AND ' )
                return criteria
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'wheredump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def setdump( self ) -> str:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            if self.__names is not None and self.__values is not None:
                _pairs = ''
                _criteria = ''
                for k, v in zip( self.__names, self.__values ):
                    _pairs += f'{k} = \'{v}\', '
                _criteria = 'SET ' + _pairs.rstrip( ', ' )
                return _criteria
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'setdump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def columndump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__names is not None:
                _colnames = ''
                for n in self.__names:
                    _colnames += f'{n}, '
                _columns = '(' + _colnames.rstrip( ', ' ) + ')'
                return _columns
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'columndump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def valuedump( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__values is not None:
                _vals = ''
                for v in self.__values:
                    _vals += f'{v}, '
                _values = 'VALUES (' + _vals.rstrip( ', ' ) + ')'
                return _values
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlConfig'
            _exc.method = 'valuedump( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SqlStatement( ):
    '''

    Constructor:

    SqlStatement( dbcfg: DbConfig, sqlcfg: SqlConfig )

    Purpose:

    Class represents the values models used in the SQLite database

    '''
    __commandtype = None
    __sqlconfig = None
    __dbconfig = None
    __source = None
    __provider = None
    __tablename = None
    __names = None
    __values = None
    __commandtext = None

    @property
    def source( self ) -> Source:
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value: Source ):
        if isinstance( value, Source ):
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
    def tablename( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    @tablename.setter
    def tablename( self, value: str ):
        if value is not None:
            self.__tablename = value

    @property
    def names( self ) -> str:
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, value: str ):
        if value is not None:
            self.__names = value

    @property
    def values( self ) -> str:
        if self.__values is not None:
            return self.__values

    @values.setter
    def values( self, value: str ):
        if value is not None:
            self.__values = value

    @property
    def commandtext( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value: str ):
        if value is not None:
            self.__commandtext = value

    @property
    def commandtype( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

    @commandtype.setter
    def commandtype( self, value: SQL ):
        if value is not None:
            self.__commandtype = value
        else:
            command = SQL( 'SELECT' )
            self.__commandtype = command

    def __init__( self, dbcfg: DbConfig, sqlcfg: SqlConfig ):
        self.__commandtype = sqlcfg.commandtype
        self.__provider = dbcfg.provider
        self.__source = dbcfg.source
        self.__tablename = dbcfg.tablename
        self.__names = sqlcfg.columndump( )
        self.__values = sqlcfg.valuedump( )
        self.__commandtext = self.__getquerytext( )

    def __str__( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    def __dir__(self) -> list[ str ]:
        '''

        Returns a list[ str ] of member names.

        '''
        return [ 'source', 'provider', 'tablename',
                'commandtype', 'names', 'values',
                'commandtext'  ]

    def __getquerytext( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            if self.__commandtype == SQL.SELECTALL:
                if self.__names is None:
                    self.__commandtext = f'SELECT * FROM {self.__tablename}'
                    return self.__commandtext
                if len( self.__names ) > 0:
                    self.__commandtext = f'SELECT ' + self.__names + f'FROM {self.__tablename}' \
                                         + f' {self.__sqlconfig.wheredump( )}'
                    return self.__commandtext
            elif self.__commandtype == SQL.SELECT:
                if len( self.__names ) == 0:
                    self.__commandtext = f'SELECT * FROM {self.__tablename}'
                    return self.__commandtext
                if len( self.__names ) > 0:
                    self.__commandtext = f'SELECT ' + self.__names + f' FROM {self.__tablename}' \
                                         + f' {self.__sqlconfig.wheredump( )}'
                    return self.__commandtext
            elif self.__commandtype == SQL.INSERT:
                self.__commandtext = f'INSERT INTO {self.__tablename} ' + f'{self.__names} ' \
                                     + f'{self.__values}'
                return self.__commandtext
            elif self.__commandtype == SQL.UPDATE:
                self.__commandtext = f'UPDATE {self.__tablename} ' + f'{self.__sqlconfig.setdump( )} ' \
                                     + f'{self.__tablename}'
                return self.__commandtext
            elif self.__commandtype == SQL.DELETE:
                self.__commandtext = f'DELETE FROM {self.__tablename} ' \
                                     + f' {self.__sqlconfig.setdump( )}'
                return self.__commandtext
            elif self.__names is not None and self.__values is not None:
                if self.__commandtype == SQL.SELECT:
                    cols = self.__names.lstrip( '(' ).rstrip( ')' )
                    self.__commandtext = f'SELECT {cols} FROM {self.__tablename}'
                    return self.__commandtext
            elif self.__commandtype == 'DELETE':
                self.__commandtext = f'DELETE FROM {self.__tablename}'
                return self.__commandtext
            else:
                if self.__names is None and self.__values is None:
                    if self.__commandtype == SQL.SELECTALL:
                        self.__commandtext = f'SELECT * FROM {self.__tablename}'
                        return self.__commandtext
                elif self.__commandtype == 'DELETE':
                    self.__commandtext = f'DELETE FROM {self.__tablename}'
                    return self.__commandtext
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlStatement'
            _exc.method = 'getcommandtext( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Query( ):
    '''

    Constructor:

    Query( connection: Connection, sqlstatement: SqlStatement ).

    Purpose:

    Base class for database interaction

    '''
    __connection = None
    __sqlstatement = None
    __sqlconfig = None
    __commandtype = None
    __source = None
    __tablename = None
    __provider = None
    __columnnames = None
    __values = None
    __path = None
    __connectionstring = None
    __commandtext = None

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
    def path( self ) -> str:
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, value: str ):
        if value is not None:
            self.__path = value

    @property
    def connection( self ) -> Connection:
        if self.__connection is not None:
            return self.__connection

    @connection.setter
    def connection( self, value: Connection ):
        if value is not None:
            self.__connection = value

    @property
    def sqlstatement( self ) -> SqlStatement:
        if self.__sqlstatement is not None:
            return self.__sqlstatement

    @sqlstatement.setter
    def sqlstatement( self, value: SqlStatement ):
        if isinstance( value, SqlStatement ):
            self.__sqlstatement = value

    @property
    def commandtype( self ) -> SQL:
        if self.__commandtype is not None:
            return self.__commandtype

        if self.__commandtype is None:
            cmd = SQL( 'SELECT' )
            return cmd

    @commandtype.setter
    def commandtype( self, value: SQL ):
        if isinstance( value, SQL ):
            self.__commandtype = value

    @property
    def tablename( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    @tablename.setter
    def tablename( self, value: str ):
        if value is not None:
            self.__tablename = value

    @property
    def columnnames( self ) -> list[ str ]:
        if self.__columnnames is not None:
            return self.__columnnames

    @columnnames.setter
    def columnnames( self, value: list[ str ] ):
        if value is not None:
            self.__columnnames = value

    @property
    def values( self ) -> tuple:
        if self.__values is not None:
            return self.__values

    @values.setter
    def values( self, value: tuple ):
        if value is not None:
            self.__values = value

    @property
    def commandtext( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value: str ):
        if value is not None:
            self.__commandtext = value

    @property
    def connectionstring( self ) -> str:
        if self.__connectionstring is not None:
            return self.__connectionstring

    @connectionstring.setter
    def connectionstring( self, value: str ):
        if value is not None:
            self.__connectionstring = value

    def __init__( self, connection: Connection, sqlstatement: SqlStatement ):
        self.__connection = connection
        self.__sqlstatement = sqlstatement
        self.__sqlconfig = SqlConfig( )
        self.__source = connection.source
        self.__provider = connection.provider
        self.__commandtype = sqlstatement.commandtype
        self.__path = connection.path
        self.__connectionstring = connection.connectionstring
        self.__columnnames = self.__sqlconfig.names
        self.__values = self.__sqlconfig.values
        self.__commandtext = self.__getquerytext( )

    def __str__( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    def __dir__( self ) -> list[ str ]:
        return [ 'source', 'provider', 'path', 'connection', 'sqlstatement',
                 'commandtype', 'tablename', 'columnnames', 'values',
                 'commandtext', 'connectionstring' ]

    @property
    def __getquerytext( self ) -> str:
        '''
        Purpose:

        Parameters:

        Returns:
        '''

        try:
            _table = self.__tablename
            _crit = self.__sqlconfig.wheredump( )
            _cols = self.__sqlconfig.columndump( )
            _vals = self.__sqlconfig.valuedump( )
            if isinstance( self.__columnnames, list ) and isinstance( _vals, tuple ):
                if self.__commandtype == SQL.SELECTALL:
                    if len( self.__columnnames ) == 0:
                        return  f'SELECT * FROM {_table}'
                    if len( self.__columnnames ) > 0:
                        return  f'SELECT ' + _cols + f'FROM {_table}' + f' {_crit}'
                elif self.__commandtype == SQL.SELECT:
                    if len( self.__columnnames ) == 0:
                        return  f'SELECT * FROM {_table}'
                    if len( self.__columnnames ) > 0:
                        return  f'SELECT ' + _cols + f' FROM {_table}' + f' {_crit}'
                elif self.__commandtype == SQL.INSERT:
                    return  f'INSERT INTO {_table} ' + f'{_cols} ' + f'{_vals}'
                elif self.__commandtype == SQL.UPDATE:
                    return f'UPDATE {_table} ' + f'{self.__sqlconfig.setdump( )} ' + f'{_vals}'
                elif self.__commandtype == SQL.DELETE:
                    return f'DELETE FROM {_table} ' + f'{_crit}'
            else:
                if isinstance( self.__columnnames, list ) and not isinstance( _vals, tuple ):
                    if self.__commandtype == SQL.SELECT:
                        cols = _cols.lstrip( '(' ).rstrip( ')' )
                        return f'SELECT {cols} FROM {_table}'
                elif not isinstance( self.__columnnames, list ) \
                        and not isinstance( _vals, tuple ):
                    if self.__commandtype == SQL.SELECTALL:
                        return f'SELECT * FROM {_table}'
                elif self.__commandtype == 'DELETE':
                    return f'DELETE FROM {_table}'
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'SqlStatement'
            _exc.method = '__getquerytext( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SQLiteData( Query ):
    '''

    Constructor:

    SQLiteData( connection: Connection, sqlstatement: SqlStatement )

    Purpose:

    Class represents the SQLite data factory

    '''
    __driver = None
    __dsn = None
    __query = None
    __data = None
    __frame = None

    @property
    def commandtext( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value: str ):
        if value is not None:
            self.__commandtext = value

    def __init__( self, connection: Connection, sqlstatement: SqlStatement ):
        super( ).__init__( connection, sqlstatement )
        self.__provider = Provider.SQLite
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sqlstatement
        self.__source = super( ).source
        self.__tablename = super( ).source.name
        self.__driver = super( ).connection.driverinfo
        self.__query = super( ).sqlstatement.__getquerytext( )

    def __str__( self ) -> str:
        if self.__query is not None:
            return self.__query

    def __dir__( self ) -> list[ str ]:
        '''

        Returns a list[ str ] of member names

        '''
        return [ 'source', 'provider', 'path', 'connection', 'sqlstatement',
                 'commandtype', 'tablename', 'columnnames', 'values',
                 'commandtext', 'connectionstring', 'createtable', 'createframe' ]

    def createtable( self ) -> list[ db.Row ]:
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
            _exc.method = 'createtable( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def createframe( self ) -> DataFrame:
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
            _exc.method = 'createframe( self )'
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
    __driver = None
    __dsn = None
    __data = None
    __columns = None
    __commandtext = None

    @property
    def commandtext( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value: str ):
        if value is not None:
            self.__commandtext = value

    def __init__( self, connection: Connection, sqlstatement: SqlStatement ):
        super( ).__init__( connection, sqlstatement )
        self.__source = super( ).source
        self.__provider = Provider.Access
        self.__connection = super( ).connection
        self.__sqlstatement = super( ).sqlstatement
        self.__cooandtext = sqlstatement.__getquerytext( )
        self.__driver = r'DRIVER={ Microsoft ACCDB Driver( *.mdb, *.accdb ) };'
        self.__data = [ ]

    def __str__( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    def __dir__( self ) -> list[ str ]:
        '''

        Returns a list[ str ] of member names

        '''
        return [ 'source', 'provider', 'path', 'connection', 'sqlstatement',
                 'commandtype', 'tablename', 'columnnames', 'values',
                 'commandtext', 'connectionstring',
                 'frame', 'createtable', 'createframe' ]

    def createtable( self ) -> list[ db.Row ]:
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

    def createframe( self ) -> DataFrame:
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

class SqlData( Query ):
    '''

     Constructor:

     SqlData( connection: Connection, sqlstatement: SqlStatement )

     Purpose:

     Class providing object represents the
     value models in the MS SQL Server database

     '''
    __querytext = None
    __serverpath = None
    __driverinfo = None
    __dsn = None
    __columns = None
    __data = None

    @property
    def commandtext( self ) -> str:
        if self.__commandtext is not None:
            return self.__commandtext

    @commandtext.setter
    def commandtext( self, value: str ):
        if value is not None:
            self.__commandtext = value

    def __init__( self, connection: Connection, sqlstatement: SqlStatement ):
        super( ).__init__( connection, sqlstatement )
        self.__provider = Provider.SqlServer
        self.__connection = connection
        self.__source = connection.source
        self.__querytext = sqlstatement.commandtext
        self.__table = connection.source.name
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
                 'frame', 'createtable', 'createframe' ]

    def createtable( self ) -> list[ db.Row ]:
        '''

        Purpose:

        Parameters:

        Returns:

        '''

        try:
            _query = self.__querytext
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
            _exc.cause = 'SqlData'
            _exc.method = 'create_table( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def createframe( self ) -> DataFrame:
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
            _exc.cause = 'SqlData'
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
    __source = None
    __tablename = None
    __path = None
    __connection = None
    __sqlcommand = None
    __data = None
    __frame = None
    __columnnames = None
    __columncount = None
    __rowcount = None
    __index = None

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
    def name( self ) -> str:
        '''Get the name of the data source'''
        if self.__tablename is not None:
            return self.__tablename

    @name.setter
    def name( self, value: str ):
        '''Sets the name of the data source'''
        if value is not None:
            self.__tablename = value

    @property
    def path( self ) -> str:
        '''
        Gets a string  to the data source
        '''
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, value: str ):
        '''
        Sets a string to the data source
        '''
        if value is not None:
            self.__path = value

    @property
    def data( self ) -> list[ tuple ]:
        '''
        Gets a list[ tupel ] representing rows in a dataframe
        '''
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ tuple ] ):
        '''
        Sets a list[ tuple ] representing rows in a dataframe
        '''
        if value is not None:
            self.__data = value

    @property
    def sqlcommand( self ) -> str:
        '''
        Gets a string representing the SQL command text
        '''
        if self.__sqlcommand is not None:
            return self.__sqlcommand

    @sqlcommand.setter
    def sqlcommand( self, value: str ):
        '''
        Sets a string representing the SQL command text
        '''
        if value is not None:
            self.__sqlcommand = value

    @property
    def columnnames( self ) -> list[ str ]:
        '''
        Gets a list[ str ] representing column names
        '''
        if self.__columnnames is not None:
            return self.__columnnames

    @columnnames.setter
    def columnnames( self, value: list[ str ] ):
        '''
        Sets a list[ str ] representing column names
        '''
        if value is not None:
            self.__columnnames = value

    @property
    def index( self ) -> int:
        '''Gets the index of the data frame'''
        if self.__index is not None:
            return self.__index

    @index.setter
    def index( self, value: int ):
        '''Sets the index of the data frame'''
        if value is not None:
            self.__index = value

    @property
    def frame( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @frame.setter
    def frame( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    def __init__( self, source: Source ):
        self.__source = source
        self.__tablename = source.name
        self.__path = DbConfig( source ).getdatapath( )
        self.__sqlcommand = f'SELECT * FROM {source.name};'
        self.__frame = self.createframe( )
        self.__data = [ tuple( i ) for i in self.__frame.iterrows( ) ]
        self.__columnnames = list( self.__frame.columns.names )
        self.__index = self.createframe( ).index

    def __dir__( self ) -> list[ str ]:
        '''
        Returns a list[ str ] of member names
        '''
        return [ 'source', 'path', 'name', 'query',
                 'data', 'columnnames', 'createframe' ]

    def createframe( self ) -> DataFrame:
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
            self.__frame = sqlreader( _sql, _connection )
            return self.__frame
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Data'
            _exc.cause = 'BudgetData'
            _exc.method = 'createframe( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class DataBuilder( ):
    '''
    Constructor:

    DataBuilder( source: Source, provider = Provider.SQLite,
                  command_type = SQL.SELECTALL, names: list[ str ] = None,
                  values: tuple = None ).

    Purpose:

    Class provides functionality to access application data.

    '''
    __names = None
    __values = None
    __commandtype = None
    __source = None
    __provider = None
    __dbconfig = None
    __sqlconfig = None
    __connection = None
    __sqlstatement = None
    __commandtext = None
    __data = None

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

    def __init__( self, source: Source, provider = Provider.SQLite,
                  command = SQL.SELECTALL, names: list[ str ] = None,
                  values: tuple = None ):
        self.__source = source
        self.__provider = provider
        self.__commandtype = command
        self.__name = names
        self.__values = values
        self.__dbconfig = DbConfig( source, provider )
        self.__connection = Connection( source )
        self.__sqlconfig = SqlConfig( command, names, values )
        self.__sqlstatement = SqlStatement( self.__dbconfig, self.__sqlconfig )

    def createtable( self ) -> list[ db.Row ]:
        try:
            if self.__provider == Provider.SQLite:
                _sqlite = SQLiteData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _sqlite.createtable( ) ]
                return self.__data
            elif self.__provider == Provider.Access:
                _access = AccessData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _access.createtable( ) ]
                return self.__data
            elif self.__provider == Provider.SqlServer:
                _sql = SqlData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _sql.createtable( ) ]
                return self.__data
            else:
                _sqlite = SQLiteData( self.__connection, self.__sqlstatement )
                self.__data = [ i for i in _sqlite.createtable( ) ]
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
    __name = None
    __value = None
    __label = None
    __id = None
    __type = None
    __caption = None
    __table = None
    __frame = None

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

    DataRow( names: list[ str ] = None, values: tuple = ( ), source: Source = None)

    Purpose:

    Defines the class representing rows of data

    '''
    __source = None
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

    def __init__( self, names: list[ str ] = None, values: tuple = ( ),
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

    DataTable( columns: list[ str ] = None, rows: list = None,
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
    __source = None

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

    def __init__( self, columns: list[ str ] = None, rows: list = None,
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
