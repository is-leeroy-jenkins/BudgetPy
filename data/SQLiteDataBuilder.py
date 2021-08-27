import sqlite3
class SQLiteDataBuilder():
    '''Builds the budget execution data classes'''
    _connection = None
    _cursor = None
    _data = None

    def __init__( self ):
        self._connection = sqlite3.connect('Data.db')
        self._cursor = self._connection.cursor()
        self._data = ''

    def get_data( self, table ):
        if self._data == '':
            self._data = self._cursor.execute(f'SELECT * FROM {0}', table)