import pandas as pd

class Account():
    '''defines the Account Code class'''
    __code = None
    __name = None
    __goal = None
    __objective = None
    __npm = None
    __programproject = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'code' ] = self.__code

    @property
    def name( self ):
        if self.__name:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def goal( self ):
        if self.__goal is not None:
            return self.__goal

    @goal.setter
    def goal( self, goal ):
        if goal is not None:
            self.__goal = str( goal )
            self.__data[ 'goal' ] = self.__goal

    @property
    def objective( self ):
        if self.__objective is not None:
            return self.__objective

    @objective.setter
    def objective( self, obj ):
        if obj is not None:
            self.__objective = str( obj )
            self.__data[ 'objective' ] = self.__objective

    @property
    def npm( self ):
        if self.__npm is not None:
            return self.__npm

    @npm.setter
    def npm( self, code ):
        if code is not None:
            self.__npm = str( code )
            self.__data[ 'npm' ] = self.__npm

    @property
    def programproject( self ):
        if self.__programproject is not None:
            return self.__programproject

    @programproject.setter
    def programproject( self, code ):
        if code is not None:
            self.__programproject = str( code )
            self.__data[ 'programproject' ] = self.__programproject

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__data = { }
        self.__code = str( code )
        self.__goal = str( self.__code[ 0 ] )
        self.__objective = str( self.__code[ 1:3 ] )
        self.__npm = str( self.__code[ 3 ] )
        self.__programproject = str( self.__code[ 4:6 ] )
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__code is not None:
            return self.__code
