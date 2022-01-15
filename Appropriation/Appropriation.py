import pandas as pd
import Fund

class Appropriation():
    '''Defines the Appropriation Class'''
    __fund = None
    __code = None
    __name = None
    __title = None
    __bfy = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )

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
    def fiscalyear( self ):
        if self.__bfy is not None:
            return self.__bfy

    @fiscalyear.setter
    def fiscalyear( self, bfy ):
        if bfy is not None:
            self.__bfy = str( bfy )
            self.__data[ 'bfy' ] = self.__bfy

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = Fund( str( code ) )
            self.__data[ 'fund' ] = self.__fund

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, title ):
        if title is not None:
            self.__title = str( title )
            self.__data[ 'title' ] = self.__title

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

    def __init__( self, code ):
        self.__code = str( code )
        self.__fund = Fund( code )
        self.__data = { 'code': self.__code,
                        'fund': self.__fund }

    def __str__( self ):
        return self.__code


