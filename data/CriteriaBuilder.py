class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __sql = None
    __and = None
    __where = None

    @property
    def and( self ):
        return self.__and

    @property
    def where( self ):
        return self.__where

    def __init__( self ):
        self.__and = ' AND '
        self.__where = ' WHERE '