import pyodbc as access
class AccessReferenceBuilder():
    '''Builds the budget execution data classes'''
    _connector = ''
    _connection = None
    _cursor = None
    _data = None

    def __init__( self ):
        self._connector = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=accdb\References.accdb;')
        self._connection = access.connect( self._connector,
            timeout = 3, attrs_before = dict() )
        self._cursor = self._connection.cursor()
        self._data = ''

    def get_data( self, table ):
        if self._data == '':
            self._data = self._cursor.execute( 'SELECT * FROM {0}', table )