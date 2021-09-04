from ninja.AllowanceHolder import AllowanceHolder
from ninja.BudgetFiscalYear import BudgetFiscalYear
from ninja.ResponsiblePlanningOffice import ResponsiblePlanningOffice

class ProgramResultsCode():
    '''Defines the PRC class'''
    __id = -1
    __rpio_code = ''
    __fiscal_year = ''
    __ah_code = ''
    __fund_code = ''
    __org_code = ''
    __account_code = ''
    __rc_code = ''
    __boc_code = ''
    __amount = 0

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id
        else:
            return - 1

    @property
    def rpio( self ):
        if self.__rpio_code is not None:
            return ResponsiblePlanningOffice( self.__rpio_code )
        else:
            return 'NS'

    @property
    def bfy( self ):
        if self.__fiscal_year is not None:
            return BudgetFiscalYear( self.__fiscal_year )
        else:
            return 'NS'

    @property
    def ah( self ):
        if self.__ah_code is not None:
            return AllowanceHolder( self.__ah_code )
        else:
            return 'NS'

    def __init__( self, rpio = None, bfy = None,
                  ah = None, fund = None, code = None,
                  boc = None, org = None ):
        '''Initializes the PRC class'''

        self.__rpio_code = rpio
        self.__fiscal_year = bfy
        self.__ah_code = ah
        self.__fund_code = fund
        self.__account_code = code
        self.__org_code = org
        self.__boc_code = boc
