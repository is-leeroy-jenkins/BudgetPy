import subprocess as sp
import os
from Static import Client
from Booger import *


# App( client )
class App( ):
    '''App( client ) initializes object providing
     factory methods run( ) and run( args ) that run
     processes based on 'client' enumeration input args'''
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
        self.__app = client if isinstance( client, Client ) else None
        self.__sqliteclient = r'db\sqlite\gui\SQLiteDatabaseBrowserPortable.exe'
        self.__accessclient = r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE'
        self.__excelapp = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        self.__edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        self.__chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.__control = r'C:\Windows\System32\control.exe'
        self.__calculator = r'C:\Windows\System32\calc.exe'

    def run( self ):
        '''instance method that runs a client program with know path'''
        try:
            if isinstance( self.__app, Client ) and self.__app == Client.SQLite:
                sp.Popen( self.__sqliteclient )
            elif isinstance( self.__app, Client ) and self.__app == Client.Access:
                sp.Popen( self.__accessclient )
            elif isinstance( self.__app, Client ) and self.__app == Client.Excel:
                sp.Popen( self.__excelapp )
            elif isinstance( self.__app, Client ) and self.__app == Client.Edge:
                sp.Popen( self.__edge )
            elif isinstance( self.__app, Client ) and self.__app == Client.Chrome:
                sp.Popen( self.__chrome )
            elif isinstance( self.__app, Client ) and self.__app == Client.ControlPanel:
                sp.Popen( self.__control )
            elif isinstance( self.__app, Client ) and self.__app == Client.Calculator:
                sp.Popen( self.__calculator )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Minion'
            exc.cause = 'App'
            exc.method = 'run( self )'
            err = ErrorDialog( exc )
            err.show( )

    def runargs( self, args ):
        '''runargs( args ) instance method that runs client application with provided string 'args' '''
        try:
            if isinstance( args, str ) and self.__app == Client.SQLite:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__sqliteclient, args ] )
            elif isinstance( args, str ) and self.__app == Client.Access:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__accessclient, args ] )
            elif isinstance( args, str ) and self.__app == Client.Excel:
                if os.path.isfile( args ):
                    sp.Popen( [ self.__excelapp, args ] )
            elif isinstance( args, str ) and self.__app == Client.Edge:
                    sp.Popen( args )
            elif isinstance( args, str ) and self.__app == Client.Chrome:
                    sp.Popen( [ self.__chrome, args ] )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Minion'
            exc.cause = 'App'
            exc.method = 'runargs( self, args )'
            err = ErrorDialog( exc )
            err.show( )

