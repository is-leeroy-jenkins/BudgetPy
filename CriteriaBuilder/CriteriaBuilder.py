class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __and = None
    __where = None
    __or = None
    __criteria = None
    __cmd = None
    __sql = None

    @property
    def AND( self ):
        if self.__and is not None:
            return self.__and

    @property
    def WHERE( self ):
        if self.__where is not None:
            return self.__where

    @property
    def command( self ):
        if self.__cmd is not None:
            return str( self.__sql[ self.__cmd ] )

    @command.setter
    def command( self, cmd ):
        if cmd is not None and cmd in self.__sql:
            self.__cmd = str( self.__sql[ cmd ] )

    def create( self, pairs ):
        ''' builds criteria from dictionary of name value pairs'''
        if isinstance( pairs, dict ):
            self.__criteria = pairs

    def __init__( self, cmd = 'SELECT' ):
        self.__and = ' AND '
        self.__where = ' WHERE '
        self.__cmd = str( cmd )
        self.__sql = [ 'SELECT', 'INSERT', 'UPDATE',
                       'DELETE', 'CREATE', 'ALTER',
                       'DROP', 'DETACH' ]

