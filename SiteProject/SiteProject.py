import pandas as pd

class SiteProject():
    '''Defines the Site Project Code Class'''
    __epaid = None
    __ssid = None
    __actioncode = None
    __opunit = None
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def ssid( self ):
        if self.__ssid is not None:
            return self.__ssid

    @ssid.setter
    def ssid( self, ssid ):
        if ssid is not None:
            self.__ssid = str( ssid )
            self.__data[ 'ssid' ] = self.__ssid

    @property
    def actioncode( self ):
        if self.__actioncode is not None:
            return self.__actioncode

    @actioncode.setter
    def actioncode( self, code ):
        if code is not None:
            self.__actioncode = str( code )
            self.__data[ 'actioncode' ] = self.__actioncode

    @property
    def operableunit( self ):
        if self.__opunit is not None:
            return self.__opunit

    @operableunit.setter
    def operableunit( self, unit ):
        if unit is not None:
            self.__opunit = str( unit )
            self.__data[ 'operableunit' ] = self.__opunit

    @property
    def epaid( self ):
        if self.__epaid is not None:
            return self.__epaid

    @epaid.setter
    def epaid( self, eid ):
        if eid is not None:
            self.__epaid = str( eid )
            self.__data[ 'epaid' ] = self.__epaid

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'code' ] = self.__code

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

    def __init__( self, code ):
        self.__code = str( code )
        self.__ssid = self.__code[ 0: 4 ]
        self.__actioncode = self.__code[ 4:6 ]
        self.__opunit = self.__code[ 6:9 ]
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code



