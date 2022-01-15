import sqlite3 as sl

class DataRow():
    '''Defines the DataRow Class'''
    __source = None
    __names = None
    __items = None
    __data = None
    __values = None
    __id = None
    __record = None

    @property
    def index( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @index.setter
    def index( self, ordinal ):
        if isinstance( ordinal, int ):
            self.__id = ordinal

    @property
    def data( self ):
        if self.__data is not None:
            return dict( self.__data )

    @data.setter
    def data( self, items ):
        if isinstance( items, dict ):
            self.__items = items

    @property
    def items( self ):
        if isinstance( self.__items, tuple ):
            return self.__items

    @items.setter
    def items( self, data ):
        if isinstance( data, tuple ):
            self.__items = data

    @property
    def names( self ):
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, data ):
        if isinstance( data, dict ):
            self.__names = data.keys()

    @property
    def values( self ):
        if self.__values is not None:
            return list( self.__values )

    @values.setter
    def values( self, items ):
        if isinstance( items, list ):
            self.__values = items

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, row ):
        if isinstance( row, sl.Row ):
            self.__source = row

    def __init__( self, items = None ):
        self.__source = sl.Row
        self.__items = tuple( items )
        self.__id = int( items[ 0 ] )
        self.__names = list( self.__items.keys() )
        self.__values = self.__items.values()

    def __str__( self ):
        return 'Row ID: ' + str( self.__id )

