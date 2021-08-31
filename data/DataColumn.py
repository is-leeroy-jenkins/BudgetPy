class DataColumn():
    '''Defines the DataColumn Class'''
    __name = None
    __type = None
    __caption = None
    __ordinal = -1
    __table = None
    __row = None
    __source = None
    __data = { }

    @property
    def name( self ):
        return self.__name

    @property
    def type( self ):
        return self.__type

    @property
    def caption( self ):
        return self.__caption

    @property
    def ordinal( self ):
        return self.__ordinal

    @property
    def table( self ):
        return self.__table

    @property
    def row( self ):
        return self.__row

    @property
    def source( self ):
        return self.__source

    @property
    def data( self ):
        return self.__data

    def __init__( self, name, data_type = 'string', source = '',
                  caption = '' ):
        self.__name = name
        self.__type = data_type
        self.__caption = caption
        self.__data = [ self.__name, self.__type, self.__ordinal ]
        self.__source = source