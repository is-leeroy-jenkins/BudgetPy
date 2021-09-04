import sqlite3
class SQLiteDataBuilder():
    '''Builds the budget execution data classes'''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connection = sqlite3.connect( 'Data.db' )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {0}', table )