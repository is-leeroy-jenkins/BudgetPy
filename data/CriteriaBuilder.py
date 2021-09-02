class CriteriaBuilder():
    '''Defines the CriteriaBuilder class'''
    __sql = ''
    __and = ''
    __where = ''
    __criteria = { }

    @property
    def AND( self ):
        return self.__and

    @property
    def WHERE( self ):
        return self.__where

    @property
    def criteria( self ):
        return self.__criteria

    @criteria.setter
    def criteria( self, name_value_pairs = None ):
        self.__criteria = name_value_pairs

    def __init__( self ):
        self.__and = ' AND '
        self.__where = ' WHERE '