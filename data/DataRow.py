class DataRow():
    '''Defines the DataRow Class'''
    __items = { }
    __values = []
    __columns = { }
    __index = -1

    @property
    def items( self ):
        return self.__items

    @property
    def columns( self ):
        return self.__columns

    @property
    def values( self ):
        return self.__values

    @property
    def index( self ):
        return self.__index

    def __init__( self, items ):
        self.__items = dict( items )
        self.__columns = dict.fromkeys( self.__items )
        self.__values = list( self.__items.values() )
        self.__index = self.__values[ 0 ]