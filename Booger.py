import sys
from PyQt5.QtWidgets import *

class BudgetWindow( QWidget ):
    '''Basic Window Class'''
    def __init__( self ):
        super( ).__init__( )

        self.initializeUI( )

    def initializeUI( self ):
        self.setGeometry( 100, 100, 400, 300 )
        self.setWindowTitle( 'Budget Execution' )
        self.show( )


if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = BudgetWindow( )
    sys.exit( app.exec_( ) )