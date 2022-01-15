import BudgetFiscalYear, Fund, ResourcePlanningOffice, AllowanceHolder
import Account, Activity, Organization, ResponsibilityCenter, BudgetObjectClass
import pandas as pd

class ProgramResultsCode():
    '''Defines the PRC class'''
    __rpio = None
    __bfy = None
    __ah = None
    __fund = None
    __org = None
    __account = None
    __activity = None
    __rc = None
    __boc = None
    __amount = None
    __data = None
    __dataframe = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if code is not None:
            self.__rpio = ResourcePlanningOffice( code )
            self.__data[ 'RPIO' ] = self.__rpio.code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__rpio = BudgetFiscalYear( year )
            self.__data[ 'BFY' ] = self.__bfy.firstyear

    @property
    def fund( self ):
        if self.__fund.code is not None:
            return Fund( self.__fund.code )

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = ResourcePlanningOffice( str( code ) )
            self.__data[ 'Fund' ] = self.__fund.code

    @property
    def ah( self ):
        if self.__ah is not None:
            return AllowanceHolder( self.__ah )

    @ah.setter
    def ah( self, code ):
        if code is not None:
            self.__ah = AllowanceHolder( str( code ) )
            self.__data[ 'AH' ] = self.__ah.code

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if code is not None:
            self.__account = Account( str( code ) )
            self.__data[ 'Account' ] = self.__account.code

    @property
    def activity( self ):
        if self.__account is not None:
            self.__activity = str( self.__account[ 5:2 ] )
            return Activity( self.__activity )

    @activity.setter
    def activity( self, code ):
        if code is not None:
            self.__activity = Activity( str( code ) )
            self.__data[ 'Activity' ] = self.__activity.code

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( str( code ) )
            self.__data[ 'ORG' ] = self.__org.code

    @property
    def rc( self ):
        if self.__rc is not None:
            return self.__rc

    @rc.setter
    def rc( self, code ):
        if code is not None:
            self.__rc = ResponsibilityCenter( str( code ) )
            self.__data[ 'RC' ] = self.__rc.code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__rpio = BudgetObjectClass( str( code ) )
            self.__data[ 'BOC' ] = self.__boc.code

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value
            self.__data[ 'Amount' ] = self.__amount

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, amount = 0 ):
        '''Initializes the PRC class'''
        self.__account = Account( str( code ) )
        self.__amount = amount
        self.__data = { 'code': self.__account.code,
                        'account': self.__account,
                        'amount': self.__amount }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__account.code is not None:
            return self.__account.code



