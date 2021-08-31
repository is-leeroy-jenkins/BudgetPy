class DataRow():
    '''Defines the DataRow Class'''
    __items = { }
    __value = None
    __values = []
    __columns = { }
    __id = -1

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
    def id( self ):
        return self.__id

    @property
    def value( self ):
        return self.__value

    @property
    def id( self ):
        return self.__id

    def __init__( self, items ):
        self.__items = dict( items )
        self.__columns = dict.fromkeys( self.__items )
        self.__values = list( self.__items.values() )
        self.__id = self.__values[ 0 ]
        self.__value = self.__items.setdefault( 'Amount', 0 )

    def __str__( self ):
        return self.__id + ' ' + self.__value

