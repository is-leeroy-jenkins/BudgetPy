import sqlite3
class SQLiteReferenceBuilder():
    '''Builds the budget execution reference models'''
    _connection = None
    _cursor = None
    _data = None

    def __init__( self ):
        self._connection = sqlite3.connect('References.db')
        self._cursor = self._connection.cursor()
        self._data = ''

    def get_data( self, table ):
        if self._data == '':
            self._data = self._cursor.execute(f'SELECT * FROM {table}')