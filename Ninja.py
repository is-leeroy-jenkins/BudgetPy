import datetime as dt
from datetime import datetime, date
from Static import Source, Provider, SQL
from Booger import Error, ErrorDialog
import sys
from sys import exc_info
from Data import DbConfig, SqlConfig, Connection, \
    SqlStatement, BudgetData, DataBuilder
from Static import Source, Provider
from datetime import datetime, date
from pandas import DataFrame
from pyodbc import Row as Row

class Unit( ):
    '''Unit( value, value ) initializes object
    representing fundemental unit of data
    in the Budget Execution application'''
    __index = None

    @property
    def id( self ):
        if isinstance( self.__index, int ):
            return self.__index

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__index = id

    def __init__( self, id ):
        self.__index = id if isinstance( id, int ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

# DataUnit( id, code, name )
class DataUnit( Unit ):
    '''DataUnit class represents fundamental program unit'''
    __index = None
    __code = None
    __name = None

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ):
            self.__name = name

    @property
    def code( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, id, code, name ):
        super( ).__init__( id )
        self.__id = super( ).__id
        self.__code = code if code is not None else None
        self.__name = name if name is not None else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

# BudgetUnit( id, code, name, treas, omb )
class BudgetUnit( DataUnit ):
    #base class for OMB reporting classes
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    def __init__( self, id, code, name, treas, omb ):
        super( ).__init__( id, code, name )
        self.__treasuryaccountcode = treas if treas is not None else None
        self.__budgetaccountcode = omb if omb is not None else None

# Account( treas, provider = Provider.SQLite )
class Account( ):
    '''defines the Account Code class'''
    __source = None
    __provider = None
    __accountsid = None
    __code = None
    __name = None
    __goalcode = None
    __objectivecode = None
    __npmcode = None
    __programprojectcode = None
    __programprojectname = None
    __fields = None
    __data = None
    __frame = None


    @property
    def id( self ):
        if self.__accountsid is not None:
            return self.__accountsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def npm_code( self ):
        if  self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if value is not None:
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__code = code
        self.__provider = provider
        self.__source = Source.Accounts
        self.__goalcode = self.__code[ 0 ]
        self.__objectivecode = self.__code[ 1:3 ]
        self.__npmcode = self.__code[ 3 ]
        self.__programprojectcode = self.__code[ 4:6 ]
        self.__fields = [ 'AccountsId',
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

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def copy( self ):
        try:
            clone = Account( code = self.__code )
            clone.goal_code = self.__goalcode
            clone.objective_code = self.__objectivecode
            clone.npm_code = self.__npmcode
            clone.program_project_code = self.__programprojectcode
            return clone
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Account'
            exc.method = 'copy( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_data( self ) -> list[ tuple ]:
        try:
            source = Source.Accounts
            provider = Provider.SQLite
            n = [ 'Code', ]
            v = ( self.__code, )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( source, provider )
            sql = SqlStatement( cnx, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ tuple( i ) for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Account'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Account'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ActivityCode( treas, provider = Provider.SQLite )
class ActivityCode( ):
    '''Defines the Activity Class'''
    __source = None
    __provider = None
    __activitycodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__activitycodesid is not None:
            return self.__activitycodesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__activitycodesid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if value is not None:
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ActivityCodes
        self.__code = code
        self.__fields = [ 'ActivityCodesId',
                           'Code',
                           'Name',
                           'Title' ]

    def __str__( self ):
        if self.__code is not None:
            return self.__code

    def get_data( self ) -> list[ tuple ]:
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = ( self.__code, )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ tuple( i ) for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Activity'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Activity'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# AllowanceHolder( fundcode, provider = Provider.SQLite )
class AllowanceHolder( ):
    '''Defines the AllowanceHolder Class'''
    __source = None
    __provider = None
    __allowancholdersid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__allowancholdersid is not None:
            return self.__allowancholdersid

    @id.setter
    def id( self, id ):
        if id is not None:
            self.__allowancholdersid = id

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if list is not None:
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if frame is not None:
            self.__frame = frame

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AllowanceHolders
        self.__code = code if isinstance( self.__code, str ) else None
        self.__fields = [ 'AllowanceHoldersId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = ( self.__code, )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'AllowanceHolder'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'AllowanceHolder'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CarryoverEstimate( bfy, provider = Provider.SQLite )
class AmericanRescuePlanCarryoverEstimate( ):
    '''CarryoverEstimate( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __arpcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__arpcarryoverestimatesid is not None:
            return self.__arpcarryoverestimatesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ):
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if value is not None:
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
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
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CarryoverEstimate( bfy, provider = Provider.SQLite )
class AnnualCarryoverEstimate( ):
    '''CarryoverEstimate( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __annualcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ):
        if self.__available is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
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
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if self.__unobligatedauthrity is not None:
            return str( self.__unobligatedauthority )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ReimbursableEstimate( bfy, provider = Provider.SQLite )
class AnnualReimbursableEstimate( ):
    '''CarryoverEstimate( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __annualreimbursableestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def available( self ):
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value


    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
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
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Appropriation( fundcode, provider = Provider.SQLite )
class Appropriation( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __appropriationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__appropriationsid is not None:
            return self.__appropriationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__appropriationsid  = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__code = code 
        self.__fields = [ 'AppropriationsId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# AppropriationAvailableBalance( bfy, efy, fundcode, provider = Provider.SQLite )
class AppropriationAvailableBalance( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __appropriationavailablebalancesid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __authority = None
    __budgeted = None
    __carryover = None
    __reimbursements = None
    __recoveries = None
    __used = None
    __available = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__appropriationavailablebalancesid is not None:
            return self.__appropriationavailablebalancesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__appropriationavailablebalancesid  = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if  self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, name ):
        if  name is not None:
            self.__fundname = name

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def authority( self ):
        if self.__authority is not None:
            return self.__authority

    @authority.setter
    def authority( self, value ):
        if value is not None:
            self.__authority = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def reimbursements( self ):
        if self.__reimbursements is not None:
            return self.__reimbursements

    @reimbursements.setter
    def reimbursements( self, value ):
        if value is not None:
            self.__reimbursements = value

    @property
    def recoveries( self ):
        if self.__recoveries is not None:
            return self.__recoveries

    @recoveries.setter
    def recoveries( self, value ):
        if value is not None:
            self.__recoveries = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__available is not None:
            return self.__available

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__available = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fundcode
        self.__fields = [ 'AppropriationAvailableBalancesId',
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
                          'TotalAvailable']

    def __str__( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    def get_data( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = (self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# AppropriationLevelAuthority( vfy, efy, fundcode, provider = Provider.SQLite )
class AppropriationLevelAuthority( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __appropriationlevelauthorityid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __treasuryaccountcode = None
    __budgeted = None
    __carryover = None
    __reimbursements = None
    __authority = None
    __recoveries = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__appropriationlevelauthorityid is not None:
            return self.__appropriationlevelauthorityid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__appropriationlevelauthorityid  = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if  self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, name ):
        if  name is not None:
            self.__fundname = name

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def authority( self ):
        if self.__authority is not None:
            return self.__authority

    @authority.setter
    def authority( self, value ):
        if value is not None:
            self.__authority = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def reimbursements( self ):
        if self.__reimbursements is not None:
            return self.__reimbursements

    @reimbursements.setter
    def reimbursements( self, value ):
        if value is not None:
            self.__reimbursements = value

    @property
    def recoveries( self ):
        if self.__recoveries is not None:
            return self.__recoveries

    @recoveries.setter
    def recoveries( self, value ):
        if value is not None:
            self.__recoveries = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fundcode
        self.__fields = [ 'AppropriationLevelAuthorityId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Allocation( bfy, fund, provider = Provider.SQLite )
class Allocation( ):
    '''object representing operating plan data'''
    __source = None
    __provider = None
    __allocationsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if  self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__source = Source.Allocations
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'AllocationsId',
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
                           'NpmName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Allocation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Allocation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ApportionmentData( bfy, efy, treas, provider = Provider.SQLite )
class ApportionmentData( ):
    '''Apportionment( bfy, efy, omb )
    initializes object representing Letters Of Apportionment'''
    __source = None
    __provider = None
    __apportionmentdataid = None
    __bfy = None
    __efy = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __linenumber = None
    __linedescription = None
    __sectionnumber = None
    __sectiondescription = None
    __subline = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__apportionmentsid is not None:
            return self.__apportionmentsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__apportionmentsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def line_number( self ):
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_description( self ):
        if self.__linedescription is not None:
            return self.__linedescription

    @line_description.setter
    def line_description( self, value ):
        if value is not None:
            self.__linedescription = value

    @property
    def section_number( self ):
        if self.__sectionnumber is not None:
            return self.__sectionnumber

    @section_number.setter
    def section_number( self, value ):
        if value is not None:
            self.__sectionnumber = value

    @property
    def section_description( self ):
        if self.__sectiondescription is not None:
            return self.__sectiondescription

    @section_description.setter
    def section_description( self, value ):
        if value is not None:
            self.__sectiondescription = value

    @property
    def subline( self ):
        if self.__subline is not None:
            return self.__subline

    @subline.setter
    def subline( self, value ):
        if value is not None:
            self.__subline = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, omb, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Apportionments
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = omb
        self.__fields = [ 'ApportionmentDataId',
                          'FiscalYear',
                          'BFY',
                          'EFY',
                          'Availability',
                          'TreasuryFundCode',
                          'TreasuryFundName',
                          'TreasuryAgencyCode',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'OmbAgencyCode',
                          'OmbBureauCode',
                          'OmbAccountCode',
                          'OmbAgencyName',
                          'OmbAccountName',
                          'ApprovalDate',
                          'LineNumber',
                          'LineName',
                          'Amount',
                          'Footnote',
                          'Narrative' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            v = (self.__bfy, self.__efy, self.__budgetaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'Apportionment'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'Apportionment'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Actual( bfy, fund, provider = Provider.SQLite  )
class Actual( ):
    '''Object representing expenditure data'''
    __source = None
    __provider = None
    __actualsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __appropriationcode = None
    __appropriationname = None
    __subappropriationcode = None
    __subappropriationname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __balance = None
    __obligations = None
    __ulo = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__actualsid is not None:
            return self.__actualsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__id = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def balance( self ):
        if self.__balance is not None:
            return self.__balance

    @balance.setter
    def balance( self, value ):
        if value is not None:
            self.__balance = value

    @property
    def ulo( self ):
        if self.__ulo is not None:
            return self.__ulo

    @ulo.setter
    def ulo( self, value ):
        if value is not None:
            self.__ulo = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if  self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Actuals
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'ActualsId',
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
                           'ULO',
                           'Obligation',
                           'Balance',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'GoalCode',
                           'GoalName',
                           'ObjectiveCode',
                           'ObjectiveName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Actual'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Actual'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ApplicationTable( name, provider = Provider.SQLite )
class ApplicationTable( ):
    # Provides tables for the application
    __source = None
    __provider = None
    __applicationtablesid = None
    __tablename = None
    __model = None
    __title = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__applicationtablesid is not None:
            return self.__applicationtablesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__applicationtablesid = value

    @property
    def table_name( self ):
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value ):
        if value is not None:
            self.__tablename = value

    @property
    def model( self ):
        if self.__model is not None:
            return self.__model

    @model.setter
    def model( self, value ):
        if value is not None:
            self.__model = value

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, value ):
        if value is not None:
            self.__title = value

    def __init__( self, name, provider = Provider.SQLite ):
        self.__source = Source.ApplicationTables
        self.__provider = provider
        self.__tablename = name

# AppropriationDocument( bfy, fund, provider = Provider.SQLite )
class AppropriationDocument( ):
    '''object representing Level 1 documents'''
    __source = None
    __provider = None
    __appropriationdocumentsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fund = None
    __documenttype = None
    __documentnumber = None
    __documentdate = None
    __lastdocumentdate = None
    __budgetlevel = None
    __budgetingcontrols = None
    __postingcontrols = None
    __precommitmentcontrols = None
    __commitmentcontrols = None
    __obligationcontrols = None
    __accrualcontrols = None
    __expenditurecontrols = None
    __expensecontrols = None
    __reimbursementcontrols = None
    __reimbursableagreementcontrols = None
    __budgeted = None
    __posted = None
    __carryoverout = None
    __carryoverin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__appropriationdocumentsid is not None:
            return self.__appropriationdocumentsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__appropriationdocumentsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, value ):
        if value is not None:
            self.__fund = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentname is not None:
            return self.__documentname

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentname = value

    @property
    def document_date( self ):
        if isinstance( self.__documentdate, datetime ):
            return self.__documentdate

    @document_date.setter
    def document_date( self, value ):
        if isinstance( value, datetime ):
            self.__documentdate = value

    @property
    def last_document_date( self ):
        if isinstance( self.__lastdocumentdate, datetime ):
            return self.__lastdocumentdate

    @last_document_date.setter
    def lastdocumentdate( self, value ):
        if isinstance( value, datetime ):
            self.__lastdocumentdate = value

    @property
    def budget_level( self ):
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def budgeting_controls( self ):
        if self.__budgetingcontrols is not None:
            return self.__budgetingcontrols

    @budgeting_controls.setter
    def budgeting_controls( self, value ):
        if value is not None:
            self.__budgetingcontrols = value

    @property
    def posting_controls( self ):
        if self.__postingcontrols is not None:
            return self.__postingcontrols

    @posting_controls.setter
    def posting_controls( self, value ):
        if value is not None:
            self.__postingcontrols = value

    @property
    def precommitment_controls( self ):
        if self.__precommitmentcontrols is not None:
            return self.__precommitmentcontrols

    @precommitment_controls.setter
    def precommitment_controls( self, value ):
        if value is not None:
            self.__precommitmentcontrols = value

    @property
    def commitment_controls( self ):
        if self.__commitmentcontrols is not None:
            return self.__commitmentcontrols

    @commitment_controls.setter
    def commitment_controls( self, value ):
        if value is not None:
            self.__commitmentcontrols = value

    @property
    def obligation_controls( self ):
        if self.__obligationcontrols is not None:
            return self.__obligationcontrols

    @obligation_controls.setter
    def obligation_controls( self, value ):
        if value is not None:
            self.__obligationcontrols = value

    @property
    def accrual_controls( self ):
        if self.__accrualcontrols is not None:
            return self.__accrualcontrols

    @accrual_controls.setter
    def accrual_controls( self, value ):
        if value is not None:
            self.__accrualcontrols = value

    @property
    def expenditure_controls( self ):
        if self.__expenditurecontrols is not None:
            return self.__expenditurecontrols

    @expenditure_controls.setter
    def expenditure_controls( self, value ):
        if value is not None:
            self.__expenditurecontrols = value

    @property
    def expense_controls( self ):
        if self.__expensecontrols is not None:
            return self.__expensecontrols

    @expense_controls.setter
    def expense_controls( self, value ):
        if value is not None:
            self.__expensecontrols = value

    @property
    def reimbursement_controls( self ):
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @reimbursement_controls.setter
    def reimbursement_controls( self, value ):
        if value is not None:
            self.__reimbursementcontrols = value

    @property
    def reimbursable_agreement_controls( self ):
        if self.__reimbursableagreementcontrols is not None:
            return self.__reimbursableagreementcontrols

    @reimbursable_agreement_controls.setter
    def reimbursable_agreement_controls( self, value ):
        if value is not None:
            self.__reimbursableagreementcontrols = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if value is not None:
            self.__posted = value

    @property
    def carryover_in( self ):
        if self.__carryoverin is not None:
            return self.__carryoverin

    @carryover_in.setter
    def carryover_in( self, value ):
        if value is not None:
            self.__carryoverin = value

    @property
    def carryover_out( self ):
        if self.__carryoverout is not None:
            return self.__carryoverout

    @carryover_out.setter
    def carryoverout( self, value ):
        if value is not None:
            self.__carryoverout = value

    @property
    def estimated_reimbursements( self ):
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @estimated_reimbursements.setter
    def estimated_reimbursements( self, value ):
        if value is not None:
            self.__estimatedreimbursements = value

    @property
    def estimated_recoveries( self ):
        if self.__estimatedrecoveries is not None:
            return self.__estimatedrecoveries

    @estimated_recoveries.setter
    def estimated_recoveries( self, value ):
        if value is not None:
            self.__estimatedrecoveries = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AppropriationDocuments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'AppropriationDocumentsId',
                           'BFY',
                           'EFY',
                           'Fund',
                           'FundCode',
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
                           'CarryOut',
                           'CarryIn',
                           'EstimatedReimbursements',
                           'EstimatedRecoveries' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'AppropriationDocument'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'AppropriationDocument'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# BudgetDocument( bfy, fund, provider = Provider.SQLite )
class BudgetDocument( ):
    '''object representing Level 2-3 documents'''
    __source = None
    __provider = None
    __budgetdocumentsid = None
    __bfy = None
    __efy = None
    __budgetlevel = None
    __fundcode = None
    __fundname = None
    __documenttype = None
    __documentnumber = None
    __documentdate = None
    __lastdocumentdate = None
    __rpiocode = None
    __rpioname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __boccode = None
    __bocname = None
    __budgetingcontrols = None
    __postingcontrols = None
    __precommitmentcontrols = None
    __commitmentcontrols = None
    __obligationcontrols = None
    __accrualcontrols = None
    __expenditurecontrols = None
    __expensecontrols = None
    __reimbursementcontrols = None
    __reimbursableagreementcontrols = None
    __budgeted = None
    __posted = None
    __carryoverout = None
    __carryoverin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if self.__statusoffundsid is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def budget_level( self ):
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fund_code is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentname = value

    @property
    def document_date( self ):
        if self.__documentdate is not None:
            return self.__documentdate

    @document_date.setter
    def document_date( self, value ):
        if value is not None:
            self.__documentdate = value

    @property
    def last_document_date( self ):
        if self.__lastdocumnetdate is not None:
            return self.__lastdocumentdate

    @last_document_date.setter
    def last_document_date( self, value ):
        if value is not None:
            self.__lastdocumentdate = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def budgeting_controls( self ):
        if self.__budgetingcontrols is not None:
            return self.__budgetingcontrols

    @budgeting_controls.setter
    def budgeting_controls( self, value ):
        if value is not None:
            self.__budgetingcontrols = value

    @property
    def posting_controls( self ):
        if  self.__postingcontrols is not None:
            return self.__postingcontrols

    @posting_controls.setter
    def posting_controls( self, value ):
        if value is not None:
            self.__postingcontrols = value

    @property
    def precommitment_controls( self ):
        if  self.__precommitmentcontrols is not None:
            return self.__precommitmentcontrols

    @precommitment_controls.setter
    def precommitment_controls( self, value ):
        if value is not None:
            self.__precommitmentcontrols = value

    @property
    def commitment_controls( self ):
        if self.__commitmentcontrols is not None:
            return self.__commitmentcontrols

    @commitment_controls.setter
    def commitment_controls( self, value ):
        if value is not None:
            self.__commitmentcontrols = value

    @property
    def obligation_controls( self ):
        if self.__obligationcontrols is not None:
            return self.__obligationcontrols

    @obligation_controls.setter
    def obligation_controls( self, value ):
        if value is not None:
            self.__obligationcontrols = value

    @property
    def accrual_controls( self ):
        if self.__accrual_controls is not None:
            return self.__accrualcontrols

    @accrual_controls.setter
    def accrual_controls( self, value ):
        if value is not None:
            self.__accrualcontrols = value

    @property
    def expenditure_controls( self ):
        if self.__expenditurecontrols is not None:
            return self.__expenditurecontrols

    @expenditure_controls.setter
    def expenditure_controls( self, value ):
        if value is not None:
            self.__expenditurecontrols = value

    @property
    def expense_controls( self ):
        if self.__expense_controls is not None:
            return self.__expensecontrols

    @expense_controls.setter
    def expense_controls( self, value ):
        if value is not None:
            self.__expensecontrols = value

    @property
    def reimbursement_controls( self ):
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @reimbursement_controls.setter
    def reimbursement_controls( self, value ):
        if value is not None:
            self.__reimbursementcontrols = value

    @property
    def reimbursable_agreement_controls( self ):
        if self.__reimbursableagreementcontrols is not NOne:
            return self.__reimbursableagreementcontrols

    @reimbursable_agreement_controls.setter
    def reimbursable_agreement_controls( self, value ):
        if value is not None:
            self.__reimbursableagreementcontrols = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if value is not None:
            self.__posted = value

    @property
    def carryover_in( self ):
        if isinstance( self.__carryoverin, float ):
            return self.__carryoverin

    @carryover_in.setter
    def carryover_in( self, value ):
        if value is not None:
            self.__carryoverin = value

    @property
    def carryover_out( self ):
        if self.__carryoverout is not None:
            return self.__carryoverout

    @carryover_out.setter
    def carryover_out( self, value ):
        if value is not None:
            self.__carryoverout = value

    @property
    def estimated_reimbursements( self ):
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @estimated_reimbursements.setter
    def estimated_reimbursements( self, value ):
        if value is not None:
            self.__estimatedreimbursements = value

    @property
    def estimated_recoveries( self ):
        if self.__estimatedrecoveries is not None:
            return self.__estimatedrecoveries

    @estimated_recoveries.setter
    def estimated_recoveries( self, value ):
        if value is not None:
            self.__estimatedrecoveries = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, efy = None,
                  fundcode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetDocuments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'BudgetDocumentsId',
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
                           'CarryOut',
                           'CarryIn',
                           'EstimatedRecoveries',
                           'EstimatedReimbursements' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetDocument'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetDocument'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# BudgetControl( fundcode, provider = Provider.SQLite )
class BudgetControl( ):
    '''object representing compass control data'''
    __source = None
    __provider = None
    __budgetcontrolsid = None
    __code = None
    __name = None
    __budgetedtranstype = None
    __postedtranstype = None
    __estimatedreimbursementstranstype = None
    __spendingadjustmenttranstype = None
    __estimatedrecoveriestranstype = None
    __actualrecoveriestranstype = None
    __statusreservetranstype = None
    __profitlosstranstype = None
    __estimatedreimbursementsspendingoptions = None
    __estimatedreimbursementsbudgetingoptions = None
    __trackagreementlowerlevels = None
    __budgetestimatedlowerlevels = None
    __recoverynextlevel = None
    __recoverybudgetmismatch = None
    __profitlossspendingoption = None
    __profitlossbudgetingoption = None
    __recoveriescarryinlowerlevelcontrol = None
    __recoveriescarryinlowerlevel = None
    __recoveriescarryinamountcontrol = None
    __budgetedcontrol = None
    __postedcontrol = None
    __precommitmentspendingcontrol = None
    __commitmentspendingcontrol = None
    __obligationspendingcontrol = None
    __accrualspendingcontrol = None
    __expenditurespendingcontrol = None
    __expensespendingcontrol = None
    __reimbursementspendingcontrol = None
    __reimbursableagreementspendingcontrol = None
    __ftebudgetingcontrol = None
    __ftespendingcontrol = None
    __transactiontypecontrol = None
    __authoritydistributioncontrol = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__budgetcontrolsid is not None:
            return self.__budgetcontrolsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__budgetcontrolsid = value

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__name = value

    @property
    def budgeted_transtype( self ):
        if self.__budgetedtranstype is not None:
            return self.__budgetedtranstype

    @budgeted_transtype.setter
    def budgeted_transtype( self, value ):
        if value is not None:
            self.__budgetedtranstype = value

    @property
    def posted_transtype( self ):
        if self.__postedtranstype is not None:
            return self.__postedtranstype

    @posted_transtype.setter
    def posted_transtype( self, value ):
        if value is not None:
            self.__postedtranstype = value

    @property
    def spending_adjustment_transtype( self ):
        if self.__spendingadjustmenttranstype is not None:
            return self.__spendingadjustmenttranstype

    @spending_adjustment_transtype.setter
    def spending_adjustment_transtype( self, value ):
        if value is not None:
            self.__spendingadjustmenttranstype = value

    @property
    def estimated_reimbursements_transtype( self ):
        if self.__estimatedreimbursementstranstype is not None:
            return self.__estimatedreimbursementstranstype

    @estimated_reimbursements_transtype.setter
    def estimated_reimbursements_transtype( self, value ):
        if value is not None:
            self.__estimatedreimbursementstranstype = value

    @property
    def estimated_recoveries_transtype( self ):
        if self.__estimatedrecoveriestranstype is not None:
            return self.__estimatedrecoveriestranstype

    @estimated_recoveries_transtype.setter
    def estimated_recoveries_transtype( self, value ):
        if value is not None:
            self.__estimatedrecoveriestranstype = value

    @property
    def actual_recoveries_transtype( self ):
        if self.__actualrecoveriestranstype is not None:
            return self.__actualrecoveriestranstype

    @actual_recoveries_transtype.setter
    def actual_recoveries_transtype( self, value ):
        if value is not None:
            self.__actualrecoveriestranstype = value

    @property
    def status_reserve_transtype( self ):
        if self.__statusreservetranstype is not None:
            return self.__statusreservetranstype

    @status_reserve_transtype.setter
    def status_reserve_transtype( self, value ):
        if value is not None:
            self.__statusreservetranstype = value

    @property
    def profit_loss_transtype( self ):
        if self.__profitlosstranstype is not None:
            return self.__profitlosstranstype

    @profit_loss_transtype.setter
    def profit_loss_transtype( self, value ):
        if value is not None:
            self.__profitlosstranstype = value

    @property
    def estimated_reimbursements_spending_options( self ):
        if self.__estimatedreimbursementsspendingoptions is not None:
            return self.__estimatedreimbursementsspendingoptions

    @estimated_reimbursements_spending_options.setter
    def estimated_reimbursements_spending_options( self, value ):
        if value is not None:
            self.__estimatedreimbursementsspendingoptions = value

    @property
    def estimated_reimbursements_budgeting_options( self ):
        if self.__estimatedreimbursementsbudgetingoptions is not None:
            return self.__estimatedreimbursementsbudgetingoptions

    @estimated_reimbursements_budgeting_options.setter
    def estimated_reimbursements_budgeting_options( self, value ):
        if value is not None:
            self.__estimatedreimbursementsbudgetingoptions = value

    @property
    def tracking_agreement_lower_levels( self ):
        if self.__trackingagreementlowerlevels is not None:
            return self.__trackingagreementlowerlevels

    @tracking_agreement_lower_levels.setter
    def tracking_agreement_lower_levels( self, value ):
        if value is not None:
            self.__trackingagreementlowerlevels = value

    @property
    def budget_estimated_lowerlevels( self ):
        if self.__budgetedestimatedlowerlevels is not None:
            return self.__budgetedestimatedlowerlevels

    @budget_estimated_lowerlevels.setter
    def budget_estimated_lowerlevels( self, value ):
        if value is not None:
            self.__budgetestimatedlowerlevels = value

    @property
    def recovery_nextlevel( self ):
        if self.__recoverynextlevel is not None:
            return self.__recoverynextlevel

    @recovery_nextlevel.setter
    def recovery_nextlevel( self, value ):
        if value is not None:
            self.__recoverynextlevel = value

    @property
    def recovery_budget_mismatch( self ):
        if self.__recoverybudgetmismatch is not None:
            return self.__recoverybudgetmismatch

    @recovery_budget_mismatch.setter
    def recovery_budget_mismatch( self, value ):
        if value is not None:
            self.__recoverybudgetmismatch = value

    @property
    def profit_loss_spending_option( self ):
        if self.__profitlossspendingoption is not None:
            return self.__profitlossspendingoption

    @profit_loss_spending_option.setter
    def profit_loss_spending_option( self, value ):
        if value is not None:
            self.__profitlossspendingoption = value

    @property
    def profit_loss_budgeting_option( self ):
        if self.__profitlossbudgetingoption is not None:
            return self.__profitlossbudgetingoption

    @profit_loss_budgeting_option.setter
    def profit_loss_budgeting_option( self, value ):
        if value is not None:
            self.__profitlossbudgetingoption = value

    @property
    def recoveries_carryin_lowerlevel_control( self ):
        if self.__recoveriescarryinlowerelevelcontrol is not None:
            return self.__recoveriescarryinlowerelevelcontrol

    @recoveries_carryin_lowerlevel_control.setter
    def recoveries_carryin_lowerlevel_control( self, value ):
        if value is not None:
            self.__recoveriescarryinlowerelevelcontrol = value

    @property
    def recoveries_carryin_lowerlevel( self ):
        if self.__recoveriescarryinlowerlevel is not None:
            return self.__recoveriescarryinlowerlevel

    @recoveries_carryin_lowerlevel.setter
    def recoveries_carryin_lowerlevel( self, value ):
        if value is not None:
            self.__recoveriescarryinlowerlevel = value

    @property
    def recoveries_carryin_amount_control( self ):
        if self.__recoveriescarryinamountcontrol is not None:
            return self.__recoveriescarryinamountcontrol

    @recoveries_carryin_amount_control.setter
    def recoveries_carryin_amount_control( self, value ):
        if value is not None:
            self.__recoveriescarryinamountcontrol = value

    @property
    def budgeted_control( self ):
        if self.__budgetedcontrol is not None:
            return self.__budgetedcontrol

    @budgeted_control.setter
    def budgeted_control( self, value ):
        if value is not None:
            self.__budgetedcontrol = value

    @property
    def posted_control( self ):
        if self.__postedcontrol is not None:
            return self.__postedcontrol

    @posted_control.setter
    def posted_control( self, value ):
        if value is not None:
            self.__postedcontrol = value

    @property
    def precommitment_spending_control( self ):
        if self.__precommitmentspendingcontrol is not None:
            return self.__precommitmentspendingcontrol

    @precommitment_spending_control.setter
    def precommitment_spending_control( self, value ):
        if value is not None:
            self.__precommitmentspendingcontrol = value

    @property
    def commitment_spending_control( self ):
        if self.__commitmentspendingcontrol is not None:
            return self.__commitmentspendingcontrol

    @commitment_spending_control.setter
    def commitment_spending_control( self, value ):
        if value is not None:
            self.__commitmentspendingcontrol = value

    @property
    def obligation_spending_control( self ):
        if self.__obligationspendingcontrol is not None:
            return self.__obligationspendingcontrol

    @obligation_spending_control.setter
    def obligation_spending_control( self, value ):
        if value is not None:
            self.__obligationspendingcontrol = value

    @property
    def accrual_spending_control( self ):
        if self.__accrualspendingcontrol is not None:
            return self.__accrualspendingcontrol

    @accrual_spending_control.setter
    def accrual_spending_control( self, value ):
        if value is not None:
            self.__accrualspendingcontrol = value

    @property
    def expenditure_spending_control( self ):
        if self.__expenditurespendingcontrol is not None:
            return self.__expenditurespendingcontrol

    @expenditure_spending_control.setter
    def expenditure_spending_control( self, value ):
        if value is not None:
            self.__expenditurespendingcontrol = value

    @property
    def expense_spending_control( self ):
        if self.__expensespendingcontrol is not None:
            return self.__expensespendingcontrol

    @expense_spending_control.setter
    def expense_spending_control( self, value ):
        if value is not None:
            self.__expensespendingcontrol = value

    @property
    def reimbursement_spending_control( self ):
        if self.__reimbursementspendingcontrol is not None:
            return self.__reimbursementspendingcontrol

    @reimbursement_spending_control.setter
    def reimbursement_spending_control( self, value ):
        if value is not None:
            self.__reimbursementspendingcontrol = value

    @property
    def reimbursableagreement_spending_control( self ):
        if self.__reimbursableagreementspendingcontrol is not None:
            return self.__reimbursableagreementspendingcontrol

    @reimbursableagreement_spending_control.setter
    def reimbursableagreement_spending_control( self, value ):
        if value is not None:
            self.__reimbursableagreementspendingcontrol = value

    @property
    def fte_budgeting_control( self ):
        if self.__ftebudgetingcontrol is not None:
            return self.__ftebudgetingcontrol

    @fte_budgeting_control.setter
    def fte_budgeting_control( self, value ):
        if value is not None:
            self.__ftebudgetingcontrol = value

    @property
    def fte_spending_control( self ):
        if  self.__ftespendingcontrol is not None:
            return self.__ftespendingcontrol

    @fte_spending_control.setter
    def fte_spending_control( self, value ):
        if value is not None:
            self.__ftespendingcontrol = value

    @property
    def transaction_type_control( self ):
        if  self.__transactiontypecontrol is not None:
            return self.__transactiontypecontrol

    @transaction_type_control.setter
    def transaction_type_control( self, value ):
        if value is not None:
            self.__transactiontypecontrol = value

    @property
    def authority_distribution_control( self ):
        if  self.__authoritydistributioncontrol is not None:
            return self.__authoritydistributioncontrol

    @authority_distribution_control.setter
    def authority_distribution_control( self, value ):
        if value is not None:
            self.__authoritydistributioncontrol = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, efy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetControls
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'BudgetControlValuesId',
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
                           'ProfLossTransType',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetControl'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetControl'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# BudgetFiscalYear( bfy, efy, date = None, provider = Provider.SQLite )
class BudgetFiscalYear( ):
    '''Class to describe the federal fiscal year'''
    __source = None
    __provider = None
    __budgetfiscalyearsid = None
    __input = None
    __bfy = None
    __efy = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = None
    __workdays = None
    __currentyear = None
    __currentmonth = None
    __currentday = None
    __holidays = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__budgetfiscalyearsid is not None:
            return self.__budgetfiscalyearsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__budgetfiscalyearsid = value

    @property
    def first_year( self ):
        if self.__bfy is not None:
            return self.__bfy

    @first_year.setter
    def first_year( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def last_year( self ):
        if self.__efy is not None:
            return self.__efy

    @last_year.setter
    def last_year( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def current_year( self ):
        if self.__currentyear is not None:
            return self.__currentyear

    @current_year.setter
    def current_year( self, value ):
        if value is not None:
            self.__currentyear = value

    @property
    def start_date( self ):
        if self.__startdate is not None:
            return self.__startdate

    @start_date.setter
    def start_date( self, value ):
        if value is not None:
            self.__startdate = value

    @property
    def end_date( self ):
        if self.__enddate is not None:
            return self.__enddate

    @end_date.setter
    def end_date( self, value ):
        if value is not None:
            self.__enddate = value

    @property
    def expiration( self ):
        if self.__expiration is not None:
            return self.__expiration

    @expiration.setter
    def expiration( self, value ):
        if value is not None:
            self.__expiration = value

    @property
    def weekends( self ):
        if self.__weekends is not None:
            return self.__weekends

    @weekends.setter
    def weekends( self, value ):
        if value is not None:
            self.__weekends = value

    @property
    def workdays( self ):
        if self.__workdays is not None:
            return self.__workdays

    @workdays.setter
    def workdays( self, value ):
        if value is not None:
            self.__workdays = value

    @property
    def today( self ):
        if self.__today is not None:
            return self.__today

    @today.setter
    def today( self, value ):
        if value is not None:
            self.__today = value

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @date.setter
    def date( self, value ):
        if value is not None:
            self.__date = value

    @property
    def current_day( self ):
        if self.__currentday is not None:
            return self.__currentday

    @current_day.setter
    def current_day( self, value ):
        if value is not None:
            self.__currentday = value

    @property
    def current_month( self ):
        if self.__currentmonth is not None:
            return self.__currentmonth

    @property
    def holidays( self ):
        if self.__holidays is not None:
            return self.__holidays

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if value is not None:
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, date = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source  = Source.FiscalYears
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__today = datetime.today( )
        self.__currentday = datetime.today( ).day
        self.__currentmonth = datetime.today( ).month
        self.__date = date if isinstance( date, datetime ) else datetime.today( )
        self.__currentyear = datetime.today( ).year
        self.__startdate = datetime( datetime.today( ).year, 10, 1 ) if isinstance( self.__currentyear, int ) else None
        self.__enddate = datetime( datetime.today( ).year + 1, 9, 30 ) if isinstance( self.__currentyear, int ) else None
        self.__holidays = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                            'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                            'Memorial', 'Juneteenth', 'Independence', 'Labor' ]
        self.__fields = [ 'FiscalYearsId',
                          'BFY',
                          'EFY',
                          'StartDate',
                          'EndDate',
                          'Columbus',
                          'Veterans',
                          'Thanksgiving',
                          'Christmas',
                          'NewYears',
                          'MartinLutherKing',
                          'Presidents',
                          'Memorial',
                          'Juneteenth',
                          'Independence',
                          'Labor',
                          'ExpiringYear',
                          'ExpirationDate',
                          'CancellationDate',
                          'Workdays',
                          'Weekdays',
                          'Weekends',
                          'Availability' ]

    def __str__( self ):
        if self.__bfy is not None:
            return self.__bfy

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetFiscalYear'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetFiscalYear'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# BudgetObjectClass( code, provider = Provider.SQLite  )
class BudgetObjectClass( ):
    '''Defines the BudgetObjectClass Class'''
    __source = None
    __provider = None
    __budgetobjectclassesid = None
    __code = None
    __boc = None
    __name = None
    __value = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__accountsid is not None:
            return self.__accountsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def value( self ):
        if self.__value is not None:
            return self.__value

    @value.setter
    def value( self, val ):
        if val is not None:
            self.__value = val

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if value is not None:
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetObjectClasses
        self.__code = code 
        self.__fields = [ 'BudgetObjectClassesId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetObjectClass'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetObjectClass'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# BudgetaryResourceExecution( bfy, efy, fundcode, provider = Provider.SQLite )
class BudgetaryResourceExecution( ):
    '''BudgetaryResourceExecution( bfy, efy, fundcode )
    initializes object representing the MAX A-11 DE/SF-133
    Status Of Budgetary Resources Execution Report'''
    __source = None
    __provider = None
    __budgetaryresourceexecutionid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__budgetaryresourceexecutionid is not None:
            return self.__budgetaryresourceexecutionid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__budgetaryresourceexecutionid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if  self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, ombcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetResourceExecution
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = ombcode
        self.__fields = [ 'BudgetaryResourceExecutionId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            v = (self.__bfy, self.__efy, self.__budgetaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetaryResourceExecution'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetaryResourceExecution'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# BudgetOutlay( account, provider = Provider.SQLite )
class BudgetOutlay( ):
    '''BudgetOutlay( bfy, omb )
    object provides OMB data'''
    __source = None
    __provider = None
    __budgetoutlaysid = None
    __reportyear = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __linenumber = None
    __linesection = None
    __linename = None
    __linecategory = None
    __beacategory = None
    __beacategoryname = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__budgetoutlaysid is not None:
            return self.__budgetoutlaysid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__budgetoutlaysid = value

    @property
    def report_year( self ):
        if self.__reportyear is not None:
            return self.__reportyear

    @report_year.setter
    def report_year( self, value ):
        if value is not None:
            self.__reportyear = value

    @property
    def line_number( self ):
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_section( self ):
        if self.__linesection is not None:
            return self.__linesection

    @line_section.setter
    def line_section( self, value ):
        if value is not None:
            self.__linesection = value

    @property
    def line_name( self ):
        if self.__linename is not None:
            return self.__linename

    @line_name.setter
    def line_name( self, value ):
        if value is not None:
            self.__linename = value

    @property
    def line_category( self ):
        if self.__linecategory is not None:
            return self.__linecategory

    @line_category.setter
    def line_category( self, value ):
        if value is not None:
            self.__linecategory = value

    @property
    def bea_category( self ):
        if self.__beacategory is not None:
            return self.__beacategory

    @bea_category.setter
    def bea_category( self, value ):
        if value is not None:
            self.__beacategory = value

    @property
    def bea_category_name( self ):
        if  self.__beacategoryname is not None:
            return self.__beacategoryname

    @bea_category_name.setter
    def bea_category_name( self, value ):
        if value is not None:
            self.__beacategoryname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def prior_year( self ):
        if self.__prioryear is not None:
            return self.__prioryear

    @prior_year.setter
    def prior_year( self, value ):
        if value is not None:
            self.__prioryear = value

    @property
    def current_year( self ):
        if self.__currentyear is not None:
            return self.__currentyear

    @current_year.setter
    def current_year( self, value ):
        if  value is not None:
            self.__currentyear = value

    @property
    def budget_year( self ):
        if self.__budgetyear is not None:
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value ):
        if value is not None:
            self.__budgetyear = value

    @property
    def out_year_1( self ):
        if self.__outyear1 is not None:
            return self.__outyear1

    @out_year_1.setter
    def out_year_1( self, value ):
        if value is not None:
            self.__outyear1 = value

    @property
    def out_year_2( self ):
        if self.__outyear2 is not None:
            return self.__outyear2

    @out_year_2.setter
    def out_year_2( self, value ):
        if value is not None:
            self.__outyear2 = value

    @property
    def out_year_3( self ):
        if isinstance( self.__outyear3, float ):
            return self.__outyear3

    @out_year_3.setter
    def out_year_3( self, value ):
        if value is not None:
            self.__outyear3 = value

    @property
    def out_year_4( self ):
        if isinstance( self.__outyear4, float ):
            return self.__outyear4

    @out_year_4.setter
    def out_year_4( self, value ):
        if value is not None:
            self.__outyear4 = value

    @property
    def out_year_5( self ):
        if self.__outyear5 is not None:
            return self.__outyear5

    @out_year_5.setter
    def out_year_5( self, value ):
        if value is not None:
            self.__outyear5 = value

    @property
    def out_year_6( self ):
        if self.__outyear6 is not None:
            return self.__outyear6

    @out_year_6.setter
    def out_year_6( self, value ):
        if value is not None:
            self.__outyear6 = value

    @property
    def out_year_7( self ):
        if self.__outyear7 is not None:
            return self.__outyear7

    @out_year_7.setter
    def outyear7( self, value ):
        if value is not None:
            self.__outyear7 = value

    @property
    def out_year_8( self ):
        if self.__outyear8 is not None:
            return self.__outyear8

    @out_year_8.setter
    def out_year_8( self, value ):
        if value is not None:
            self.__outyear8 = value

    @property
    def out_year_9( self ):
        if self.__outyear9 is not None:
            return self.__outyear9

    @out_year_9.setter
    def out_year_9( self, value ):
        if value is not None:
            self.__outyear9 = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetOutlays
        self.__budgetaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'BudgetOutlaysId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'OmbAccountCode', ]
            v = (self.__budgetaccountcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetOutlay'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetOutlay'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CongressionalControl( bfy, fund, provider = Provider.SQLite )
class CongressionalControl( ):
    '''object representing congressional control data'''
    __source = None
    __provider = None
    __congressionalcontrolsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __subprojectcode = None
    __subprojectname = None
    __reprogrammingrestriction = None
    __increaserestriction = None
    __decreaserestriction = None
    __memorandumrequired = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__congressionalcontrolsid is not None:
            return self.__congressionalcontrolsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__congressionalcontrolsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def sub_project_code( self ):
        if self.__subprojectcode is not None:
            return self.__subprojectcode

    @sub_project_code.setter
    def sub_project_code( self, value ):
        if value is not None:
            self.__subprojectcode = value

    @property
    def sub_project_name( self ):
        if self.__subprojectname is not None:
            return self.__subprojectname

    @sub_project_name.setter
    def sub_project_name( self, value ):
        if value is not None:
            self.__subprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def reprogramming_restriction( self ):
        if self.__reprogrammingrestriction is not None:
            return self.__reprogrammingrestriction

    @reprogramming_restriction.setter
    def reprogramming_restriction( self, value ):
        if value is not None:
            self.__reprogrammingrestriction = value

    @property
    def increase_restriction( self ):
        if self.__increaserestriction is not None:
            return self.__increaserestriction

    @increase_restriction.setter
    def increase_restriction( self, value ):
        if value is not None:
            self.__increaserestriction = value

    @property
    def decrease_restriction( self ):
        if self.__decreaserestriction is not None:
            return self.__decreaserestriction

    @decrease_restriction.setter
    def decrease_restriction( self, value ):
        if value is not None:
            self.__decreaserestriction = value

    @property
    def memorandum_required( self ):
        if self.__memorandumrequired is not None:
            return self.__memorandumrequired

    @memorandum_required.setter
    def memorandum_required( self, value ):
        if value is not None:
            self.__memorandumrequired = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fundcode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CongressionalControls
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'CongressionalControlsId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'CongressionalControl'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

# CompassLevel( bfy, efy, fund, provider = Provider.SQLite )
class CompassLevel( ):
    '''object representing Compass data levels 1-7'''
    __source = None
    __provider = None
    __compasslevelsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __appropriationcode = None
    __subappropriationcode = None
    __appropriationname = None
    __treasurysymbol = None
    __documenttype = None
    __lowername = None
    __description = None
    __postedcontrolflag = None
    __actualrecoverytranstype = None
    __commitmentspendingcontrolflag = None
    __budgetdefault = None
    __lowerchildexpenditurecontrolflag = None
    __lowerchildexpensespendingcontrolflag = None
    __ftecontrolflag = None
    __accrualspendigcontrolflag = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __lowercommitmentspendingcontrolflag = None
    __lowerobligationspendingcontrolflag = None
    __lowerexpenditurespendingcontrolflag = None
    __lowerexpensespendingcontrolflag = None
    __lowerpostedcontrolflag = None
    __lowerpostedtranstype = None
    __lowerpostedflag = None
    __lowerprecommitmentspendingcontrolflag = None
    __lowerrecoveriesspendingoption = None
    __lowerrecoveriesoption = None
    __lowerreimbursablespendingoption = None
    __date = None
    __totalauthority = None
    __originalauthority = None
    __carryoveravailabilitypercentage = None
    __carryoverin = None
    __carryoverout = None
    __fundsin = None
    __fundsout = None
    __recoverieswithdrawn = None
    __actualrecoveries = None
    __actualreimbursements = None
    __agreementreimbursables = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__compasslevelsid is not None:
            return self.__compasslevelsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__compasslevelsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def appropriation_code( self ):
        if self.__appropriationcode is not None:
            return self.__appropriationcode

    @appropriation_code.setter
    def appropriation_code( self, value ):
        if value is not None:
            self.__appropriationcode = value

    @property
    def appropriation_name( self ):
        if self.__appropriationname is not None:
            return self.__appropriationname

    @appropriation_name.setter
    def appropriation_name( self, value ):
        if value is not None:
            self.__appropriationname = value

    @property
    def sub_appropriation_code( self ):
        if self.__subappropriationcode is not None:
            return self.__subappropriationcode

    @sub_appropriation_code.setter
    def sub_appropriation_code( self, value ):
        if value is not None:
            self.__subappropriationcode = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CompassLevels
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'CompassLevelsId',
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
                           'AgreementReimbursables' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'CompassLevel'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'CompassLevel'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Commitment( bfy, fund, account, boc, provider = Provider.SQLite )
class Commitment( ):
    '''Defines the CommitmentS class.'''
    __source = None
    __provider = None
    __opencommitmentsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__expendituresid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if self.__referencedocumentnumbe is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ):
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if  self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if  self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.OpenCommitments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'CommitmentsId',
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
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Commitment'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Commitment'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CarryoverOutlay( bfy, omb, provider = Provider.SQLite )
class CarryoverOutlay( ):
    ''' object provides OMB data '''
    __source = None
    __provider = None
    __carryoveroutlaysid = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __linenumber = None
    __carryover = None
    __carryoveroutlays = None
    __budgetyear = None
    __budgetyearadjustment = None
    __currentyear = None
    __currentyearadjustment = None
    __delta = None
    __avaiablebalance = None
    __ulo = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None


    @property
    def id( self ):
        if isinstance( self.__carryoveroutlaysid, int ):
            return self.__carryoveroutlaysid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__carryoveroutlaysid = value

    @property
    def budget_year( self ):
        if self.__budgetyear is not None:
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value ):
        if value is not None:
            self.__budgetyear = value

    @property
    def line_number( self ):
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def carryover( self ):
        if self.__carryover is not None:
            return self.__carryover

    @carryover.setter
    def carryover( self, value ):
        if value is not None:
            self.__carryover = value

    @property
    def carryover_outlays( self ):
        if self.__carryoveroutlays is not None:
            return self.__carryoveroutlays

    @carryover_outlays.setter
    def carryover_outlays( self, value ):
        if value is not None:
            self.__carryoveroutlays = value

    @property
    def unliquidated_obligations( self ):
        if self.__ulo is not None:
            return self.__ulo

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__ulo = value

    @property
    def delta( self ):
        if self.__delta is not None:
            return self.__delta

    @delta.setter
    def delta( self, value ):
        if isinstance( value, float ) and value > 0:
            self.__delta = value

    @property
    def available_balance( self ):
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available_balance.setter
    def available_balance( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def current_year( self ):
        if self.__currentyear is not None:
            return self.__currentyear

    @current_year.setter
    def current_year( self, value ):
        if value is not None:
            self.__currentyear = value

    @property
    def current_year_adjustment( self ):
        if self.__currentyearadjustment is not None:
            return self.__currentyearadjustment

    @current_year_adjustment.setter
    def current_year_adjustment( self, value ):
        if value is not None:
            self.__currentyearadjustment = value

    @property
    def budget_year( self ):
        if self.__budgetyear is not None:
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value ):
        if value is not None:
            self.__budgetyear = value

    @property
    def budget_year_adjustment( self ):
        if self.__budgetyearadjustment is not None:
            return self.__budgetyearadjustment

    @budget_year_adjustment.setter
    def budget_year_adjustment( self, value ):
        if value is not None:
            self.__budgetyearadjustment = value

    @property
    def out_year_1( self ):
        if self.__outyear1 is not None:
            return self.__outyear1

    @out_year_1.setter
    def out_year_1( self, value ):
        if value is not None:
            self.__outyear1 = value

    @property
    def out_year_2( self ):
        if self.__outyear2 is not None:
            return self.__outyear2

    @out_year_2.setter
    def out_year_2( self, value ):
        if value is not None:
            self.__outyear2 = value

    @property
    def out_year_3( self ):
        if self.__outyear3 is not None:
            return self.__outyear3

    @out_year_3.setter
    def out_year_3( self, value ):
        if value is not None:
            self.__outyear3 = value

    @property
    def out_year_4( self ):
        if self.__outyear4 is not None:
            return self.__outyear4

    @out_year_4.setter
    def out_year_4( self, value ):
        if value is not None:
            self.__outyear4 = value

    @property
    def out_year_5( self ):
        if self.__outyear5 is not None:
            return self.__outyear5

    @out_year_5.setter
    def out_year_5( self, value ):
        if value is not None:
            self.__outyear5 = value

    @property
    def out_year_6( self ):
        if self.__outyear6 is not None:
            return self.__outyear6

    @out_year_6.setter
    def out_year_6( self, value ):
        if value is not None:
            self.__outyear6 = value

    @property
    def out_year_7( self ):
        if self.__outyear7 is not None:
            return self.__outyear7

    @out_year_7.setter
    def outyear7( self, value ):
        if value is not None:
            self.__outyear7 = value

    @property
    def out_year_8( self ):
        if self.__outyear8 is not None:
            return self.__outyear8

    @out_year_8.setter
    def out_year_8( self, value ):
        if value is not None:
            self.__outyear8 = value

    @property
    def out_year_9( self ):
        if self.__outyear9 is not None:
            return self.__outyear9

    @out_year_9.setter
    def out_year_9( self, value ):
        if value is not None:
            self.__outyear9 = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, omb, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverOutlays
        self.__budgetyear = bfy if isinstance( bfy, str ) and bfy != '' else None
        self.__budgetaccountcode = omb if isinstance( omb, str ) and omb != '' else None
        self.__fields = [ 'CarryoverOutlaysId',
                          'ReportYear',
                          'AgencyName',
                          'OmbAccountName',
                          'LINE',
                          'Carryover',
                          'CarryoverOutlay',
                          'Delta',
                          'AvailableBalance',
                          'ULO',
                          'CurrentYearAdjustment',
                          'BudgetYearAdjustment',
                          'CurrentYear',
                          'BudgetYear',
                          'OutYear1',
                          'OutYear2',
                          'OutYear3',
                          'OutYear4',
                          'OutYear5',
                          'OutYear6',
                          'OutYear7',
                          'OutYear8',
                          'OutYear9' ]

    def get_data( self  ):
        try:
            source = Source.CarryoverOutlays
            provider = Provider.SQLite
            n = [ 'BudgetYear', 'OmbAccountCode' ]
            v = (self.__budgetyear, self.__budgetaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverOutlay'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverOutlay'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CostArea( fundcode, provider = Provider.SQLite )
class CostArea( ):
    __source = None
    __provider = None
    __code = None
    __fields = None

    @property
    def id( self ):
        if isinstance( self.__transfersid, int ):
            return self.__transfersid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__transfersid = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__code = code 
        self.__provider = provider
        self.__fields = [ 'CostAreasId',
                          'Code',
                          'Name' ]

# CarryoverSurvey( bfy, efy, fund, provider = Provider.SQLite )
class CarryoverSurvey( ):
    '''CarryoverSurvey( bfy ) initializes object
    providing carry_over survey data'''
    __source = None
    __provider = None
    __carryoversurveyid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__allocationsid, int ):
            return self.__allocationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__allocationsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverSurvey
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'CarryoverSurveyId',
                          'FundCode',
                          'FundName',
                          'Amount' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode', ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverOutlay'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarrryoverOutlays'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CapitalPlanningInvestmentCodes( treas, provider = Provider.SQLite  )
class CapitalPlanningInvestmentCodes( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __capitalplanninginvestmentcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__capitalplanninginvestmentcodesid, int ):
            return self.__capitalplanninginvestmentcodesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CapitalPlanningInvestmentCodes
        self.__code = code
        self.__fields = [ 'CpicId',
                          'Type'
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = ( self.__code, )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ITProjectCode'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ITProjectCode'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ColumnSchema( column, table, provider = Provider.SQLite )
class ColumnSchema( ):
    '''Provides data on the columns used in the application'''
    __source = None
    __provider = None
    __columnschemaid = None
    __datatype = None
    __columnname = None
    __tablename = None
    __columncaption = None
    __fields = None
    __data = None
    __frame = None


    @property
    def id( self ):
        if self.__columnschemaid is not None:
            return self.__columnschemaid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__columnschemaid = value

    @property
    def data_type( self ):
        if self.__datatype is not None:
            return self.__datatype

    @data_type.setter
    def data_type( self, value ):
        if value is not None:
            self.__datatype = value

    @property
    def column_name( self ):
        if self.__columnname is not None:
            return self.__columnname

    @column_name.setter
    def column_name( self, value ):
        if value is not None:
            self.__columnname = value

    @property
    def table_name( self ):
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value ):
        if value is not None:
            self.__tablename = value

    @property
    def column_caption( self ):
        if self.__columncaption is not None:
            return self.__columncaption

    @column_caption.setter
    def column_caption( self, value ):
        if value is not None:
            self.__columncaption = value

    def __init__( self, column, table, provider = Provider.SQLite ):
        self.__source = Source.ColumnSchema
        self.__provider = provider
        self.__columnname = column
        self.__tablename = table

# DataRuleDescription( schedule, line, rule, provider = Provider.SQLite )
class DataRuleDescription( ):
    ''' DataRuleDescription( schedule, line, rule )
    initializes object providing OMB MAX A11 rule data '''
    __source = None
    __provider = None
    __dataruledescriptionsid = None
    __schedule = None
    __linenumber = None
    __rulenumber = None
    __ruledescription = None
    __scheduleorder = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__dataruledescriptionsid, int ):
            return self.__dataruledescriptionsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__dataruledescriptionsid = value

    @property
    def schedule( self ):
        if isinstance( self.__schedule, str ) and self.__schedule != '':
            return self.__schedule

    @schedule.setter
    def schedule( self, value ):
        if value is not None:
            self.__schedule = value

    @property
    def line_number( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_description( self ):
        if isinstance( self.__linedescription, str ) and self.__linedescription != '':
            return self.__linedescription

    @line_description.setter
    def line_description( self, value ):
        if value is not None:
            self.__linedescription = value

    @property
    def rule_number( self ):
        if isinstance( self.__rulenumber, str ) and self.__rulenumber != '':
            return self.__rulenumber

    @rule_number.setter
    def rule_number( self, value ):
        if value is not None:
            self.__rulenumber = value

    @property
    def rule_description( self ):
        if isinstance( self.__ruledescription, str ) and self.__ruledescription != '':
            return self.__ruledescription

    @rule_description.setter
    def rule_description( self, value ):
        if value is not None:
            self.__ruledescription = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, schedule, line, rule, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.DataRuleDescriptions
        self.__schedule = schedule
        self.__linenumber = line
        self.__rulenumber = rule
        self.__fields = [ 'DataRuleDescriptionsId',
                          'Schedule',
                          'LineNumber',
                          'RuleNumber',
                          'RuleDescription',
                          'ScheduleOrder' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Schedule', 'LineNumber', 'RuleNumber' ]
            v = (self.__schedule, self.__linenumber, self.__rulenumber)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'DataRuleDescription'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'DataRuleDescription'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Defacto( bfy, fund, provider = Provider.SQLite )
class Defacto( ):
    '''object representing defacto obligations'''
    __source = None
    __provider = None
    __defactosid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.Defactos
        self.__provider = provider
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'DefactosId',
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
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Defacto'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Defacto'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Deobligation( bfy, fund, account, boc, provider = Provider.SQLite )
class Deobligation( ):
    '''Deobligation( bfy, fund, account, boc )
    initializes object providing Deobligation data '''
    __source = None
    __provider = None
    __deobligationsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__deobligationsid, int ):
            return self.__deobligationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__deobligationsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if value is not None:
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ):
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ):
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Deobligations
        self.__bfy = bfy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'DeobligationsId',
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

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Deobligations'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Deobligations'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# DocumentControlNumber( dcn, provider = Provider.SQLite )
class DocumentControlNumber( ):
    ''' object provides DCN data'''
    __source = None
    __provider = None
    __documentcontrolnumbersid = None
    __rpiocode = None
    __rpioname = None
    __documenttype = None
    __documentnumber = None
    __documentprefix = None
    __documentcontrolnumber = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__documentcontrolnumbersid is not None:
            return self.__documentcontrolnumbersid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__documentcontrolnumbersid = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_prefix( self ):
        if self.__documentprefix is not None:
            return self.__documentprefix

    @document_prefix.setter
    def document_prefix( self, value ):
        if value is not None:
            self.__documentprefix = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, dcn, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.DocumentControlNumbers
        self.__documentcontrolnumber = dcn
        self.__fields = [ 'DocumentControlNumbersId',
                           'RpioCode',
                           'RpioName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentPrefix',
                           'DocumentControlNumbe' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'DocumentControlNumber', ]
            v = (self.__dcn,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'DocumentControlNumber'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'DocumentControlNumber'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Expenditure( bfy, fund, account, boc, provider = Provider.SQLite )
class Expenditure( ):
    '''Expenditure( bfy, fund, account, fundcode, provider = Provider.SQLite )
    initializes object providing Expenditure data'''
    __source = None
    __provider = None
    __expendituresid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__expendituresid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if value is not None:
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ):
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ):
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, fund , account,
                  boc, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Expenditures
        self.__bfy = bfy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'ExpendituresId',
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

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Expenditure'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Expenditure'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# FinanceObjectClass( treas, provider = Provider.SQLite  )
class FinanceObjectClass( ):
    '''Defines the Finance Object Class'''
    __source = None
    __provider = None
    __financeobjectclassesid = None
    __code = None
    __name = None
    __boccode = None
    __bocname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__financeobjectclassesid is not None:
            return self.__financeobjectclassesid

    @id.setter
    def id( self, id ):
        if id is not None:
            self.__financeobjectclassesid = id

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, name ):
        if  name is not None:
            self.__bocname = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if list is not None:
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FinanceObjectClasses
        self.__code = code
        self.__fields = [ 'FinanceObjectClassesId',
                          'Code',
                          'Name',
                          'BocCode',
                          'BocName' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FinanceObjectClass'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FinanceObjectClass'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Fund( bfy, efy, fundcode, provider = Provider.SQLite )
class Fund( ):
    '''Defines the Fund Class'''
    __source = None
    __provider = None
    __fundsid = None
    __code = None
    __name = None
    __bfy = None
    __efy = None
    __shortname = None
    __status = None
    __beginningperiodofavailability = None
    __endingperiodofavailability = None
    __main = None
    __multiyearindicator = None
    __sublevelprefix = None
    __allocationtransferagency = None
    __agencyidentifier = None
    __fundcategory = None
    __appropriationcode = None
    __appropriationname = None
    __fundgroup = None
    __noyear = None
    __carryover = None
    __cancelledyearspendingaccount = None
    __applyatalllevels = None
    __batsfund = None
    __batsenddate = None
    __batsoptionid = None
    __securityorg = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __apportionmentaccountcode = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        ''' Gets the 'id' property '''
        if self.__fundsid is not None:
            return self.__fundsid

    @id.setter
    def id( self, value ):
        ''' Sets the 'id' property '''
        if value is not None:
            self.__fundsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def short_name( self ):
        if self.__shortname is not None:
            return self.__shortname

    @short_name.setter
    def short_name( self, value ):
        if value is not None:
            self.__shortname = value

    @property
    def status( self ):
        if self.__status is not None:
            return self.__status

    @status.setter
    def status( self, value ):
        if isinstance( value, str ) and value in [ 'ACTIVE', 'INACTIVE' ]:
            self.__status = value

    @property
    def bpoa( self ):
        if self.__beginningperiodofavailability is not None:
            return self.__beginningperiodofavailability

    @bpoa.setter
    def bpoa( self, value ):
        if value is not None:
            self.__beginningperiodofavailability = value

    @property
    def epoa( self ):
        if self.__endingperiodofavailability is not None:
            return self.__endingperiodofavailability

    @epoa.setter
    def epoa( self, value ):
        if value is not None:
            self.__endingperiodofavailability = value

    @property
    def main( self ):
        if self.__main is not None:
            return self.__main

    @main.setter
    def main( self, value ):
        if value is not None:
           self.__main = value

    @property
    def multiyear_indicator( self ):
        if self.__multiyearindicator is not None:
            return self.__multiyearindicator

    @multiyear_indicator.setter
    def multiyear_indicator( self, value ):
        if value is not None:
            self.__multiyearindicator = value

    @property
    def sub_level( self ):
        if self.__sublevelprefix is not None:
            return self.__sublevelprefix

    @sub_level.setter
    def sub_level( self, value ):
        if value is not None:
            self.__sublevelprefix = value

    @property
    def allocation_transfer_agency( self ):
        if self.__allocationtransferagency is not None:
            return self.__allocationtransferagency

    @allocation_transfer_agency.setter
    def allocation_transfer_agency( self, value ):
        if value is not None:
            self.__allocationtransferagency = value

    @property
    def agency_identifier( self ):
        if self.__agencyidentifier is not None:
            return self.__agencyidentifier

    @agency_identifier.setter
    def agency_identifier( self, value ):
        if value is not None:
            self.__agencyidentifier = value

    @property
    def fund_category( self ):
        if self.__fundcategory is not None:
            return self.__fundcategory

    @fund_category.setter
    def fund_category( self, value ):
        if value is not None:
            self.__fundcategory = value

    @property
    def appropriation_code( self ):
        if self.__appropriationcode is not None:
            return self.__appropriationcode

    @appropriation_code.setter
    def appropriation_code( self, value ):
        if value is not None:
            self.__appropriationcode = value

    @property
    def appropriation_name( self ):
        if self.__appropriationname is not None:
            return self.__appropriationname

    @appropriation_name.setter
    def appropriation_name( self, name ):
        if  name is not None:
            self.__appropriationname = name

    @property
    def fund_group( self ):
        if self.__fundgroup is not None:
            return self.__fundgroup

    @fund_group.setter
    def fund_group( self, value ):
        if value is not None:
            self.__fundgroup = value

    @property
    def no_year( self ):
        if self.__noyear is not None:
            return self.__noyear

    @no_year.setter
    def no_year( self, value ):
        if value is not None:
            self.__noyear = value

    @property
    def carry_over( self ):
        if self.__carryover is not None:
            return self.__carryover

    @carry_over.setter
    def carry_over( self, value ):
        if value is not None:
            self.__carryover = value

    @property
    def cancelled_spending_account( self ):
        if self.__cancelledyearspendingaccount is not None:
            return self.__cancelledyearspendingaccount

    @cancelled_spending_account.setter
    def cancelled_spending_account( self, acct ):
        if  acct is not None:
            self.__cancelledyearspendingaccount = acct

    @property
    def apply_all_levels( self ):
        if  self.__applyatalllevels is not None:
            return self.__applyatalllevels

    @apply_all_levels.setter
    def apply_all_levels( self, value ):
        if value is not None:
           self.__applyatalllevels = value

    @property
    def bats_fund( self ):
        if self.__batsfund is not None:
            return self.__batsfund

    @bats_fund.setter
    def bats_fund( self, value ):
        if value is not None:
            self.__batsfund = value

    @property
    def bats_end_date( self ):
        if self.__batsenddate is not None:
            return self.__batsenddate

    @bats_end_date.setter
    def bats_end_date( self, value ):
        if isinstance( value, datetime ):
            self.__batsenddate = value

    @property
    def bats_option_id( self ):
        if self.__batsoptionid is not None:
            return self.__batsoptionid

    @bats_option_id.setter
    def bats_option_id( self, value ):
        if value is not None:
            self.__batsoptionid = value

    @property
    def security_org( self ):
        if self.__securityorg is not None:
            return self.__securityorg

    @security_org.setter
    def security_org( self, value ):
        if value is not None:
            self.__securityorg = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def apportionment_account_code( self ):
        if self.__apportionmentaccountcode is not None:
            return self.__apportionmentaccountcode

    @apportionment_account_code.setter
    def apportionment_account_code( self, value ):
        if value is not None:
            self.__apportionmentaccountcode = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Funds
        self.__bfy = bfy 
        self.__efy = efy 
        self.__code = code 
        self.__fields = [ 'FundsId',
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

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'Code', ]
            v = (self.__bfy, self.__efy, self.__code)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Fund'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Fund'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# FederalHoliday( bfy, efy, name, provider = Provider.SQLite )
class FederalHoliday( ):
    '''Defines the FederalHoliday class'''
    __source = None
    __provider = None
    __federalholidaysid = None
    __bfy = None
    __efy = None
    __name = None
    __newyearsday = None
    __martinlutherking = None
    __memorial = None
    __juneteenth = None
    __independence = None
    __washingtons = None
    __labor = None
    __columbus = None
    __veterans = None
    __thanksgiving = None
    __christmas = None
    __list = None
    __today = None
    __date = None
    __dayofweek = None
    __day = None
    __month = None
    __year = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__federalholidaysid is not None:
            return self.__federalholidaysid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__federalholidaysid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value in self.__list:
            self.__name = value

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @property
    def month( self ):
        if self.__month is not None:
            return self.__month

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def list( self ):
        if self.__list is not None:
            return self.__list

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def observances( self ):
        if isinstance( self.__observance, dict ):
            return self.__observance

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, name = '', provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FederalHolidays
        self.__list = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                        'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                        'Memorial', 'Juneteenth', 'Independence', 'Labor' ]
        self.__observance = { 'Columbus': 'The second Monday in October',
                              'Veterans': 'Veterans Day, November 11',
                              'Thanksgiving': 'The fourth Thursday in November',
                              'Christmas': 'Christmas Day, December 25',
                              'NewYearsDay': 'January 1',
                              'MartinLutherKing': 'The third Monday in January',
                              'Washingtons': 'The third Monday in February',
                              'Memorial': 'The last Monday in May.',
                              'Juneteenth': 'Juneteenth National Independence Day, June 19',
                              'Independence': 'Independence Day, July 4',
                              'Labor': 'The first Monday in September' }
        self.__bfy = bfy
        self.__efy = efy
        self.__year = int( bfy )
        self.__today = dt.datetime.today( )
        self.__name = self.set_name( name )
        self.__date = self.set_date( name )
        self.__dayofweek = self.__date.day
        self.__month = self.__date.month
        self.__day = self.__date.isoweekday( )
        self.__fields = [ 'FederalHolidaysId',
                          'BFY',
                          'Columbus',
                          'Veterans',
                          'Thanksgiving',
                          'Christmas',
                          'NewYears',
                          'MartinLutherKing',
                          'Presidents',
                          'Memorial',
                          'Juneteenth',
                          'Independence',
                          'Labor' ]
        self.__data = None
        self.__frame = None

    def __str__( self ):
        if not self.__name == '':
            return self.__name

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'Name', ]
            v = (self.__bfy, self.__efy, self.__name,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

    def columbus_day( self ):
        '''The second Monday in October'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 10, 1 )
                __end = datetime( self.__year, 10, 31 )
                __delta = ( __start - __end ).days
                for i in range( 1, 31 ):
                    d = datetime( self.__year, 10, __start.day + i )
                    if ( 15 < d.day < 28 ) and datetime( self.__year, 10, d.day ).isoweekday( ) == 1:
                        self.__columbus = datetime( self.__year, 10, d.day )
                        return self.__columbus
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'columnbusday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def veterans_day( self ):
        '''Veterans Day, November 11'''
        try:
            if self.__year is not None:
                self.__veterans = datetime( self.__year, 11, 11 )
                return self.__veterans
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'veterans_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def thanksgiving_day( self ):
        '''The fourth Thursday in November'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 11, 15 )
                __end = datetime( self.__year, 11, 30 )
                __delta = ( __start - __end ).days
                for i in range( 15, 31 ):
                    d = datetime( self.__year, 11, i )
                    if ( 21 < d.day < 31 ) and datetime( self.__year, 11, d.day ).isoweekday( ) == 4:
                        self.__thanksgiving = datetime( self.__year, 11, d.day )
                        return self.__thanksgiving
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'thanksgiving_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def christmas_day( self ):
        '''Christmas Day, December 25'''
        try:
            if self.__year is not None:
                self.__christmas = datetime( self.__year, 12, 25 )
                return self.__christmas
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'christmas_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def new_years_day( self ):
        '''January 1'''
        try:
            if self.__year is not None:
                self.__newyearsday = datetime( self.__year, 1, 1 )
                return self.__newyearsday
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'new_years_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def martinlutherkings_day( self ):
        '''The third Monday in January'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 1, 15 )
                __end = datetime( self.__year, 1, 31 )
                __delta = ( __start - __end ).days
                for i in range( __delta ):
                    d = datetime( self.__year, 1, __start.day + i )
                    if ( 15 < d.day < 31) and datetime( self.__year, 1, d.day ).isoweekday( ) == 1:
                        self.__martinlutherking = datetime( self.__year, 1, d.day )
                        return self.__martinlutherking
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'martinlutherkings_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def washingtons_day( self ):
        '''The third Monday in February'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 2, 15 )
                __end = datetime( self.__year, 2, 28 )
                __delta = ( __start - __end ).days
                for i in range( __delta ):
                    d = datetime( self.__year, 2, __start.day + i )
                    if (15 < d.day < 28) and datetime( self.__year, 2, d.day ).isoweekday( ) == 1:
                        self.__washingtons = datetime( self.__year, 2, d.day )
                        return self.__washingtons
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'washingtons_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def memorial_day( self ):
        '''The last Monday in May'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 5, 1 )
                __end = datetime( self.__year, 5, 31 )
                __delta = ( __start - __end ).days
                for i in range( 15, 31 ):
                    d = datetime( self.__year, 5, i )
                    if ( 21 < d.day < 31 ) and datetime( self.__year, 5, d.day ).isoweekday( ) == 1:
                        self.__memorial = datetime( self.__year, 5, d.day )
                        return self.__memorial
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'memorial_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def juneteenth_day( self ):
        '''Juneteenth National Independence Day, June 19'''
        try:
            if self.__year is not None:
                self.__juneteenth = datetime( self.__year, 6, 19 )
                return self.__juneteenth
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'juneteenth_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def independence_day( self ):
        '''Independence Day, July 4'''
        try:
            if self.__year is not None:
                self.__independence = datetime( self.__year, 7, 4 )
                return self.__independence
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'independence_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def labor_day( self ):
        '''The first Monday in September'''
        try:
            if self.__year is not None:
                __monday = list( )
                __month = dt.date( self.__year, 9, 1 ) - dt.date( self.__year, 9, 31 )
                for i in range( 1, __month.days - 1 ):
                    if datetime( self.__year, 9, i ).isoweekday( ) == 1:
                        __monday.append( datetime( self.__year, 9, i ) )
                y = __monday[ 0 ].date( ).year
                m = __monday[ 0 ].date( ).currentmonth
                d = __monday[ 0 ].date( ).currentday
                self.__labor = datetime( y, m, d )
                return self.__labor
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'labor_day( self )'
            err = ErrorDialog( exc )
            err.show( )

    def day_of_week( self ):
        try:
            if 0 < self.__day < 8 and  self.__day == 1:
                self.__dayofweek = 'Monday'
                return self.__dayofweek
            elif 0 <  self.__day < 8 and  self.__day == 2:
                self.__dayofweek = 'Tuesday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 3:
                self.__dayofweek = 'Wednesday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 4:
                self.__dayofweek = 'Thursday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 5:
                self.__dayofweek = 'Friday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 6:
                self.__dayofweek = 'Saturday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 7:
                self.__dayofweek = 'Sunday'
                return self.__dayofweek
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'day_of_week( self )'
            err = ErrorDialog( exc )
            err.show( )

    def is_weekday( self ):
        try:
            if 1 <= self.__date.isoweekday() <= 5:
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'is_weekday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def is_weekend( self ):
        try:
            if 5 < self.__date.isoweekday() <= 7:
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'is_weekend( self )'
            err = ErrorDialog( exc )
            err.show( )

    def set_date( self, name ):
        try:
            if isinstance( name, str ) and name in self.__list:
                if name == 'Columbus':
                    self.__date = self.columbus_day( )
                    return self.__date
                elif name == 'Veterans':
                    self.__date = self.veterans_day( )
                    return self.__date
                elif name == 'Thanksgiving':
                    self.__date = self.thanksgiving_day( )
                    return self.__date
                elif name == 'Christmas':
                    self.__date = self.christmas_day( )
                    return self.__date
                elif name == 'NewYearsDay':
                    self.__date = self.new_years_day( )
                    return self.__date
                elif name == 'MartinLutherKing':
                    self.__date = self.martinlutherkings_day( )
                    return self.__date
                elif name == 'Washingtons':
                    self.__date = self.washingtons_day( )
                    return self.__date
                elif name == 'Memorial':
                    self.__date = self.memorial_day( )
                    return self.__date
                elif name == 'Juneteenth':
                    self.__date = self.juneteenth_day( )
                    return self.__date
                elif name == 'Labor':
                    self.__date = self.labor_day( )
                    return self.__date
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'set_date( self, value )'
            err = ErrorDialog( exc )
            err.show( )

    def set_name( self, name ):
        try:
            if isinstance( name, str ) and name in self.__list:
                self.__name = name
                return self.__name
            else:
                self.__name = 'NS'
                return self.__name
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'set_name( self, value  ) '
            err = ErrorDialog( exc )
            err.show( )

# FullTimeEquivalent( bfy, fund, provider = Provider.SQLite )
class FullTimeEquivalent( ):
    '''object representing Operating Plan FTE'''
    __source = None
    __provider = None
    __fulltimeequivalentsid = None
    __operatingplansid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__fulltimeequivalentsid is not None:
            return self.__fulltimeequivalentsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__fulltimeequivalentsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FullTimeEquivalents
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'FullTimeEquivalentsId', 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
                           'FundCode', 'OrgCode', 'AccountCode', 'BocCode', 'BocName',
                           'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
                           'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode', 'ProgramAreaCode',
                           'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName', 'ProgramProjectName',
                           'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName', 'ProgramAreaName',
                           'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
                           'ObjectiveCode', 'ObjectiveName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'FullTimeEquivalent'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'FullTimeEquivalent'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# GeneralLedgerAccount( bfy, number, provider = Provider.SQLite )
class GeneralLedgerAccount( ):
    __source = None
    __provider = None
    __generalledgeraccountsid = None
    __bfy = None
    __efy = None
    __treasurysymbol = None
    __fundcode = None
    __fundname = None
    __accountnumber = None
    __accountname = None
    __fields = None

    @property
    def id( self ):
        if self.__ledgeraccountsid is not None:
            return self.__ledgeraccountsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__ledgeraccountsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def account_number( self ):
        if self.__accountnumber is not None:
            return self.__accountnumber

    @account_number.setter
    def account_number( self, value ):
        if value is not None:
            self.__accountnumber = value

    @property
    def account_name( self ):
        if self.__accountname is not None:
            return self.__accountname

    @account_name.setter
    def account_name( self, value ):
        if value is not None:
            self.__accountname = value

    @property
    def treasury_symbol( self ):
        if self.__treasuryaccount is not None:
            return self.__treasuryaccount

    @treasury_symbol.setter
    def treasury_symbol( self, value ):
        if value is not None:
            self.__treasuryaccount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, number, provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__accountnumber = number
        self.__provider = provider
        self.__source = Source.GeneralLedgerAccounts
        self.__fields = [ 'GeneralLedgerAccountsId',
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

# Goal( treas, provider = Provider.SQLite )
class Goal( ):
    '''Defines the Goal Class'''
    __source = None
    __provider = None
    __goalsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__goalsid is not None:
            return self.__goalsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__goalsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Goals
        self.__code = code
        self.__fields = [ 'GoalsId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Goal'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

# GrowthRate( bfy, id, provider = Provider.SQLite )
class GrowthRate( ):
    '''GrowthRate( bfy, id )
    initializes object providing OMB growth rate data'''
    __source = None
    __provider = None
    __growthratesid = None
    __rateid = None
    __description = None
    __budgetyear = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__growthratesid is not None:
            return self.__growthratesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__growthratesid = value

    @property
    def rateid( self ):
        if self.__rateid is not None:
            return self.__rateid

    @rateid.setter
    def rateid( self, value ):
        if value is not None:
            self.__rateid = value

    @property
    def description( self ):
        if self.__description is not None:
            return self.__description

    @description.setter
    def description( self, value ):
        if value is not None:
            self.__description = value

    @property
    def budget_year( self ):
        if self.__budgetyear is not None:
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value ):
        if value is not None:
            self.__budgetyear = value

    @property
    def out_year_1( self ):
        if self.__outyear1 is not None:
            return self.__outyear1

    @out_year_1.setter
    def out_year_1( self, value ):
        if value is not None:
            self.__outyear1 = value

    @property
    def out_year_2( self ):
        if self.__outyear2 is not None:
            return self.__outyear2

    @out_year_2.setter
    def out_year_2( self, value ):
        if value is not None:
            self.__outyear2 = value

    @property
    def out_year_3( self ):
        if self.__outyear3 is not None:
            return self.__outyear3

    @out_year_3.setter
    def out_year_3( self, value ):
        if value is not None:
            self.__outyear3 = value

    @property
    def out_year_4( self ):
        if self.__outyear4 is not None:
            return self.__outyear4

    @out_year_4.setter
    def out_year_4( self, value ):
        if value is not None:
            self.__outyear4 = value

    @property
    def out_year_5( self ):
        if self.__outyear5 is not None:
            return self.__outyear5

    @out_year_5.setter
    def out_year_5( self, value ):
        if value is not None:
            self.__outyear5 = value

    @property
    def out_year_6( self ):
        if self.__outyear6 is not None:
            return self.__outyear6

    @out_year_6.setter
    def out_year_6( self, value ):
        if value is not None:
            self.__outyear6 = value

    @property
    def out_year_7( self ):
        if self.__outyear7 is not None:
            return self.__outyear7

    @out_year_7.setter
    def out_year_7( self, value ):
        if value is not None:
            self.__outyear7 = value

    @property
    def out_year_8( self ):
        if self.__outyear8 is not None:
            return self.__outyear8

    @out_year_8.setter
    def out_year_8( self, value ):
        if value is not None:
            self.__outyear8 = value

    @property
    def out_year_9( self ):
        if self.__outyear9 is not None:
            return self.__outyear9

    @out_year_9.setter
    def out_year_9( self, value ):
        if value is not None:
            self.__outyear9 = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, id, provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__rateid = id
        self.__provider = provider
        self.__source = Source.GrowthRates
        self.__fields = [ 'GrowthRatesId',
                          'RateId',
                          'Description',
                          'BudgetYearRate',
                          'OutYear1',
                          'OutYear2',
                          'OutYear3',
                          'OutYear4',
                          'OutYear5',
                          'OutYear6',
                          'OutYear7',
                          'OutYear8',
                          'OutYear9',
                          'Sort' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RateId', ]
            v = (self.__bfy, self.__rateid)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'GrowthRate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'GrowthRate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# HeadquartersAuthority( bfy, rpio, provider = Provider.SQLite )
class HeadquartersAuthority( ):
    '''object representing HQ Allocation'''
    __source = None
    __provider = None
    __headquartersauthorityid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, rpio, provider = Provider.SQLite ):
        self.__source = Source.HeadquartersAuthority
        self.__provider = provider
        self.__bfy = bfy
        self.__efy = efy
        self.__rpiocode = rpio
        self.__fields = [ 'HeadquartersAuthorityId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'HeadquartersAuthority'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'HeadquartersAuthority'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# HeadquartersOffice( treas, provider = Provider.SQLite  )
class HeadquartersOffice( ):
    '''Defines a regional RPIO'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.___resourceplanningofficesid = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__rpiocode = code
        self.__provider = provider
        self.__source = Source.HeadquartersOffices
        self.__fields = [ 'HeadquartersOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]


    def __str__( self ):
        if self.__code is not None:
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'RpioCode', ]
            v = (self.__rpiocode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HeadquartersOffice'
            exc.method = 'get_data( self ) '
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HeadquartersOffice'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# HumanResourceOrganization( treas, provider = Provider.SQLite )
class HumanResourceOrganization( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __humanresourceorganizationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__humanresourceorganizationsid is not None:
            return self.__humanresourceorganizationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__humanresourceorganizationsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.HumanResourceOrganizations
        self.__code = code
        self.__frame = DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HumanResourceOrganization'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HumanResourceOrganization'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CarryoverEstimate( bfy, provider = Provider.SQLite )
class InflationReductionActCarryoverEstimate( ):
    '''CarryoverEstimate( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __iracarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__annualcarryoverestimatesid, int ):
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ):
        if isinstance( self.__availablebalance, float ):
            return self.__availablebalance

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
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
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CarryoverEstimate( bfy, provider = Provider.SQLite )
class JobsActCarryoverEstimate( ):
    '''CarryoverEstimate( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __jobsactcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__jobsactcarryoverestimatesid, int ):
            return self.__jobsactcarryoverestimatesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ):
        if isinstance( self.__availablebalance, float ):
            return self.__availablebalance

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
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
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Actual( bfy, fund, provider = Provider.SQLite  )
class MonthlyActual( ):
    '''Object representing expenditure data'''
    __source = None
    __provider = None
    __monthlyactualsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __rpiocode = None
    __rpioname = None
    __ahcode = None
    __ahname = None
    __appropriationcode = None
    __appropriationname = None
    __subappropriationcode = None
    __subappropriationname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __netoutlays = None
    __grossoutlays = None
    __obligations = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__actualsid is not None:
            return self.__actualsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__id = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def gross_outlays( self ):
        if self.__grossoutlays is not None:
            return self.__grossoutlays

    @gross_outlays.setter
    def gross_outlays( self, value ):
        if value is not None:
            self.__grossoutlays = value

    @property
    def net_outlays( self ):
        if self.__netoutlays is not None:
            return self.__netoutlays

    @net_outlays.setter
    def net_outlays( self, value ):
        if value is not None:
            self.__netoutlays  = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.MonthlyActuals
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'ActualsId',
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
                           'ULO',
                           'Obligation',
                           'Balance',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'GoalCode',
                           'GoalName',
                           'ObjectiveCode',
                           'ObjectiveName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Actual'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Actual'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# MonthlyOutlay( bfy, efy, account, provider = Provider.SQLite )
class MonthlyOutlay( ):
    '''MonthlyOutlay( bfy, efy, omb ) initializes
    object providing OMB outlay data'''
    __source = None
    __provider = None
    __monthlyoutlaysid = None
    __reportyear = None
    __bfy = None
    __efy = None
    __linenumber = None
    __linename = None
    __taxationcode = None
    __treasuryagency = None
    __treasuryaccount = None
    __treasuryaccountname = None
    __subaccount = None
    __ombagency = None
    __ombbureau = None
    __ombaccount = None
    __budgetaccountname = None
    __january = None
    __february = None
    __march = None
    __april = None
    __may = None
    __june = None
    __july = None
    __august = None
    __september = None
    __october = None
    __november = None
    __december = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__monthlyoutlaysid, int ):
            return self.__monthlyoutlaysid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__monthlyoutlaysid = value

    @property
    def line_number( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_name( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @line_name.setter
    def line_name( self, value ):
        if value is not None:
            self.__linename = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def taxationcode( self ):
        if self.__taxationcode is not None:
            return self.__taxationcode

    @taxationcode.setter
    def taxationcode( self, value ):
        if value is not None:
            self.__taxationcode = value

    @property
    def treasuryagency( self ):
        if self.__treasuryagency is not None:
            return self.__treasuryagency

    @treasuryagency.setter
    def treasuryagency( self, value ):
        if value is not None:
            self.__treasuryagency = value

    @property
    def treasuryaccount( self ):
        if self.__treasuryaccount is not None:
            return self.__treasuryaccount

    @treasuryaccount.setter
    def treasuryaccount( self, value ):
        if value is not None:
            self.__treasuryaccount = value

    @property
    def ombaccount( self ):
        if self.__ombaccount is not None:
            return self.__ombaccount

    @ombaccount.setter
    def ombaccount( self, value ):
        if value is not None:
            self.__ombaccount = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.MonthlyOutlays
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = account
        self.__fields = [ 'MonthlyOutlaysId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            v = (self.__bfy, self.__efy, self.__budgetaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'MonthlyOutlay'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'MonthlyOutlay'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# NationalProgram( treas value, provider = Provider.SQLite )
class NationalProgram( ):
    '''Defines the NationalProgram Class'''
    __source = None
    __provider = None
    __nationalprogramsid = None
    __code = None
    __name = None
    __rpio = None
    __title = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__nationalprogramsid, int ):
            return self.__nationalprogramsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__nationalprogramsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def rpio( self ):
        if isinstance( self.__rpio, str ) and self.__rpio != '':
            return self.__rpio

    @rpio.setter
    def rpio( self, value ):
        if value is not None:
            self.__rpio = value

    @property
    def title( self ):
        if isinstance( self.__title, str ) and self.__title != '':
            return self.__title

    @title.setter
    def title( self, value ):
        if value is not None:
            self.__title = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.NationalPrograms
        self.__code = code
        self.__fields = [ 'NationalProgramsId',
                          'Code',
                          'Name',
                          'RpioCode',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'NationalProgram'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'NationalProgram'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Objective( treas, provider = Provider.SQLite )
class Objective( ):
    '''Defines the Objective Class'''
    __source = None
    __provider = None
    __objectivesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__objectivesid, int ):
            return self.__objectivesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__objectivesid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Objectives
        self.__code = code
        self.__fields = [ 'ObjectivesId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = Source.Objectives
            provider = Provider.SQLite
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Objective'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Objective'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Organization( fundcode, provider = Provider.SQLite  )
class Organization( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __organizationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__organizationsid, int ):
            return self.__organizationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__organizationsid = id

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if list is not None:
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Organizations
        self.__code = code
        self.__fields = [ 'OrganizationsId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Organization'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

# ObjectClassOutlay( account, provider = Provider.SQLite )
class ObjectClassOutlay( ):
    '''ObjectClassOutlay( bfy, omb )
    object provides OMB outlay data'''
    __source = None
    __provider = None
    __objectclassoutlaysid = None
    __reportyear = None
    __ombagencycode = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __obligationtype = None
    __directreimbursabletitle = None
    __objectclassgroupnumber = None
    __objectclassgroupname = None
    __boccode = None
    __bocname = None
    __financeobjectclass = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__objectclassoutlaysid, int ):
            return self.__objectclassoutlaysid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__objectclassoutlaysid = value

    @property
    def report_year( self ):
        if self.__reportyear is not None:
            return self.__reportyear

    @report_year.setter
    def report_year( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__reportyear = value

    @property
    def ombagencycode( self ):
        if self.__ombagencycode is not None:
            return self.__ombagencycode

    @ombagencycode.setter
    def ombagencycode( self, value ):
        if value is not None:
            self.__ombagencycode = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def obligation_type( self ):
        if self.__obligationtype is not None:
            return self.__obligationtype

    @obligation_type.setter
    def obligation_type( self, value ):
        if value is not None:
            self.__obligationtype = value

    @property
    def direct_reimbursable_title( self ):
        if self.__directreimbursabletitle is not None:
            return self.__directreimbursabletitle

    @direct_reimbursable_title.setter
    def direct_reimbursable_title( self, value ):
        if value is not None:
            self.__directreimbursabletitle = value

    @property
    def object_class_group_number( self ):
        if self.__objectclassgroupnumber is not None:
            return self.__objectclassgroupnumber

    @object_class_group_number.setter
    def object_class_group_number( self, value ):
        if value is not None:
            self.__objectclassgroupnumber = value

    @property
    def object_class_group_name( self ):
        if self.__objectclassgroupname is not None:
            return self.__objectclassgroupname

    @object_class_group_name.setter
    def object_class_group_name( self, value ):
        if value is not None:
            self.__objectclassgroupname = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def finance_object_class( self ):
        if self.__financeobjectclass is not None:
            return self.__financeobjectclass

    @finance_object_class.setter
    def finance_object_class( self, value ):
        if value is not None:
            self.__financeobjectclass = value

    @property
    def prior_year( self ):
        if self.__prioryear is not None:
            return self.__prioryear

    @prior_year.setter
    def prior_year( self, value ):
        if value is not None:
            self.__prioryear = value

    @property
    def current_year( self ):
        if self.__currentyear is not None:
            return self.__currentyear

    @current_year.setter
    def current_year( self, value ):
        if value is not None:
            self.__currentyear = value

    @property
    def budget_year( self ):
        if self.__budgetyear is not None:
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value ):
        if value is not None:
            self.__budgetyear = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, year, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ObjectClassOutlays
        self.__reportyear = year
        self.__budgetaccountcode = account
        self.__fields = [ 'ObjectClassOutlaysId',
                          'ReportYear',
                          'OmbAgencyCode',
                          'OmbAgencyName',
                          'OmbBureauCode',
                          'OmbBureauName',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'ObligationType',
                          'DirectReimbursableTitle',
                          'ObjectClassGroupNumber',
                          'ObjectClassGroupName',
                          'BocCode',
                          'BocName',
                          'FinanceObjectClass',
                          'PriorYear',
                          'CurrentYear',
                          'BudgetYear' ]

    def get_data( self  ):
        try:
            source = Source.ObjectClassOutlays
            provider = Provider.SQLite
            n = [ 'OmbAccountCode', ]
            v = (self.__budgetaccountcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlay'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlay'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# OperatingPlan( bfy, efy, treas, provider = Provider.SQLite )
class OperatingPlan( ):
    '''object representing Operating plan allocations'''
    __operatingplansid = None
    __source = None
    __provider = None
    __operatingplansid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__operatingplansid is not None:
            return self.__operatingplansid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__operatingplansid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccod is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.OperatingPlans
        self.__provider = provider
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
                           'FundCode', 'OrgCode', 'AccountCode', 'RcCode', 'BocCode', 'BocName',
                           'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
                           'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode', 'ProgramAreaCode',
                           'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName', 'ProgramProjectName',
                           'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName', 'ProgramAreaName',
                           'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
                           'ObjectiveCode', 'ObjectiveName' ]

    def get_data( self  ):
        try:
            src = self.__source
            pdr = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source = src, provider = pdr )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OperatingPlan'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OperatingPlan'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# OpenCommitment( bfy, efy, fund, account, boc, provider = Provider.SQLite )
class OpenCommitment( ):
    ''' OpenCommitment( bfy, fund, account, boc )
    initializes object providing OpenCommitment data.'''
    __source = None
    __provider = None
    __opencommitmentsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__opencommitmentsid is not None:
            return self.__opencommitmentsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__opencommitmentsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if  self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ):
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ):
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, account, boc, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.OpenCommitments
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'OpenCommitmentsId',
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
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OpenCommitment'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OpenCommitment'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Obligation( bfy, efy, fund, account, boc, provider = Provider.SQLite )
class Obligation( ):
    '''Obligation( bfy, efy, fund, account, boc )
    initializes object providing Obligation data'''
    __source = None
    __provider = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__obligationsid, int ):
            return self.__obligationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__obligationsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def document_type( self ):
        if self.__documenttyp is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ):
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, account, boc, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Obligations
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'ObligationsId',
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
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Obligaions'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Obligation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ProgramFinancingScedule( bfy, efy, account, provider = Provider.SQLite )
class ProgramFinancingSchedule( ):
    __source = None
    __provider = None
    __bfy = None
    __efy = None
    __programfinancingscheduleid = None
    __reportyear = None
    __ledgeraccountcode = None
    __treasuryagencycode = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __fundname = None
    __sectionnumber = None
    __sectionname = None
    __linenumber = None
    __linedescription = None
    __originalamount = None
    __budgetamount = None
    __agencyamount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ):
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, account, provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = account
        self.__provider = provider
        self.__source = Source.ProgramFinancingSchedule
        self.__fields = [ 'ProgramFinancingScheduleId',
                          'ReportYear',
                          'TreasuryAccountCode',
                          'LedgerAccountCode',
                          'SectionNumber',
                          'SectionName',
                          'LineNumber',
                          'LineDescription',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'FundName',
                          'OriginalAmount',
                          'BudgetAmount',
                          'AgencyAmount',
                          'Amount' ]

# PublicLaw( bfy, number, provider = Provider.SQLite )
class PublicLaw( ):
    __source = None
    __provider = None
    __publiclawsid = None
    __bfy = None
    __efy = None
    __lawnumber = None
    __enacteddate = None
    __congress = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__publiclawsid, int ):
            return self.__publiclawsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__publiclawsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def lawnumber( self ):
        if self.__lawnumber is not None:
            return self.__lawnumber

    @lawnumber.setter
    def lawnumber( self, value ):
        if value is not None:
            self.__lawnumber = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, number, provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__efy = efy
        self.__lawnumber = number
        self.__provider = provider
        self.__source = Source.PublicLaws
        self.__fields = [ 'PublicLawsId',
                          'LawNumber',
                          'BillTitle',
                          'EnactedDate',
                          'Congress',
                          'BFY' ]

# PayrollActivity( bfy, efy, fund, provider = Provider.SQLite )
class PayrollActivity( ):
    '''provides payroll data'''
    __source = None
    __provider = None
    __payrollactivityid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __rccode = None
    __rcname = None
    __subrccode = None
    __subrcname = None
    __hrorgcode = None
    __hrorgname = None
    __workcode = None
    __workcodename = None
    __payperiod = None
    __startdate = None
    __enddate = None
    __checkdate = None
    __foccode = None
    __focname = None
    __amount = None
    __hours = None
    __basepaid = None
    __basehours = None
    __benefits = None
    __overtimepaid = None
    __overtimehours = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__payrollactivityid, int ):
            return self.__payrollactivityid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__payrollactivityid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def subrccode( self ):
        if isinstance( self.__subrccode, str ) and self.__subrccode != '':
            return self.__subrccode

    @subrccode.setter
    def subrccode( self, value ):
        if value is not None:
            self.__subrccode = value

    @property
    def subrcname( self ):
        if isinstance( self.__subrcname, str ) and self.__subrcname != '':
            return self.__subrcname

    @subrcname.setter
    def subrcname( self, value ):
        if value is not None:
            self.__subrcname = value

    @property
    def program_project_code( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def hrorgcode( self ):
        if self.__hrorgcode is not None:
            return self.__hrorgcode

    @hrorgcode.setter
    def hrorgcode( self, value ):
        if value is not None:
            self.__hrorgcode = value

    @property
    def hrorgname( self ):
        if self.__hrorgname is not None:
            return self.__hrorgname

    @hrorgname.setter
    def hrorgname( self, value ):
        if value is not None:
            self.__hrorgname = value

    @property
    def workcode( self ):
        if self.__workcode is not None:
            return self.__workcode

    @workcode.setter
    def workcode( self, value ):
        if value is not None:
            self.__workcode = value

    @property
    def workcodename( self ):
        if self.__workcodename is not None:
            return self.__workcodename

    @workcodename.setter
    def workcodename( self, value ):
        if value is not None:
            self.__workcodename = value

    @property
    def payperiod( self ):
        if self.__payperiod is not None:
            return self.__payperiod

    @payperiod.setter
    def payperiod( self, value ):
        if value is not None:
            self.__payperiod = value

    @property
    def startdate( self ):
        if self.__startdate is not None:
            return self.__startdate

    @startdate.setter
    def startdate( self, value ):
        if isinstance( value, datetime ):
            self.__startdate = value

    @property
    def enddate( self ):
        if self.__enddate is not None:
            return self.__enddate

    @enddate.setter
    def enddate( self, value ):
        if isinstance( value, datetime ):
            self.__startdate = value

    @property
    def checkdate( self ):
        if self.__checkdate is not None:
            return self.__checkdate

    @checkdate.setter
    def checkdate( self, value ):
        if isinstance( value, datetime ):
            self.__checkdate = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def hours( self ):
        if self.__hours is not None:
            return self.__hours

    @hours.setter
    def hours( self, value ):
        if value is not None:
            self.__hours = value

    @property
    def basepaid( self ):
        if self.__basepaid is not None:
            return self.__basepaid

    @basepaid.setter
    def basepaid( self, value ):
        if isinstance( value, float):
            self.__basepaid = value

    @property
    def basehours( self ):
        if self.__basehours is not None:
            return self.__basehours

    @basehours.setter
    def basehours( self, value ):
        if value is not None:
            self.__basehours = value

    @property
    def benefits( self ):
        if self.__benefits is not None:
            return self.__benefits

    @benefits.setter
    def benefits( self, value ):
        if value is not None:
            self.__benefits = value

    @property
    def overtimepaid( self ):
        if  self.__overtimepaid is not None:
            return self.__overtimepaid

    @overtimepaid.setter
    def overtimepaid( self, value ):
        if value is not None:
            self.__overtimepaid = value

    @property
    def overtimehours( self ):
        if self.__overtimehours is not None:
            return self.__overtimehours

    @overtimehours.setter
    def overtimehours( self, value ):
        if value is not None:
            self.__overtimehours = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.PayrollActivity
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'PayrollActivityId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'AhCode',
                           'AhName',
                           'RcCode',
                           'RcName',
                           'SubRcCode',
                           'SubRcName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'NpmCode',
                           'NpmName',
                           'FocCode',
                           'FocName',
                           'HrOrgCode',
                           'HrOrgName',
                           'WorkCode',
                           'WorkCodeName',
                           'PayPeriod',
                           'StartDate',
                           'EndDate',
                           'CheckDate',
                           'Amount',
                           'Hours',
                           'BasePaid',
                           'BaseHours',
                           'Benefits',
                           'OvertimePaid',
                           'OvertimeHours' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'PayrollActivity'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'PayrollActivity'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Project( code, provider = Provider.SQLite  )
class Project( ):
    '''Defines the Organization Class'''
    __source = None
    __projectsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__projectsid, int ):
            return self.__projectsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Projects
        self.__code = code
        self.__fields = [ 'ProjectId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Project'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Project'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ProgramArea( code, provider = Provider.SQLite  )
class ProgramArea( ):
    '''defines the ProgramArea class'''
    __source = None
    __provider = None
    __programareasid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__programareasid, int ):
            return self.__programareasid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ProgramAreas
        self.__code = code 
        self.__fields = [ 'ProgramAreasId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramArea'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramArea'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ProgramProject( code, provider = Provider.SQLite  )
class ProgramProject( ):
    '''Defines the ProgramProject Class'''
    __source = None
    __provider = None
    __programprojectsid = None
    __code = None
    __name = None
    __programareacode = None
    __programareaname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__programprojectsid , int ):
            return self.__programprojectsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__programprojectsid  = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def program_area_code( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.____programareaname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ProgramProjects
        self.__code = code 
        self.__fields = [ 'ProgramProjectsId',
                          'Code',
                          'Name',
                          'ProgramAreaCode',
                          'ProgramAreaName' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramProject'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

# PayrollCostCode( bfy, efy, code, provider = Provider.SQLite )
class PayrollCostCode( ):
    __source = None
    __provider = None
    __payrollcostcodesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __ahcode = None
    __rccode = None
    __rcname = None
    __workcode = None
    __workcodename = None
    __hrorgcode = None
    __hrorgname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__payrollcostcodesid, int ):
            return self.__payrollcostcodesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__payrollcostcodesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def rc_code( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def workcode( self ):
        if isinstance( self.__workcode, str ) and self.__workcode != '':
            return self.__workcode

    @workcode.setter
    def workcode( self, value ):
        if value is not None:
            self.__workcode = value

    @property
    def workcodename( self ):
        if isinstance( self.__workcodename, str ) and self.__workcodename != '':
            return self.__workcodename

    @workcodename.setter
    def workcodename( self, value ):
        if value is not None:
            self.__workcodename = value

    @property
    def hrorgcode( self ):
        if isinstance( self.__hrorgcode, str ) and self.__hrorgcode != '':
            return self.__hrorgcode

    @hrorgcode.setter
    def hrorgcode( self, value ):
        if value is not None:
            self.__hrorgcode = value

    @property
    def hrorgname( self ):
        if isinstance( self.__hrorgname, str ) and self.__hrorgname != '':
            return self.__hrorgname

    @hrorgname.setter
    def hrorgname( self, value ):
        if value is not None:
            self.__hrorgname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, rpio, provider = Provider.SQLite ):
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None
        self.__provider = provider
        self.__source = Source.PayrollCostCodes
        self.__fields = [ 'PayrollCostCodesId',
                           'RPIO',
                           'AhCode',
                           'BFY',
                           'RcCode',
                           'RcName',
                           'WorkCode',
                           'WorkCodeName',
                           'HrOrgCode',
                           'HrOrgName' ]

# ProgramResultsCode( bfy, efy, rpio, ah, account, boc, amount = 0.0, provider = Provider.SQLite )
class ProgramResultsCode( ):
    '''Defines the PRC class'''
    __source = None
    __provider = None
    __allocationsid = None
    __rpiocode = None
    __rpioname = None
    __bfy = None
    __efy = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __accountname = None
    __activitycode = None
    __activityname = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__allocationsid, int ):
            return self.__allocationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__allocationsid = id

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def activitycode( self ):
        if isinstance( self.__activitycode, str ) and self.__activitycode != '':
            return self.__activitycode

    @activitycode.setter
    def activitycode( self, value ):
        if isinstance( value, str ) and self.__activitycode != '':
            self.__activitycode = value

    @property
    def activityname( self ):
        if isinstance( self.__activityname, str ) and self.__activityname != '':
            return self.__activityname

    @activityname.setter
    def activityname( self, value ):
        if isinstance( value, str ) and self.__activityname != '':
            self.__activityname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, efy = None,
                  fund = None, rpio = None, ah = None,
                  account = None, boc = None,
                  amount = 0.0, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Allocations
        self.__accountcode = account
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__rpiocode = rpio
        self.__ahcode = ah
        self.__boccode = boc
        self.__amount = amount if isinstance( amount, float ) else 0.0
        self.__fields = [ 'AllocationsId',
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
                           'NpmCode',
                           'NpmName' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            command = SQL.SELECTALL
            names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
                      'AccountCode', 'BocCode', 'Amount' ]
            values = ( self.__bfy, self.__efy, self.__fundcode, self.__rpiocode,
                       self.__ahcode, self.__accountcode, self.__boccode, self.__amount )
            db = DataBuilder( provider, source, command, names, values )
            self.__data = db.create_table( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramResultsCode'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramResultsCode'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ResponsibilityCenter( fundcode, provider = Provider.SQLite  )
class ResponsibilityCenter( ):
    '''Defines the ResponsibilityCenter Class'''
    __source = None
    __provider = None
    __responsibilitycentersid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__responsibilitycentersid, int ):
            return self.__responsibilitycentersid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResponsibilityCenters
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResponsibilityCentersId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
            provider = Provider.SQLite
            source = Source.ResponsibilityCenters
            command = SQL.SELECTALL
            names = [ 'Code', ]
            values = ( self.__fundcode,)
            df = DataBuilder( provider, source, command, names, values )
            self.__data = df.create_table( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResponsibilityCenter'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResponsibilityCenter'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ResourcePlanningOffice( fundcode, provider = Provider.SQLite  )
class ResourcePlanningOffice( ):
    '''defines the ResponsiblePlanningOffice class'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__resourceplanningofficesid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResourcePlanningOffices
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResourcePlanningOfficesId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResourcePlanningOffice'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResourcePlanningOffice'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# RegionalOffice( fundcode, provider = Provider.SQLite  )
class RegionalOffice( ):
    '''Defines a regional RPIO'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.___resourceplanningofficesid = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str) and len( self.__rpio ) == 2:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if isinstance( value, str ) and len( value ) == 2:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResourcePlanningOffices
        self.__rpiocode = code if isinstance( code, str ) and len( code ) == 2 else None
        self.__fields = [ 'RegionalOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]

    def __str__( self ):
        if self.__code is not None:
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'RegionalOffice'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

# ReimbursableSurvey( bfy, efy, fund, provider = Provider.SQLite )
class ReimbursableSurvey( ):
    '''ReimbursableSurvey( bfy, fund ) initializes
    object providing Reimbursable Authority data'''
    __source = None
    __provider = None
    __reimbursablesurveyid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__reimbursablesurveyid, int ):
            return self.__reimbursablesurveyid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__reimbursablesurveyid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ReimbursableSurvey
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'ReimbursableSurveyId',
                           'BFY',
                           'FundCode',
                           'FundName',
                           'Amount' ]

    def get_data( self  ):
        try:
            src = self.__source
            pro = self.__provider
            n = [ 'BFY', 'FundCode', ]
            v = (self.__bfy, self.__fundcode)
            cfg = SqlConfig( names = n, values = v )
            cnx = Connection( source = src, provider = pro )
            sql = SqlStatement( cnx, cfg )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ReimbursableSurvey'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ReimbursableSurvey'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# ReimbursableAgreement( number, provider = Provide.SQLite )
class ReimbursableAgreement( ):
    __source = None
    __provider = None
    __reimbursableagreementsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __rpiocode = None
    __agreementnumber = None
    __startdate = None
    __enddate = None
    __rccode = None
    __rcname = None
    __orgcode = None
    __siteprojectcode = None
    __accountcode = None
    __vendorcode = None
    __vendorname = None
    __amount = None
    __opencommitments = None
    __unliquidatedobligations = None
    __obligations = None
    __available = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__reimbursableagreementsid, int ):
            return self.__reimbursableagreementsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__reimbursableagreementsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def agreementnumber( self ):
        if isinstance( self.__agreementnumber, str ) and self.__agreementnumber != '':
            return self.__agreementnumber

    @agreementnumber.setter
    def agreementnumber( self, value ):
        if value is not None:
            self.__agreementnumber = value

    @property
    def account_code( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def org_code( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def rc_code( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def vendor_code( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def open_commitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if isinstance( self.__obligations, float ):
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def available( self ):
        if isinstance( self.__avaialable, float ):
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, number, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ReimbursableAgreements
        self.__agreementnumber = number
        self.__fields = [ 'ReimbursableAgreementsId'
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
                          'OpenCommitment',
                          'Obligation',
                          'ULO',
                          'Available' ]

    def __str__( self ):
        if isinstance( self.__agreementnumber, str ) and self.__agreementnumber != '':
            return self.__agreementnumber

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', ]
            v = (self.__bfy,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlay'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlay'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# RegionalAuthority( bfy, efy, fund, provider = Provider.SQLite )
class RegionalAuthority( ):
    '''object representing Regional Allocation'''
    __source = None
    __provider = None
    __regionalauthorityid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__source = Source.RegionalAuthority
        self.__provider = provider
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'RegionalAuthorityId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'RegionalAuthority'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'RegionalAuthority'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# StatusOfFunds( bfy, fund, provider = Provider.SQLite )
class StatusOfFunds( ):
    '''Object representing execution data'''
    __source = None
    __provider = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.StatusOfFunds
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'StatusOfFundsId',
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
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfFunds'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfFunds'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# StatusOfSupplementalFunding( bfy, fund, provider = Provider.SQLite )
class StatusOfSupplementalFunding( ):
    '''Class representing Supplemental Funding execution data'''
    __source = None
    __provider = None
    __statusofsupplementalfundsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__source = Source.StatusOfSupplementalFunding
        self.__provider = Provider.SQLite
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'StatusOfFundsId',
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
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]


    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfSupplementalFunding'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfSupplementalFunding'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# StateGrantObligation( bfy, rpio, provider = Provider.SQLite )
class StateGrantObligation( ):
    '''object representing the BIS'''
    __source = None
    __provider = None
    __stategrantobligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __statecode = None
    __statename = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__stategrantobligationsid, int ):
            return self.__stategrantobligationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__stategrantobligationsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def state_code( self ):
        if isinstance( self.__statecode, str ) and self.__statecode != '':
            return self.__statecode

    @state_code.setter
    def state_code( self, value ):
        if value is not None:
            self.__statecode = value

    @property
    def state_name( self ):
        if isinstance( self.__statename, str ) and self.__statename != '':
            return self.__statename

    @state_name.setter
    def state_name( self, value ):
        if value is not None:
            self.__statename = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, rpio, provider = Provider.SQLite ):
        self.__source = Source.StateGrantObligations
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None
        self.__fields = [ 'StateGrantObligationsId',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__rpiocode, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StateGrantObligation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StateGrantObligation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# SpecialAccount( bfy, fund, account, boc, provider = Provider.SQLite )
class SpecialAccount( ):
    '''' object providing SF Special Account data'''
    __source = None
    __provider = None
    __specialaccountsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __rpiocode = None
    __rpioname = None
    __specialaccountfundcode = None
    __specialaccountfundname = None
    __specialaccountnumber = None
    __specialaccountname = None
    __accountstatus = None
    __nplstatus = None
    __nplstatusname = None
    __nplstatuscode = None
    __siteid = None
    __cerclisid = None
    __sitecode = None
    __sitename = None
    __operableunit = None
    __pipelinecode = None
    __pipelinedescription = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __transactiontype = None
    __transactiontypename = None
    __availablebalance = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __disbursements = None
    __unpaidbalances = None
    __collections = None
    __cumulativereciepts = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__specialaccountsid, int ):
            return self.__specialaccountsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__specialaccountsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def foc_code( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def account_code( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def special_account_fund_code( self ):
        if isinstance( self.__specialaccountfundcode, str ) and self.__specialaccountfundcode != '':
            return self.__specialaccountfundcode

    @special_account_fund_code.setter
    def special_account_fund_code( self, value ):
        if value is not None:
            self.__specialaccountfundcode = value

    @property
    def special_account_fund_name( self ):
        if isinstance( self.__specialaccountfundname, str ) and self.__specialaccountfundname != '':
            return self.__specialaccountfundname

    @special_account_fund_name.setter
    def special_account_fund_name( self, value ):
        if value is not None:
            self.__specialaccountfundname = value

    @property
    def special_account_number( self ):
        if isinstance( self.__specialaccountnumber, str ) and self.__specialaccountnumber != '':
            return self.__specialaccountnumber

    @special_account_number.setter
    def special_account_number( self, value ):
        if value is not None:
            self.__specialaccountnumber = value

    @property
    def special_account_name( self ):
        if isinstance( self.__specialaccountnumber, str ) and self.__specialaccountnumber != '':
            return self.__specialaccountnumber

    @special_account_name.setter
    def special_account_name( self, value ):
        if value is not None:
            self.__specialaccountnumber = value

    @property
    def account_status( self ):
        if isinstance( self.__accountstatus, str ) and self.__accountstatus != '':
            return self.__accountstatus

    @account_status.setter
    def account_status( self, value ):
        if value is not None:
            self.__accountstatus = value

    @property
    def npl_status( self ):
        if isinstance( self.__nplstatus, str ) and self.__nplstatus != '':
            return self.__nplstatus

    @npl_status.setter
    def npl_status( self, value ):
        if value is not None:
            self.__nplstatus = value

    @property
    def npl_status_code( self ):
        if isinstance( self.__nplstatuscode, str ) and self.__nplstatuscode != '':
            return self.__nplstatuscode

    @npl_status_code.setter
    def npl_status_code( self, value ):
        if value is not None:
            self.__nplstatuscode = value

    @property
    def npl_status_name( self ):
        if isinstance( self.__nplstatusname, str ) and self.__nplstatusname != '':
            return self.__nplstatusname

    @npl_status_name.setter
    def npl_status_name( self, value ):
        if value is not None:
            self.__nplstatusname = value

    @property
    def site_id( self ):
        if isinstance( self.__siteid, str ) and self.__siteid != '':
            return self.__siteid

    @site_id.setter
    def site_id( self, value ):
        if value is not None:
            self.__value = value

    @property
    def cerclis_id( self ):
        if isinstance( self.__cerclisid, str ) and self.__cerclisid != '':
            return self.__cerclisid

    @cerclis_id.setter
    def cerclis_id( self, value ):
        if value is not None:
            self.__cerclisid = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SpecialAccounts
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'SpecialAccountsId',
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
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Disbursements',
                           'UnpaidBalances',
                           'Collections',
                           'CumulativeReceipts' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SpecialAccount'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SpecialAccount'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# SuperfundSite( bfy, rpio, provider = Provider.SQLite )
class SuperfundSite( ):
    ''' object providing SF Site data '''
    __source = None
    __provider = None
    __superfundsitesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __siteprojectname = None
    __city = None
    __state = None
    __ssid = None
    __epasiteid = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__specialaccountsid, int ):
            return self.__specialaccountsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__specialaccountsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpioname = value

    @property
    def city( self ):
        if isinstance( self.__nplstatus, str ) and self.__nplstatus != '':
            return self.__nplstatus

    @city.setter
    def city( self, value ):
        if value is not None:
            self.__nplstatus = value

    @property
    def state( self ):
        if isinstance( self.__nplstatuscode, str ) and self.__nplstatuscode != '':
            return self.__nplstatuscode

    @state.setter
    def state( self, value ):
        if value is not None:
            self.__nplstatuscode = value

    @property
    def site_project_name( self ):
        if isinstance( self.__nplstatusname, str ) and self.__nplstatusname != '':
            return self.__nplstatusname

    @site_project_name.setter
    def site_project_name( self, value ):
        if value is not None:
            self.__nplstatusname = value

    @property
    def ssid( self ):
        if isinstance( self.__ssid, str ) and self.__ssid != '':
            return self.__ssid

    @ssid.setter
    def ssid( self, value ):
        if value is not None:
            self.__ssid = value

    @property
    def epa_site_id( self ):
        if isinstance( self.__cerclisid, str ) and self.__cerclisid != '':
            return self.__cerclisid

    @epa_site_id.setter
    def epa_site_id( self, value ):
        if value is not None:
            self.__cerclisid = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy = None, rpiocode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SuperfundSites
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpiocode if isinstance( rpiocode, str ) and rpiocode != '' else None
        self.__fields = [ 'SuperfundSitesId',
                           'RpioCode',
                           'RpioName',
                           'City',
                           'State',
                           'SSID',
                           'SiteProjectName',
                           'EpaSiteId' ]


    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'SuperfundSite'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SuperfundSite'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Appropriation( bfy, efy, fundcode, provider = Provider.SQLite )
class SubAppropriation( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __subappropriationsid = None
    __bfy = None
    __efy = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__subappropriationsid , int ):
            return self.__appropriationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__appropriationsid  = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Appropriations
        self.__bfy = bfy
        self.__efy = efy
        self.__code = code 
        self.__fields = [ 'SubAppropriationsId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SubAppropriation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# SiteProjectCode( code, provider = Provider.SQLite  )
class SiteProjectCode( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __siteprojectcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteprojectcodesid, int ):
            return self.__siteprojectcodesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__siteprojectcodesid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SiteProjectCodes
        self.__code = code

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SiteProjectCode'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SiteProjectCode'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# StateOrganization( fundcode, provider = Provider.SQLite  )
class StateOrganization( ):
    '''StateOrganization( code ) class
    representing state codes'''
    __source = None
    __provider = None
    __stateorganizationsid = None
    __code = None
    __name = None
    __orgcode = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None

    @property
    def id( self ):
        if isinstance( self.__stateorganizationsid, int ):
            return self.__stateorganizationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__stateorganizationsid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StateOrganizations
        self.__code = code
        self.__fields = [ 'StateOrganizationsId',
                          'Name',
                          'Code',
                          'RpioName',
                          'RpioCode' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'StateOrganization'
            exc.method = 'get_data( self ) '
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'StateOrganization'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# StatusOfAppropriations( bfy, efy, fund, provider = Provider.SQLite )
class StatusOfAppropriations( ):
    '''StatusOfAppropriations( bfy, efy, fund )
    object representing Appropriation-level execution data'''
    __source = None
    __provider = None
    __statusofappropriationsid = None
    __bfy = None
    __efy = None
    __budgetlevel = None
    __appropriationfundcode = None
    __appropriationfundname = None
    __appropriationcreationdate = None
    __appropriationcode = None
    __subappropriationcode = None
    __appropriationdescription = None
    __fundgroup = None
    __fundgroupname = None
    __documenttype = None
    __transtype = None
    __actualrecoverytranstype = None
    __commitmentspendingcontrolflag = None
    __expensespendingcontrolflag = None
    __agreementlimit = None
    __estimatedrecoveriestranstype = None
    __estimatedreimbursementstranstype = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __postedcontrolflag = None
    __postedflag = None
    __recordcarryoveratlowerlevel = None
    __reimbursablespendingoption = None
    __recoveriesoption = None
    __recoveriesspendingoption = None
    __originalbudgetedamount = None
    __apportionmentsposted = None
    __totalauthority = None
    __totalbudgeted = None
    __totalpostedamount = None
    __fundswithdrawnprioryearamounts = None
    __fundinginamount = None
    __fundingoutamount = None
    __totalaccrualrecoveries = None
    __totalactualreimbursements = None
    __totalagreeementreimbursables = None
    __totalcarriedforwardin = None
    __totalcarriedforwardout = None
    __totalcommited = None
    __totalestimatedrecoveries = None
    __totalestimatedreimbursements = None
    __totalexpenses = None
    __totalexpenditureexpenses = None
    __totalexpenseaccruals = None
    __totalprecommitments = None
    __unliquidatedprecommitments = None
    __totalobligations = None
    __unliquidatedobligations = None
    __voidedamount = None
    __totalusedamount = None
    __availableamount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofappropriationsid, int ):
            return self.__statusofappropriationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusofappropriationsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def budget_level( self ):
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def appropriation_fund_code( self ):
        if self.__appropriationfundcode is not None:
            return self.__appropriationfundcode

    @appropriation_fund_code.setter
    def appropriation_fund_code( self, value ):
        if value is not None:
            self.__appropriationfundcode = value

    @property
    def appropriation_fund_name( self ):
        if isinstance( self.__appropriationfundname, str ) \
                and self.__appropriationfundname != '':
            return self.__appropriationfundname

    @appropriation_fund_name.setter
    def appropriation_fund_name( self, value ):
        if value is not None:
            self.__appropriationfundname = value

    @property
    def appropriation_creation_date( self ):
        if self.__appropriationcreationdate is not None:
            return self.__appropriationcreationdate

    @appropriation_creation_date.setter
    def appropriation_creation_date( self, value ):
        if isinstance( value, datetime ):
            self.__appropriationcreationdate = value

    @property
    def appropriation_code( self ):
        if self.__appropriationcode is not None:
            return self.__appropriationcode

    @appropriation_code.setter
    def appropriation_code( self, value ):
        if value is not None:
            self.__appropriationcode = value

    @property
    def subappropriation_code( self ):
        if self.__subappropriationcode is not None:
            return self.__subappropriationcode

    @subappropriation_code.setter
    def subappropriation_code( self, value ):
        if value is not None:
            self.__subappropriationcode = value

    @property
    def appropriation_description( self ):
        if self.__appropriationdescription is not None:
            return self.__appropriationdescription

    @appropriation_description.setter
    def appropriation_description( self, value ):
        if value is not None:
            self.__appropriationdescription = value

    @property
    def fund_group( self ):
        if self.__fundgroup is not None:
            return self.__fundgroup

    @fund_group.setter
    def fund_group( self, value ):
        if value is not None:
            self.__fundgroup = value

    @property
    def fund_group_name( self ):
        if self.__fundgroupname is not None:
            return self.__fundgroupname

    @fund_group_name.setter
    def fund_group_name( self, value ):
        if value is not None:
            self.__fundgroupname = value

    @property
    def document_type( self ):
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def trans_type( self ):
        if self.__transtype is not None:
            return self.__transtype

    @trans_type.setter
    def trans_type( self, value ):
        if value is not None:
            self.__transtype = value

    @property
    def actual_recovery_trans_type( self ):
        if self.__actualrecoverytranstype is not None:
            return self.__actualrecoverytranstype

    @actual_recovery_trans_type.setter
    def actual_recovery_trans_type( self, value ):
        if value is not None:
            self.__actualrecoverytranstype = value

    @property
    def commitment_spending_control_flag( self ):
        if self.__commitmentspendingcontrolflag is not None:
            return self.__commitmentspendingcontrolflag

    @commitment_spending_control_flag.setter
    def commitment_spending_control_flag( self, value ):
        if value is not None:
            self.__commitmentspendingcontrolflag = value

    @property
    def agreement_limit( self ):
        if self.__agreementlimit is not None:
            return self.__agreementlimit

    @agreement_limit.setter
    def agreement_limit( self, value ):
        if value is not None:
            self.__agreementlimit = value

    @property
    def estimated_recoveries_trans_type( self  ):
        if self.__estimatedrecoveriestranstype is not None:
            return self.__estimatedrecoveriestranstype

    @estimated_recoveries_trans_type.setter
    def estimated_recoveries_trans_type( self, value ):
        if value is not None:
            self.__estimatedrecoveriestranstype = value

    @property
    def estimated_reimbursements_trans_type( self ):
        if self.__estimatedreimbursementstranstype is not None:
            return self.__estimatedreimbursementstranstype

    @estimated_reimbursements_trans_type.setter
    def estimated_reimbursements_trans_type( self, value ):
        if value is not None:
            self.__estimatedreimbursementstranstype = value

    @property
    def expense_spending_control_flag( self ):
        if self.__expensespendingcontrolflag is not None:
            return self.__expensespendingcontrolflag

    @expense_spending_control_flag.setter
    def expense_spending_control_flag( self, value ):
        if value is not None:
            self.__expensespendingcontrolflag = value

    @property
    def obligation_spending_control_flag( self ):
        if self.__obligationspendingcontrolflag is not None:
            return self.__obligationspendingcontrolflag

    @obligation_spending_control_flag.setter
    def obligation_spending_control_flag( self, value ):
        if value is not None:
            self.__obligationspendingcontrolflag = value

    @property
    def precommitment_spending_control_flag( self ):
        if self.__precommitmentspendingcontrolflag is not None:
            return self.__precommitmentspendingcontrolflag

    @precommitment_spending_control_flag.setter
    def precommitment_spending_control_flag( self, value ):
        if value is not None:
            self.__precommitmentspendingcontrolflag = value

    @property
    def posted_control_flag( self ):
        if self.__postedcontrolflag is not None:
            return self.__postedcontrolflag

    @posted_control_flag.setter
    def posted_control_flag( self, value ):
        if value is not None:
            self.__expensespendingcontrolflag = value

    @property
    def posted_flag( self ):
        if self.__postedflag is not None:
            return self.__postedflag

    @posted_flag.setter
    def posted_flag( self, value ):
        if value is not None:
            self.__postedflag = value

    @property
    def record_carryover_at_lower_level( self ):
        if self.__recordcarryoveratlowerlevel is not None:
            return self.__recordcarryoveratlowerlevel

    @record_carryover_at_lower_level.setter
    def record_carryover_at_lower_level( self, value ):
        if value is not None:
            self.__recordcarryoveratlowerlevel = value

    @property
    def reimbursable_spending_option( self ):
        if self.__reimbursablespendingoption is not None:
            return self.__reimbursablespendingoption

    @reimbursable_spending_option.setter
    def reimbursable_spending_option( self, value ):
        if value is not None:
            self.__reimbursablespendingoption = value

    @property
    def recoveries_option( self ):
        if self.__recoveriesoption is not None:
            return self.__recoveriesoption

    @recoveries_option.setter
    def recoveries_option( self, value ):
        if value is not None:
            self.__recoveriesoption = value

    @property
    def recoveries_spending_option( self ):
        if self.__recoveriesspendingoption is not None:
            return self.__recoveriesspendingoption

    @recoveries_spending_option.setter
    def recoveries_spending_option( self, value ):
        if value is not None:
            self.__recoveriesspendingoption = value

    @property
    def original_budgeted_amount( self ):
        if self.__originalbudgetedamount is not None:
            return self.__originalbudgetedamount

    @original_budgeted_amount.setter
    def original_budgeted_amount( self, value ):
        if value is not None:
            self.__originalbudgetedamount = value

    @property
    def apportionments_posted( self ):
        if self.__apportionmentsposted is not None:
            return self.__apportionmentsposted

    @apportionments_posted.setter
    def apportionments_posted( self, value ):
        if value is not None:
            self.__apportionmentsposted = value

    @property
    def total_authority( self ):
        if self.__totalauthority is not None:
            return self.__totalauthority

    @total_authority.setter
    def total_authority( self, value ):
        if value is not None:
            self.__totalauthority = value

    @property
    def total_budgeted( self ):
        if self.__totalbudgeted is not None:
            return self.__totalbudgeted

    @total_budgeted.setter
    def total_budgeted( self, value ):
        if value is not None:
            self.__totalbudgeted = value

    @property
    def total_posted_amount( self ):
        if self.__totalpostedamount is not None:
            return self.__totalpostedamount

    @total_posted_amount.setter
    def total_posted_amount( self, value ):
        if value is not None:
            self.__totalpostedamount = value

    @property
    def funds_withdrawn_prior_year_amounts( self ):
        if self.__fundswithdrawnprioryearamounts is not None:
            return self.__fundswithdrawnprioryearamounts

    @funds_withdrawn_prior_year_amounts.setter
    def funds_withdrawn_prior_year_amounts( self, value ):
        if value is not None:
            self.__fundswithdrawnprioryearamounts = value

    @property
    def funding_in_amount( self ):
        if self.__fundinginamount is not None:
            return self.__fundinginamount

    @funding_in_amount.setter
    def funding_in_amount( self, value ):
        if value is not None:
            self.__fundinginamount = value

    @property
    def funding_out_amount( self ):
        if self.__fundingoutamount is not None:
            return self.__fundingoutamount

    @funding_out_amount.setter
    def funding_out_amount( self, value ):
        if value is not None:
            self.__fundingoutamount = value

    @property
    def total_accrual_recoveries( self ):
        if self.__totalaccrualrecoveries is not None:
            return self.__totalaccrualrecoveries

    @total_accrual_recoveries.setter
    def total_accrual_recoveries( self, value ):
        if value is not None:
            self.__totalaccrualrecoveries = value

    @property
    def total_actual_reimbursements( self ):
        if self.__totalactualreimbursements is not None:
            return self.__totalactualreimbursements

    @total_actual_reimbursements.setter
    def total_actual_reimbursements( self, value ):
        if value is not None:
            self.__totalactualreimbursements = value

    @property
    def total_agreement_reimbursables( self ):
        if self.__totalagreementreimbursables is not None:
            return self.__totalagreementreimbursables

    @total_agreement_reimbursables.setter
    def total_agreement_reimbursables( self, value ):
        if value is not None:
            self.__totalagreementreimbursables = value

    @property
    def total_carried_forward_in( self ):
        if self.__totalcarriedforwardin is not None:
            return self.__totalcarriedforwardin

    @total_carried_forward_in.setter
    def total_carried_forward_in( self, value ):
        if value is not None:
            self.__totalcarriedforwardin = value

    @property
    def total_carried_forward_out( self ):
        if self.__totalcarriedforwardout is not None:
            return self.__totalcarriedforwardout

    @total_carried_forward_out.setter
    def total_carried_forward_out( self, value ):
        if value is not None:
            self.__totalcarriedforwardout = value

    @property
    def total_estimated_recoveries( self ):
        if self.__totalestimatedrecoveries is not None:
            return self.__totalestimatedrecoveries

    @total_estimated_recoveries.setter
    def total_estimated_recoveries( self, value ):
        if value is not None:
            self.__totalestimatedrecoveries = value

    @property
    def total_estimated_reimbursements( self ):
        if self.__totalestimatedreimbursements is not None:
            return self.__totalestimatedreimbursements

    @total_estimated_reimbursements.setter
    def total_estimated_reimbursements( self, value ):
        if value is not None:
            self.__totalestimatedreimbursements = value

    @property
    def total_expenses( self ):
        if self.__totalexpenses is not None:
            return self.__totalexpenses

    @total_expenses.setter
    def total_expenses( self, value ):
        if value is not None:
            self.__totalexpenses = value

    @property
    def total_expenditure_expenses( self ):
        if self.__totalexpenditureexpenses is not None:
            return self.__totalexpenditureexpenses

    @total_expenditure_expenses.setter
    def total_expenditure_expenses( self, value ):
        if value is not None:
            self.__totalexpenditureexpenses = value

    @property
    def total_expense_accruals( self ):
        if self.__totalexpenseaccruals is not None:
            return self.__totalexpenseaccruals

    @total_expense_accruals.setter
    def total_expense_accruals( self, value ):
        if value is not None:
            self.__totalexpenseaccruals = value

    @property
    def total_precommitments( self ):
        if self.__totalprecommitments is not None:
            return self.__totalprecommitments

    @total_precommitments.setter
    def total_precommitments( self, value ):
        if value is not None:
            self.__totalprecommitments = value

    @property
    def unliquidated_precommitments( self ):
        if self.__unliquidatedprecommitments is not None:
            return self.__unliquidatedprecommitments

    @unliquidated_precommitments.setter
    def unliquidated_precommitments( self, value ):
        if value is not None:
            self.__unliquidatedprecommitments = value

    @property
    def total_obligations( self ):
        if self.__totalobligations is not None:
            return self.__totalobligations

    @total_obligations.setter
    def total_obligations( self, value ):
        if value is not None:
            self.__totalobligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def voided_amount( self ):
        if self.__voidedamount is not None:
            return self.__voidedamount

    @voided_amount.setter
    def voided_amount( self, value ):
        if value is not None:
            self.__voidedamount = value

    @property
    def total_used_amount( self ):
        if self.__totalusedamount is not None:
            return self.__totalusedamount

    @total_used_amount.setter
    def total_used_amount( self, value ):
        if value is not None:
            self.__totalusedamount = value

    @property
    def available_amount( self ):
        if self.__availableamount is not None:
            return self.__availableamount

    @available_amount.setter
    def available_amount( self, value ):
        if value is not None:
            self.__availableamount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfAppropriations
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__appropriationfundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields =[ 'StatusOfAppropriationsId',
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
                           'ULO',
                           'VoidedAmount',
                           'TotalUsedAmount',
                           'AvailableAmount' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'AppropriationFundCode', ]
            v = (self.__bfy, self.__efy, self.__appropriationfundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'StatusOfAppropriations'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'StatusOfAppropriations'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# SpendingRate( account, provider = Provider.SQLite )
class SpendingRate( ):
    '''SpendingRate( fundcode ) initializes
    object providing OMB spending rate data'''
    __source = None
    __provider = None
    __spendingratesid = None
    __ombagencycode = None
    __ombagencyname = None
    __treasuryagencycode = None
    __treasuryagencyname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __ombaccounttitle = None
    __subfunction = None
    __linenumber = None
    __linename = None
    __category = None
    __subcategory = None
    __subcategoryname = None
    __jurisdiction = None
    __yearofauthority = None
    __budgetauthority = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __outyear10 = None
    __outyear11 = None
    __totalspendout = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__spendingratesid, int ):
            return self.__spendingratesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__spendingratesid = value

    @property
    def treasury_agency_code( self ):
        if isinstance( self.__treasuryagencycode, str ) and self.__treasuryagencycode != '':
            return self.__treasuryagencycode

    @treasury_agency_code.setter
    def treasury_agency_code( self, value ):
        if value is not None:
            self.__treasuryagencycode = value

    @property
    def treasury_agency_name( self ):
        if isinstance( self.__treasuryagencyname, str ) and self.__treasuryagencyname != '':
            return self.__treasuryagencyname

    @treasury_agency_name.setter
    def treasury_agency_name( self, value ):
        if value is not None:
            self.__treasuryagencyname = value

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def omb_agency_code( self ):
        if isinstance( self.__ombagencycode, str ) and self.__ombagencycode != '':
            return self.__ombagencycode

    @omb_agency_code.setter
    def omb_agency_code( self, value ):
        if value is not None:
            self.__ombagencycode = value

    @property
    def omb_agency_name( self ):
        if isinstance( self.__ombagencyname, str ) and self.__ombagencyname != '':
            return self.__ombagencyname

    @omb_agency_name.setter
    def omb_agency_name( self, value ):
        if value is not None:
            self.__ombagencyname = value

    @property
    def budget_account_code( self ):
        if isinstance( self.__budgetaccountcode, str ) and self.__budgetaccountcode != '':
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if isinstance( self.__budgetaccountname, str ) and self.__budgetaccountname != '':
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def subfunction( self ):
        if isinstance( self.__subfunction, str ) and self.__subfunction != '':
            return self.__subfunction

    @subfunction.setter
    def subfunction( self, value ):
        if value is not None:
            self.__subfunction = value

    @property
    def category( self ):
        if isinstance( self.__category, str ) and self.__category != '':
            return self.__category

    @category.setter
    def category( self, value ):
        if value is not None:
            self.__category = value

    @property
    def subcategory( self ):
        if isinstance( self.__subcategory, str ) and self.__subcategory != '':
            return self.__subcategory

    @subcategory.setter
    def subcategory( self, value ):
        if value is not None:
            self.__subcategory = value

    @property
    def line_number( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_name( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @line_name.setter
    def line_name( self, value ):
        if value is not None:
            self.__linename = value

    @property
    def year_of_authority( self ):
        if isinstance( self.__yearofauthority, str ) and self.__yearofauthority != '':
            return self.__yearofauthority

    @year_of_authority.setter
    def year_of_authority( self, value ):
        if value is not None:
            self.__yearofauthority = value

    @property
    def budget_authority( self ):
        if isinstance( self.__budgetauthority, float ):
            return self.__budgetauthority

    @budget_authority.setter
    def budget_authority( self, value ):
        if value is not None:
            self.__budgetauthority = value

    @property
    def out_year_1( self ):
        if isinstance( self.__outyear1, float ):
            return self.__outyear1

    @out_year_1.setter
    def out_year_1( self, value ):
        if value is not None:
            self.__outyear1 = value

    @property
    def out_year_2( self ):
        if isinstance( self.__outyear2, float ):
            return self.__outyear2

    @out_year_2.setter
    def out_year_2( self, value ):
        if value is not None:
            self.__outyear2 = value

    @property
    def out_year_3( self ):
        if isinstance( self.__outyear3, float ):
            return self.__outyear3

    @out_year_3.setter
    def out_year_3( self, value ):
        if value is not None:
            self.__outyear3 = value

    @property
    def out_year_4( self ):
        if isinstance( self.__outyear4, float ):
            return self.__outyear4

    @out_year_4.setter
    def out_year_4( self, value ):
        if value is not None:
            self.__outyear4 = value

    @property
    def out_year_5( self ):
        if isinstance( self.__outyear5, float ):
            return self.__outyear5

    @out_year_5.setter
    def out_year_5( self, value ):
        if value is not None:
            self.__outyear5 = value

    @property
    def out_year_6( self ):
        if isinstance( self.__outyear6, float ):
            return self.__outyear6

    @out_year_6.setter
    def out_year_6( self, value ):
        if value is not None:
            self.__outyear6 = value

    @property
    def out_year_7( self ):
        if isinstance( self.__outyear7, float ):
            return self.__outyear7

    @out_year_7.setter
    def out_year_7( self, value ):
        if value is not None:
            self.__outyear7 = value

    @property
    def out_year_8( self ):
        if isinstance( self.__outyear8, float ):
            return self.__outyear8

    @out_year_8.setter
    def out_year_8( self, value ):
        if value is not None:
            self.__outyear8 = value

    @property
    def out_year_9( self ):
        if isinstance( self.__outyear9, float ):
            return self.__outyear9

    @out_year_9.setter
    def out_year_9( self, value ):
        if value is not None:
            self.__outyear9 = value

    @property
    def out_year_10( self ):
        if isinstance( self.__outyear10, float ):
            return self.__outyear10

    @out_year_10.setter
    def out_year_10( self, value ):
        if value is not None:
            self.__outyear10 = value

    @property
    def out_year_11( self ):
        if isinstance( self.__outyear11, float ):
            return self.__outyear11

    @out_year_11.setter
    def out_year_11( self, value ):
        if value is not None:
            self.__outyear11 = value

    @property
    def total_spendout( self ):
        if isinstance( self.__totalspendout, float ):
            return self.__totalspendout

    @total_spendout.setter
    def total_spendout( self, value ):
        if value is not None:
            self.__totalspendout = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SpendingRates
        self.__budgetaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'SpendingRatesId',
                          'OmbAgencyCode',
                          'OmbAgencyName',
                          'OmbBureauCode',
                          'OmbBureauName',
                          'TreausuryAgencyCode',
                          'TreausuryAccountCode',
                          'TreausuryAccountName',
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

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            command = SQL.SELECTALL
            names = [ 'OmbAccountCode', ]
            values = ( self.__budgetaccountcode, )
            data = DataBuilder( provider, source, command, names, values )
            self.__data = data.create_table( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'SpendingRate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'SpendingRate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# StatusOfSupplementalFunds( bfy, efy, fundcode, provider = Provider.SQLite )
class StatusOfSupplementalFunds( ):
    __statusofsupplementalfundsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofsupplementalfundsid, int ):
            return self.__statusofsupplementalfundsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusofsupplementalfundsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfSupplementalFunding
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields =[ 'StatusOfSupplementalFundsId',
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
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

# StatusOfJobsActFunding( bfy, efy, fundcode, provider = Provider.SQLite )
class StatusOfJobsActFunding( ):
    __source = None
    __provider = None
    __statusofjobsactfundingid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofjobsactfundingid, int ):
            return self.__statusofjobsactfundingid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusofjobsactfundingid= value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__provider = provider
        self.__source = Source.StatusOfJobsActFunding
        self.__fields = [ 'StatusOfJobsActFundingId',
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
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available' ]

# StatusOfEarmarks( bfy, efy, fundcode, provider = Provider.SQLite )
class StatusOfEarmarks( ):
    __source = None
    __provider = None
    __statusofearmarksid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofearmarksid, int ):
            return self.__statusofearmarksid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__statusofearmarksid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def open_commitments( self ):
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__provider = provider
        self.__source = Source.StatusOfEarmarks
        self.__fields = [ 'StatusOfEarmarksId',
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
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available' ]

# SiteActivity( bfy, rpio, provider = Provider.SQLite  )
class SiteActivity( ):
    '''provides data on superfund site spending'''
    __source = None
    __provider = None
    __siteactivityid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __city = None
    __siteprojectcode = None
    __stieprojectname = None
    __ssid = None
    __actioncode = None
    __operableunit = None
    __congress = None
    __startdate = None
    __enddate = None
    __lastactivitydate = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __foccode = None
    __focname = None
    __requested = None
    __accepted = None
    __closed = None
    __outstanding = None
    __refunded = None
    __reversal = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteactivityid, int ):
            return self.__siteactivityid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__siteactivityid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def epa_site_id( self ):
        if self.__epasiteid is not None:
            return self.__epasiteid

    @epa_site_id.setter
    def epa_site_id( self, value ):
        if value is not None:
            self.__epasiteid = value

    @property
    def project_type( self ):
        if self.__projecttype is not None:
            return self.__projecttype

    @project_type.setter
    def project_type( self, value ):
        if value is not None:
            self.__projecttype = value

    @property
    def site_project_code( self ):
        if self.__siteprojectcode is not None:
            return self.__siteprojectcode

    @site_project_code.setter
    def site_project_code( self, value ):
        if value is not None:
            self.__siteprojectcode = value

    @property
    def site_project_name( self ):
        if self.__siteprojectname is not None:
            return self.__siteprojectname

    @site_project_name.setter
    def site_project_name( self, value ):
        if value is not None:
            self.__siteprojectname = value

    @property
    def ssid( self ):
        if self.__ssid is not None:
            return self.__ssid

    @ssid.setter
    def ssid( self, value ):
        if value is not None:
            self.__ssid = value

    @property
    def action_code( self ):
        if self.__actioncode is not None:
            return self.__actioncode

    @action_code.setter
    def action_code( self, code ):
        if code is not None:
            self.__actioncode = code

    @property
    def operable_unit( self ):
        if self.__operableunit is not None:
            return self.__operableunit

    @operable_unit.setter
    def operable_unit( self, value ):
        if value is not None:
            self.__operableunit = value

    @property
    def state( self ):
        if self.__state is not None:
            return self.__state

    @state.setter
    def state( self, value ):
        if value is not None:
            self.__state = value

    @property
    def city( self ):
        if self.__city is not None:
            return self.__city

    @city.setter
    def city( self, value ):
        if value is not None:
            self.__city = value

    @property
    def congress( self ):
        if self.__congress is not None:
            return self.__congress

    @congress.setter
    def congress( self, value ):
        if value is not None:
            self.__congress = value

    @property
    def start_date( self ):
        if self.__startdate is not None:
            return self.__startdate

    @start_date.setter
    def start_date( self, value ):
        if value is not None:
            self.__startdate = value

    @property
    def end_date( self ):
        if self.__enddate is not None:
            return self.__enddate

    @end_date.setter
    def end_date( self, value ):
        if value is not None:
            self.__enddate = value

    @property
    def last_activity_date( self ):
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def requested( self ):
        if self.__requested is not None:
            return self.__requested

    @requested.setter
    def requested( self, value ):
        if value is not None:
            self.__requested = value

    @property
    def accepted( self ):
        if self.__accepted is not None:
            return self.__accepted

    @accepted.setter
    def accepted( self, value ):
        if value is not None:
            self.__accepted = value

    @property
    def closed( self ):
        if self.__closed is not None:
            return self.__closed

    @closed.setter
    def closed( self, value ):
        if value is not None:
            self.__closed = value

    @property
    def refunded( self ):
        if self.__refunded is not None:
            return self.__refunded

    @refunded.setter
    def refunded( self, value ):
        if value is not None:
            self.__refunded = value

    @property
    def reversal( self ):
        if self.__reversal is not None:
            return self.__reversal

    @reversal.setter
    def reversal( self, value ):
        if value is not None:
            self.__reversal = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, rpio, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SiteActivity
        self.__bfy = bfy
        self.__efy = efy
        self.__rpiocode = rpio
        self.__fields = [ 'SiteActivityId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'FundCode',
                           'FundName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'BocCode',
                           'BocName',
                           'OrgCode',
                           'OrgName',
                           'FocCode',
                           'FocName',
                           'EpaSiteId',
                           'SiteProjectCode',
                           'SSID',
                           'ActionCode',
                           'OperableUnit',
                           'SiteProjectName',
                           'State',
                           'City',
                           'CongressionalDistrict',
                           'ProjectType',
                           'StartDate',
                           'LastActivity',
                           'EndDate',
                           'Requested',
                           'Accepted',
                           'Closed',
                           'Outstanding',
                           'Refunded',
                           'Reversal' ]

    def get_data( self  ) -> list[ tuple ]:
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ tuple( i ) for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SiteActivity'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SiteActivity'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# SpendingDocumnet( bfy, efy, fund, account, boc, provider = Provider.SQLite )
class SpendingDocument( ):
    # provides data on spending documents
    __source = None
    __provider = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __commitments = None
    __obligations = None
    __deobligations = None
    __unliquidatedobligations = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__obligationsid, int ):
            return self.__obligationsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__obligationsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ):
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ):
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def commitments( self ):
        if self.__commitments is not None:
            return self.__commitments

    @commitments.setter
    def commitments( self, value ):
        if value is not None:
            self.__commitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ):
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ):
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value ):
        if value is not None:
            self.__used = value

    @property
    def available( self ):
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ):
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def document_type( self ):
        if self.__documenttyp is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ):
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fund, account, boc, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Obligations
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'ObligationsId',
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
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self ) -> list[ Row ]:
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Obligaions'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Obligation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# CarryoverEstimate( bfy, provider = Provider.SQLite )
class SupplementalCarryoverEstimate( ):
    '''CarryoverEstimate( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __supplementalcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__annualcarryoverestimatesid, int ):
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ):
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ):
        if isinstance( self.__availablebalance, float ):
            return self.__availablebalance

    @available.setter
    def available( self, value ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ):
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
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
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimate'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# TreasurySymbol( bfy, efy, fundcode, provider = Provider.SQLite )
class TreasurySymbol( ):
    '''TreasurySymbol( value )
    creates object that represents a TAFS'''
    __source = None
    __provider = None
    __treasurysymbolsid = None
    __ombagencycode = None
    __treasuryagencycode = None
    __bfy = None
    __efy = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__treasurysymbolsid, int ):
            return self.__treasurysymbolsid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__treasurysymbolsid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ):
        if isinstance( self.__budgetaccountcode, str ) and self.__budgetaccountcode != '':
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if isinstance( self.__budgetaccountname, str ) and self.__budgetaccountname != '':
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, treas, provider = Provider.SQLite ):
        self.__provider = provider
        self.__soruce = Source.FundSymbols
        self.__bfy = bfy
        self.__efy = efy
        self.__treasuryaccountcode = treas
        self.__fields = [ 'TreasurySymbolsId',
                          'BFY',
                          'EFY',
                          'FundCode',
                          'FundName',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'ApportionmentAccountCode' ]

    def __str__( self ):
        if isinstance( self.__treasuryaccountname, str ) and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            command = SQL.SELECTALL
            n = [ 'BFY', 'EFY', 'TreasuryAccountCode' ]
            v = (self.__bfy, self.__efy, self.__treasuryaccountcode)
            dbcfg = DbConfig( source, provider )
            sqlcfg = SqlConfig( names = n, values = v )
            cnx = Connection( dbcfg )
            sql = SqlStatement( dbcfg, sqlcfg )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'TreasurySymbol'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'TreasurySymbol'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# Transfer( documentnumber, provider = Provider.SQLite )
class Transfer( ):
    ''' Transfer( documentnumber ) initializes object
    representing EPA reprogrammings'''
    __source = None
    __provider = None
    __transfersid = None
    __documenttype = None
    __documentnumber = None
    __processeddate = None
    __budgetlevel = None
    __rpiocode = None
    __rpioname = None
    __bfy = None
    __efy = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__transfersid, int ):
            return self.__transfersid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__transfersid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def budget_level( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != '':
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def document_type( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def processed_date( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_name.setter
    def rpio_name( self, name ):
        if  name is not None:
            self.__rpiocode = name

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def ah_code( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def account_code( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def program_project_code( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def activitycode( self ):
        if isinstance( self.__activitycode, str ) and self.__activitycode != '':
            return self.__activitycode

    @activitycode.setter
    def activitycode( self, value ):
        if isinstance( value, str ) and self.__activitycode != '':
            self.__activitycode = value

    @property
    def activityname( self ):
        if isinstance( self.__activityname, str ) and self.__activityname != '':
            return self.__activityname

    @activityname.setter
    def activityname( self, value ):
        if isinstance( value, str ) and self.__activityname != '':
            self.__activityname = value

    @property
    def org_code( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def rc_code( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def boc_code( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_area_code( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, documentnumber, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Transfers
        self.__documentnumber = documentnumber if isinstance( documentnumber, str ) else None
        self.__fields = [ 'TransfersId',
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

    def get_data( self  ):
        try:
            src = self.__source
            pdr = self.__provider
            command = SQL.SELECTALL
            n = [ 'DocumentNumber', ]
            v = (self.__documentnumber,)
            dconfig = DbConfig( source = src, provider = pdr )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Transfer'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Transfer'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# TransType( bfy, fundcode, provider = Provider.SQLite )
class TransType( ):
    __source = None
    __provider = None
    __transtypesid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __doctype = None
    __appropriationbill = None
    __continuingresolution = None
    __rescissioncurrentyear = None
    __rescissionprioryear = None
    __sequesterreduction = None
    __sequesterreturn = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__transtypesid, int ):
            return self.__transtypesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__transtypesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def appropriation( self ):
        if isinstance( self.__appropriation, str ) and self.__appropriation != '':
            return self.__appropriation

    @appropriation.setter
    def appropriation( self, value ):
        if value is not None:
            self.__appropriation = value

    @property
    def treasury_symbol( self ):
        if isinstance( self.__treasuryaccount, str ) and self.__treasuryaccount != '':
            return self.__treasuryaccount

    @treasury_symbol.setter
    def treasury_symbol( self, value ):
        if value is not None:
            self.__treasuryaccount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, fundcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.TransTypes
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'TransTypesId',
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

# Unobligated Authority( account, provider = Provider.SQLite )
class UnobligatedAuthority( ):
    '''UnobligatedAuthority( bfy, omb )
    object provides OMB data'''
    __source = None
    __provider = None
    __unobligatedauthorityid = None
    __reportyear = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __ombaccounttitle = None
    __linenumber = None
    __linename = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__unobligatedauthorityid, int ):
            return self.__unobligatedauthorityid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__unobligatedauthorityid = value

    @property
    def report_year( self ):
        if isinstance( self.__reportyear, str ) and len( self.__reportyear ) == 4:
            return self.__reportyear

    @report_year.setter
    def report_year( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__reportyear = value

    @property
    def line_number( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @line_number.setter
    def line_number( self, value ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_name( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @line_name.setter
    def line_name( self, value ):
        if value is not None:
            self.__linename = value

    @property
    def budget_account_code( self ):
        if isinstance( self.__budgetaccountcode, str ) and self.__budgetaccountcode != '':
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ):
        if isinstance( self.__budgetaccountname, str ) and self.__budgetaccountname != '':
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def prior_year( self ):
        if isinstance( self.__prioryear, float ):
            return self.__prioryear

    @prior_year.setter
    def prior_year( self, value ):
        if value is not None:
            self.__prioryear = value

    @property
    def current_year( self ):
        if isinstance( self.__currentyear, float ):
            return self.__currentyear

    @current_year.setter
    def current_year( self, value ):
        if value is not None:
            self.__currentyear = value

    @property
    def budget_year( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value ):
        if value is not None:
            self.__budgetyear = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnobligatedAuthority
        self.__budgetaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'UnobligatedAuthorityId',
                          'ReportYear',
                          'AgencyCode',
                          'BureauCode',
                          'AccountCode',
                          'OmbAccount',
                          'OmbAccountName',
                          'LineName',
                          'LineNumber',
                          'BudgetYear',
                          'PriorYear',
                          'CurrentYear',
                          'AgencyName',
                          'BureauName' ]

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'OmbAccountCode', ]
            v = (self.__budgetaccountcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedAuthority'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedAuthority'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# UnobligatedBalance( bfy, efy, fundcode, provider = Provider.SQLite )
class UnobligatedBalance( ):
    '''object provides OMB data on unobligated
    balances by Fund Code and General Ledger Account'''
    __source = None
    __provider = None
    __unobligatedbalancesid = None
    __bfy = None
    __efy = None
    __treasurysymbol = None
    __fundcode = None
    __fundname = None
    __accountnumber = None
    __accountname = None
    __amount = None
    __fields = None
    __frame = None
    __data = None

    @property
    def id( self ):
        if isinstance( self.__unobligatedbalancesid, int ):
            return self.__unobligatedbalancesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__unobligatedbalancesid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def account_number( self ):
        if isinstance( self.__accountnumber, str ) and self.__accountnumber != '':
            return self.__accountnumber

    @account_number.setter
    def account_number( self, value ):
        if value is not None:
            self.__accountnumber = value

    @property
    def account_name( self ):
        if isinstance( self.__accountname, str ) and self.__accountname != '':
            return self.__accountname

    @account_name.setter
    def account_name( self, value ):
        if value is not None:
            self.__accountname = value

    @property
    def treasury_symbol( self ):
        if isinstance( self.__treasuryaccount, str ) and self.__treasuryaccount != '':
            return self.__treasuryaccount

    @treasury_symbol.setter
    def treasury_symbol( self, value ):
        if value is not None:
            self.__treasuryaccount = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnobligatedBalances
        self.__bfy = bfy if isinstance( bfy, str ) and bfy != '' else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields =[ 'UnobligatedBalancesId',
                           'BudgetYear',
                           'BFY',
                           'EFY',
                           'TreasurySymbol',
                           'FundCode',
                           'FundName',
                           'AccountNumber',
                           'AccountName',
                           'Amount' ]

    def get_data( self  ):
        try:
            source = Source.CarryoverOutlays
            provider = Provider.SQLite
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedBalance'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedBalance'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# UnliquidatedObligation( bfy, fund, account, boc, provider = Provider.SQLite )
class UnliquidatedObligation( ):
    '''UnliquidatedObligation( bfy, fund, account, boc )
    initializes object providing ULO data'''
    __source = None
    __provider = None
    __unliquidatedobligationsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__expendituresid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ):
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @org_code.setter
    def org_code( self, value ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @account_code.setter
    def account_code( self, value ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @document_type.setter
    def document_type( self, value ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @foc_name.setter
    def foc_name( self, value ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, fund, account, boc, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnliquidatedObligations
        self.__bfy = bfy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'UnliquidatedObligationsId'
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
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'UnliquidatedObligation'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'UnliquidatedObligation'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

# WorkCode( fundcode, provider = Provider.SQLite )
class WorkCode( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __workcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__workcodesid, int ):
            return self.__workcodesid

    @id.setter
    def id( self, value ):
        if value is not None:
            self.__workcodesid = value

    @property
    def code( self ):
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value ):
        if value is not None:
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ):
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.WorkCodes
        self.__code = code
        self.__frame = DataFrame
        self.__fields = None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'WorkCode'
            exc.method = 'get_data( self )'
            err = ErrorDialog( exc )
            err.show( )

    def get_frame( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.get_frame( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'WorkCode'
            exc.method = 'get_frame( self )'
            err = ErrorDialog( exc )
            err.show( )

