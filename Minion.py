import subprocess as sp
from enum import Enum, auto
import os


class Client( Enum ):
    '''Enumeration of auxiliary applications'''
    NS = auto( )
    SQLite = auto( )
    Access = auto( )
    Excel = auto( )
    Linq = auto( )
    Edge = auto( )
    Chrome = auto( )


class App( ):
    '''factory methods for running process'''
    __app = None
    __sqliteclient = None
    __accessclient = None
    __excelapp = None
    __edge = None
    __chrome = None

    @property
    def sqlite( self ):
        if isinstance( self.__sqliteclient, str ) and self.__sqliteclient != '':
            return self.__sqliteclient

    @property
    def access( self ):
        if isinstance( self.__accessclient, str ) and self.__accessclient != '':
            return self.__accessclient

    @property
    def excel( self ):
        if isinstance( self.__excelapp, str ) and self.__excelapp != '':
            return self.__excelapp

    def __init__( self, app ):
        self.__app = app if isinstance( app, Client ) else None
        self.__sqliteclient = r'db\sqlite\gui\SQLiteDatabaseBrowserPortable.exe'
        self.__accessclient = r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE'
        self.__excelapp = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        self.__edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        self.__chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    def run( self ):
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

    def runargs( self, args ):
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

