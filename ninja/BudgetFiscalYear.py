import datetime
class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    _fiscal_year = ''
    _today = ''
    _date = None
    _year = ''
    _start_date = ''
    _end_date = ''
    _expiration = ''
    _weekends = 0
    _workdays = 0
    _day = ''
    _month = ''
    _federal_holidays = { }

    def __init__( self, year ):
        self._year = year
        self._today = datetime.date
        self._day = self._today.day
        self._month = self._today.month
