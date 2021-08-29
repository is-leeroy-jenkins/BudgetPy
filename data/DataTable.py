class DataTable():
    '''Defines the DataTable Class'''
    __name = None
    __data = [ ]
    __schema = { }

    @property
    def name( self ):
        return self.__name

    @property
    def data( self ):
        return self.__data

    def __init__( self, name  ):
        self.__name = name