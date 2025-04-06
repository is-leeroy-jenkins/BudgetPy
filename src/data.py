'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                data.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="data.py" company="Terry D. Eppler">

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
    data.py
  </summary>
  ******************************************************************************************
  '''
#  ***********************************************************************
#  Assembly         : BudgetPy
#  Author           : Terry D. Eppler
#  Created          : 05-29-2023
#  #
#  Last Modified By : Terry D. Eppler
#  Last Modified On : 05-29-2023
#  ***********************************************************************
#  <copyright file=".py" company="Terry Eppler">
#     Copyright ©  2023  Terry Eppler
#  #
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#  #
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#  #
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https:#www.gnu.org/licenses/>.
#  #
#     Contact: terryeppler@gmail.com or eppler.terry@epa.gov
#  </copyright>
#  <summary>
#  #
#  </summary>
#  ***********************************************************************

import sqlite3 as sqlite
from pandas import DataFrame
from pandas import read_sql as sqlreader
import pyodbc as db
import os
from static import Source, Provider, SQL, ParamStyle
from booger import Error, ErrorDialog

class Pascal( ):
	'''

	Constructor:
	Pascal( input: str )

	Purpose:
	Class splits string 'input' argument into Pascal Casing

	'''

	def __init__( self, input: str=None ):
		self.input = input
		self.output = input if input.istitle( ) else self.join( )

	def __str__( self ) -> str:
		if self.output is not None:
			return self.output

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
			_buffer = [ str( c ) for c in self.output ]
			_output = [ ]
			_retval = ''
			for char in _buffer:
				if char.islower( ):
					_output.append( char )
				elif char.isupper( ) and _buffer.index( char ) == 0:
					_output.append( char )
				elif char.isupper( ) and _buffer.index( char ) > 0:
					_output.append( ' ' )
					_output.append( char )
			for o in _output:
				_retval += f'{o}'
			return _retval
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'Pascal'
			_exc.method = 'join( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def join( self ) -> str:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			if self.input.count( ' ' ) > 0:
				_buffer = [ str( c ) for c in self.input ]
				_output = [ ]
				_retval = ''
				for char in _buffer:
					if char != ' ':
						_output.append( char )
					elif char == ' ':
						_index = _buffer.index( char )
						_next = str( _buffer[ _index + 1 ] )
						if _next.islower( ):
							_cap = _next.upper( )
							_buffer.remove( _next )
							_buffer.insert( _index + 1, _cap )
						_buffer.remove( char )
						_output.append( _next.upper( ) )

			for o in _output:
				_retval += f'{o}'

			return _retval.replace( 'AH', 'Ah' ).replace( 'BOC', 'Boc' ) \
				.replace( 'RPIO', 'Rpio' ).replace( 'RC', 'Rc' ) \
				.replace( 'PRC', 'Prc' ).replace( 'ID', 'Id' ) \
				.replace( 'OMB', 'Omb' ).replace( 'NPM', 'Npm' ) \
				.replace( 'FOC', 'Foc' ).replace( 'ORG', 'Org' ) \
				.replace( 'THE', 'The' ).replace( 'OR', 'Or' ) \
				.replace( 'AND', 'And' ).replace( 'BUT', 'But' ) \
				.replace( 'OF', 'Of' )
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

	def __init__( self ):
		self.sqlite_driver = 'sqlite3'
		self.sqlite_path = r'../data/sqlite/datamodels/sql'
		self.access_driver = r'DRIVER={Microsoft ACCDB Driver (*.mdb, *.accdb)};DBQ='
		self.access_path = r'../data/access/datamodels/sql'
		self.sqlserver_driver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
		self.sqlserver_database = r'data\mssql\datamodels\sql'

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

		SqlFile( source: Source=None, provider: Provider  = Provider.SQLite,
				command: SQL=SQL.SELECTALL )

	Purpose:

		Class providing access to sqlstatement sub-folders in the application provided
		optional arguments source, provider, and command.

	'''

	def __init__( self, source: Source=None, provider: Provider=Provider.SQLite,
	              commandtype: SQL = SQL.SELECTALL ):
		self.command_type = commandtype
		self.source = source
		self.provider = provider
		self.data = [ 'Actuals',
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

	def __dir__( self ) -> list[ str ]:
		'''
		Retunes a list[ str ] of member names.
		'''
		return [ 'source', 'provider', 'command_type', 'get_file_path',
		         'get_folder_path', 'get_command_text' ]

	def get_file_path( self ) -> str:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			_sqlpath = SqlPath( )
			_data = self.data
			_provider = self.provider.name
			_tablename = self.source.name
			_command = self.command_type.name
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
			_data = self.data
			_source = self.source.name
			_provider = self.provider.name
			_command = self.command_type.name
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
			_source = self.source.name
			_paths = self.get_file_path( )
			_folder = self.get_folder_path( )
			_sql = ''
			for name in os.listdir( _folder ):
				if name.endswith( '.sql' ) and os.path.splitext( name )[ 0 ] == _source:
					_path = os.path.join( _folder, name )
					_query = open( _path )
					_sql = _query.read( )
				if _sql is None:
					_msg = 'INVALID INPUT!'
					raise ValueError( _msg )
				else:
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
		DbConfig( source: Source, provider: Provider=Provider.SQLite )

	Purpose:
		Class provides list of Budget Execution tables across two databases

	'''

	def __init__( self, src: Source, pro: Provider=Provider.SQLite ):
		self.provider = pro
		self.source = src
		self.table_name = src.name
		self.sqlite_path = os.getcwd( ) + r'\data\sqlite\datamodels\Data.data'
		self.access_driver = r'DRIVER={ Microsoft Access Driver (*.mdb, *.accdb) };DBQ='
		self.access_path = os.getcwd( ) + r'\db\access\datamodels\sql\Data.accdb'
		self.sqlserver_driver = r'DRIVER={ ODBC Driver 17 for SQL Server };SERVER=.\SQLExpress;'
		self.sqlserver_path = os.getcwd( ) + r'\db\mssql\datamodels\Data.mdf'
		self.data = [ 'Actuals',
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
		if self.table_name is not None:
			return self.table_name

	def __dir__( self ) -> list[ str ]:
		'''
		Retunes a list[ str ] of member names.
		'''
		return [ 'source', 'provider', 'table_name', 'get_driver_info',
		         'sqlite_path', 'access_driver', 'access_path',
		         'sqlserver_driver', 'sqlserver_path',
		         'get_data_path', 'get_connection_string' ]

	def get_driver_info( self ) -> str:
		'''

		Purpose:
			Returns a string defining the driverinfo being used

		Parameters:  None

		Returns:  str

		'''
		try:
			if self.provider.name == 'SQLite':
				return self.sqlite_path
			elif self.provider.name == 'Access':
				return self.access_driver
			elif self.provider.name == 'SqlServer':
				return self.sqlserver_driver
			else:
				return self.sqlite_driver
		except Exception as e:
			_exc = Error( e )
			_exc.cause = 'DbConfig Class'
			_exc.method = 'getdriver_info( self )'
			_error = ErrorDialog( _exc )
			_error.show( )

	def get_data_path( self ) -> str:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			if self.provider.name == 'SQLite':
				return self.sqlite_path
			elif self.provider.name == 'Access':
				return self.access_path
			elif self.provider.name == 'SqlServer':
				return self.sqlserver_path
			else:
				return self.sqlite_path
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
			if self.provider.name == Provider.Access.name:
				return self.get_driver_info( ) + _path
			elif self.provider.name == Provider.SqlServer.name:
				return r'DRIVER={ ODBC Driver 17 for SQL Server };Server=.\SQLExpress;' \
					+ f'AttachDBFileName={_path}' \
					+ f'DATABASE={_path}Trusted_Connection=yes;'
			else:
				return f'{_path} '
		except Exception as e:
			_exc = Error( e )
			_exc.cause = 'DbConfig Class'
			_exc.method = 'get_connection_string( self )'
			_error = ErrorDialog( _exc )
			_error.show( )

class Connection( DbConfig ):
	'''

	Constructor:
		Connection( source: Source, provider: Provider=Provider.SQLite )

	Purpose:
		Class providing object used to connect to the databases

	'''

	def __init__( self, src: Source, pro: Provider=Provider.SQLite ):
		super( ).__init__( src, pro )
		self.source = super( ).source
		self.provider = super( ).provider
		self.data_path = super( ).get_data_path( )
		self.driver = super( ).get_driver_info( )
		self.dsn = super( ).table_name + ';'
		self.connection_string = super( ).get_connection_string( )

	def __dir__( self ) -> list[ str ]:
		'''
		Retunes a list[ str ] of member names.
		'''
		return [ 'source', 'provider', 'table_name', 'getdriver_info',
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
			if self.provider.name == Provider.Access.name:
				return db.connect( self.connection_string )
			elif self.provider.name == Provider.SqlServer.name:
				return db.connect( self.connection_string )
			else:
				return sqlite.connect( self.connection_string )
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
					columnvalues: tuple=None, paramstyle: ParamStyle = None )

	 Purpose:

		 Class provides database interaction behavior

	 '''

	def __init__( self, cmd: SQL = SQL.SELECTALL, names: list[ str ]=None,
	              values: tuple=None, paramstyle: ParamStyle = None ):
		self.command_type = cmd
		self.column_names = names
		self.column_values = values
		self.parameter_style = paramstyle
		self.criteria = dict( zip( names, list( values ) ) ) \
			if names is not None and values is not None else None

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
			if self.column_names is not None and self.column_values is not None:
				_pairs = ''
				_kvp = zip( self.column_names, self.column_values )
				for k, v in _kvp:
					_pairs += f'{k} = \'{v}\' AND '
				_criteria = _pairs.rstrip( ' AND ' )
				if _criteria is None:
					_msg = 'INVALID INPUT!'
					raise ValueError( _msg )
			else:
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
			if (isinstance( self.column_names, list ) and
					isinstance( self.column_values, tuple )):
				pairs = ''
				for k, v in zip( self.column_names, self.column_values ):
					pairs += f'{k} = \'{v}\' AND '
				_criteria = 'WHERE ' + pairs.rstrip( ' AND ' )
				if _criteria is None:
					_msg = 'INVALID INPUT!'
					raise ValueError( _msg )
			else:
				return _criteria
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
			if self.column_names is not None and self.column_values is not None:
				_pairs = ''
				_criteria = ''
				for k, v in zip( self.column_names, self.column_values ):
					_pairs += f'{k} = \'{v}\', '
				_criteria = 'SET ' + _pairs.rstrip( ', ' )
				if _criteria is None:
					_msg = 'INVALID INPUT!'
					raise ValueError( _msg )
			else:
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
			if self.column_names is not None:
				_colnames = ''
				for n in self.column_names:
					_colnames += f'{n}, '
				_columns = '(' + _colnames.rstrip( ', ' ) + ')'
				if _columsn is None:
					_msg = 'INVALID INPUT!'
					raise ValueError( _msg )
			else:
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
			if self.column_values is not None:
				_vals = ''
				for v in self.column_values:
					_vals += f'{v}, '
					_values = 'VALUES (' + _vals.rstrip( ', ' ) + ')'
					if _values is None:
						_msg = 'INVALID INPUT!'
						raise ValueError( _msg )
			else:
				return _values
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'SqlConfig'
			_exc.method = 'value_dump( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SqlStatement( ):
	'''

	Constructor:

		SqlStatement( dbcfg: DbConfig, sqlcfg: SqlConfig )

	Purpose:

		Class represents the values models used in the SQLite database

	'''

	def __init__( self, dbcfg: DbConfig, sqcfg: SqlConfig ):
		self.command_type = sqcfg.command_type
		self.provider = dbcfg.provider
		self.source = dbcfg.source
		self.table_name = dbcfg.table_name
		self.column_names = sqcfg.column_dump( )
		self.column_values = sqcfg.value_dump( )
		self.updates = sqcfg.set_dump( )
		self.criteria = dict( zip( self.column_names, list( self.column_values ) ) ) \
			if self.column_names is not None and self.column_values is not None else None
		self.command_text = self.__getquerytext( )

	def __str__( self ) -> str:
		if self.command_text is not None:
			return self.command_text

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names.

		'''
		return [ 'provider', 'table_name',
		         'command_type', 'column_names', 'values',
		         'updates', 'command_text' ]

	def __getquerytext( self ) -> str:
		'''
		Purpose:

		Parameters:

		Returns:
		'''

		try:
			_table = self.table_name
			_cols = self.column_names
			_vals = self.column_values
			_where = self.criteria
			_cmd = self.command_type
			_updates = self.updates
			if _cmd == SQL.SELECTALL and _cols is None and _vals is None and _where is None:
				return f'SELECT * FROM {_table}'
			elif _cmd == SQL.SELECT and _cols is not None and _vals is None and _where is not None:
				return f'SELECT ' + _cols + f'FROM {_table}' + f' {_where}'
			elif _cmd == SQL.INSERT and len( _where.items( ) ) > 0:
				return f'SELECT ' + _cols + f' FROM {_table}' + f' {_where}'
			elif _cmd == SQL.INSERT and _cols is not None and _vals is not None:
				return f'INSERT INTO {_table} ' + f'{_cols} ' + f'{_vals}'
			elif _cmd == SQL.UPDATE and _cols is not None and _vals is None and _where is not None:
				_set = self.updates
				return f'UPDATE {_table} ' + f'{_set}' + f'{_vals}' + f'{_where}'
			elif _cmd == SQL.DELETE and _cols is None and _vals is None and _where is not None:
				return f'DELETE FROM {_table} ' + f'{_where}'
			elif _cmd == SQL.SELECT and _cols is not None and _vals is None and _where is None:
				cols = _cols.lstrip( '(' ).rstrip( ')' )
				return f'SELECT {cols} FROM {_table}'
			elif _cmd == SQL.SELECTALL and _cols is None and _vals is None and _where is not None:
				return f'SELECT * FROM {_table}' + f'{_where}'
			elif _cmd == SQL.DELETE and _cols is None and _vals is None and _where is not None:
				return f'DELETE FROM {_table}' + f'{_where}'
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

	def __init__( self, conn: Connection, sql: SqlStatement ):
		self.connection = conn
		self.sql_statement = sql
		self.sql_config = SqlConfig( conn.source, conn.provider )
		self.source = conn.source
		self.table_name = self.source.name
		self.provider = conn.provider
		self.command_type = sql.command_type
		self.data_path = conn.data_path
		self.connection_string = conn.connection_string
		self.column_names = self.sql_config.column_names
		self.column_values = tuple( self.sql_config.criteria.values( ) ) \
			if self.column_values is not None else None
		self.command_text = sql.command_text

	def __str__( self ) -> str:
		if self.command_text is not None:
			return self.command_text

	def __dir__( self ) -> list[ str ]:
		return [ 'source', 'provider', 'data_path', 'connection', 'sql_statement',
		         'command_type', 'table_name', 'column_names', 'values',
		         'command_text', 'connection_string' ]

class SQLiteData( Query ):
	'''

	Constructor:

		SQLiteData( connection: Connection, sqlstatement: SqlStatement )

	Purpose:

		Class represents the SQLite data factory

	'''

	def __init__( self, conn: Connection, sql: SqlStatement ):
		super( ).__init__( conn, sql )
		self.provider = Provider.SQLite
		self.connection = super( ).connection
		self.sql_statement = super( ).sqlstatement
		self.source = super( ).source
		self.table_name = super( ).source.name
		self.command_type = super( ).command_type
		self.data_path = super( ).data_path
		self.driver_info = super( ).connection.driver_info
		self.connection_string = super( ).connection_string
		self.column_names = super( ).column_names
		self.column_values = super( ).column_values
		self.command_text = super( ).command_text

	def __str__( self ) -> str:
		if self.__query is not None:
			return self.__query

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names

		'''
		return [ 'source', 'provider', 'data_path', 'connection', 'sql_statement',
		         'command_type', 'table_name', 'column_names', 'column_values', 'driver_info',
		         'command_text', 'connection_string', 'create_table', 'create_frame' ]

	def create_frame( self ) -> DataFrame:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			if _frame is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _frame
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'SQLiteData'
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
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			_data = [ tuple( i ) for i in _frame.iterrows( ) ]
			if _data is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'SQLiteData'
			_exc.method = 'create_tuples( self )'
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

	def __init__( self, conn: Connection, sql: SqlStatement ):
		super( ).__init__( conn, sql )
		self.source = super( ).source
		self.provider = Provider.Access
		self.connection = super( ).connection
		self.sql_statement = super( ).sqlstatement
		self.command_text = super( ).command_text
		self.driver_info = r'DRIVER={ Microsoft ACCDB Driver( *.mdb, *.accdb ) };'
		self.data = [ ]

	def __str__( self ) -> str:
		if self.command_text is not None:
			return self.command_text

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names

		'''
		return [ 'source', 'provider', 'data_path', 'connection', 'sql_statement',
		         'command_type', 'table_name', 'column_names', 'column_values',
		         'command_text', 'connection_string',
		         'create_table', 'create_frame' ]

	def create_frame( self ) -> DataFrame:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			if _frame is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _frame
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'AccessData'
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
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			_data = [ tuple( i ) for i in _frame.iterrows( ) ]
			if _data is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'AccessData'
			_exc.method = 'create_tuples( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SqlServerData( Query ):
	'''

	 Constructor: SqlData( connection: Connection, sqlstatement: SqlStatement )

	 Purpose: Class providing object represents the value models in the MS SQL Server database

	 '''

	def __init__( self, conn: Connection, sql: SqlStatement ):
		super( ).__init__( conn, sql )
		self.provider = Provider.SqlServer
		self.connection = super( ).connection
		self.source = super( ).source
		self.command_text = super( ).command_text
		self.table_name = super( ).table_name
		self.sqlserver_path = r'(LocalDB)\MSSQLLocalDB;'
		self.driver_info = r'{ SQL Server Native Client 11.0 };'

	def __str__( self ) -> str:
		if self.source is not None:
			return self.source.name

	def __dir__( self ) -> list[ str ]:
		'''

		Returns a list[ str ] of member names

		'''
		return [ 'source', 'provider', 'sqlserver_path', 'connection',
		         'table_name', 'driver_info',
		         'command_text', 'create_table', 'create_frame' ]

	def create_frame( self ) -> DataFrame:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			if _frame is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _frame
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'SqlServerData'
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
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			_data = [ tuple( i ) for i in _frame.iterrows( ) ]
			if _data is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'SqlServerData'
			_exc.method = 'create_tuples( self )'
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

	def __init__( self, src: Source ):
		self.source = src
		self.table_name = src.name
		self.data_path = DbConfig( src ).get_data_path( )
		self.command_text = f'SELECT * FROM {src.name};'

	def __dir__( self ) -> list[ str ]:
		'''
			Returns a list[ str ] of member names
		'''
		return [ 'source', 'data_path', 'table_name',
		         'command_text', 'create_frame', 'create_tuples' ]

	def create_frame( self ) -> DataFrame:
		'''

		Purpose:

		Parameters:

		Returns:

		'''

		try:
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			if _frame is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
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
			_path = self.data_path
			_source = self.source
			_table = self.source.name
			_connection = sqlite.connect( _path )
			_sql = f'SELECT * FROM {_table};'
			_frame = sqlreader( _sql, _connection )
			_data = [ tuple( i ) for i in _frame.iterrows( ) ]
			if _data is None:
				_msg = "INVALID INPUT!"
				raise ValueError( _msg )
			else:
				return _data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'BudgetData'
			_exc.method = 'create_tuples( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class DataBuilder( BudgetData ):
	'''
	Constructor:

		DataBuilder( source: Source, provider = Provider.SQLite,
					  commandtype = SQL.SELECTALL, names: list[ str ]=None,
					  values: tuple=None ).

	Purpose:

		Class provides functionality to access application data.

	'''

	# Fields
	source: Source=None
	table_name: str=None
	data_path: str=None
	command_text: str=None

	def __init__( self, src: Source ):
		super( ).__init__( src )
		self.source = super( ).source
		self.table_name = super( ).table_name
		self.data_path = super( ).data_path
		self.command_text = super( ).command_text

	def create_tuples( self ) -> list[ tuple ]:
		try:
			_data = super( ).create_tuples( )
			if _data is None:
				_msg = 'INVALID INPUT!'
				raise ValueError( _msg )
			else:
				return _data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'DataBuilder'
			_exc.method = 'create_tuples( self )'
			_error = ErrorDialog( _exc )
			_error.show( )

	def create_frame( self ) -> DataFrame:
		try:
			_frame = super( ).create_frame( )
			if _frame is None:
				_msg = 'INVALID INPUT!'
				raise ValueError( _msg )
			else:
				return _frame
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Data'
			_exc.cause = 'DataBuilder'
			_exc.method = 'create_frame( self )'
			_error = ErrorDialog( _exc )
			_error.show( )

class DataColumn( ):
	'''

	Constructor:

		DataColumn( name: str = '', dtype: type = None, value: object = None )

	Purpose:

		Defines the class providing schema information.

	 '''

	# Fields
	name: str=None
	label: str=None
	caption: str=None
	type: type = None
	value: object = None

	def __init__( self, name: str = '', dtype: type = None, value: object = None ):
		self.name = name
		self.label = name
		self.caption = name
		self.type = dtype
		self.value = value

	def __str__( self ) -> str:
		if self.name is not None:
			return self.name

	def is_numeric( self ) -> bool:
		try:
			if self.value is not None:
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
			if self.value is not None:
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

	DataRow( names: list[ str ]=None, values: tuple = ( ), source: Source=None)

	Purpose:

	Defines the class representing rows of data

	'''

	def __init__( self, names: list[ str ]=None, values: tuple=( ),
	              source: Source=None ):
		self.source = source
		self.names = names
		self.column_values = values
		self.items = zip( names, list( values ) )
		self.key = str( self.names[ 0 ] )
		self.index = int( self.column_values[ 0 ] )

	def __str__( self ) -> str:
		if self.index is not None:
			return 'Row ID: ' + str( self.index )

class DataTable( ):
	'''
	Constructor:

	DataTable( columns: list[ str ]=None, rows: list = None,
		source: Source=None, dataframe: DataFrame = None  )

	Purpose:

	Defines the class representing table of data

	'''

	def __init__( self, columns: list[ str ]=None, rows: list=None,
	              source: Source=None, dataframe: DataFrame=None ):
		self.frame = dataframe
		self.name = source.name
		self.rows = [ tuple( r ) for r in dataframe.iterrows( ) ]
		self.data = self.rows
		self.columns = [ str( c ) for c in columns ]
		self.schema = [ DataColumn( c ) for c in columns ]

	def __str__( self ) -> str:
		if self.name is not None:
			return self.name
