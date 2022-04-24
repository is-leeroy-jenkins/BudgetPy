import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window( QWidget ):
    '''Basic Window Class'''
    def __init__( self ):
        super( ).__init__( )
        __black = '#050505'
        __blue = '#1697FD'

        self.initializeUI( )

    def initializeUI( self ):
        self.setGeometry( 100, 100, 1400, 800 )
        self.setWindowTitle( 'Budget Execution' )
        self.show( )


if __name__ == '__main__':
    app = QApplication( sys.argv )
    window = Window( )
    sys.exit( app.exec_( ) )