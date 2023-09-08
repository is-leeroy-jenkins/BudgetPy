'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Minion.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Minion.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2023  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Minion.py
  </summary>
  ******************************************************************************************
  '''
import subprocess as sp
from Booger import *
from Static import APP

class App( ):
    '''
    Constructor:  App( client: enum )

    Purpose:  Class defines object providing
    factory methods run( ) and run( args ) that run
    processes based on 'APP' enumeration input args
    '''
    __app = None
    __sqliteclient = None
    __accessclient = None
    __excelapp = None
    __edge = None
    __chrome = None
    __control = None
    __calculator = None

    @property
    def sqlite( self ):
        if isinstance( self.__sqliteclient, str ) and self.__sqliteclient != '':
            return self.__sqliteclient

    @sqlite.setter
    def sqlite( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqliteclient = value

    @property
    def access( self ):
        if isinstance( self.__accessclient, str ) and self.__accessclient != '':
            return self.__accessclient

    @access.setter
    def access( self, value ):
        if isinstance( value, str ) and value!= '':
            self.__accessclient = value

    @property
    def excel( self ):
        if isinstance( self.__excelapp, str ) and self.__excelapp != '':
            return self.__excelapp

    @excel.setter
    def excel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__excelapp = value

    @property
    def chrome( self ):
        if isinstance( self.__chrome, str ) and self.__chrome != '':
            return self.__chrome

    @chrome.setter
    def chrome( self, value ):
        if isinstance( value, str ) and value != '':
            self.__chrome = value

    @property
    def edge( self ):
        if isinstance( self.__edge, str ) and self.__edge != '':
            return self.__edge

    @edge.setter
    def edge( self, value ):
        if isinstance( value, str ) and value != '':
            self.__edge = value

    def __init__( self, client ):
        self.__app = client if isinstance( client, APP ) else None
        self.__sqliteclient = r'db\sqlite\gui\SQLiteDatabaseBrowserPortable.exe'
        self.__accessclient = r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE'
        self.__excelapp = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        self.__edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        self.__chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.__control = r'C:\Windows\System32\control.exe'
        self.__calculator = r'C:\Windows\System32\calc.exe'

    def run( self ):
        '''Method that starts process running the member client program'''
        try:
            if isinstance( self.__app, APP ) and self.__app == APP.SQLite:
                sp.Popen( self.__sqliteclient )
            elif isinstance( self.__app, APP ) and self.__app == APP.Access:
                sp.Popen( self.__accessclient )
            elif isinstance( self.__app, APP ) and self.__app == APP.Excel:
                sp.Popen( self.__excelapp )
            elif isinstance( self.__app, APP ) and self.__app == APP.Edge:
                sp.Popen( self.__edge )
            elif isinstance( self.__app, APP ) and self.__app == APP.Chrome:
                sp.Popen( self.__chrome )
            elif isinstance( self.__app, APP ) and self.__app == APP.ControlPanel:
                sp.Popen( self.__control )
            elif isinstance( self.__app, APP ) and self.__app == APP.Calculator:
                sp.Popen( self.__calculator )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Minion'
            _exc.cause = 'App'
            _exc.method = 'run( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def run_args( self, args ):
        '''Method starts a process running the member
         client program with the provided string 'args' '''
        try:
            if isinstance( args, str ) and self.__app == APP.SQLite:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__sqliteclient, args ] )
            elif isinstance( args, str ) and self.__app == APP.Access:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__accessclient, args ] )
            elif isinstance( args, str ) and self.__app == APP.Excel:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__excelapp, args ] )
            elif isinstance( args, str ) and self.__app == APP.Edge:
                    sp.Popen( args )
            elif isinstance( args, str ) and self.__app == APP.Chrome:
                    sp.Popen( [ self.__chrome, args ] )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Minion'
            _exc.cause = 'App'
            _exc.method = 'run_args( self, args )'
            _err = ErrorDialog( _exc )
            _err.show( )

