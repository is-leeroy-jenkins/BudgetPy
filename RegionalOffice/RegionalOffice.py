class RegionalOffice():
    '''Defines a regional RPIO'''
    __rpio = None
    __name = None
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
            self.__data[ 'rpio' ] = self.__rpio

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
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, rpio ):
        self.__rpio = ResourcePlanningOffice( str( rpio ) )
        self.__name = self.__rpio.name
        self.__data = { 'rpio': self.__rpio,
                        'name': self.__name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__rpio is not None:
            return str( self.__rpio )


