'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Ninja.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Ninja.py" company="Terry D. Eppler">

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

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    The Ninja module defines the data transfer objects used in the
    BudgetPy application.
  </summary>
  ******************************************************************************************
  '''
import datetime as dt
from datetime import datetime
from pandas import DataFrame
from sqlite3 import Row
from Booger import Error, ErrorDialog
from Static import Source, Provider, SQL
from Data import (DbConfig, SqlConfig, Connection, SqlStatement,
                  BudgetData, DataBuilder )
from sqlalchemy.orm import ( Session, sessionmaker, DeclarativeBase, Mapped,
                             mapped_column, registry )
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base( )

class Account( Base ):
	'''
    Constructor:
    Account( treas: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Account Codes
    '''
	__tablename__ = 'Accounts'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	goal_code = Column( String( 55 ) )
	objective_code = Column( String( 55 ) )
	npm_code = Column( String( 55 ) )
	npm_name = Column( String( 155 ) )
	program_project_code = Column( String( 55 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 55 ) )
	program_area_name = Column( String( 55 ) )
	
	def __init__( self, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Accounts
		self.fields = [ 'AccountsId',
		                'Code',
		                'GoalCode',
		                'ObjectiveCode',
		                'NpmCode',
		                'NpmName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'ActivityCode',
		                'ActivityName',
		                'AgencyActivity' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code',
		         'goal_code', 'objective_code', 'npm_code',
		         'program_project_code',
		         'data', 'fields', 'frame',
		         'copy', 'getdata', 'getframe' ]
	
	def copy( self ):
		try:
			_clone = Account( code=self.code )
			_clone.goal_code = self.goal_code
			_clone.objective_code = self.objective_code
			_clone.npm_code = self.npm_code
			_clone.programprojectcode = self.programprojectcode
			return _clone
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Account'
			_exc.method = 'copy( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getdata( self ) -> list[ Row ]:
		try:
			_source = Source.Accounts
			_provider = Provider.SQLite
			_names = [ 'Code', ]
			_values = (self.code,)
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( _source, _provider )
			_sql = SqlStatement( _connection, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Account'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_src = self.source
			_data = BudgetData( _src )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Account'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ActivityCode( Base ):
	'''

    Constructor:
        ActivityCode( code: str, provider: Provider=Provider.SQLite )

    Purpose:
        Data class representing Activity Codes

    '''
	__tablename__ = 'ActivityCodes'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 55 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ActivityCodes
		self.id = id
		self.code = code
		self.name = None
		self.title = None
		self.fields = [ 'ActivityCodesId',
		                'Code',
		                'Name',
		                'Title' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'data', 'fields', 'frame',
		         'fields', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Activity'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
		
        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Activity'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AdjustedTrialBalance( Base ):
	'''

	Constructor:
	AdjustedTrialBalances( bfy: str, number: str )

	Purpose:
	Data class representing a record in the ATB

	'''
	__tablename__ = 'AdjustedTrialBalances'
	id = Column( Integer( ), primary_key=True )
	agency_identifier = Column( String( 80 ) )
	allocation_transfer_agency = Column( String( 80 ) )
	availability_type = Column( String( 80 ) )
	main_account = Column( String( 80 ) )
	subaccount = Column( String( 80 ) )
	treasury_symbol = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	ledger_account = Column( String( 80 ) )
	account_name = Column( String( 155 ) )
	beginning_balance = Column( Float( ) )
	credit_balance = Column( Float( ) )
	debit_balance = Column( Float( ) )
	ending_balance = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str,
	              fundcode: str, provider: Provider = Provider.SQLite ):
		self.source = Source.AdjustedTrialBalances
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'AdjustedTrialBalancesId',
		                'BFY',
		                'EFY',
		                'FundCode',
		                'FundName',
		                'TreasurySymbol',
		                'AccountNumber',
		                'AccountName',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.accountnumber is not None:
			return self.accountnumber
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'treasury_symbol', 'account_number', 'account_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AdjustedTrialBalances'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AdjustedTrialBalances'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AllowanceHolder( Base ):
	'''

    Constructor:
    AllowanceHolder( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Data class representing Allowance Holders

    '''
	__tablename__ = 'AllowanceHolders'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 25 ) )
	code = Column( String( 55 ) )
	name = Column( String( 55 ) )
	earmark_flag = Column( String( 50 ) )
	
	
	def __init__( self, code: str = None,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.AllowanceHolders
		self.code = code
		self.fields = [ 'AllowanceHoldersId',
		                'Code',
		                'Name'
		                'Status'
		                'EarmarkFlag' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'status', 'earmark_flag', 'usage',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        	
        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'AllowanceHoldersId', 'Code', 'Name', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AllowanceHolder'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AllowanceHolder'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AmericanRescuePlanCarryoverEstimate( Base ):
	'''

    Constructor:
    CarryoverEstimate( bfy: str, pvdr = Provider.SQLite )

    Purpose:
    Class representing estimates for ARP carryover

    '''
	__tablename__ = 'AmericanRescuePlanCarryoverEstimates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	amount = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	available = Column( Float( ) )
	estimate = Column( Float( ) )
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.AmericanRescuePlanCarryoverEstimates
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy )==4 else None
		self.fields = [ 'CarryoverEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'rpio_code', 'rpio_name', 'fund_code', 'fund_name',
		         'amount', 'available', 'open_commitments', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name', 'estimate',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_data = BudgetData( self.source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AnnualCarryoverEstimate( Base ):
	'''
    Constructor:
    AnnualCarryoverEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class providing Carryover Estimate data for
    '''
	__tablename__ = 'AnnualCarryoverEstimates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	amount = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	available = Column( Float( ) )
	estimate = Column( Float( ) )
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.AnnualCarryoverEstimates
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy )==4 else None
		self.frame = DataFrame( )
		self.fields = [ 'CarryoverEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'rpio_code', 'rpio_name', 'amount',
		         'available', 'open_commitments', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AnnualReimbursableEstimate( Base ):
	'''
    Constructor:
    AnnualReimbursableEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defining object representing reimbursable estimates'''
	__tablename__ = 'AnnualReimbursableEstimates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	amount = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	available = Column( Float( ) )
	estimate = Column( Float( ) )
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.AnnualReimbursableEstimates
		self.bfy = bfy
		self.fields = [ 'AnnualReimbursableEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'rpio_code', 'rpio_name', 'amount', 'estimate',
		         'available', 'open_commitments', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Appropriation( Base ):
	'''
    Constructor:
    Appropriation( fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Data class representing Appropriations
    '''
	__tablename__ = 'Appropriations'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str ):
		self.source = Source.Appropriations
		self.provider = Provider.SQLite
		self.code = code
		self.fields = [ 'AppropriationsId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'data', 'fields',
		         'code', 'name',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AppropriationAvailableBalance( Base ):
	'''
    Constructor:
     AppropriationAvailableBalance( bfy: str, efy: str, fund: str )

    Purpose:
        Data class representing Appropriation-level balances
    '''
	__tablename__ = 'AppropriationAvailableBalances'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	original_amount = Column( Float( ) )
	authority = Column( Float( ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	transfer_in = Column( Float( ) )
	transfer_out = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	unliquidated_obligations = Column( Float( ) )
	expenditures = Column( Float( ) )
	total_available = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fundcode: str ):
		self.source = Source.Appropriations
		self.provider = Provider.SQLite
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'AppropriationAvailableBalancesId',
		                'BFY',
		                'EFY',
		                'FundCode',
		                'FundName',
		                'OmbAccountCode',
		                'OmbAccountName',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'TotalAuthority',
		                'Budgeted',
		                'TotalReimbursements',
		                'TotalRecoveries',
		                'TotalUsed',
		                'TotalAvailable' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'authority',
		         'budgeted', 'reimbursements', 'recoveries', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = (self.fundcode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AppropriationLevelAuthority( Base ):
	'''
    Constructor:
    AppropriationLevelAuthority( bfy: str, efy: str, fund: str )

    Purpose:
    Data class representing Appropriation-level authority
    '''
	__tablename__ = 'AppropriationLevelAuthority'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	budget_level = Column( String( 10 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	reimbursements = Column( Float( ) )
	recoveries = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	transfer_in = Column( Float( ) )
	transfer_out = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	unliquidated_obligations = Column( Float( ) )
	expenditures = Column( Float( ) )
	total_available = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fundcode: str ):
		self.source = Source.AppropriationLevelAuthority
		self.provider = Provider.SQLite
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'AppropriationLevelAuthorityId',
		                'BFY',
		                'EFY',
		                'FundCode',
		                'FundName',
		                'MainAccount',
		                'Authority',
		                'Budgeted',
		                'Reimbursements',
		                'Recoveries',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if isinstance( self.fundcode, str ) and self.fundcode!='':
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'authority',
		         'budgeted', 'reimbursements', 'recoveries', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = tuple( self.fundcode, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Allocation( Base ):
	'''
    Constructor:
    Allocation( bfy = None, fund = None, provider: Provider=Provider.SQLite )

    Purpose:
    Class defining object representing Allocations

    '''
	__tablename__ = 'Allocations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	status_of_funds_id = Column( Integer( ) )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	amount = Column( Float( ) )
	npm_code = Column( String( 25 ) )
	npm_name = Column( String( 255 ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fundcode: str,
	              provider: Provider = Provider.SQLite ):
		self.source = Source.Allocations
		self.provider = provider
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy )==4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund!='' else None
		self.fields = [ 'AllocationsId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'LowerName',
		                'Amount',
		                'NpmCode',
		                'NpmName',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.programprojectname is not None:
			return self.programprojectname
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'rpio_code', 'rpio_name', 'ah_code', 'ah_name',
		         'org_code', 'org_name', 'boc_code', 'boc_name',
		         'rc_code', 'rc_name', 'npm_code', 'npm_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'goal_code', 'goal_name',
		         'account_code', 'objective_code', 'objective_name', 'authority',
		         'budgeted', 'reimbursements', 'recoveries', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Allocations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

		Purpose: Method returning pandas dataframe
        comprised of datatable data

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Allocations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ApportionmentData( Base ):
	'''
    Constructor:
    ApportionmentData( bfy: str, efy: str, main: str,
                       provider: Provider=Provider.SQLite )

    Purpose:
    Data class representing Letters Of Apportionment
    '''
	__tablename__ = 'ApportionmentData'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	fiscal_year = Column( String( 25 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	main_account = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	availability_type = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	approval_date = Column( String( 80 ) )
	line_number = Column( String( 80 ) )
	line_name = Column( String( 155 ) )
	line_split = Column( String( 80 ) )
	amount = Column( Float( ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	
	def __init__( self, year: str, bfy: str, efy: str,
	              main: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ApportionmentData
		self.fiscalyear = year
		self.bfy = bfy
		self.efy = efy
		self.mainaccount = main
		self.fields = [ 'ApportionmentDataId',
		                'FiscalYear',
		                'BFY',
		                'EFY',
		                'AvailabilityType',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName',
		                'ApprovalDate',
		                'LineNumber',
		                'LineSplit',
		                'LineName',
		                'Amount',
		                'FundCode',
		                'FundName' ]
	
	def __str__( self ) -> str:
		if self.mainaccount is not None:
			return self.mainaccount
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fiscal_year', 'bfy', 'efy', 'availability_type',
		         'approval_date', 'line_number', 'line_split', 'line_name',
		         'amount', 'fund_code', 'fund_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
			_values = (self.bfy, self.efy, self.budgetaccountcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'Apportionment'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'Apportionment'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Actual( Base ):
	'''
    Constructor:
    Actual( bfy, fund, pvdr = Provider.SQLite  )

    Purpose:
    Object representing expenditure data
    '''
	__tablename__ = 'Actuals'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	subappropriation_code = Column( String( 80 ) )
	subappropriation_name = Column( String( 155 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	current_authority = Column( Float( ) )
	current_obligations = Column( Float( ) )
	carryover_authority = Column( Float( ) )
	carryover_obligations = Column( Float( ) )
	available_balance = Column( String( 80 ) )
	activity_code = Column( String( 80 ) )
	activity_name = Column( String( 155 ) )
	goal_code = Column( String( 25 ) )
	goal_name = Column( String( 155 ) )
	objective_code = Column( String( 25 ) )
	objective_name = Column( String( 155 ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Actuals
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'ActualsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'AppropriationCode',
		                'AppropriationName',
		                'SubAppropriationCode',
		                'SubAppropriationName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RpioActivityCode',
		                'RpioActivityName',
		                'BocCode',
		                'BocName',
		                'UnliquidatedObligations',
		                'Obligations',
		                'Balance',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'GoalCode',
		                'GoalName',
		                'ObjectiveCode',
		                'ObjectiveName',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.programprojectname is not None:
			return self.programprojectname
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'appropriation_code', 'appropriation_name', 'subappropriation_code',
		         'subappropriation_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'balance',
		         'obligations', 'unliquidated_obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ApplicationTable( Base ):
	'''
    Constructor:
    ApplicationTable( name, pvdr = Provider.SQLite )

    Purpose:
    Class defines object that represents all the tables
    '''
	__tablename__ = 'ApplicationTables'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	name = Column( String( 150 ) )
	model = Column( String( 80 ) )
	title = Column( String( 255 ) )
	
	def __init__( self, name: str, provider: Provider = Provider.SQLite ):
		self.source = Source.ApplicationTables
		self.provider = provider
		self.name = name
		self.fields = [ 'ApplicationTablesId',
		                'Name',
		                'Model',
		                'Caption' ]
	
	def __str__( self ) -> str:
		if self.name is not None:
			return self.name
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'name', 'model',
		         'caption', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Name', ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( self.source, self.provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ApplicationTables'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose: Method returning pandas dataframe
        comprised of datatable data

        Parameters:

        Returns:

        	'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ApplicationTables'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AppropriationDocument( Base ):
	'''
    Constructor:
    AppropriationDocument( bfy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing Level 1 documents
    '''
	__tablename__ = 'AppropriationDocuments'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	fiscal_year = Column( String( 10 ) )
	bfy = Column( String( 25 ) )
	efy = Column( String( 25 ) )
	fund_code = Column( String( 80 ) )
	appropriation = Column( String( 80 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_date = Column( String( 80 ) )
	budget_level = Column( String( 10 ) )
	budgeting_controls = Column( String( 80 ) )
	posting_controls = Column( String( 80 ) )
	precommitment_controls = Column( String( 80 ) )
	commitment_controls = Column( String( 80 ) )
	obligation_controls = Column( String( 80 ) )
	accrual_controls = Column( String( 80 ) )
	expenditure_controls = Column( String( 80 ) )
	expense_controls = Column( String( 80 ) )
	reimbursement_controls = Column( String( 80 ) )
	reimbursable_agreement_controls = Column( String( 80 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	
	def __init__( self, bfy: str, efy: str, fund: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.AppropriationDocuments
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy )==4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund!='' else None
		self.fields = [ 'AppropriationDocumentsId',
		                'BFY',
		                'EFY',
		                'Fund',
		                'Appropriation',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentDate',
		                'LastDocumentDate',
		                'BudgetLevel',
		                'BudgetingControls',
		                'PostingControls',
		                'PreCommitmentControls',
		                'CommitmentControls',
		                'ObligationControls',
		                'AccrualControls',
		                'ExpenditureControls',
		                'ExpenseControls',
		                'ReimbursementControls',
		                'ReimbursableAgreementControls',
		                'Budgeted',
		                'Posted',
		                'CarryoverOut',
		                'CarryoverIn',
		                'EstimatedReimbursements',
		                'EstimatedRecoveries',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ):
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'appropriation',
		         'budget_level', 'document_type', 'document_number', 'document_date',
		         'last_document_date', 'budgeting_controls', 'posting_controls',
		         'precommitment_controls', 'commitment_controls', 'obligation_controls',
		         'accrual_controls', 'expenditure_controls', 'expense_controls',
		         'reimbursement_controls', 'reimbursement_controls',
		         'reimbursable_agreement_controls', 'budgeted', 'posted',
		         'carryover_in', 'carryover_out',
		         'estimated_reimbursments', 'estimated_recoveries',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AppropriationDocument'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AppropriationDocument'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetDocument( Base ):
	'''
    Constructor:
    BudgetDocument( bfy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing Level 2-3 documents
    '''
	__tablename__ = 'BudgetDocuments'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	budget_level = Column( String( 10 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_date = Column( String( 80 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fundcode: str,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetDocuments
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'BudgetDocumentsId',
		                'BFY',
		                'EFY',
		                'BudgetLevel',
		                'DocumentDate',
		                'LastDocumentDate',
		                'DocumentType',
		                'DocumentNumber',
		                'FundCode',
		                'FundName',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'ReimbursableAgreementControls',
		                'BudgetingControls',
		                'PostingControls',
		                'PreCommitmentControls',
		                'CommitmentControls',
		                'ObligationControls',
		                'ExpenditureControls',
		                'ExpenseControls',
		                'AccrualControls',
		                'ReimbursementControls',
		                'Budgeted',
		                'Posted',
		                'CarryoverOut',
		                'CarryoverIn',
		                'EstimatedRecoveries',
		                'EstimatedReimbursements',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.documentnumber is not None:
			return self.documentnumber
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'budget_level', 'document_date',
		         'last_document_date', 'document_type', 'document_number', 'fund_code',
		         'fund_name', 'rpio_code', 'rpio_name', 'ah_code', 'ah_name',
		         'org_code', 'org_name', 'account_code', 'program_project_pame',
		         'program_area_code', 'program_area_name', 'boc_code', 'boc_name',
		         'reimbursable_agreement_controls', 'budgeting_controls', 'posting_controls',
		         'precommitment_controls', 'commitment_controls', 'obligation_controls',
		         'expenditure_controls', 'expense_controls', 'accrual_controls',
		         'reimbursement_controls', 'budgeted', 'posted', 'carryover_out',
		         'carryover_in', 'estimated_recoveries', 'estimated_reimbursements',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.bfy, self.efy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetDocument'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetDocument'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetContact( Base ):
	'''
    Constructor:
    BudgetContact( last: str, first: str )

    Purpose:
    Class defines object represent budget contact info
    '''
	__tablename__ = 'BudgetContacts'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	first_name = Column( String( 155 ) )
	last_name = Column( String( 155 ) )
	rpio_name = Column( String( 255 ) )
	email_address = Column( String( 80 ) )
	phone = Column( String( 80 ) )
	section = Column( String( 80 ) )
	job_title = Column( String( 80 ) )
	street = Column( String( 80 ) )
	city = Column( String( 80 ) )
	state = Column( String( 80 ) )
	zip_code = Column( String( 80 ) )
	account = Column( String( 80 ) )
	display_name = Column( String( 155 ) )
	office_location = Column( String( 80 ) )
	
	def __init__( self, last: str, first: str, provider: Provider = Provider.SQLite ):
		self.lastname = last
		self.__first = first
		self.fields = [ 'BudgetContactsId',
		                'FirstName',
		                'LastName',
		                'RpioCode',
		                'RpioName',
		                'Section',
		                'JobTitle',
		                'City',
		                'State',
		                'ZipCode',
		                'OfficeLocation',
		                'Account',
		                'EmailAddress',
		                'EmailType',
		                'DisplayName' ]
	
	def __str__( self ) -> str:
		if self.emailaddress is not None:
			return self.emailaddress
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'first_name', 'last_name', 'rpio_code', 'rpio_name',
		         'section', 'job_title', 'state', 'zip_code', 'office_location',
		         'city', 'account', 'email_type', 'display_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetContacts'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetContacts'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetControl( Base ):
	'''
    Constructor:  BudgetControl( fund, pvdr = Provider.SQLite )

    Purpose;  Class defines object representing compass control data'''
	__tablename__ = 'BudgetControls'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 80 ) )
	name = Column( String( 80 ) )
	security_org = Column( String( 80 ) )
	budgeting_transtype = Column( String( 80 ) )
	posted_transtype = Column( String( 80 ) )
	estimated_reimbursable_transtype = Column( String( 80 ) )
	spending_adjustment_transtype = Column( String( 80 ) )
	estimated_recoveries_transtype = Column( String( 80 ) )
	actual_recoveries_transtype = Column( String( 80 ) )
	stategic_reserve_transtype = Column( String( 80 ) )
	profit_loss_transtype = Column( String( 80 ) )
	reimbursable_spending_option = Column( String( 80 ) )
	reimbursable_budgeting_option = Column( String( 80 ) )
	track_lower_level = Column( String( 80 ) )
	budget_lower_level = Column( String( 80 ) )
	recoveries_spending_option = Column( String( 80 ) )
	recoveries_budgeting_option = Column( String( 80 ) )
	record_next_level = Column( String( 80 ) )
	record_budgeting_mismatch = Column( String( 80 ) )
	profit_loss_spending_option = Column( String( 80 ) )
	profit_loss_budgeting_option = Column( String( 80 ) )
	carryin_lower_level = Column( String( 80 ) )
	carryin_lower_level = Column( String( 80 ) )
	carryin_amount_control = Column( String( 80 ) )
	budgeting_control = Column( String( 80 ) )
	posting_control = Column( String( 80 ) )
	precommitment_spending_control = Column( String( 80 ) )
	commitment_spending_control = Column( String( 80 ) )
	obligation_spending_control = Column( String( 80 ) )
	accrual_spending_control = Column( String( 80 ) )
	expenditure_spending_control = Column( String( 80 ) )
	expense_spending_control = Column( String( 80 ) )
	reimbursable_spending_control = Column( String( 80 ) )
	reimbursable_spending_control = Column( String( 80 ) )
	fte_budgeting_control = Column( String( 80 ) )
	fte_spending_control = Column( String( 80 ) )
	transaction_type_control = Column( String( 80 ) )
	authority_distribution_control = Column( String( 80 ) )
	
	def __init__( self, bfy: str, efy: str,
	              fund: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetControls
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'BudgetControlValuesId',
		                'Code',
		                'Name',
		                'SecurityOrg',
		                'BudgetingTransType',
		                'PostedTransType',
		                'EstimatedReimbursableTransType',
		                'SpendingAdjustmentTransType',
		                'EstimatedRecoveriesTransType',
		                'ActualRecoveriesTransType',
		                'StategicReserveTransType',
		                'ProfitLossTransType',
		                'EstimatedReimbursableSpendingOption',
		                'EstimatedReimbursableBudgetingOption',
		                'TrackAgreementLowerLevel',
		                'BudgetEstimateLowerLevel',
		                'EstimatedRecoveriesSpendingOption',
		                'EstimatedRecoveriesBudgetingOption',
		                'RecordNextLevel',
		                'RecordBudgetingMismatch',
		                'ProfitLossSpendingOption',
		                'ProfitLossBudgetingOption',
		                'RecordCarryInLowerLevel',
		                'RecordCarryInLowerLevelControl',
		                'RecordCarryInAmountControl',
		                'BudgetingControl',
		                'PostingControl',
		                'PreCommitmentSpendingControl',
		                'CommitmentSpendingControl',
		                'ObligationSpendingControl',
		                'AccrualSpendingControl',
		                'ExpenditureSpendingControl',
		                'ExpenseSpendingControl',
		                'ReimbursableSpendingControl',
		                'ReimbursableAgreementSpendingControl',
		                'FteBudgetingControl',
		                'FteSpendingControl',
		                'TransactionTypeControl',
		                'AuthorityDistributionControl' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name', 'security_org', 'posted_trans_type',
		         'estimated_reimbursements_transtype', 'spending_adjustment_transtype',
		         'estimated_recoveries_transtype', 'actual_recoveries_transtype',
		         'strategic_reserve_transtype', 'profit_loss_transtype',
		         'estimated_reimbursements_spending_option',
		         'estimated_reimbursable_budgeting_option',
		         'track_agreement_lower_level', 'budget_estimate_lower_level',
		         'estimated_recoveries_spending_option', 'estimated_recoveries_budgeting_option',
		         'record_next_level', 'record_budgeting_mismatch', 'profitloss_spending_option',
		         'profitloss_budgeting_option', 'record_carryoverin_lowerlevel',
		         'RecordCarryInLowerLevelControl', 'record_carryin_amount_control',
		         'BudgetingControl', 'PostingControl', 'PreCommitmentSpendingControl',
		         'CommitmentSpendingControl', 'ObligationSpendingControl',
		         'accrual_spending_control', 'expenditure_spending_control',
		         'expense_spending_control', 'reimbursable_spending_control',
		         'reimbursable_agreement_spending_control', 'fte_budgeting_control',
		         'fte_spending_control', 'transaction_type_control',
		         'authority_distribution_control'
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.bfy, self.efy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetControl'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetControl'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetFiscalYear( Base ):
	'''
    Constructor:
    BudgetFiscalYear( bfy, efy, date = None, pvdr = Provider.SQLite ).


    Purpose:
    Class to describe the federal fiscal year
    '''
	__tablename__ = 'BudgetFiscalYears'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	start_date = Column( String( 80 ) )
	end_date = Column( String( 80 ) )
	columbus = Column( String( 80 ) )
	christmas = Column( String( 80 ) )
	thanksgiving = Column( String( 80 ) )
	veterans = Column( String( 80 ) )
	labor = Column( String( 80 ) )
	independence = Column( String( 80 ) )
	juneteenth = Column( String( 80 ) )
	memorial = Column( String( 80 ) )
	washingtons = Column( String( 80 ) )
	martin_luther_king = Column( String( 80 ) )
	new_years = Column( String( 80 ) )
	expiring_year = Column( String( 80 ) )
	expiration_date = Column( String( 80 ) )
	cancellation_date = Column( String( 80 ) )
	workdays = Column( Float( ) )
	weekdays = Column( Float( ) )
	weekends = Column( Float( ) )
	availability = Column( Float( ) )
	
	def __init__( self, bfy: str, efy: str,
	              dt: datetime = None, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.FiscalYears
		self.bfy = bfy
		self.efy = efy
		self.today = datetime.today( )
		self.currentday = datetime.today( ).day
		self.currentmonth = datetime.today( ).month
		self.date = dt if dt is not None else datetime.today( )
		self.currentyear = datetime.today( ).year
		self.startdate = datetime( datetime.today( ).year, 10, 1 )
		self.enddate = datetime( datetime.today( ).year + 1, 9, 30 )
		self.holidays = [ 'ColumbusDay', 'VeteransDay', 'ThanksgivingDay', 'ChristmasDay',
		                  'NewYearsDay', 'MartinLutherKingDay', 'PresidentsDay',
		                  'MemorialDay', 'JuneteenthDay', 'IndependenceDay', 'LaborDay' ]
		self.fields = [ 'FiscalYearsId',
		                'BFY',
		                'EFY',
		                'StartDate',
		                'EndDate',
		                'ColumbusDay',
		                'VeteransDay',
		                'ThanksgivingDay',
		                'ChristmasDay',
		                'NewYearsDay',
		                'MartinLutherKingsDay',
		                'PresidentsDay',
		                'MemorialDay',
		                'JuneteenthDay',
		                'IndependenceDay',
		                'LaborDay',
		                'ExpiringYear',
		                'ExpirationDate',
		                'CancellationDate',
		                'Workdays',
		                'Weekdays',
		                'Weekends',
		                'Availability' ]
	
	def __str__( self ) -> str:
		if self.bfy is not None:
			return self.bfy
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'first_year', 'last_year', 'weekdays', 'weekends',
		         'today', 'date', 'current_day', 'current_month', 'current_year',
		         'start_date', 'end_date', 'holidays', 'expiring_year', 'expiration_date',
		         'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetFiscalYear'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetFiscalYear'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetObjectClass( Base ):
	'''
    Constructor:
    BudgetObjectClass( code, pvdr = Provider.SQLite  ).

    Purpose:
    Defines the BudgetObjectClass Class
    '''
	__tablename__ = 'BudgetObjectClasses'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetObjectClasses
		self.code = code
		self.fields = [ 'BudgetObjectClassesId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetObjectClass'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetObjectClass'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetaryResourceExecution( Base ):
	'''
    Constructor:
    BudgetaryResourceExecution( bfy: str, efy: str,
                                main: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the MAX A-11 DE/SF-133
    Status Of Budgetary Resources Execution Report
    '''
	__tablename__ = 'BudgetaryResourceExecution'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	
	def __init__( self, bfy: str, efy: str,
	              main: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetaryResourceExecution
		self.bfy = bfy
		self.efy = efy
		self.budgetaccountcode = main
		self.fields = [ 'BudgetaryResourceExecutionId',
		                'FiscalYear',
		                'BFY',
		                'EFY',
		                'LastUpdate',
		                'TreasurySymbol',
		                'OmbAccount',
		                'TreasuryAgencyCode',
		                'TreasuryAccountCode',
		                'STAT',
		                'CreditIndicator',
		                'LineNumber',
		                'LineDescription',
		                'SectionName',
		                'SectionNumber',
		                'LineType',
		                'FinancingAccounts',
		                'November',
		                'January',
		                'Feburary',
		                'April',
		                'May',
		                'June',
		                'August',
		                'October',
		                'Amount1',
		                'Amount2',
		                'Amount3',
		                'Amount4',
		                'Agency',
		                'Bureau' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
			_values = (self.bfy, self.efy, self.budgetaccountcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetaryResourceExecution'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetaryResourceExecution'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CongressionalControl( Base ):
	'''
    Constructor:
    CongressionalControl( bfy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defining object representing congressional control data
    '''
	__tablename__ = 'CongressionalControls'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	program_area_code = Column( String( 80 ) )
	program_area_name = Column( String( 155 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	subproject_code = Column( String( 80 ) )
	subproject_name = Column( String( 155 ) )
	reprogramming_restriction = Column( String( 80 ) )
	increase_restriction = Column( String( 80 ) )
	decrease_restriction = Column( String( 80 ) )
	memo_requirement = Column( String( 80 ) )
	
	
	def __init__( self, bfy: str = None, fundcode: str = None,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.CongressionalControls
		self.bfy = bfy
		self.fundcode = fundcode
		self.fields = [ 'CongressionalControlsId',
		                'FundCode',
		                'FundName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'SubProjectCode',
		                'SubProjectName',
		                'ReprogrammingRestriction',
		                'IncreaseRestriction',
		                'DecreaseRestriction',
		                'MemoRequirement' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'sub_project_code', 'sub_project_name',
		         'reprogramming_restriction', 'increase_restriction', 'decrease_restiction',
		         'memorandum_required', 'data', 'fields', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalControls'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalControls'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CongressionalProject( Base ):
	'''
	Constructor:
	CongressionalProjects( bfy: str, fund: str, rpio: str, ahcode: str )

	Purpose:
	Class used to allocated Earmarks
	'''
	__tablename__ = 'CongressionalProjects'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	program_area_code = Column( String( 80 ) )
	program_area_name = Column( String( 155 ) )
	state_code = Column( String( 80 ) )
	state_name = Column( String( 155 ) )
	project = Column( String( 80 ) )
	amount = Column( Float( ) )
	subappropriation_code = Column( String( 80 ) )
	main_account = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, fund: str,
	              rpio: str, ahcode: str, provider: Provider = Provider.SQLite ):
		self.source = Source.CongressionalProjects
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.rpiocode = rpio
		self.ahcode = ahcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'fund_code', 'ah_code', 'amount'
		                                 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalProjects'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalProjects'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CompassLevel( Base ):
	'''
    Constructor:
    CompassLevel( bfy: str, efy: str,
                  fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Compass data levels 1-7
    '''
	__tablename__ = 'CompassLevels'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	appropriation_code = Column( String( 80 ) )
	subappropriation_code = Column( String( 80 ) )
	appropriation_name = Column( String( 155 ) )
	treasury_symbol = Column( String( 80 ) )
	document_type = Column( String( 80 ) )
	document_date = Column( String( 80 ) )
	authority = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	recoveries = Column( Float( ) )
	reimbursements = Column( Float( ) )
	treasury_account_code = Column( Float( ) )
	treasury_account_name = Column( Float( ) )
	budget_account_code = Column( Float( ) )
	budget_account_name = Column( Float( ) )
	
	def __init__( self, bfy: str, efy: str,
	              fund: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.CompassLevels
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'CompassLevelsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'FundCode',
		                'FundName',
		                'AppropriationCode',
		                'SubAppropriationCode',
		                'AppropriationName'
		                'TreasurySymbol',
		                'DocumentType',
		                'LowerName',
		                'Description',
		                'PostedControlFlag',
		                'ActualRecoveryTransType',
		                'CommitmentSpendingControlFlag',
		                'BudgetDefault'
		                'LowerChildExpenditureSpendingControlFlag',
		                'LowerChildExpenseSpendingControlFlag',
		                'FteControlFlag',
		                'AccrualSpendingControlFlag',
		                'ObligationSpendingControlFlag',
		                'PreCommitmentSpendingControlFlag',
		                'LowerCommitmentSpendingControlFlag',
		                'LowerObligationSpendingControlFlag',
		                'LowerExpenditureSpendingControlFlag',
		                'LowerExpenseSpendingControlFlag',
		                'LowerPostedControlFlag',
		                'LowerPostedTransType',
		                'LowerTransType',
		                'LowerPostedFlag',
		                'LowerPreCommitmentSpendingControlFlag',
		                'LowerRecoveriesSpendingOption',
		                'LowerRecoveriesOption',
		                'LowerReimbursableSpendingOption',
		                'Date',
		                'TotalAuthority',
		                'OriginalAmount',
		                'CarryoverAvailabilityPercentage',
		                'CarryIn',
		                'CarryOut',
		                'FundsIn',
		                'FundOut',
		                'RecoveriesWithdrawn',
		                'ActualRecoveries',
		                'ActualReimbursements',
		                'AgreementReimbursables',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.documenttype is not None:
			return self.documenttype
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members
		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'appropriation',
		         'subappropriation_code', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.bfy, self.efy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CompassLevel'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CompassLevel'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Commitment( Base ):
	'''
    Constructor:
    Commitment( bfy: str=None, fund: str=None,
                account: str=None, boc: str=None, provider: Provider=Provider.SQLite )

    Purpose:
    Defines the CommitmentS class.
    '''
	__tablename__ = 'Commitments'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 155 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_control_number = Column( String( 80 ) )
	reference_document_number = Column( String( 80 ) )
	processed_date = Column( String( 80 ) )
	last_activity_date = Column( String( 80 ) )
	age = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 155 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	vendor_code = Column( String( 80 ) )
	vendor_name = Column( String( 155 ) )
	amount = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, efy: str, fund: str = None, account: str = None,
	              boc: str = None, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.OpenCommitments
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy )==4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund!='' else None
		self.accountcode = account if isinstance( account, str ) and account!='' else None
		self.boccode = boc if isinstance( boc, str ) and boc!='' else None
		self.fields = [ 'CommitmentsId',
		                'ObligationsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentControlNumber',
		                'ReferenceDocumentNumber',
		                'ProcessedDate',
		                'LastActivityDate',
		                'Age',
		                'BocCode',
		                'BocName',
		                'FocCode',
		                'FocName',
		                'NpmCode',
		                'NpmName',
		                'VendorCode',
		                'VendorName',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Expenditures' ]
	
	def __str__( self ) -> str:
		if isinstance( self.amount, float ):
			return str( self.amount )
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Commitment'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Commitment'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CostArea( Base ):
	'''
    Constructor:
    CostArea( fund, pvdr = Provider.SQLite )

    Purpose:
    Data class object for cost areas
    '''
	__tablename__ = 'CostAreas'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.code = code
		self.provider = provider
		self.fields = [ 'CostAreasId',
		                'Code',
		                'Name' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CostAreas'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CostAreas'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CapitalPlanningInvestmentCode( Base ):
	'''
    Constructor:
    CapitalPlanningInvestmentCodes( treas, pvdr = Provider.SQLite  )

    Purpose:
    Class eefines the CPIC Codes'''
	__tablename__ = 'CapitalPlanningInvestmentCodes'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.CapitalPlanningInvestmentCodes
		self.code = code
		self.fields = [ 'CpicId',
		                'Type'
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code!='':
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ITProjectCode'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ITProjectCode'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ColumnSchema( Base ):
	'''
    Constructor:
    ColumnSchema( column, table_name, pvdr = Provider.SQLite )

    Purpose:
    Provides data on the coolumn_names used in the application
    '''
	__tablename__ = 'ColumnSchema'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	data_type = Column( String( 80 ) )
	column_name = Column( String( 155 ) )
	table_name = Column( String( 155 ) )
	column_caption = Column( String( 155 ) )
	
	def __init__( self, column: str, table: str, provider: Provider = Provider.SQLite ):
		self.source = Source.ColumnSchema
		self.provider = provider
		self.columnname = column
		self.tablename = table
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ColumnSchema'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ColumnSchema'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class DataRuleDescription( Base ):
	'''
    Constructor:
    DataRuleDescription( schedule, line, rule, pvdr = Provider.SQLite )

    Purpose:
    Class defines object providing OMB MAX A11 rule data '''
	__tablename__ = 'DataRuleDescriptions'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	schedule = Column( String( 80 ) )
	line_number = Column( String( 80 ) )
	rule_number = Column( String( 80 ) )
	rule_description = Column( String( 80 ) )
	schedule_order = Column( String( 80 ) )
	
	
	def __init__( self, schedule: str, line: str,
	              rule: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.DataRuleDescriptions
		self.schedule = schedule
		self.linenumber = line
		self.rulenumber = rule
		self.fields = [ 'DataRuleDescriptionsId',
		                'Schedule',
		                'LineNumber',
		                'RuleNumber',
		                'RuleDescription',
		                'ScheduleOrder' ]
	
	def __str__( self ) -> str:
		if self.ruledescription is not None:
			return self.ruledescription
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Schedule', 'LineNumber', 'RuleNumber' ]
			_values = (self.schedule, self.linenumber, self.rulenumber)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'DataRuleDescription'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'DataRuleDescription'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Defacto( Base ):
	'''
    Constructor:
    Defacto(  bfy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing defacto obligations
    '''
	__tablename__ = 'Defactos'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	rc_code = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	program_area_code = Column( String( 80 ) )
	program_area_name = Column( String( 155 ) )
	rc_name = Column( String( 155 ) )
	lower_name = Column( String( 155 ) )
	amount = Column( Float( ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	open_commitments = Column( Float( ) )
	ulo = Column( Float( ) )
	expenditures = Column( Float( ) )
	obligations = Column( Float( ) )
	used = Column( Float( ) )
	available = Column( Float( ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
		self.source = Source.Defactos
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'DefactosId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'LowerName',
		                'Amount',
		                'Budgeted',
		                'Posted',
		                'OpenCommitments',
		                'UnliquidatedObligations',
		                'Expenditure',
		                'Obligations',
		                'Used',
		                'Available',
		                'NpmCode',
		                'NpmName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Defacto'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Defacto'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Deobligation( Base ):
	'''
    Constructor:
    Deobligation( bfy, fund, account, boc, pvdr = Provider.SQLite )

    Purpose:
    Class defines object providing Deobligation data
    '''
	__tablename__ = 'Deobligations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	document_number = Column( String( 80 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 155 ) )
	processed_date = Column( String( 80 ) )
	amount = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy=None, fund=None,
	              account=None, boc=None, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Deobligations
		self.bfy = bfy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'DeobligationsId',
		                'BFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'AccountCode',
		                'NpmCode',
		                'NpmName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'OrgCode',
		                'OrgName',
		                'BocCode',
		                'BocName',
		                'DocumentNumber',
		                'FocCode',
		                'FocName',
		                'ProcessedDate',
		                'Amount' ]
	
	def __str__( self ) -> str:
		if isinstance( self.amount, float ):
			return str( self.amount )
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Deobligations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Deobligations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class DocumentControlNumber( Base ):
	'''
    Constructor:
    DocumentControlNumber( dcn, pvdr = Provider.SQLite )

    Purpose:
    Class defines object provides DCN data
    '''
	__tablename__ = 'DocumentControlNumbers'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_prefix = Column( String( 80 ) )
	document_control_number = Column( String( 80 ) )
	
	
	def __init__( self, dcn: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.DocumentControlNumbers
		self.documentcontrolnumber = dcn
		self.fields = [ 'DocumentControlNumbersId',
		                'RpioCode',
		                'RpioName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentPrefix',
		                'DocumentControlNumbe' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'DocumentControlNumber', ]
			_values = (self.documentcontrolnumber,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'DocumentControlNumber'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'DocumentControlNumber'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Expenditure( Base ):
	'''
    Constructor:
    Expenditure( bfy: str, fund: str, account: str,
                 boc: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing Expenditure data
    '''
	__tablename__ = 'Expenditures'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 155 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_control_number = Column( String( 80 ) )
	reference_document_number = Column( String( 80 ) )
	processed_date = Column( String( 80 ) )
	last_activity_date = Column( String( 80 ) )
	age = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 155 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	vendor_code = Column( String( 80 ) )
	vendor_name = Column( String( 155 ) )
	amount = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, efy: str, fund: str, account: str = None,
	              boc: str = None, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Expenditures
		self.bfy = bfy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'ExpendituresId',
		                'ObligationsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentControlNumber',
		                'ReferenceDocumentNumber',
		                'ProcessedDate',
		                'LastActivityDate',
		                'Age',
		                'BocCode',
		                'BocName',
		                'FocCode',
		                'FocName',
		                'NpmCode',
		                'NpmName',
		                'VendorCode',
		                'VendorName',
		                'Amount' ]
	
	def __str__( self ) -> str:
		if self.amount is not None:
			return str( self.amount )
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Expenditure'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Expenditure'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class FinanceObjectClass( Base ):
	'''
    Constructor:
    FinanceObjectClass( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the Finance Object Class'''
	__tablename__ = 'FinanceObjectClasses'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	boc_code = Column( String( 25 ) )
	boc_name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.FinanceObjectClasses
		self.code = code
		self.fields = [ 'FinanceObjectClassesId',
		                'Code',
		                'Name',
		                'BocCode',
		                'BocName' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FinanceObjectClass'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_src = self.source
			_data = BudgetData( _src )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FinanceObjectClass'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Fund( Base ):
	'''
    Constructor:
    Fund( bfy: str, efy: str,
          code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object represening Funds
    '''
	__tablename__ = 'Funds'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	status = Column( String( 80 ) )
	short_name = Column( String( 255 ) )
	sub_level_prefix = Column( String( 80 ) )
	agency_identifier = Column( String( 80 ) )
	allocation_transfer_agency = Column( String( 80 ) )
	beginning_period_of_availability = Column( String( 80 ) )
	ending_period_of_availability = Column( String( 80 ) )
	start_date = Column( String( 80 ) )
	end_date = Column( String( 80 ) )
	multiyear_indicator = Column( String( 80 ) )
	main_account = Column( String( 80 ) )
	main_name = Column( String( 155 ) )
	subaccount = Column( String( 80 ) )
	fund_category = Column( String( 80 ) )
	appropriation_code = Column( String( 80 ) )
	subappropriation_code = Column( String( 80 ) )
	fund_group = Column( String( 80 ) )
	no_year = Column( String( 80 ) )
	carryover = Column( String( 80 ) )
	apply_at_all_levels = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	
	def __init__( self, bfy: str, efy: str, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Funds
		self.bfy = bfy
		self.efy = efy
		self.code = code
		self.fields = [ 'FundsId',
		                'BFY',
		                'EFY',
		                'Code',
		                'Name',
		                'ShortName',
		                'Status',
		                'SubLevelPrefix',
		                'ATA',
		                'BeginningPeriodOfAvailability',
		                'EndingPeriodOfAvailability',
		                'MAIN',
		                'A',
		                'AID',
		                'SUB',
		                'FundCategory',
		                'AppropriationCode',
		                'SubAppropriationCode',
		                'FundGroup',
		                'NoYear',
		                'Carryover',
		                'CancelledYearSpendingAccount',
		                'ApplyAtAllLevels',
		                'BatsFund',
		                'BatsEndDate',
		                'BatsOptionId',
		                'SecurityOrg' ]
	
	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code!='':
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'Code', ]
			_values = (self.bfy, self.efy, self.code)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Fund'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Fund'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class FederalHoliday( Base ):
	'''
    Constructor:
    FederalHoliday( bfy: str, efy: str,
                    name: str, provider: Provider=Provider.SQLite )

    Purpose:
    Defines the FederalHoliday class
    '''
	__tablename__ = 'FederalHolidays'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	columbus = Column( String( 80 ) )
	veterans = Column( String( 80 ) )
	thanksgiving = Column( String( 80 ) )
	christmas = Column( String( 80 ) )
	newyears = Column( String( 80 ) )
	martinlutherking = Column( String( 80 ) )
	washingtons = Column( String( 80 ) )
	memorial = Column( String( 80 ) )
	juneteenth = Column( String( 80 ) )
	independence = Column( String( 80 ) )
	labor = Column( String( 80 ) )
	
	
	def __init__( self, bfy: str, efy: str, name: str = '',
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.FederalHolidays
		self.holidays = [ 'ColumbusDay', 'VeteransDay', 'ThanksgivingDay', 'ChristmasDay',
		                  'NewYearsDay', 'MartinLutherKingsDay', 'PresidentsDay',
		                  'MemorialDay', 'JuneteenthDay', 'IndependenceDay', 'LaborDay' ]
		self.__observance = { 'ColumbusDay': 'The second Monday in October',
		                      'VeteransDay': 'Veterans Day, November 11',
		                      'ThanksgivingDay': 'The fourth Thursday in November',
		                      'ChristmasDay': 'Christmas Day, December 25',
		                      'NewYearsDay': 'January 1',
		                      'MartinLutherKingDay': 'The third Monday in January',
		                      'WashingtonsDay': 'The third Monday in February',
		                      'MemorialDay': 'The last Monday in May.',
		                      'JuneteenthDay': 'Juneteenth National Independence Day, June 19',
		                      'IndependenceDay': 'Independence Day, July 4',
		                      'LaborDay': 'The first Monday in September' }
		self.bfy = bfy
		self.efy = efy
		self.__year = bfy
		self.today = dt.datetime.today( )
		self.name = self.set_name( name )
		self.fields = [ 'FederalHolidaysId',
		                'BFY',
		                'ColumbusDay',
		                'VeteransDay',
		                'ThanksgivingDay',
		                'ChristmasDay',
		                'NewYearsDay',
		                'MartinLutherKingDay',
		                'PresidentsDay',
		                'MemorialDay',
		                'JuneteenthDay',
		                'IndependenceDay',
		                'LaborDay' ]
		self.data: list[ Row ] = None
		self.frame: DataFrame = None
	
	def __str__( self ) -> str:
		if not self.name=='':
			return self.name
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe',
		         'get_columbus_day', 'get_veterans_day', 'get_thanksgiving_day',
		         'get_christmas_day', 'get_newyears_day', 'get_martinlutherking_day',
		         'get_presidents_day', 'get_memorial_day', 'independence_day',
		         'labor_day', 'day_of_week', 'is_weekday', 'is_weekend', 'set_date',
		         'set_name' ]
	
	def getdata( self ) -> list:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'Name', ]
			_values = (self.bfy, self.efy, self.name,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_columbus_day( self ) -> datetime:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			if self.__year is not None:
				__start = datetime( self.__year, 10, 1 )
				__end = datetime( self.__year, 10, 31 )
				__delta = (__start - __end).days
				for i in range( 1, 31 ):
					d = datetime( self.__year, 10, __start.day + i )
					if (15 < d.day < 28) and \
							datetime( self.__year, 10, d.day ).isoweekday( )==1:
						self.__columbus = datetime( self.__year, 10, d.day )
						return self.__columbus
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_columnbus_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_veterans_day( self ) -> datetime:
		'''Veterans Day, November 11'''
		try:
			if self.__year is not None:
				self.__veterans = datetime( self.__year, 11, 11 )
				return self.__veterans
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_veterans_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_thanksgiving_day( self ) -> datetime:
		'''The fourth Thursday in November'''
		try:
			if self.__year is not None:
				__start = datetime( self.__year, 11, 15 )
				__end = datetime( self.__year, 11, 30 )
				__delta = (__start - __end).days
				for i in range( 15, 31 ):
					d = datetime( self.__year, 11, i )
					if (21 < d.day < 31) and \
							datetime( self.__year, 11, d.day ).isoweekday( )==4:
						self.__thanksgiving = datetime( self.__year, 11, d.day )
						return self.__thanksgiving
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_thanksgiving_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_christmas_day( self ) -> datetime:
		'''Christmas Day, December 25'''
		try:
			if self.__year is not None:
				self.__christmas = datetime( self.__year, 12, 25 )
				return self.__christmas
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_christmas_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_newyears_day( self ) -> datetime:
		'''January 1'''
		try:
			if self.__year is not None:
				self.newyearsday = datetime( self.__year, 1, 1 )
				return self.newyearsday
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_newyears_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_martinlutherking_day( self ) -> datetime:
		'''The third Monday in January'''
		try:
			if self.__year is not None:
				__start = datetime( self.__year, 1, 15 )
				__end = datetime( self.__year, 1, 31 )
				__delta = (__start - __end).days
				for i in range( __delta ):
					d = datetime( self.__year, 1, __start.day + i )
					if (15 < d.day < 31) and datetime( self.__year, 1, d.day ).isoweekday( )==1:
						self.__martinlutherking = datetime( self.__year, 1, d.day )
						return self.__martinlutherking
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_martinlutherking_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_presidents_day( self ) -> datetime:
		'''The third Monday in February'''
		try:
			if self.__year is not None:
				__start = datetime( self.__year, 2, 15 )
				__end = datetime( self.__year, 2, 28 )
				__delta = (__start - __end).days
				for i in range( __delta ):
					d = datetime( self.__year, 2, __start.day + i )
					if (15 < d.day < 28) and datetime( self.__year, 2, d.day ).isoweekday( )==1:
						self.__washingtons = datetime( self.__year, 2, d.day )
						return self.__washingtons
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_presidents_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_memorial_day( self ) -> datetime:
		'''The last Monday in May'''
		try:
			if self.__year is not None:
				__start = datetime( self.__year, 5, 1 )
				__end = datetime( self.__year, 5, 31 )
				__delta = (__start - __end).days
				for i in range( 15, 31 ):
					d = datetime( self.__year, 5, i )
					if (21 < d.day < 31) and datetime( self.__year, 5, d.day ).isoweekday( )==1:
						self.__memorial = datetime( self.__year, 5, d.day )
						return self.__memorial
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_memorial_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_juneteenth_day( self ) -> datetime:
		'''Juneteenth National Independence Day, June 19'''
		try:
			if self.__year is not None:
				self.uneteenth = datetime( self.__year, 6, 19 )
				return self.uneteenth
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_juneteenth_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_independence_day( self ) -> datetime:
		'''Independence Day, July 4'''
		try:
			if self.__year is not None:
				self.__independence = datetime( self.__year, 7, 4 )
				return self.__independence
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_independence_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def get_labor_day( self ) -> datetime:
		'''The first Monday in September'''
		try:
			if self.__year is not None:
				__monday = list( )
				__month = dt.date( self.__year, 9, 1 ) - dt.date( self.__year, 9, 31 )
				for i in range( 1, __month.days - 1 ):
					if datetime( self.__year, 9, i ).isoweekday( )==1:
						__monday.append( datetime( self.__year, 9, i ) )
				y = __monday[ 0 ].date( ).year
				m = __monday[ 0 ].date( ).month
				d = __monday[ 0 ].date( ).day
				self.__labor = datetime( y, m, d )
				return self.__labor
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_labor_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def day_of_week( self ) -> str:
		try:
			if 0 < self.__day < 8 and self.__day==1:
				self.dayofweek = 'Monday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day==2:
				self.dayofweek = 'Tuesday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day==3:
				self.dayofweek = 'Wednesday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day==4:
				self.dayofweek = 'Thursday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day==5:
				self.dayofweek = 'Friday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day==6:
				self.dayofweek = 'Saturday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day==7:
				self.dayofweek = 'Sunday'
				return self.dayofweek
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'day_of_week( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def is_weekday( self ) -> bool:
		try:
			if 1 <= self.date.isoweekday( ) <= 5:
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'is_weekday( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def is_weekend( self ) -> bool:
		try:
			if 5 < self.date.isoweekday( ) <= 7:
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'is_weekend( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def set_date( self, name: str ):
		try:
			if isinstance( name, str ) and name in self.holidays:
				if name=='ColumbusDay':
					self.date = self.get_columbus_day( )
					return self.date
				elif name=='VeteransDay':
					self.date = self.get_veterans_day( )
					return self.date
				elif name=='ThanksgivingDay':
					self.date = self.get_thanksgiving_day( )
					return self.date
				elif name=='ChristmasDay':
					self.date = self.get_christmas_day( )
					return self.date
				elif name=='NewYearsDay':
					self.date = self.get_newyears_day( )
					return self.date
				elif name=='MartinLutherKingDay':
					self.date = self.get_martinlutherking_day( )
					return self.date
				elif name=='PresidentsDay':
					self.date = self.get_presidents_day( )
					return self.date
				elif name=='MemorialDay':
					self.date = self.get_memorial_day( )
					return self.date
				elif name=='JuneteenthDay':
					self.date = self.get_juneteenth_day( )
					return self.date
				elif name=='LaborDay':
					self.date = self.get_labor_day( )
					return self.date
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'set_date( self, value )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def set_name( self, name: str ):
		try:
			if isinstance( name, str ) and name in self.holidays:
				self.name = name
				return self.name
			else:
				self.name = 'NS'
				return self.name
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'set_name( self, value  ) '
			_err = ErrorDialog( _exc )
			_err.show( )

class FullTimeEquivalent( Base ):
	'''

    Constructor: FullTimeEquivalent( bfy: str, fund: str,
        provider: Provider=Provider.SQLite )

    Purpose:  Object representing Operating Plan FTE

    '''
	__tablename__ = 'FullTimeEquivalents'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	amount = Column( 'Amount', String( 80 ) )
	activity_code = Column( 'ActivityCode', String( 80 ) )
	activity_name = Column( 'ActivityName', String( 80 ) )
	goal_code = Column( 'GoalCode', String( 25 ) )
	goal_name = Column( 'GoalName', String( 255 ) )
	objective_code = Column( 'ObjectiveCode', String( 25 ) )
	objective_name = Column( 'ObjectiveName', String( 255 ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	
	def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.FullTimeEquivalents
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'FullTimeEquivalentsId',
		                'OperatingPlansId',
		                'RpioCode',
		                'RpioName',
		                'BFY',
		                'EFY',
		                'AhCode',
		                'FundCode',
		                'OrgCode',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'Amount',
		                'ITProjectCode',
		                'ProjectCode',
		                'ProjectName',
		                'NpmCode',
		                'ProjectTypeName',
		                'ProjectTypeCode',
		                'ProgramProjectCode',
		                'ProgramAreaCode',
		                'NpmName',
		                'AhName',
		                'FundName',
		                'OrgName',
		                'RcName',
		                'ProgramProjectName',
		                'ActivityCode',
		                'ActivityName',
		                'LocalCode',
		                'LocalCodeName',
		                'ProgramAreaName',
		                'CostAreaCode',
		                'CostAreaName',
		                'GoalCode',
		                'GoalName',
		                'ObjectiveCode',
		                'ObjectiveName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name', 'account_code',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'amount', 'npm_code', 'npm_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FullTimeEquivalent'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FullTimeEquivalent'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class GeneralLedgerAccount( Base ):
	'''
    Constructor:
    GeneralLedgerAccount( bfy: str, number: str,
        provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object representing General Ledger Accounts
    '''
	__tablename__ = 'GeneralLedgerAccounts'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	treasury_symbol = Column( String( 80 ) )
	account_number = Column( String( 80 ) )
	account_name = Column( String( 155 ) )
	beginning_balance = Column( Float( ) )
	credit_balance = Column( Float( ) )
	debit_balance = Column( Float( ) )
	closing_amount = Column( Float( ) )
	
	
	def __init__( self, bfy: str, number: str, provider: Provider = Provider.SQLite ):
		self.bfy = bfy
		self.accountnumber = number
		self.provider = provider
		self.source = Source.GeneralLedgerAccounts
		self.fields = [ 'GeneralLedgerAccountsId',
		                'BFY',
		                'EFY',
		                'FundCode',
		                'FundName',
		                'TreasurySymbol',
		                'AccountNumber',
		                'AccountName',
		                'BeginningBalance',
		                'CreditBalance',
		                'DebitBalance',
		                'ClosingAmount' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'GeneralLedgerAccounts'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'GeneralLedgerAccounts'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Goal( Base ):
	'''
    Constructor:
    Goal( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing EPA  Goals
    '''
	__tablename__ = 'Goals'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Goals
		self.code = code
		self.fields = [ 'GoalsId',
		                'Code',
		                'Name',
		                'Title' ]
	
	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code!='':
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Goals'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Goals'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class HeadquartersAuthority( Base ):
	'''
    Constructor:
    HeadquartersAuthority( bfy, rpio, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing HQ Allocation
    '''
	__tablename__ = 'HeadquartersAuthority'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	status_of_funds_id = Column( Integer( ) )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, rpio: str, provider: Provider = Provider.SQLite ):
		self.source = Source.HeadquartersAuthority
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.rpiocode = rpio
		self.fields = [ 'HeadquartersAuthorityId',
		                'AllocationsId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'BocCode',
		                'BocName',
		                'Amount',
		                'NpmCode',
		                'NpmName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = (self.bfy, self.rpiocode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersAuthority'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersAuthority'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class HeadquartersOffice( Base ):
	'''
    Constructor:
    HeadquartersOffice( code: str, provider: Provider=Provider.SQLite )

    Prupose:
    Class defines object representing RPIO'''
	__tablename__ = 'HeadquartersOffices'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.rpiocode = code
		self.provider = provider
		self.source = Source.HeadquartersOffices
		self.fields = [ 'HeadquartersOfficesId',
		                'ResourcePlanningOfficesId',
		                'RpioCode',
		                'RpioName' ]
	
	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'rpio_code', 'rpio_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'RpioCode', ]
			_values = (self.rpiocode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersOffice'
			_exc.method = 'getdata( self ) '
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersOffice'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class InflationReductionActCarryoverEstimate( Base ):
	'''
    Constructor:
    InflationReductionActCarryoverEstimate( bfy: str,
        provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing IRA Carryover Estimates
    '''
	__tablename__ = 'InflationReductionActCarryoverEstimates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	treasury_account_code = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	amount = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	available = Column( Float( ) )
	estimate = Column( Float( ) )
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.AnnualCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'AnnualCarryoverEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'rpio_code', 'rpio_name',
		         'fund_code', 'fund_name', 'amount', 'available',
		         'open_commitments', 'obligations', 'main_account',
		         'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class JobsActCarryoverEstimate( Base ):
	'''

    Constructor:
    JobsActCarryoverEstimate( bfy )

    Purpose:
    Class defines object providing IIJA Carryover Estimate data for

    '''
	__tablename__ = 'JobsActCarryoverEstimates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.JobsActCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'CarryoverEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MainAccount( Base ):
	'''
	Constructor:
	MainAccounts( bfy: str, code: str )

	Purpose:
	class models the OMB Budget Account
	'''
	__tablename__ = 'MainAccounts'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.code = code
		self.provider = provider
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'subfunction_code', 'subfunction_name',
		         'budget_enforcement_act_category',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'MainAccounts'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'MainAccounts'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MonthlyActual( Base ):
	'''
    Constructor:
    Actual( bfy = None, fund = None, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing expenditure data
    '''
	__tablename__ = 'MonthlyActuals'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	appropriation_code = Column( String( 80 ) )
	appropriation_name = Column( String( 155 ) )
	subappropriation_code = Column( String( 80 ) )
	subappropriation_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	activity_code = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	obligations = Column( Float( ) )
	gross_outlays = Column( Float( ) )
	net_outlays = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str = None, fund: str = None,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.MonthlyActuals
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy )==4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund!='' else None
		self.fields = [ 'ActualsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'AppropriationCode',
		                'AppropriationName',
		                'SubAppropriationCode',
		                'SubAppropriationName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RpioActivityCode',
		                'RpioActivityName',
		                'BocCode',
		                'BocName',
		                'UnliquidatedObligations',
		                'Obligations',
		                'Balance',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'GoalCode',
		                'GoalName',
		                'ObjectiveCode',
		                'ObjectiveName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members
		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'program_project_code',
		         'program_project_name', 'npm_code', 'npm_name',
		         'goal_code', 'goal_name',
		         'gross_outlays', 'net_outlays', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MonthlyOutlay( Base ):
	'''
    Constructor:
    MonthlyOutlay( bfy, efy, main )

    Purpose:
    Class defines object providing OMB outlay data
    '''
	__tablename__ = ' MonthlyOutlays'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	agency_title = Column( String( 80 ) )
	bureau_title = Column( String( 80 ) )
	omb_account_title = Column( String( 80 ) )
	treasury_account_title = Column( String( 80 ) )
	october = Column( Float( ) )
	november = Column( Float( ) )
	december = Column( Float( ) )
	january = Column( Float( ) )
	feburary = Column( Float( ) )
	march = Column( Float( ) )
	april = Column( Float( ) )
	may = Column( Float( ) )
	june = Column( Float( ) )
	july = Column( Float( ) )
	august = Column( Float( ) )
	september = Column( Float( ) )
	
	def __init__( self, bfy, efy, account, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.MonthlyOutlays
		self.bfy = bfy
		self.efy = efy
		self.budgetaccountcode = account
		self.fields = [ 'MonthlyOutlaysId',
		                'FiscalYear',
		                'LineNumber',
		                'LineTitle',
		                'TaxationCode',
		                'TreasuryAgency',
		                'TreasuryAccount',
		                'SubAccount',
		                'BFY',
		                'EFY',
		                'OmbAgency',
		                'OmbBureau',
		                'OmbAccount',
		                'AgencySequence',
		                'BureauSequence',
		                'AccountSequence',
		                'AgencyTitle',
		                'BureauTitle',
		                'OmbAccountTitle',
		                'TreasuryAccountTitle',
		                'October',
		                'November',
		                'December',
		                'January',
		                'Feburary',
		                'March',
		                'April',
		                'May',
		                'June',
		                'July',
		                'August',
		                'September' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'line_number', 'line_name', 'bfy', 'efy',
		         'fund_code', 'fund_name', 'taxation_code',
		         'treasury_agency_code', 'january',
		         'feburary', 'march', 'april',
		         'may', 'june', 'july', 'august',
		         'september', 'october', 'november',
		         'january', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
			_values = (self.bfy, self.efy, self.budgetaccountcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'MonthlyOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'MonthlyOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class NationalProgram( Base ):
	'''
    Constructor:
    NationalProgram( code: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing the NationalProgram Class'''
	__tablename__ = 'NationalPrograms'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.NationalPrograms
		self.code = code
		self.fields = [ 'NationalProgramsId',
		                'Code',
		                'Name',
		                'RpioCode',
		                'Title' ]
	
	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code!='':
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'NationalProgram'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'NationalProgram'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Objective( Base ):
	'''
    Constructor:
    Objective( code: str, provider: Provider=Provider.SQLite )


    Purpose:
    Class defines object representing the Objective Class
    '''
	__tablename__ = 'Objectives'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Objectives
		self.code = code
		self.fields = [ 'ObjectivesId',
		                'Code',
		                'Name',
		                'Title' ]
	
	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code!='':
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = Source.Objectives
			_provider = Provider.SQLite
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Objective'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Objective'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Organization( Base ):
	'''
    Constructor:
    Organization( code: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object representing the Organization Codes'''
	__tablename__ = 'Organizations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Organizations
		self.code = code
		self.fields = [ 'OrganizationsId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = (self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Organizations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Organizations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class OperatingPlan( Base ):
	'''
    Constructor:
    OperatingPlan( bfy, efy, treas, pvdr = Provider.SQLite )

    Purpose:
    Class defining object representing Operating plan allocations
    '''
	__tablename__ = 'OperatingPlans'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	ah_code = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	amount = Column( Float( ) )
	npm_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_area_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	ah_name = Column( String( 155 ) )
	fund_name = Column( String( 155 ) )
	org_name = Column( String( 155 ) )
	program_project_name = Column( String( 155 ) )
	activitycode = Column( String( 80 ) )
	activityname = Column( String( 80 ) )
	program_area_name = Column( String( 155 ) )
	goal_code = Column( String( 80 ) )
	goal_name = Column( String( 155 ) )
	objective_code = Column( String( 80 ) )
	objective_name = Column( String( 155 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	version = Column( String( 80 ) )
	
	
	def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
		self.source = Source.OperatingPlans
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
		                'FundCode', 'OrgCode', 'AccountCode', 'RcCode', 'BocCode', 'BocName',
		                'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
		                'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode',
		                'ProgramAreaCode',
		                'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName',
		                'ProgramProjectName',
		                'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName',
		                'ProgramAreaName',
		                'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
		                'ObjectiveCode', 'ObjectiveName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name', 'amount',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( self.source, self.provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OperatingPlan'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OperatingPlan'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class OpenCommitment( Base ):
	'''
    Constructor:
    OpenCommitment( bfy: str, efy: str, fund: str,
                  account: str, boc: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing OpenCommitment data.
    '''
	__tablename__ = 'OpenCommitments'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 155 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 155 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_control_number = Column( String( 80 ) )
	reference_document_number = Column( String( 80 ) )
	processed_date = Column( String( 80 ) )
	last_activity_date = Column( String( 80 ) )
	age = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 155 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 155 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 155 ) )
	vendor_code = Column( String( 80 ) )
	vendor_name = Column( String( 155 ) )
	amount = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 155 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, efy: str, fund: str,
	              account: str, boc: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.OpenCommitments
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'OpenCommitmentsId',
		                'ObligationsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentControlNumber',
		                'ReferenceDocumentNumber',
		                'ProcessedDate',
		                'LastActivityDate',
		                'Age',
		                'BocCode',
		                'BocName',
		                'FocCode',
		                'FocName',
		                'NpmCode',
		                'NpmName',
		                'VendorCode',
		                'VendorName',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Expenditures' ]
	
	def __str__( self ) -> str:
		if self.accountcode is not None:
			return self.accountcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OpenCommitment'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OpenCommitment'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Obligation( Base ):
	'''
    Constructor:  Obligation( bfy: str, efy: str, fund: str,
                  account: str, boc: str, provider: Provider=Provider.SQLite )

    Purpose:  Class defines object providing Obligation data'''
	__tablename__ = 'Obligations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 80 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 80 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_control_number = Column( String( 80 ) )
	reference_document_number = Column( String( 80 ) )
	processed_date = Column( String( 80 ) )
	last_activity_date = Column( String( 80 ) )
	age = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 80 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 80 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 80 ) )
	vendor_code = Column( String( 80 ) )
	vendor_name = Column( String( 80 ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	ulo = Column( Float( ) )
	expenditures = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 80 ) )
	
	def __init__( self, bfy: str, efy: str, fund: str,
	              account: str = None, boc: str = None, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Obligations
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'ObligationsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentControlNumber',
		                'ReferenceDocumentNumber',
		                'ProcessedDate',
		                'LastActivityDate',
		                'Age',
		                'BocCode',
		                'BocName',
		                'FocCode',
		                'FocName',
		                'NpmCode',
		                'NpmName',
		                'VendorCode',
		                'VendorName',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Expenditures' ]
	
	def __str__( self ) -> str:
		if self.amount is not None:
			return str( self.amount )
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Obligaions'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Obligation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class OutlayRate( Base ):
	'''
    Constructor:
        Outlay( account: str, provider: Provider=Provider.SQLite  )

    Purpose:
	    Class defines object that provides OMB data
    '''
	__tablename__ = 'OutlayRates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	fiscal_year = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 80 ) )
	category = Column( String( 80 ) )
	baseline = Column( String( 80 ) )
	year1 = Column( Float( ) )
	year2 = Column( Float( ) )
	year3 = Column( Float( ) )
	year4 = Column( Float( ) )
	year5 = Column( Float( ) )
	year6 = Column( Float( ) )
	year7 = Column( Float( ) )
	year8 = Column( Float( ) )
	year9 = Column( Float( ) )
	year10 = Column( Float( ) )
	year11 = Column( Float( ) )
	
	def __init__( self, account: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Outlays
		self.budgetaccountcode = account
		self.fields = [ 'BudgetOutlaysId',
		                'ReportYear',
		                'Category',
		                'AgencyName',
		                'LineNumber',
		                'LineSection',
		                'OmbAccount',
		                'LineTitle',
		                'AccountType',
		                'AuthorityTypeName',
		                'Line',
		                'AuthorityType',
		                'PriorYear',
		                'CurrentYear',
		                'BudgetYear',
		                'BudgetYear1',
		                'BudgetYear2',
		                'BudgetYear3',
		                'BudgetYear4',
		                'BudgetYear5',
		                'BudgetYear6',
		                'BudgetYear7',
		                'BudgetYear8',
		                'BudgetYear9' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'report_year', 'line_number',
		         'line_section', 'line_name', 'line_category',
		         'bea_category', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'prior_year', 'current_year', 'budget_year', 'out_year_1', 'out_year_2',
		         'out_year_3', 'out_year_4', 'out_year_5', 'out_year_6', 'out_year_7',
		         'out_year_8', 'out_year_9',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'OmbAccountCode', ]
			_values = (self.budgetaccountcode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetOutlay'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class PublicLaw( Base ):
	'''
    Constructor: PublicLaw( bfy: str, efy: str,
                  number: str, provider: Provider=Provider.SQLite  )

    Purpose:
    '''
	__tablename__ = 'PublicLaws'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	
	def __init__( self, bfy: str, efy: str,
	              number: str, provider: Provider = Provider.SQLite ):
		self.bfy = bfy
		self.efy = efy
		self.lawnumber = number
		self.provider = provider
		self.source = Source.PublicLaws
		self.fields = [ 'PublicLawsId',
		                'LawNumber',
		                'BillTitle',
		                'EnactedDate',
		                'Congress',
		                'BFY' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = (self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'PublicLaws'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'PublicLaws'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Project( Base ):
	'''
    Constructor:  Project( code: str, provider: Provider=Provider.SQLite )

    Purpoe:  Class defines the Organization Class'''
	__tablename__ = 'Projects'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Projects
		self.code = code
		self.fields = [ 'ProjectId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Project'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Project'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProgramArea( Base ):
	'''
    Constructor:   ProgramArea( code: str, provider: Provider=Provider.SQLite  )

    Purpose:  defines the ProgramArea class
    '''
	__tablename__ = 'ProgramAreas'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ProgramAreas
		self.code = code
		self.fields = [ 'ProgramAreasId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramArea'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramArea'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProgramProject( Base ):
	'''
    Constructor:  ProgramProject( code: str, provider: Provider=Provider.SQLite )

    Purpose:  Defines the ProgramProject Class
    '''
	__tablename__ = 'ProgramProjects'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ProgramProjects
		self.code = code
		self.fields = [ 'ProgramProjectsId',
		                'Code',
		                'Name',
		                'ProgramAreaCode',
		                'ProgramAreaName' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = (self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramProjects'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramProjects'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProgramResultsCode( Base ):
	'''
    Constructor:   ProgramResultsCode( bfy: str=None, efy: str=None, fund: str=None,
                  rpio: str=None, ah: str=None, account: str=None, boc: str=None,
                  amount: float = 0.0, provider: Provider=Provider.SQLite )

    Purpose:  Class defines the PRCs
    '''
	__tablename__ = 'ProgramResultsCodes'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	def __init__( self, bfy: str = None, efy: str = None, fund: str = None,
	              rpio: str = None, ah: str = None, account: str = None, boc: str = None,
	              amount: float = 0.0, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Allocations
		self.accountcode = account
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.rpiocode = rpio
		self.ahcode = ah
		self.boccode = boc
		self.amount = amount
		self.fields = [ 'AllocationsId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'Amount',
		                'ActivityCode',
		                'ActivityName',
		                'NpmCode',
		                'NpmName',
		                'ObjectiveCode',
		                'ObjectiveName',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'activity_code', 'activity_name',
		         'amount', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = (self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramResultsCode'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramResultsCode'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ReportingLine( Base ):
	'''
	Constructor:
	ReportingLines( bfy: str, code: str )

	Purpose:
	class models the lines on the SF-133 and SF-132
	'''
	__tablename__ = 'ReportingLines'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	
	def __init__( self, bfy: str, code: str, provider: Provider = Provider.SQLite ):
		self.bfy = bfy
		self.code = code
		self.provider = provider
		self.source = Source.ReportingLines
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ReportingLines'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ReportingLines'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ResponsibilityCenter( Base ):
	'''
    Constructor:
    ResponsibilityCenter( code: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines the ResponsibilityCenter Class
    '''
	__tablename__ = 'ResponsibilityCenters'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ResponsibilityCenters
		self.code = code if isinstance( code, str ) else None
		self.fields = [ 'ResponsibilityCentersId',
		                'Code',
		                'Name',
		                'Title' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ tuple ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResponsibilityCenter'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResponsibilityCenter'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ResourcePlanningOffice( Base ):
	'''
    Constuctor:
    ResourcePlanningOffice( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Defines the ResponsiblePlanningOffice class
    '''
	__tablename__ = 'ResourcePlanningOffices'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ResourcePlanningOffices
		self.code = code
		self.fields = [ 'ResourcePlanningOfficesId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResourcePlanningOffice'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResourcePlanningOffice'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class RegionalOffice( Base ):
	'''
    Constructor:
    RegionalOffice( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Defines a regional RPIO
    '''
	__tablename__ = 'RegionalOffices'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ResourcePlanningOffices
		self.rpiocode = code
		self.fields = [ 'RegionalOfficesId',
		                'ResourcePlanningOfficesId',
		                'RpioCode',
		                'RpioName' ]
	
	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'rpio_code', 'rpio_name', 'fields',
		         'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.rpiocode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'RegionalOffice'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ReimbursableAgreement( Base ):
	'''
    Constructor:
    ReimbursableAgreement( number: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object representing Reimbursable Agreements
    '''
	__tablename__ = 'ReimbursableAgreements'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	rpio = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	agreement_number = Column( String( 80 ) )
	start_date = Column( String( 80 ) )
	end_date = Column( String( 80 ) )
	rc_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	division_name = Column( String( 80 ) )
	site_project_code = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	vendor_code = Column( String( 80 ) )
	vendor_name = Column( String( 80 ) )
	amount = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	ulo = Column( Float( ) )
	available = Column( Float( ) )
	
	def __init__( self, number: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.ReimbursableAgreements
		self.__agreementnumber = number
		self.fields = [ 'ReimbursableAgreementsId'
		                'BFY',
		                'EFY',
		                'FundCode',
		                'RpioCode',
		                'AgreementNumber',
		                'StartDate',
		                'EndDate',
		                'RcCode',
		                'RcName',
		                'OrgCode',
		                'SiteProjectCode',
		                'AccountCode',
		                'VendorCode',
		                'VendorName',
		                'Amount',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Available' ]
	
	def __str__( self ) -> str:
		if self.__agreementnumber is not None:
			return self.__agreementnumber
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', ]
			_values = (self.bfy,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'ObjectClassOutlay'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'ObjectClassOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class RegionalAuthority( Base ):
	'''
    Constructor:
    RegionalAuthority( bfy: str, efy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Regional Allocation
    '''
	__tablename__ = 'RegionalAuthority'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	status_of_funds_id = Column( Integer( ) )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fund: str,
	              provider: Provider = Provider.SQLite ):
		self.source = Source.RegionalAuthority
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'RegionalAuthorityId',
		                'AllocationsId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'BocCode',
		                'BocName',
		                'Amount',
		                'NpmCode',
		                'NpmName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = (self.bfy, self.rpiocode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'RegionalAuthority'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'RegionalAuthority'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfFunds( Base ):
	'''
    Constructor:
    StatusOfFunds( bfy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing execution data
    '''
	__tablename__ = 'StatusOfFunds'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	unliquidated_obligations = Column( Float( ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
		self.source = Source.StatusOfFunds
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'LowerName',
		                'Amount',
		                'Budgeted',
		                'Posted',
		                'OpenCommitments',
		                'UnliquidatedObligations',
		                'Expenditure',
		                'Obligations',
		                'Used',
		                'Available',
		                'NpmCode',
		                'NpmName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfFunds'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfFunds'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfBudgetaryResources( Base ):
	'''
    Constructor:
    StatusOfBudgetaryResources( tsym: str )

    Purpose:
    Class representing the Monthly SF-133
    '''
	__tablename__ = 'StatusOfBudgetaryResources'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	last_update = Column( String( 80 ) )
	budget_account_name = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 80 ) )
	beginning_period_of_availability = Column( String( 80 ) )
	ending_period_of_availability = Column( String( 80 ) )
	section_number = Column( String( 80 ) )
	section_name = Column( String( 80 ) )
	line_number = Column( String( 80 ) )
	line_name = Column( String( 80 ) )
	line_type = Column( String( 80 ) )
	november = Column( Float( ) )
	december = Column( Float( ) )
	january = Column( Float( ) )
	feburary = Column( Float( ) )
	april = Column( Float( ) )
	may = Column( Float( ) )
	june = Column( Float( ) )
	august = Column( Float( ) )
	september = Column( Float( ) )
	october = Column( Float( ) )
	last_update = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 80 ) )
	budget_account_name = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	beginning_period_of_availability = Column( String( 80 ) )
	ending_period_of_availability = Column( String( 80 ) )
	section_number = Column( String( 80 ) )
	section_name = Column( String( 80 ) )
	line_number = Column( String( 80 ) )
	line_name = Column( String( 80 ) )
	november = Column( Float( ) )
	december = Column( Float( ) )
	january = Column( Float( ) )
	feburary = Column( Float( ) )
	march = Column( Float( ) )
	may = Column( Float( ) )
	june = Column( Float( ) )
	july = Column( Float( ) )
	august = Column( Float( ) )
	september = Column( Float( ) )
	october = Column( Float( ) )
	last_update = Column( String( 80 ) )
	
	def __init__( self, year: str, account: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfBudgetaryResources
		self.fiscalyear = year
		self.budgetaccountcode = account
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fiscal_year', 'bfy', 'efy',
		         'fund_code', 'fund_name', 'begging_period_availability',
		         'ending_period_availability', 'january',
		         'feburary', 'march', 'april',
		         'may', 'june', 'july', 'august',
		         'september', 'october', 'november',
		         'january', 'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetaryResources'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetaryResources'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfBudgetExecution( Base ):
	'''
    Constructor:
    StatusOfBudgetaryResources( tsym: str )

    Purpose:
    Class representing the Monthly SF-133
    '''
	__tablename__ = 'StatusOfBudgetExecution'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	linecaption = Column( String( 80 ) )
	line_name = Column( String( 80 ) )
	line_number = Column( String( 80 ) )
	amount = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 80 ) )
	
	def __init__( self, account: str, provider: Provider = Provider.SQLite ):
		self.source = Source.StatusOfBudgetExecution
		self.treasuryaccountcode = account
		self.provider = provider
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fiscal_year', 'bfy', 'efy',
		         'section_name', 'section_number', 'line_number',
		         'amount', 'treasury_account_code', 'treasury_account_name',
		         'budget_accocunt_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetExecution'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:  Method returning pandas dataframe
        comprised of datatable data


        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetExecution'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StateGrantObligations( Base ):
	'''
    Constructor:
    StateGrantObligation( bfy: str, rpio: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the BIS
    '''
	__tablename__ = 'StatusOfGrantObligations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 80 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 80 ) )
	state_code = Column( String( 80 ) )
	state_name = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 80 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 80 ) )
	amount = Column( Float( ) )
	
	def __init__( self, bfy: str, rpio: str, provider: Provider = Provider.SQLite ):
		self.source = Source.StateGrantObligations
		self.provider = provider
		self.bfy = bfy
		self.rpiocode = rpio
		self.fields = [ 'StateGrantObligationsId',
		                'RpioCode',
		                'RpioName',
		                'FundCode',
		                'FundName',
		                'AhCode',
		                'AhName',
		                'OrgCode',
		                'OrgName',
		                'StateCode',
		                'StateName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'BocCode',
		                'BocName',
		                'Amount' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = (self.rpiocode, self.rpiocode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateGrantObligation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateGrantObligation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSpecialAccountFunds( Base ):
	'''
     Constructor:
     StatusOfSpecialAccountFunds( bfy = None, fund = None,
                                 account = None, boc = None, pvdr = Provider.SQLite )

     Purpose:
     Class defines object providing SF Special Account data
     '''
	__tablename__ = 'StatusOfSpecialAccountFunds'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	special_account_fund = Column( String( 80 ) )
	special_account_number = Column( String( 80 ) )
	special_account_name = Column( String( 80 ) )
	account_status = Column( String( 80 ) )
	npl_status_code = Column( String( 80 ) )
	npl_status_name = Column( String( 80 ) )
	site_code = Column( String( 80 ) )
	site_name = Column( String( 80 ) )
	operable_unit = Column( String( 80 ) )
	pipeline_code = Column( String( 80 ) )
	pipeline_description = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 80 ) )
	transaction_type = Column( String( 80 ) )
	transaction_typename = Column( String( 80 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 80 ) )
	transaction_date = Column( String( 80 ) )
	available_balance = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	ulo = Column( Float( ) )
	disbursements = Column( Float( ) )
	unpaid_balances = Column( Float( ) )
	collections = Column( Float( ) )
	cumulative_receipts = Column( Float( ) )
	
	
	def __init__( self, bfy=None, fund=None, account=None,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfSpecialAccountFunds
		self.bfy = bfy
		self.fundcode = fund
		self.__programcode = account
		self.fields = [ 'SpecialAccountsId',
		                'BFY',
		                'RpioCode',
		                'FundCode',
		                'SpecialAccountFund',
		                'SpecialAccountNumber',
		                'SpecialAccountName',
		                'AccountStatus',
		                'NplStatusCode',
		                'NplStatusName',
		                'SiteId',
		                'CerclisId',
		                'SiteCode',
		                'SiteName',
		                'OperableUnit',
		                'PipelineCode',
		                'PipelineDescription',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'TransactionType',
		                'TransactionTypeName',
		                'FocCode',
		                'FocName',
		                'TransactionDate',
		                'AvailableBalance',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Disbursements',
		                'UnpaidBalances',
		                'Collections',
		                'CumulativeReceipts' ]
	
	def __str__( self ) -> str:
		if self.__sitecode is not None:
			return self.__sitecode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.__programcode, self.__interestdate)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSpecialAccountFunds'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSpecialAccountFunds'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SubAppropriation( Base ):
	'''

    Constructor:
    SubAppropriation( bfy: str, efy: str, code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the Sub-Appropriations

    '''
	__tablename__ = 'SubAppropriations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, efy: str, code: str,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Appropriations
		self.bfy = bfy
		self.efy = efy
		self.code = code
		self.fields = [ 'SubAppropriationsId',
		                'Code',
		                'Name' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'SubAppropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StateOrganization( Base ):
	'''
    Constructor:
    StateOrganization( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing state organization codes
    '''
	__tablename__ = 'StateOrganizations'
	id = Column( Integer( ), primary_key=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, code: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.StateOrganizations
		self.code = code
		self.fields = [ 'StateOrganizationsId',
		                'Name',
		                'Code',
		                'RpioName',
		                'RpioCode' ]
	
	def __str__( self ) -> str:
		if self.code is not None:
			return self.code
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = (self.code,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateOrganization'
			_exc.method = 'getdata( self ) '
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateOrganization'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfAppropriations( Base ):
	'''
    Constructor:
    StatusOfAppropriations( bfy: str, efy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Appropriation-level execution data
    '''
	__tablename__ = 'StatusOfAppropriations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	budget_level = Column( String( 80 ) )
	appropriation_fund_code = Column( String( 80 ) )
	appropriation_fund_name = Column( String( 80 ) )
	availability = Column( String( 80 ) )
	treasury_symbol = Column( String( 80 ) )
	appropriation_creation_date = Column( String( 80 ) )
	appropriation_code = Column( String( 80 ) )
	subappropriation_code = Column( String( 80 ) )
	appropriation_description = Column( String( 80 ) )
	fund_group = Column( String( 80 ) )
	fund_group_name = Column( String( 80 ) )
	document_type = Column( String( 80 ) )
	transtype = Column( String( 80 ) )
	actual_recovery_transtype = Column( String( 80 ) )
	commitment_spending_controlflag = Column( String( 80 ) )
	agreement_limit = Column( String( 80 ) )
	estimated_recoveries_transtype = Column( String( 80 ) )
	reimbursment_transtype = Column( String( 80 ) )
	expense_spending_controlflag = Column( String( 80 ) )
	obligation_spending_controlflag = Column( String( 80 ) )
	precommitment_spending_controlflag = Column( String( 80 ) )
	posted_control_flag = Column( String( 80 ) )
	posted_flag = Column( String( 80 ) )
	record_carryover_lower_level = Column( String( 80 ) )
	reimbursable_spending_option = Column( String( 80 ) )
	recoveries_option = Column( String( 80 ) )
	recoveries_spending_option = Column( String( 80 ) )
	original_budgeted_amount = Column( Float( ) )
	apportionments_posted = Column( Float( ) )
	total_authority = Column( Float( ) )
	total_budgeted = Column( Float( ) )
	total_posted_amount = Column( Float( ) )
	funds_withdrawn_amount = Column( Float( ) )
	funding_in_amount = Column( Float( ) )
	funding_out_amount = Column( Float( ) )
	total_recoveries = Column( Float( ) )
	total_actual_reimbursements = Column( Float( ) )
	total_agreement_reimbursables = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	total_committed = Column( Float( ) )
	total_estimated_recoveries = Column( Float( ) )
	total_estimated_reimbursements = Column( Float( ) )
	total_expenses = Column( Float( ) )
	total_expenditure_expenses = Column( Float( ) )
	total_expense_accruals = Column( Float( ) )
	total_precommitments = Column( Float( ) )
	unliquidated_precommitments = Column( Float( ) )
	total_obligations = Column( Float( ) )
	ulo = Column( Float( ) )
	voided_amount = Column( Float( ) )
	total_used = Column( Float( ) )
	available_amount = Column( Float( ) )
	
	
	def __init__( self, bfy: str, efy: str, fund: str,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfAppropriations
		self.bfy = bfy
		self.efy = efy
		self.appropriationfundcode = fund
		self.fields = [ 'StatusOfAppropriationsId',
		                'BFY',
		                'EFY',
		                'BudgetLevel',
		                'AppropriationFundCode',
		                'AppropriationFundName',
		                'Availability',
		                'TreasurySymbol',
		                'AppropriationCreationDate',
		                'AppropriationCode',
		                'SubAppropriationCode',
		                'AppropriationDescription',
		                'FundGroup',
		                'FundGroupName',
		                'DocumentType',
		                'TransType',
		                'ActualRecoveryTransType',
		                'CommitmentSpendingControlFlag',
		                'AgreementLimit',
		                'EstimatedRecoveriesTransType',
		                'EstimatedReimbursmentsTransType',
		                'ExpenseSpendingControlFlag',
		                'ObligationSpendingControlFlag',
		                'PreCommitmentSpendingControlFlag',
		                'PostedControlFlag',
		                'PostedFlag',
		                'RecordCarryoverAtLowerLevel',
		                'ReimbursableSpendingOption',
		                'RecoveriesOption',
		                'RecoveriesSpendingOption',
		                'OriginalBudgetedAmount',
		                'ApportionmentsPosted',
		                'TotalAuthority',
		                'TotalBudgeted',
		                'TotalPostedAmount',
		                'FundsWithdrawnPriorYearsAmount',
		                'FundingInAmount',
		                'FundingOutAmount',
		                'TotalAccrualRecoveries',
		                'TotalActualReimbursements',
		                'TotalAgreementReimbursables',
		                'TotalCarriedForwardIn',
		                'TotalCarriedForwardOut',
		                'TotalCommitted',
		                'TotalEstimatedRecoveries',
		                'TotalEstimatedReimbursements',
		                'TotalExpenses',
		                'TotalExpenditureExpenses',
		                'TotalExpenseAccruals',
		                'TotalPreCommitments',
		                'UnliquidatedPreCommitments',
		                'TotalObligations',
		                'UnliquidatedObligations',
		                'VoidedAmount',
		                'TotalUsedAmount',
		                'AvailableAmount' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'AppropriationFundCode', ]
			_values = (self.bfy, self.efy, self.appropriationfundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'StatusOfAppropriations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'StatusOfAppropriations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SpendingRate( Base ):
	'''
    Constructor:
    SpendingRate( accountcode: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class object providing OMB spending rate data
    '''
	__tablename__ = 'SpendingRates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	omb_agency_code = Column( String( 80 ) )
	omb_agency_name = Column( String( 80 ) )
	omb_bureau_code = Column( String( 80 ) )
	omb_bureau_name = Column( String( 80 ) )
	treausury_agency_code = Column( String( 80 ) )
	treausury_account_code = Column( String( 80 ) )
	treausury_account_name = Column( String( 80 ) )
	account_title = Column( String( 80 ) )
	subfunction = Column( String( 80 ) )
	line = Column( String( 80 ) )
	line_number = Column( String( 80 ) )
	category = Column( String( 80 ) )
	subcategory = Column( String( 80 ) )
	subcategory_name = Column( String( 80 ) )
	main_account = Column( String( 80 ) )
	jurisdiction = Column( String( 80 ) )
	year_of_authority = Column( String( 80 ) )
	budget_authority = Column( Float( ) )
	out_year_1 = Column( Float( ) )
	out_year_2 = Column( Float( ) )
	out_year_3 = Column( Float( ) )
	out_year_4 = Column( Float( ) )
	out_year_5 = Column( Float( ) )
	out_year_6 = Column( Float( ) )
	out_year_7 = Column( Float( ) )
	out_year_8 = Column( Float( ) )
	out_year_9 = Column( Float( ) )
	out_year_10 = Column( Float( ) )
	out_year_11 = Column( Float( ) )
	total_spendout = Column( Float( ) )
	
	def __init__( self, account: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.SpendingRates
		self.budgetaccountcode = account
		self.fields = [ 'SpendingRatesId',
		                'OmbAgencyCode',
		                'OmbAgencyName',
		                'OmbBureauCode',
		                'OmbBureauName',
		                'TreausuryAgencyCode',
		                'TreausuryAccountCode',
		                'TreausuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName',
		                'AccountTitle',
		                'Subfunction',
		                'Line',
		                'LineNumber',
		                'Category',
		                'Subcategory',
		                'SubcategoryName',
		                'AccountCode',
		                'Jurisdiction',
		                'YearOfAuthority',
		                'BudgetAuthority',
		                'OutYear1',
		                'OutYear2',
		                'OutYear3',
		                'OutYear4',
		                'OutYear5',
		                'OutYear6',
		                'OutYear7',
		                'OutYear8',
		                'OutYear9',
		                'OutYear10',
		                'OutYear11',
		                'TotalSpendout' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		returns a list[ str ] of class members

		'''
		return [ 'id', 'treasury_agency_code', 'treasury_agency_name',
		         'omb_agency_code', 'omb_agency_name', 'main_account',
		         'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name', 'subaccount',
		         'subcategory', 'subfunction', 'category',
		         'line_number', 'line_name', 'year_of_authority',
		         'budget_authority', 'out_year_1', 'out_year_2', 'out_year_3',
		         'out_year_4', 'out_year_5', 'out_year_6',
		         'out_year_7', 'out_year_8', 'out_year_9',
		         'out_year_10', 'out_year_11', 'total_spendout',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BudgetAccountCode', ]
			_values = (self.budgetaccountcode,)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = [ i for i in _db.createtable( ) ]
			return [ i for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'SpendingRate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'SpendingRate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSupplementalFunds( Base ):
	'''
    Constructor:
    StatusOfSupplementalFunds( bfy, efy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defines object used for reporting on Supplemental funding
    '''
	__tablename__ = 'StatusOfSupplementalFunds'
	id = Column( Integer( ), primary_key=True, index=True )
	status_of_funds_id = Column( Integer( ) )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fund: str,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfSupplementalFunding
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'StatusOfSupplementalFundsId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'RcCode',
		                'RcName',
		                'LowerName',
		                'Amount',
		                'Budgeted',
		                'Posted',
		                'OpenCommitments',
		                'UnliquidatedObligations',
		                'Expenditure',
		                'Obligations',
		                'Used',
		                'Available',
		                'NpmCode',
		                'NpmName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSupplementalFunds'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSupplementalFunds'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfJobsActFunding( Base ):
	'''
    Constructor:
    StatusOfJobsActFunding(  bfy: str, efy: str,
        fundcode: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object for reporting on IIJA funds
    '''
	__tablename__ = 'StatusOfJobsActFunding'
	id = Column( Integer( ), primary_key=True, nullable=False )
	status_of_funds_id = Column( Integer( ) )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str, fundcode: str,
	              provider: Provider = Provider.SQLite ):
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.provider = provider
		self.source = Source.StatusOfJobsActFunding
		self.fields = [ 'StatusOfJobsActFundingId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'NpmCode',
		                'NpmName',
		                'RcCode',
		                'RcName',
		                'LowerName',
		                'Amount',
		                'Budgeted',
		                'Posted',
		                'OpenCommitments',
		                'UnliquidatedObligations',
		                'Expenditure',
		                'Obligations',
		                'Used',
		                'Available',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ) -> str:
		if self.fundname is not None:
			return self.fundname
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfJobsActFunding'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfJobsActFunding'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfEarmarks( Base ):
	'''
    Constructor:
    StatusOfEarmarks(  bfy: str, efy: str, fundcode: str, pvdr = Provider.SQLite )

     Purpose:
     Class defines object for reporting on Earmarks
    '''
	__tablename__ = 'StatusOfEarmarks'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	budget_level = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 255 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 255 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 255 ) )
	account_code = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 155 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 255 ) )
	rc_code = Column( String( 25 ) )
	rc_name = Column( String( 255 ) )
	budgeted = Column( Float( ) )
	posted = Column( Float( ) )
	carryover_in = Column( Float( ) )
	carryover_out = Column( Float( ) )
	estimated_reimbursements = Column( Float( ) )
	estimated_recoveries = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	program_project_code = Column( String( 25 ) )
	program_project_name = Column( String( 255 ) )
	program_area_code = Column( String( 25 ) )
	program_area_name = Column( String( 255 ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 255 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 255 ) )
	
	def __init__( self, bfy: str, efy: str,
	              fundcode: str, provider: Provider = Provider.SQLite ):
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.provider = provider
		self.source = Source.StatusOfEarmarks
		self.fields = [ 'StatusOfEarmarksId',
		                'StatusOfFundsId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'BocCode',
		                'BocName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'NpmCode',
		                'NpmName',
		                'RcCode',
		                'RcName',
		                'StateCode',
		                'ZipCode'
		                'StateName',
		                'Amount',
		                'Budgeted',
		                'Posted',
		                'OpenCommitments',
		                'UnliquidatedObligations',
		                'Expenditures',
		                'Obligations',
		                'Used',
		                'Available'
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'state_code', 'state_name', 'zip_code',
		         'county_name', 'city_name', 'site_id', 'site_name',
		         'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfEarmark'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:  Method returning pandas dataframe
        comprised of datatable data


        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfEarmark'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSuperfundSites( Base ):
	'''
    Constructor:
    StatusOfSuperfundSites(  bfy: str, efy: str, fundcode: str, pvdr = Provider.SQLite )

     Purpose:
     Class defines object for reporting on Earmarks
    '''
	__tablename__ = 'StatusOfSuperfundSites'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	city = Column( String( 80 ) )
	state = Column( String( 80 ) )
	site_project_name = Column( String( 80 ) )
	
	def __init__( self, bfy: str, efy: str, rpio: str,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfSuperfundSites
		self.bfy = bfy
		self.efy = efy
		self.rpiocode = super( ).code
		self.fields = [ 'SiteActivityId',
		                'FiscalYear',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'FundCode',
		                'FundName',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'SiteId',
		                'SiteName',
		                'CityName',
		                'StreetAddres',
		                'ZipCode',
		                'CountyName',
		                'StateName',
		                'Obligations',
		                'Deobligations',
		                'Expenditures'
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName' ]
	
	def __str__( self ):
		if self.__sitename is not None:
			return self.__sitename
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'state_code', 'state_name', 'zip_code',
		         'county_name', 'city_name', 'site_id', 'site_name',
		         'budgeted', 'posted', 'open_commitments',
		         'obligations', 'deobligations', 'expenditures',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = (self.bfy, self.rpiocode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSuperfundSites'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSuperfundSites'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SpendingDocument( Base ):
	'''
    Constructor:
    SpendingDocument(  bfy: str, efy: str, fund: str, account: str,
                  boc: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing Spending documnets
    '''
	__tablename__ = 'SpendingDocuments'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	
	def __init__( self, bfy: str, efy: str, fund: str, account: str,
	              boc: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Obligations
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'ObligationsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentControlNumber',
		                'ReferenceDocumentNumber',
		                'ProcessedDate',
		                'LastActivityDate',
		                'Age',
		                'BocCode',
		                'BocName',
		                'FocCode',
		                'FocName',
		                'NpmCode',
		                'NpmName',
		                'VendorCode',
		                'VendorName',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Expenditures' ]
	
	def __str__( self ) -> float:
		if self.amount is not None:
			return self.amount
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'SpendingDocuments'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'SpendingDocuments'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SupplementalCarryoverEstimate( Base ):
	'''

    Constructor:
    CarryoverEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing Supplemental Carryover Estimates

    '''
	__tablename__ = 'SupplementalCarryoverEstimates'
	id = Column( Integer( ), primary_key=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	treasury_account_code = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 155 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 155 ) )
	amount = Column( Float( ) )
	open_commitments = Column( Float( ) )
	obligations = Column( Float( ) )
	available = Column( Float( ) )
	estimate = Column( Float( ) )
	
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.SupplementalCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'CarryoverEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SupplementalObligationEstimate( Base ):
	'''
    Constructor:
    CarryoverEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing Supplemental Carryover Estimate data for
    '''
	__tablename__ = 'SupplementalObligationEstimates'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	
	
	def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.SupplementalCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'CarryoverEstimatesId',
		                'BudgetLevel',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'BocCode',
		                'BocName',
		                'AvailableBalance',
		                'OpenCommitments',
		                'UnobligatedAuthority' ]
	
	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = (self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class TreasurySymbol( Base ):
	'''
    Constructor:
    TreasurySymbol( bfy: str, efy: str, treas: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object that represents a TAFS
    '''
	__tablename__ = 'TreasurySymbols'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, efy: str, account: str,
	              provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.__soruce = Source.FundSymbols
		self.bfy = bfy
		self.efy = efy
		self.treasuryaccountcode = account
		self.fields = [ 'TreasurySymbolsId',
		                'BFY',
		                'EFY',
		                'FundCode',
		                'FundName',
		                'MainAccount',
		                'TreasuryAccountCode',
		                'TreasuryAccountName',
		                'BudgetAccountCode',
		                'BudgetAccountName',
		                'ApportionmentAccountCode' ]
	
	def __str__( self ) -> str:
		if self.treasuryaccountname is not None:
			return self.treasuryaccountname
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code',
		         'budget_account_name', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'TreasuryAccountCode' ]
			_values = (self.bfy, self.efy, self.treasuryaccountcode)
			dbcfg = DbConfig( _source, _provider )
			sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( dbcfg, sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TreasurySymbol'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TreasurySymbol'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Transfer( Base ):
	'''
     Constructor:
     Transfer( documentnumber: str, pvdr = Provider.SQLite )

     Purpose:
     Class defines object representing EPA reprogrammings
     '''
	__tablename__ = 'Transfers'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	budget_level = Column( String( 80 ) )
	doc_prefix = Column( String( 80 ) )
	doc_type = Column( String( 80 ) )
	bfy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	rpio_name = Column( String( 155 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 80 ) )
	reprogramming_number = Column( String( 80 ) )
	control_number = Column( String( 80 ) )
	processed_date = Column( String( 80 ) )
	quarter = Column( String( 80 ) )
	line = Column( String( 80 ) )
	subline = Column( String( 80 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 80 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	program_area_code = Column( String( 80 ) )
	program_area_name = Column( String( 80 ) )
	program_project_name = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	from_to = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 80 ) )
	npm_code = Column( String( 80 ) )
	amount = Column( Float( ) )
	resource_type = Column( String( 80 ) )
	purpose = Column( String( 80 ) )
	extended_purpose = Column( String( 80 ) )
	
	def __init__( self, documentnumber: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.Transfers
		self.documentnumber = documentnumber
		self.fields = [ 'TransfersId',
		                'BudgetLevel',
		                'DocPrefix',
		                'DocType',
		                'BFY',
		                'RpioCode',
		                'RpioName',
		                'FundCode',
		                'FundName',
		                'ReprogrammingNumber',
		                'ControlNumber',
		                'ProcessedDate',
		                'Quarter',
		                'Line',
		                'Subline',
		                'AhCode',
		                'AhName',
		                'OrgCode',
		                'OrgName',
		                'RcCode',
		                'RcName',
		                'AccountCode',
		                'ProgramAreaCode',
		                'ProgramAreaName',
		                'ProgramProjectName',
		                'ProgramProjectCode',
		                'FromTo',
		                'BocCode',
		                'BocName',
		                'NpmCode',
		                'Amount',
		                'ResourceType',
		                'Purpose',
		                'ExtendedPurpose' ]
	
	def __dir__( self ) -> list[ str ]:
		'''
	
		:return: a list[ str ] of object members
	
		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''
	
		:return: list[ Row ]
	
		:param: self
	
		:purpose:
	
		'''
		
		try:
			_source = self.source
			command = SQL.SELECTALL
			_names = [ 'DocumentNumber', ]
			_values = (self.documentnumber,)
			_dbconfig = DbConfig( _source )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Transfer'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
		Purpose:
	
		Parameters:
	
		Returns:
		'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Transfer'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class TransType( Base ):
	'''
    Constructor:
    TransType( bfy: str, fundcode: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing trans types
    '''
	__tablename__ = 'TransTypes'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	code = Column( String( 55 ) )
	name = Column( String( 155 ) )
	
	
	def __init__( self, bfy: str, fundcode: str, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.TransTypes
		self.bfy = bfy
		self.fundcode = fundcode
		self.fields = [ 'TransTypesId',
		                'FundCode',
		                'Appropriation',
		                'BFY',
		                'EFY',
		                'TreasurySymbol',
		                'DocType',
		                'AppropriationBill',
		                'ContinuingResolution',
		                'RescissionCurrentYear',
		                'RescissionPriorYear',
		                'SequesterReduction',
		                'SequesterReturn' ]
	
	def __dir__( self ) -> list[ str ]:
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = (self.bfy, self.fundcode)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TransTypes'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''

        Purpose:  Method returning pandas dataframe
        comprised of datatable data


        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TransTypes'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class UnliquidatedObligation( Base ):
	'''
    Constructor:
    UnliquidatedObligation( bfy: str, fund: str, account: str, 
        boc: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object providing ULO data
    '''
	__tablename__ = 'UnliquidatedObligations'
	id = Column( Integer( ), primary_key=True, nullable=False, index=True )
	bfy = Column( String( 80 ) )
	efy = Column( String( 80 ) )
	rpio_code = Column( String( 80 ) )
	name = Column( String( 155 ) )
	ah_code = Column( String( 80 ) )
	ah_name = Column( String( 80 ) )
	fund_code = Column( String( 80 ) )
	fund_name = Column( String( 80 ) )
	org_code = Column( String( 80 ) )
	org_name = Column( String( 80 ) )
	account_code = Column( String( 80 ) )
	program_project_code = Column( String( 80 ) )
	program_project_name = Column( String( 80 ) )
	rc_code = Column( String( 80 ) )
	rc_name = Column( String( 80 ) )
	document_type = Column( String( 80 ) )
	document_number = Column( String( 80 ) )
	document_control_number = Column( String( 80 ) )
	reference_document_number = Column( String( 80 ) )
	processed_date = Column( DateOnly )
	last_activity_date = Column( DateOnly )
	age = Column( String( 80 ) )
	boc_code = Column( String( 80 ) )
	boc_name = Column( String( 80 ) )
	foc_code = Column( String( 80 ) )
	foc_name = Column( String( 80 ) )
	npm_code = Column( String( 80 ) )
	npm_name = Column( String( 80 ) )
	vendor_code = Column( String( 80 ) )
	vendor_name = Column( String( 80 ) )
	amount = Column( Float( ) )
	treasury_account_code = Column( String( 80 ) )
	treasury_account_name = Column( String( 80 ) )
	budget_account_code = Column( String( 80 ) )
	budget_account_name = Column( String( 80 ) )
	
	
	def __init__( self, bfy: str, efy: str, fund: str, account: str = None,
	              boc: str = None, provider: Provider = Provider.SQLite ):
		self.provider = provider
		self.source = Source.UnliquidatedObligations
		self.bfy = bfy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'UnliquidatedObligationsId'
		                'ObligationsId',
		                'BFY',
		                'EFY',
		                'RpioCode',
		                'RpioName',
		                'AhCode',
		                'AhName',
		                'FundCode',
		                'FundName',
		                'OrgCode',
		                'OrgName',
		                'AccountCode',
		                'ProgramProjectCode',
		                'ProgramProjectName',
		                'RcCode',
		                'RcName',
		                'DocumentType',
		                'DocumentNumber',
		                'DocumentControlNumber',
		                'ReferenceDocumentNumber',
		                'ProcessedDate',
		                'LastActivityDate',
		                'Age',
		                'BocCode',
		                'BocName',
		                'FocCode',
		                'FocName',
		                'NpmCode',
		                'NpmName',
		                'VendorCode',
		                'VendorName',
		                'OpenCommitments',
		                'Obligations',
		                'UnliquidatedObligations',
		                'Expenditures' ]
	
	def __str__( self ) -> str:
		if self.amount is not None:
			return self.amount
	
	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]
	
	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''
		
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = (self.bfy, self.fundcode, self.accountcode, self.boccode)
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_command = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _command.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'UnliquidatedObligations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
	
	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'UnliquidatedObligations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
