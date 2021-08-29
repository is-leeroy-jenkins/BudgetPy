class DataColumn():
    '''Defines the DataColumn Class'''
    __name = None
    __type = None
    __caption = None
    __ordinal = -1

    @property
    def name( self ):
        return self.__name

    @property
    def type( self ):
        return self.__type

    @property
    def caption( self ):
        return self.__caption

    def __init__( self, name, data_type = 'string', caption = '' ):
        self.__name = name
        self.__type = data_type
        self.__caption = caption