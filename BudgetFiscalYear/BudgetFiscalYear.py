class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __base = None
    __bfy = None
    __efy = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = 0
    __workdays = 0
    __year = None
    __month = None
    __day = None
    __holidays = None
    __data = None
    __dataframe = None

    @property
    def firstyear( self ):
        if self.__base is not None:
            return self.__bfy

    @firstyear.setter
    def firstyear( self, yr ):
        if yr is not None:
            self.__bfy = str( yr )
            self.__data[ 'firstyear' ] = self.__bfy

    @property
    def lastyear( self ):
        if self.__efy is not None:
            return self.__efy

    @lastyear.setter
    def lastyear( self, yr ):
        if yr is not None:
            self.__efy = str( yr )
            self.__data[ 'lastyear' ] = self.__efy

    @property
    def calendaryear( self ):
        if self.__year:
            return self.__year

    @calendaryear.setter
    def calendaryear( self, yr ):
        if yr is not None:
            self.__year = str( yr )
            self.__data[ 'calendaryear' ] = self.__year

    @property
    def startdate( self ):
        if isinstance( self.__startdate, dt.date ):
            return self.__startdate

    @startdate.setter
    def startdate( self, start ):
        if isinstance( start, dt.date ):
            self.__startdate = start
            self.__data[ 'startdate' ] = self.__startdate

    @property
    def enddate( self ):
        if isinstance( self.__enddate, dt.date ):
            return self.__enddate

    @enddate.setter
    def enddate( self, end ):
        if isinstance( end, dt.date ):
            self.__enddate = end
            self.__data[ 'enddate' ] = self.__enddate

    @property
    def expiration( self ):
        if isinstance( self.__expiration, dt.date ):
            return self.__expiration

    @expiration.setter
    def expiration( self, exp ):
        if isinstance( exp, dt.date ):
            self.__expiration = exp
            self.__data[ 'expiration' ] = self.__expiration

    @property
    def weekends( self ):
        if self.__weekends is not None:
            return self.__weekends

    @weekends.setter
    def weekends( self, end ):
        if isinstance( end, int ):
            self.__weekends = end
            self.__data[ 'weekends' ] = self.__weekends

    @property
    def workdays( self ):
        if self.__workdays is not None:
            return float( self.__workdays )

    @workdays.setter
    def workdays( self, work ):
        if isinstance( work, int ):
            self.__workdays = work
            self.__data[ 'workdays' ] = self.__workdays

    @property
    def date( self ):
        if isinstance( self.__date, dt.date ):
            return self.__date

    @date.setter
    def date( self, today ):
        if isinstance( today, dt.date ):
            self.__date = today
            self.__data[ 'date' ] = self.__date

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @day.setter
    def day( self, today ):
        if isinstance( today, dt.date ):
            self.__day = today
            self.__data[ 'day' ] = self.__day

    @property
    def month( self ):
        if self.__month is not None:
            return self.__month

    @property
    def holidays( self ):
        if self.__holidays is not None:
            return self.__holidays

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, bfy ):
        self.__today = dt.date.today()
        self.__base = str( bfy )
        self.__date = self.__today
        self.__year = int( self.__base )
        self.__day = self.__date.day
        self.__month = self.__date.month
        self.__startdate = dt.date( self.__year, 10, 1 )
        self.__bfy = str( self.__startdate.year )
        self.__enddate = dt.date( self.__year + 1, 9, 30 )
        self.__efy = str( self.__enddate.year )
        self.__data = { 'base': self.__base,
                        'date': self.__date,
                        'calendaryear': self.__year,
                        'day': self.__day,
                        'month': self.__month,
                        'startdate': self.__startdate,
                        'enddate': self.__enddate }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return str( self.__year )


