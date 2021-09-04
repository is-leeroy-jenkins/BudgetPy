class Unit:
    '''Defines the basic budget data unit'''
    __name = ''
    __value = ''

    @property
    def name( self ):
        if self.__name != '':
            return self.__name

    @property
    def value( self ):
        if self.__value != '':
            return self.__value

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def __str__(self):
        return self.__name