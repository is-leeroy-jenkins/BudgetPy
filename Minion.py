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
     Copyright ©  2024  Terry Eppler

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
from Static import Client

class App( ):
    '''
    Constructor:
    App( client: enum )


    Purpose:
    Class defines object providing factory methods run( ) and run( args ) that run
    processes based on 'Client' enumeration input args
    '''
    __app: Client=None
    __sqlite: str=None
    __access: str=None
    __excel: str=None
    __edge: str=None
    __chrome: str=None
    __controlpanel: str=None
    __calculator: str=None

    @property
    def sqlite( self ) -> str:
        if self.__sqlite is not None:
            return self.__sqlite

    @sqlite.setter
    def sqlite( self, value: str ):
        if value is not None:
            self.__sqlite = value

    @property
    def access( self ) -> str:
        if self.__access is not None:
            return self.__access

    @access.setter
    def access( self, value: str ):
        if value is not None:
            self.__access = value

    @property
    def excel( self ) -> str:
        if self.__excel is not None:
            return self.__excel

    @excel.setter
    def excel( self, value: str ):
        if value is not None:
            self.__excel = value

    @property
    def chrome( self ) -> str:
        if self.__chrome is not None:
            return self.__chrome

    @chrome.setter
    def chrome( self, value: str ):
        if value is not None:
            self.__chrome = value

    @property
    def edge( self ) -> str:
        if self.__edge is not None:
            return self.__edge

    @edge.setter
    def edge( self, value: str ):
        if value is not None:
            self.__edge = value

    def __init__( self, client: Client ):
        self.__app = client
        self.__sqlite = r'db\sqlite\gui\SQLiteDatabaseBrowserPortable.exe'
        self.__access = r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE'
        self.__excel = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        self.__edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        self.__chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.__controlpanel = r'C:\Windows\System32\control.exe'
        self.__calculator = r'C:\Windows\System32\calc.exe'

    def run( self ):
        '''
        Purpose:

        Parameters:

        Returns:
        '''
        try:
            if self.__app == Client.SQLite:
                sp.Popen( self.__sqlite )
            elif self.__app == Client.Access:
                sp.Popen( self.__access )
            elif self.__app == Client.Excel:
                sp.Popen( self.__excel )
            elif self.__app == Client.Edge:
                sp.Popen( self.__edge )
            elif self.__app == Client.Chrome:
                sp.Popen( self.__chrome )
            elif self.__app == Client.ControlPanel:
                sp.Popen( self.__controlpanel )
            elif self.__app == Client.Calculator:
                sp.Popen( self.__calculator )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Minion'
            _exc.cause = 'App'
            _exc.method = 'run( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def run_args( self, args: str ):
        '''
        Purpose:

        Parameters:

        Returns:
        '''
        try:
            if args is not None and self.__app == Client.SQLite:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__sqlite, args ] )
            elif args is not None and self.__app == Client.Access:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__access, args ] )
            elif args is not None and self.__app == Client.Excel:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__excel, args ] )
            elif args is not None and self.__app == Client.Edge:
                    sp.Popen( args )
            elif args is not None and self.__app == Client.Chrome:
                    sp.Popen( [ self.__chrome, args ] )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Minion'
            _exc.cause = 'App'
            _exc.method = 'run_args( self, args )'
            _err = ErrorDialog( _exc )
            _err.show( )
