import datetime
class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __fiscal_year = ''
    __today = ''
    __date = None
    __year = ''
    __start_date = ''
    __end_date = ''
    __expiration = ''
    __weekends = 0
    __workdays = 0
    __day = ''
    __month = ''
    __federal_holidays = { }

    def __init__( self, year ):
        self.__year = year
        self.__today = datetime.date
        self.__day = self.__today.day
        self.__month = self.__today.month

    def __str__( self ):
        return self.__fiscal_year
