import sqlite3
class SQLiteReferenceBuilder():
    '''Builds the budget execution reference models'''
    __connection = None
    __cursor = None
    __data = None

    def __init__( self ):
        self.__connection = sqlite3.connect( 'References.db' )
        self.__cursor = self.__connection.cursor()
        self.__data = ''

    def get_data( self, table ):
        if self.__data == '':
            self.__data = self.__cursor.execute( f'SELECT * FROM {table}' )