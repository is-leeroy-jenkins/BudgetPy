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
    __outlook: str=None

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

    @property
    def control_panel( self ) -> str:
        if self.__controlpanel is not None:
            return self.__controlpanel

    @control_panel.setter
    def control_panel( self, value: str ):
        if value is not None:
            self.__controlpanel = value

    @property
    def calculator( self ) -> str:
        if self.__calculator is not None:
            return self.__calculator

    @calculator.setter
    def calculator( self, value: str ):
        if value is not None:
            self.__calculator = value

    @property
    def task_manager( self ) -> str:
        if self.__taskmanager is not None:
            return self.__taskmanager

    @task_manager.setter
    def task_manager( self, value: str ):
        if value is not None:
            self.__taskmanager = value

    @property
    def outlook( self ) -> str:
        if self.__outlook is not None:
            return self.__outlook

    @outlook.setter
    def outlook( self, value: str ):
        if value is not None:
            self.__outlook = value

    @property
    def pyscripter( self ) -> str:
        if self.__pyscripter is not None:
            return self.__pyscripter

    @pyscripter.setter
    def pyscripter( self, value: str ):
        if value is not None:
            self.__pyscripter = value

    @property
    def storage( self ) -> str:
        if self.__storage is not None:
            return self.__storage

    @storage.setter
    def storage( self, value: str ):
        if value is not None:
            self.__storage = value

    @property
    def word( self ) -> str:
        if self.__word is not None:
            return self.__word

    @word.setter
    def word( self, value: str ):
        if value is not None:
            self.__word = value

    def __init__( self, client: Client ):
        self.__app = client
        self.__sqlite = r'db\sqlite\gui\SQLiteDatabaseBrowserPortable.exe'
        self.__access = r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE'
        self.__excel = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        self.__edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        self.__chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.__controlpanel = r'C:\Windows\System32\control.exe'
        self.__calculator = r'C:\Windows\System32\calc.exe'
        self.__outlook = r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE'
        self.__pyscripter = r'db\python\PyScripter\PyScripter.exe'
        self.__taskmanager = r'C:\Windows\System32\Taskmgr.exe'
        self.__storage = r'C:\Users\teppler\AppData\Local\Microsoft\OneDrive\OneDrive.exe'
        self.__word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'

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
            elif self.__app == Client.Outlook:
                sp.Popen( self.__outlook )
            elif self.__app == Client.Pyscripter:
                sp.Popen( self.__pyscripter )
            elif self.__app == Client.TaskManager:
                sp.Popen( self.__taskmanager )
            elif self.__app == Client.Storage:
                sp.Popen( self.__storage )
            elif self.__app == Client.Word:
                sp.Popen( self.__word )
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
            elif args is not None and self.__app == Client.Outlook:
                    sp.Popen( [ self.__outlook, args ] )
            elif args is not None and self.__app == Client.Pyscripter:
                    sp.Popen( [ self.__pyscripter, args ] )
            elif args is not None and self.__app == Client.Word:
                    sp.Popen( [ self.__word, args ] )
            elif args is not None and self.__app == Client.TaskManager:
                    sp.Popen( [ self.__taskmanager, args ] )
            elif args is not None and self.__app == Client.ControlPanel:
                    sp.Popen( [ self.__controlpanel, args ] )
            elif args is not None and self.__app == Client.Storage:
                    sp.Popen( [ self.__storage, args ] )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Minion'
            _exc.cause = 'App'
            _exc.method = 'run_args( self, args )'
            _err = ErrorDialog( _exc )
            _err.show( )