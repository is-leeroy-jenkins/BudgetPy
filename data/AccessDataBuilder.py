import pyodbc as access
class AccessDataBuilder():
    '''Builds the budget execution data classes'''
    __connector = ''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connector = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=accdb\Data.accdb;')
        self.__connection = access.connect( self.__connector,
            timeout = 3, attrs_before = dict() )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )