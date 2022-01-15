class Holiday():
    '''Defines the Holiday class'''
    __bfy = None
    __name = None
    __date = None
    __day = None
    __data = None
    __dataframe = None

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = str( year )
            self.__data[ 'bfy' ] = self.__bfy

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @date.setter
    def date( self, date ):
        if isinstance( date, dt.date ):
            self.__date = date
            self.__data[ 'date' ] = str( self.__date )

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @day.setter
    def day( self, day ):
        if isinstance( day, int ):
            self.__day = day
            self.__data[ 'day' ] = str( self.__day )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, bfy, name ):
        self.__bfy = str( bfy )
        self.__name = str( name )
        self.__date = dt.date.today()
        self.__day = self.__date.day
        self.__data = { 'bfy': self.__bfy,
                        'name': self.__name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__name is not None:
            return self.__name


