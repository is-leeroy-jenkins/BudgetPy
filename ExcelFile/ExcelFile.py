import openpyxl as xl
import os

class ExcelFile():
    ''' Provides the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __rows = None
    __columns = None
    __dimensions = None

    @property
    def name( self ):
        ''' Get the name of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, filename ):
        if filename is not None and len( filename ) > 0:
            self.__name = str( filename )

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, count ):
        if isinstance( count, int ) and count > 0:
            self.__rows = count

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, count ):
        if isinstance( count, int ) and count > 0:
            self.__columns = count

    @property
    def dimensions( self ):
        if self.__dimensions is not None:
            return self.__dimensions

    @dimensions.setter
    def dimensions( self, grid = () ):
        if isinstance( grid, tuple ) and len( grid ) < 3:
            self.__dimensions = grid

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = xl.open( self.__path )
            return self.__workbook

    @workbook.setter
    def workbook( self, path ):
        ''' Gets the report template '''
        if path is not None and os.path.exists( path ):
            self.__workbook = xl.open( path )

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__worksheet is not None:
            return self.__worksheet

    @worksheet.setter
    def worksheet( self, name ):
        ''' Gets the workbooks worksheet '''
        if self.__workbook is not None and name is not None:
            self.__workbook.worksheets.clear()
            self.__worksheet = self.__workbook.create_sheet( title = name, index = 1 )

    def __init__( self, name, rows = 46, cols = 12 ):
        self.__path = r'etc\templates\report\Excel.xlsx'
        self.__name = str( name )
        self.__rows = int( rows )
        self.__columns = int( cols )
        self.__dimensions = ( self.__rows, self.__columns )
