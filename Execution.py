import datetime as dt
from datetime import datetime, date
from Static import Source, Provider, SQL
from Booger import Error, ErrorDialog
import sys
from sys import exc_info
from Ninja import DbConfig, SqlConfig, Connection, \
    SqlStatement, BudgetData, DataBuilder
from Static import Source, Provider
from datetime import datetime, date
from pandas import DataFrame



class Unit( ):
    '''Unit( value, value ) initializes object
    representing fundemental unit of data
    in the Budget Execution application'''
    __index = None

    @property
    def id( self ):
        if isinstance( self.__index, int ):
            return self.__index

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__index = id

    def __init__( self, id ):
        self.__index = id if isinstance( id, int ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Element( Unit ):
    '''Element class represents fundemental program unit'''
    __index = None
    __code = None
    __name = None

    @property
    def name( self ):
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ):
            self.__name = name

    @property
    def code( self ):
        if isinstance( self.__name, str ):
            return self.__name

    def __init__( self, id, code, name ):
        super( ).__init__( id )
        self.__id = super( ).__id
        self.__code = code if isinstance( code, str ) else None
        self.__name = name if isinstance( name, str ) else None
        self.__code = code if isinstance( code, str ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


# Accounts( code, provider = Provider.SQLite )
class Accounts( ):
    '''defines the Account Code class'''
    __source = None
    __provider = None
    __accountsid = None
    __code = None
    __name = None
    __goalcode = None
    __objectivecode = None
    __npmcode = None
    __programprojectcode = None
    __programprojectname = None
    __fields = None
    __data = None
    __frame = None


    @property
    def id( self ):
        if isinstance( self.__accountsid, int ):
            return self.__accountsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__accountsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ):
            self.__npmcode = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode , str ):
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ):
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectcode

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ):
            self.__programprojectname = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Accounts
        self.__code = code if isinstance( code, str ) and len( code ) >= 6 else None
        self.__goalcode = self.__code[ 0 ]
        self.__objectivecode = self.__code[ 1:3 ]
        self.__npmcode = self.__code[ 3 ]
        self.__programprojectcode = self.__code[ 4:6 ]
        self.__fields = [ 'AccountsId',
                           'Code',
                           'GoalCode',
                           'ObjectiveCode',
                           'NpmCode',
                           'NpmName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'ActivityCode',
                           'ActivityName',
                           'AgencyActivity' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def copy( self ):
        try:
            clone = Account( code = self.__code )
            clone.code = self.__code
            clone.goalcode = self.__goalcode
            clone.objectivecode = self.__objectivecode
            clone.npmcode = self.__npmcode
            clone.programprojectcode = self.__programprojectcode
            return clone
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Account'
            exc.method = 'copy( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getdata( self ):
        try:
            source = Source.Accounts
            provider = Provider.SQLite
            n = [ 'Code', ]
            v = ( self.__code, )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( source, provider )
            sql = SqlStatement( cnx, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Account'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Account'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ActivityCodes( code, provider = Provider.SQLite )
class ActivityCodes( ):
    '''Defines the Activity Class'''
    __source = None
    __provider = None
    __activitycodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__activitycodesid, int ):
            return self.__activitycodesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__activitycodesid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ActivityCodes
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'ActivityCodesId',
                           'Code',
                           'Name',
                           'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Activity'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Activity'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# AllowanceHolders( code, provider = Provider.SQLite )
class AllowanceHolders( ):
    '''Defines the AllowanceHolder Class'''
    __source = None
    __provider = None
    __allowancholdersid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__allowancholdersid, int ):
            return self.__allowancholdersid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__allowancholdersid = id

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, code ):
        if isinstance( code, str ) and code != '':
            self.__code = code

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__data = cache

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AllowanceHolders
        self.__code = code if isinstance( self.__code, str ) else None
        self.__fields = [ 'AllowanceHoldersId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'AllowanceHolder'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'AllowanceHolder'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Appropriations( code, provider = Provider.SQLite )
class Appropriations( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __appropriationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__appropriationsid , int ):
            return self.__appropriationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__appropriationsid  = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'AppropriationsId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# AppropriationAvailableBalances( code, provider = Provider.SQLite )
class AppropriationAvailableBalances( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __appropriationavailablebalancesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__appropriationavailablebalancesid, int ):
            return self.__appropriationavailablebalancesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__appropriationavailablebalancesid  = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'AppropriationAvailableBalancesId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# AppropriationLevelAuthority( code, provider = Provider.SQLite )
class AppropriationLevelAuthority( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __appropriationlevelauthorityid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__appropriationlevelauthorityid , int ):
            return self.__appropriationlevelauthorityid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__appropriationlevelauthorityid  = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'AppropriationLevelAuthorityId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Allocation( bfy, fund, provider = Provider.SQLite )
class Allocations( ):
    '''object representing operating plan data'''
    __source = None
    __provider = None
    __allocationsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__source = Source.Allocations
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Allocations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Allocations'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ApportionmentData( bfy, efy, code, provider = Provider.SQLite )
class ApportionmentData( ):
    '''Apportionment( bfy, efy, omb )
    initializes object representing Letters Of Apportionment'''
    __source = None
    __provider = None
    __apportionmentdataid = None
    __bfy = None
    __efy = None
    __treasuryfundsymbol = None
    __ombaccountcode = None
    __ombaccountname = None
    __ombagency = None
    __treasuryagency = None
    __linenumber = None
    __linedescription = None
    __sectionnumber = None
    __sectiondescription = None
    __subline = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__apportionmentsid, int ):
            return self.__apportionmentsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__apportionmentsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def treasuryfundsymbol( self ):
        if isinstance( self.__treasuryfundsymbol, str ) and self.__treasuryfundsymbol != "":
            return self.__treasuryfundsymbol

    @treasuryfundsymbol.setter
    def treasuryfundsymbol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryfundsymbol = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def ombagency( self ):
        if isinstance( self.__ombagency, str ) \
                and self.__ombagency != '':
            return self.__ombagency

    @ombagency.setter
    def ombagency( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombagency = value

    @property
    def treasuryagency( self ):
        if isinstance( self.__treasuryagency, str ) \
                and self.__treasuryagency != '':
            return self.__treasuryagency

    @treasuryagency.setter
    def treasuryagency( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryagency = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) \
                and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def linedescription( self ):
        if isinstance( self.__linedescription, str ) \
                and self.__linedescription != '':
            return self.__linedescription

    @linedescription.setter
    def linedescription( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linedescription = value

    @property
    def sectionnumber( self ):
        if isinstance( self.__sectionnumber, str ) \
                and self.__sectionnumber != '':
            return self.__sectionnumber

    @sectionnumber.setter
    def sectionnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sectionnumber = value

    @property
    def sectiondescription( self ):
        if isinstance( self.__sectiondescription, str ) \
                and self.__sectiondescription != '':
            return self.__sectiondescription

    @sectiondescription.setter
    def sectiondescription( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sectiondescription = value

    @property
    def subline( self ):
        if isinstance( self.__subline, str ) \
                and self.__subline != '':
            return self.__subline

    @subline.setter
    def subline( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subline = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, omb, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Apportionments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__ombaccountcode = omb if isinstance( omb, str ) and len( omb ) == 4 else None
        self.__fields = [ 'ApportionmentDataId',
                          'FiscalYear',
                          'BFY',
                          'EFY',
                          'Availability',
                          'TreasuryFundCode',
                          'TreasuryFundName',
                          'TreasuryAgencyCode',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'OmbAgencyCode',
                          'OmbBureauCode',
                          'OmbAccountCode',
                          'OmbAgencyName',
                          'OmbAccountName',
                          'ApprovalDate',
                          'LineNumber',
                          'LineName',
                          'Amount',
                          'Footnote',
                          'Narrative' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            v = (self.__bfy, self.__efy, self.__ombaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'Apportionment'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'Apportionment'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Acutals( bfy, fund, provider = Provider.SQLite  )
class Actuals( ):
    '''Object representing expenditure data'''
    __source = None
    __provider = None
    __actualsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __appropriationcode = None
    __appropriationname = None
    __subappropriationcode = None
    __subappropriationname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __balance = None
    __obligations = None
    __ulo = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__actualsid, int ):
            return self.__actualsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__id = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__efy = year

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def balance( self ):
        if isinstance( self.__balance, float ):
            return self.__balance

    @balance.setter
    def balance( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Actuals
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'ActualsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'AppropriationCode',
                           'AppropriationName',
                           'SubAppropriationCode',
                           'SubAppropriationName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RpioActivityCode',
                           'RpioActivityName',
                           'BocCode',
                           'BocName',
                           'ULO',
                           'Obligations',
                           'Balance',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'GoalCode',
                           'GoalName',
                           'ObjectiveCode',
                           'ObjectiveName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Actuals'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Actuals'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# AppropriationDocuments( bfy, fund, provider = Provider.SQLite )
class AppropriationDocuments( ):
    '''object representing Level 1 documents'''
    __source = None
    __provider = None
    __appropriationdocumentsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fund = None
    __documenttype = None
    __documentnumber = None
    __documentdate = None
    __lastdocumentdate = None
    __budgetlevel = None
    __budgetingcontrols = None
    __postingcontrols = None
    __precommitmentcontrols = None
    __commitmentcontrols = None
    __obligationcontrols = None
    __accrualcontrols = None
    __expenditurecontrols = None
    __expensecontrols = None
    __reimbursementcontrols = None
    __reimbursableagreementcontrols = None
    __budgeted = None
    __posted = None
    __carryoverout = None
    __carryoverin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__appropriationdocumentsid, int ):
            return self.__appropriationdocumentsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__appropriationdocumentsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fund( self ):
        if isinstance( self.__fund, str ) and self.__fund != '':
            return self.__fund

    @fund.setter
    def fund( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fund = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ):
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ):
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentname, str ):
            return self.__documentname

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ):
            self.__documentname = value

    @property
    def documentdate( self ):
        if isinstance( self.__documentdate, datetime ):
            return self.__documentdate

    @documentdate.setter
    def documentdate( self, value ):
        if isinstance( value, datetime ):
            self.__documentdate = value

    @property
    def lastdocumentdate( self ):
        if isinstance( self.__lastdocumentdate, datetime ):
            return self.__lastdocumentdate

    @lastdocumentdate.setter
    def lastdocumentdate( self, value ):
        if isinstance( value, datetime ):
            self.__lastdocumentdate = value

    @property
    def budgetlevel( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != '':
            return self.__budgetlevel

    @budgetlevel.setter
    def budgetlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetlevel = value

    @property
    def budgetingcontrols( self ):
        if isinstance( self.__budgetingcontrols, str ):
            return self.__budgetingcontrols

    @budgetingcontrols.setter
    def budgetingcontrols( self, value ):
        if isinstance( value, str ):
            self.__budgetingcontrols = value

    @property
    def postingcontrols( self ):
        if isinstance( self.__postingcontrols, str ):
            return self.__postingcontrols

    @postingcontrols.setter
    def postingcontrols( self, value ):
        if isinstance( value, str ):
            self.__postingcontrols = value

    @property
    def precommitmentcontrols( self ):
        if isinstance( self.__precommitmentcontrols, str ):
            return self.__precommitmentcontrols

    @precommitmentcontrols.setter
    def precommitmentcontrols( self, value ):
        if isinstance( value, str ):
            self.__precommitmentcontrols = value

    @property
    def commitmentcontrols( self ):
        if isinstance( self.__commitmentcontrols, str ):
            return self.__commitmentcontrols

    @commitmentcontrols.setter
    def commitmentcontrols( self, value ):
        if isinstance( value, str ):
            self.__commitmentcontrols = value

    @property
    def obligationcontrols( self ):
        if isinstance( self.__obligationcontrols, str ):
            return self.__obligationcontrols

    @obligationcontrols.setter
    def obligationcontrols( self, value ):
        if isinstance( value, str ):
            self.__obligationcontrols = value

    @property
    def accrualcontrols( self ):
        if isinstance( self.__accrualcontrols, str ):
            return self.__accrualcontrols

    @accrualcontrols.setter
    def accrualcontrols( self, value ):
        if isinstance( value, str ):
            self.__accrualcontrols = value

    @property
    def expenditurecontrols( self ):
        if isinstance( self.__expenditurecontrols, str ):
            return self.__expenditurecontrols

    @expenditurecontrols.setter
    def expenditurecontrols( self, value ):
        if isinstance( value, str ):
            self.__expenditurecontrols = value

    @property
    def expensecontrols( self ):
        if isinstance( self.__expensecontrols, str ):
            return self.__expensecontrols

    @expensecontrols.setter
    def expensecontrols( self, value ):
        if isinstance( value, str ):
            self.__expensecontrols = value

    @property
    def reimbursementcontrols( self ):
        if isinstance( self.__reimbursementcontrols, str ):
            return self.__reimbursementcontrols

    @reimbursementcontrols.setter
    def reimbursementcontrols( self, value ):
        if isinstance( value, str ):
            self.__reimbursementcontrols = value

    @property
    def reimbursableagreementcontrols( self ):
        if isinstance( self.__reimbursableagreementcontrols, str ):
            return self.__reimbursableagreementcontrols

    @reimbursableagreementcontrols.setter
    def reimbursableagreementcontrols( self, value ):
        if isinstance( value, str ):
            self.__reimbursableagreementcontrols = value

    @property
    def budgeted( self ):
        if isinstance( self.__budgeted, float ):
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if isinstance( value, float ):
            self.__budgeted = value

    @property
    def posted( self ):
        if isinstance( self.__posted, float ):
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( value, float ):
            self.__posted = value

    @property
    def carryoverin( self ):
        if isinstance( self.__carryoverin, float ):
            return self.__carryoverin

    @carryoverin.setter
    def carryoverin( self, value ):
        if isinstance( value, float ):
            self.__carryoverin = value

    @property
    def carryoverout( self ):
        if isinstance( self.__carryoverout, float ):
            return self.__carryoverout

    @carryoverout.setter
    def carryoverout( self, value ):
        if isinstance( value, float ):
            self.__carryoverout = value

    @property
    def estimatedreimbursements( self ):
        if isinstance( self.__reimbursementcontrols, float ):
            return self.__reimbursementcontrols

    @estimatedreimbursements.setter
    def estimatedreimbursements( self, value ):
        if isinstance( value, float ):
            self.__estimatedreimbursements = value

    @property
    def estimatedrecoveries( self ):
        if isinstance( self.__estimatedrecoveries, float ):
            return self.__estimatedrecoveries

    @estimatedrecoveries.setter
    def estimatedrecoveries( self, value ):
        if isinstance( value, float ):
            self.__estimatedrecoveries = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AppropriationDocuments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'AppropriationDocumentsId',
                           'BFY',
                           'EFY',
                           'Fund',
                           'FundCode',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentDate',
                           'LastDocumentDate',
                           'BudgetLevel',
                           'BudgetingControls',
                           'PostingControls',
                           'PreCommitmentControls',
                           'CommitmentControls',
                           'ObligationControls',
                           'AccrualControls',
                           'ExpenditureControls',
                           'ExpenseControls',
                           'ReimbursementControls',
                           'ReimbursableAgreementControls',
                           'Budgeted',
                           'Posted',
                           'CarryOut',
                           'CarryIn',
                           'EstimatedReimbursements',
                           'EstimatedRecoveries' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'AppropriationDocument'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'AppropriationDocument'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetDocuments( bfy, fund, provider = Provider.SQLite )
class BudgetDocuments( ):
    '''object representing Level 2-3 documents'''
    __source = None
    __provider = None
    __budgetdocumentsid = None
    __bfy = None
    __efy = None
    __budgetlevel = None
    __fundcode = None
    __fundname = None
    __documenttype = None
    __documentnumber = None
    __documentdate = None
    __lastdocumentdate = None
    __rpiocode = None
    __rpioname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __boccode = None
    __bocname = None
    __budgetingcontrols = None
    __postingcontrols = None
    __precommitmentcontrols = None
    __commitmentcontrols = None
    __obligationcontrols = None
    __accrualcontrols = None
    __expenditurecontrols = None
    __expensecontrols = None
    __reimbursementcontrols = None
    __reimbursableagreementcontrols = None
    __budgeted = None
    __posted = None
    __carryoverout = None
    __carryoverin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def budgetlevel( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != '':
            return self.__budgetlevel

    @budgetlevel.setter
    def budgetlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetlevel = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ):
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ):
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentname, str ):
            return self.__documentname

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ):
            self.__documentname = value

    @property
    def documentdate( self ):
        if isinstance( self.__documentdate, datetime ):
            return self.__documentdate

    @documentdate.setter
    def documentdate( self, value ):
        if isinstance( value, datetime ):
            self.__documentdate = value

    @property
    def lastdocumentdate( self ):
        if isinstance( self.__lastdocumentdate, datetime ):
            return self.__lastdocumentdate

    @lastdocumentdate.setter
    def lastdocumentdate( self, value ):
        if isinstance( value, datetime ):
            self.__lastdocumentdate = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def budgetingcontrols( self ):
        if isinstance( self.__budgetingcontrols, str ):
            return self.__budgetingcontrols

    @budgetingcontrols.setter
    def budgetingcontrols( self, value ):
        if isinstance( value, str ):
            self.__budgetingcontrols = value

    @property
    def postingcontrols( self ):
        if isinstance( self.__postingcontrols, str ):
            return self.__postingcontrols

    @postingcontrols.setter
    def postingcontrols( self, value ):
        if isinstance( value, str ):
            self.__postingcontrols = value

    @property
    def precommitmentcontrols( self ):
        if isinstance( self.__precommitmentcontrols, str ):
            return self.__precommitmentcontrols

    @precommitmentcontrols.setter
    def precommitmentcontrols( self, value ):
        if isinstance( value, str ):
            self.__precommitmentcontrols = value

    @property
    def commitmentcontrols( self ):
        if isinstance( self.__commitmentcontrols, str ):
            return self.__commitmentcontrols

    @commitmentcontrols.setter
    def commitmentcontrols( self, value ):
        if isinstance( value, str ):
            self.__commitmentcontrols = value

    @property
    def obligationcontrols( self ):
        if isinstance( self.__obligationcontrols, str ):
            return self.__obligationcontrols

    @obligationcontrols.setter
    def obligationcontrols( self, value ):
        if isinstance( value, str ):
            self.__obligationcontrols = value

    @property
    def accrualcontrols( self ):
        if isinstance( self.__accrualcontrols, str ):
            return self.__accrualcontrols

    @accrualcontrols.setter
    def accrualcontrols( self, value ):
        if isinstance( value, str ):
            self.__accrualcontrols = value

    @property
    def expenditurecontrols( self ):
        if isinstance( self.__expenditurecontrols, str ):
            return self.__expenditurecontrols

    @expenditurecontrols.setter
    def expenditurecontrols( self, value ):
        if isinstance( value, str ):
            self.__expenditurecontrols = value

    @property
    def expensecontrols( self ):
        if isinstance( self.__expensecontrols, str ):
            return self.__expensecontrols

    @expensecontrols.setter
    def expensecontrols( self, value ):
        if isinstance( value, str ):
            self.__expensecontrols = value

    @property
    def reimbursementcontrols( self ):
        if isinstance( self.__reimbursementcontrols, str ):
            return self.__reimbursementcontrols

    @reimbursementcontrols.setter
    def reimbursementcontrols( self, value ):
        if isinstance( value, str ):
            self.__reimbursementcontrols = value

    @property
    def reimbursableagreementcontrols( self ):
        if isinstance( self.__reimbursableagreementcontrols, str ):
            return self.__reimbursableagreementcontrols

    @reimbursableagreementcontrols.setter
    def reimbursableagreementcontrols( self, value ):
        if isinstance( value, str ):
            self.__reimbursableagreementcontrols = value

    @property
    def budgeted( self ):
        if isinstance( self.__budgeted, float ):
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if isinstance( value, float ):
            self.__budgeted = value

    @property
    def posted( self ):
        if isinstance( self.__posted, float ):
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( value, float ):
            self.__posted = value

    @property
    def carryoverin( self ):
        if isinstance( self.__carryoverin, float ):
            return self.__carryoverin

    @carryoverin.setter
    def carryoverin( self, value ):
        if isinstance( value, float ):
            self.__carryoverin = value

    @property
    def carryoverout( self ):
        if isinstance( self.__carryoverout, float ):
            return self.__carryoverout

    @carryoverout.setter
    def carryoverout( self, value ):
        if isinstance( value, float ):
            self.__carryoverout = value

    @property
    def estimatedreimbursements( self ):
        if isinstance( self.__reimbursementcontrols, float ):
            return self.__reimbursementcontrols

    @estimatedreimbursements.setter
    def estimatedreimbursements( self, value ):
        if isinstance( value, float ):
            self.__estimatedreimbursements = value

    @property
    def estimatedrecoveries( self ):
        if isinstance( self.__estimatedrecoveries, float ):
            return self.__estimatedrecoveries

    @estimatedrecoveries.setter
    def estimatedrecoveries( self, value ):
        if isinstance( value, float ):
            self.__estimatedrecoveries = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, efy = None,
                  fundcode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetDocuments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'BudgetDocumentsId',
                           'BFY',
                           'EFY',
                           'BudgetLevel',
                           'DocumentDate',
                           'LastDocumentDate',
                           'DocumentType',
                           'DocumentNumber',
                           'FundCode',
                           'FundName',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'ReimbursableAgreementControls',
                           'BudgetingControls',
                           'PostingControls',
                           'PreCommitmentControls',
                           'CommitmentControls',
                           'ObligationControls',
                           'ExpenditureControls',
                           'ExpenseControls',
                           'AccrualControls',
                           'ReimbursementControls',
                           'Budgeted',
                           'Posted',
                           'CarryOut',
                           'CarryIn',
                           'EstimatedRecoveries',
                           'EstimatedReimbursements' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetDocument'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetDocument'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetControls( code, provider = Provider.SQLite )
class BudgetControls( ):
    '''object representing compass control data'''
    __source = None
    __provider = None
    __budgetcontrolsid = None
    __code = None
    __name = None
    __budgetedtranstype = None
    __postedtranstype = None
    __estimatedreimbursementstranstype = None
    __spendingadjustmenttranstype = None
    __estimatedrecoveriestranstype = None
    __actualrecoveriestranstype = None
    __statusreservetranstype = None
    __profitlosstranstype = None
    __estimatedreimbursementsspendingoptions = None
    __estimatedreimbursementsbudgetingoptions = None
    __trackagreementlowerlevels = None
    __budgetestimatedlowerlevels = None
    __recoverynextlevel = None
    __recoverybudgetmismatch = None
    __profitlossspendingoption = None
    __profitlossbudgetingoption = None
    __recoveriescarryinlowerlevelcontrol = None
    __recoveriescarryinlowerlevel = None
    __recoveriescarryinamountcontrol = None
    __budgetedcontrol = None
    __postedcontrol = None
    __precommitmentspendingcontrol = None
    __commitmentspendingcontrol = None
    __obligationspendingcontrol = None
    __accrualspendingcontrol = None
    __expenditurespendingcontrol = None
    __expensespendingcontrol = None
    __reimbursementspendingcontrol = None
    __reimbursableagreementspendingcontrol = None
    __ftebudgetingcontrol = None
    __ftespendingcontrol = None
    __transactiontypecontrol = None
    __authoritydistributioncontrol = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__budgetcontrolsid, int ):
            return self.__budgetcontrolsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__budgetcontrolsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str ):
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ):
            return self.__name

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def budgetedtranstype( self ):
        if isinstance( self.__budgetedtranstype, str ) and self.__budgetedtranstype != '':
            return self.__budgetedtranstype

    @budgetedtranstype.setter
    def budgetedtranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetedtranstype = value

    @property
    def postedtranstype( self ):
        if isinstance( self.__postedtranstype, str ) and self.__postedtranstype != '':
            return self.__postedtranstype

    @postedtranstype.setter
    def postedtranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__postedtranstype = value

    @property
    def spendingadjustmenttranstype( self ):
        if isinstance( self.__spendingadjustmenttranstype, str ) and self.__spendingadjustmenttranstype != '':
            return self.__spendingadjustmenttranstype

    @spendingadjustmenttranstype.setter
    def spendingadjustmenttranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__spendingadjustmenttranstype = value

    @property
    def estimatedreimbursementstranstype( self ):
        if isinstance( self.__estimatedreimbursementstranstype, str ) and self.__estimatedreimbursementstranstype != '':
            return self.__estimatedreimbursementstranstype

    @estimatedreimbursementstranstype.setter
    def estimatedreimbursementstranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__estimatedreimbursementstranstype = value

    @property
    def estimatedrecoveriestranstype( self ):
        if isinstance( self.__estimatedrecoveriestranstype, str ) and self.__estimatedrecoveriestranstype != '':
            return self.__estimatedrecoveriestranstype

    @estimatedrecoveriestranstype.setter
    def estimatedrecoveriestranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__estimatedrecoveriestranstype = value

    @property
    def actualrecoveriestranstype( self ):
        if isinstance( self.__actualrecoveriestranstype, str ) and self.__actualrecoveriestranstype != '':
            return self.__actualrecoveriestranstype

    @actualrecoveriestranstype.setter
    def actualrecoveriestranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__actualrecoveriestranstype = value

    @property
    def statusreservetranstype( self ):
        if isinstance( self.__statusreservetranstype, str ) and self.__statusreservetranstype != '':
            return self.__statusreservetranstype

    @statusreservetranstype.setter
    def statusreservetranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__statusreservetranstype = value

    @property
    def profitlosstranstype( self ):
        if isinstance( self.__profitlosstranstype, str ) and self.__profitlosstranstype != '':
            return self.__profitlosstranstype

    @profitlosstranstype.setter
    def profitlosstranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__profitlosstranstype = value

    @property
    def estimatedreimbursementsspendingoptions( self ):
        if isinstance( self.__estimatedreimbursementsspendingoptions, str ) and self.__estimatedreimbursementsspendingoptions != '':
            return self.__estimatedreimbursementsspendingoptions

    @estimatedreimbursementsspendingoptions.setter
    def estimatedreimbursementsspendingoptions( self, value ):
        if isinstance( value, str ) and value != '':
            self.__estimatedreimbursementsspendingoptions = value

    @property
    def estimatedreimbursementsbudgetingoptions( self ):
        if isinstance( self.__estimatedreimbursementsbudgetingoptions, str ) and self.__estimatedreimbursementsbudgetingoptions != '':
            return self.__estimatedreimbursementsbudgetingoptions

    @estimatedreimbursementsbudgetingoptions.setter
    def estimatedreimbursementsbudgetingoptions( self, value ):
        if isinstance( value, str ) and value != '':
            self.__estimatedreimbursementsbudgetingoptions = value

    @property
    def trackingagreementlowerlevels( self ):
        if isinstance( self.__trackingagreementlowerlevels, str ) and self.__trackingagreementlowerlevels != '':
            return self.__trackingagreementlowerlevels

    @trackingagreementlowerlevels.setter
    def trackingagreementlowerlevels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__trackingagreementlowerlevels = value

    @property
    def budgetestimatedlowerlevels( self ):
        if isinstance( self.__budgetedestimatedlowerlevels, str ) and self.__budgetedestimatedlowerlevels != '':
            return self.__budgetedestimatedlowerlevels

    @budgetestimatedlowerlevels.setter
    def budgetestimatedlowerlevels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetedestimatedlowerlevels = value

    @property
    def recoverynextlevel( self ):
        if isinstance( self.__recoverynextlevel, str ) and self.__recoverynextlevel != '':
            return self.__recoverynextlevel

    @recoverynextlevel.setter
    def recoverynextlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoverynextlevel = value

    @property
    def recoverybudgetmismatch( self ):
        if isinstance( self.__recoverybudgetmismatch, str ) and self.__recoverybudgetmismatch != '':
            return self.__recoverybudgetmismatch

    @recoverybudgetmismatch.setter
    def recoverybudgetmismatch( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoverybudgetmismatch = value

    @property
    def profitlossspendingoption( self ):
        if isinstance( self.__profitlossspendingoption, str ) and self.__profitlossspendingoption != '':
            return self.__profitlossspendingoption

    @profitlossspendingoption.setter
    def profitlossspendingoption( self, value ):
        if isinstance( value, str ) and value != '':
            self.__profitlossspendingoption = value

    @property
    def profitlossbudgetingoption( self ):
        if isinstance( self.__profitlossbudgetingoption, str ) and self.__profitlossbudgetingoption != '':
            return self.__profitlossbudgetingoption

    @profitlossbudgetingoption.setter
    def profitlossbudgetingoption( self, value ):
        if isinstance( value, str ) and value != '':
            self.__profitlossbudgetingoption = value

    @property
    def recoveriescarryinlowerelevelcontrol( self ):
        if isinstance( self.__recoveriescarryinlowerelevelcontrol, str ) and self.__recoveriescarryinlowerelevelcontrol != '':
            return self.__recoveriescarryinlowerelevelcontrol

    @recoveriescarryinlowerelevelcontrol.setter
    def recoveriescarryinlowerelevelcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoveriescarryinlowerelevelcontrol = value

    @property
    def recoveriescarryinlowerlevel( self ):
        if isinstance( self.__recoveriescarryinlowerlevel, str ) and self.__recoveriescarryinlowerlevel != '':
            return self.__recoveriescarryinlowerlevel

    @recoveriescarryinlowerlevel.setter
    def recoveriescarryinlowerlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoveriescarryinlowerlevel = value

    @property
    def recoveriescarryinamountcontrol( self ):
        if isinstance( self.__recoveriescarryinamountcontrol, str ) and self.__recoveriescarryinamountcontrol != '':
            return self.__recoveriescarryinamountcontrol

    @recoveriescarryinamountcontrol.setter
    def recoveriescarryinamountcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoveriescarryinamountcontrol = value

    @property
    def budgetedcontrol( self ):
        if isinstance( self.__budgetedcontrol, str ) and self.__budgetedcontrol != '':
            return self.__budgetedcontrol

    @budgetedcontrol.setter
    def budgetedcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetedcontrol = value

    @property
    def postedcontrol( self ):
        if isinstance( self.__postedcontrol, str ) and self.__postedcontrol != '':
            return self.__postedcontrol

    @postedcontrol.setter
    def postedcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__postedcontrol = value

    @property
    def precommitmentspendingcontrol( self ):
        if isinstance( self.__precommitmentspendingcontrol, str ) and self.__precommitmentspendingcontrol != '':
            return self.__precommitmentspendingcontrol

    @precommitmentspendingcontrol.setter
    def precommitmentspendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__precommitmentspendingcontrol = value

    @property
    def commitmentspendingcontrol( self ):
        if isinstance( self.__commitmentspendingcontrol, str ) and self.__commitmentspendingcontrol != '':
            return self.__commitmentspendingcontrol

    @commitmentspendingcontrol.setter
    def commitmentspendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__commitmentspendingcontrol = value

    @property
    def obligationspendingcontrol( self ):
        if isinstance( self.__obligationspendingcontrol, str ) and self.__obligationspendingcontrol != '':
            return self.__obligationspendingcontrol

    @obligationspendingcontrol.setter
    def obligationspendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__obligationspendingcontrol = value

    @property
    def accrualspendingcontrol( self ):
        if isinstance( self.__accrualspendingcontrol,  str ) and self.__accrualspendingcontrol != '':
            return self.__accrualspendingcontrol

    @accrualspendingcontrol.setter
    def accrualspendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accrualspendingcontrol = value

    @property
    def expenditurespendingcontrol( self ):
        if isinstance( self.__expenditurespendingcontrol, str ) and self.__expenditurespendingcontrol != '':
            return self.__expenditurespendingcontrol

    @expenditurespendingcontrol.setter
    def expenditurespendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__expenditurespendingcontrol = value

    @property
    def expensespendingcontrol( self ):
        if isinstance( self.__expensespendingcontrol, str ) and self.__expensespendingcontrol != '':
            return self.__expensespendingcontrol

    @expensespendingcontrol.setter
    def expensespendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__expensespendingcontrol = value

    @property
    def reimbursementspendingcontrol( self ):
        if isinstance( self.__reimbursementspendingcontrol, str ) and self.__reimbursementspendingcontrol != '':
            return self.__reimbursementspendingcontrol

    @reimbursementspendingcontrol.setter
    def reimbursementspendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__reimbursementspendingcontrol = value

    @property
    def reimbursableagreementspendingcontrol( self ):
        if isinstance( self.__reimbursableagreementspendingcontrol, str ) and self.__reimbursableagreementspendingcontrol != '':
            return self.__reimbursableagreementspendingcontrol

    @reimbursableagreementspendingcontrol.setter
    def reimbursableagreementspendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__reimbursableagreementspendingcontrol = value

    @property
    def ftebudgetingcontrol( self ):
        if isinstance( self.__ftebudgetingcontrol, str ) and self.__ftebudgetingcontrol != '':
            return self.__ftebudgetingcontrol

    @ftebudgetingcontrol.setter
    def ftebudgetingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ftebudgetingcontrol = value

    @property
    def ftespendingcontrol( self ):
        if isinstance( self.__ftespendingcontrol, str ) and self.__ftespendingcontrol != '':
            return self.__ftespendingcontrol

    @ftespendingcontrol.setter
    def ftespendingcontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ftespendingcontrol = value

    @property
    def transactiontypecontrol( self ):
        if isinstance( self.__transactiontypecontrol, str ) and self.__transactiontypecontrol != '':
            return self.__transactiontypecontrol

    @transactiontypecontrol.setter
    def transactiontypecontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__transactiontypecontrol = value

    @property
    def authoritydistributioncontrol( self ):
        if isinstance( self.__authoritydistributioncontrol, str ) and self.__authoritydistributioncontrol != '':
            return self.__authoritydistributioncontrol

    @authoritydistributioncontrol.setter
    def authoritydistributioncontrol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__authoritydistributioncontrol = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, efy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetControls
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'BudgetControlValuesId',
                           'Code',
                           'Name',
                           'SecurityOrg',
                           'BudgetingTransType',
                           'PostedTransType',
                           'EstimatedReimbursableTransType',
                           'SpendingAdjustmentTransType',
                           'EstimatedRecoveriesTransType',
                           'ActualRecoveriesTransType',
                           'StategicReserveTransType',
                           'ProfLossTransType',
                           'EstimatedReimbursableSpendingOption',
                           'EstimatedReimbursableBudgetingOption',
                           'TrackAgreementLowerLevel',
                           'BudgetEstimateLowerLevel',
                           'EstimatedRecoveriesSpendingOption',
                           'EstimatedRecoveriesBudgetingOption',
                           'RecordNextLevel',
                           'RecordBudgetingMismatch',
                           'ProfitLossSpendingOption',
                           'ProfitLossBudgetingOption',
                           'RecordCarryInLowerLevel',
                           'RecordCarryInLowerLevelControl',
                           'RecordCarryInAmountControl',
                           'BudgetingControl',
                           'PostingControl',
                           'PreCommitmentSpendingControl',
                           'CommitmentSpendingControl',
                           'ObligationSpendingControl',
                           'AccrualSpendingControl',
                           'ExpenditureSpendingControl',
                           'ExpenseSpendingControl',
                           'ReimbursableSpendingControl',
                           'ReimbursableAgreementSpendingControl',
                           'FteBudgetingControl',
                           'FteSpendingControl',
                           'TransactionTypeControl',
                           'AuthorityDistributionControl' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetControl'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'BudgetControl'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetFiscalYear( bfy, efy, date = None, provider = Provider.SQLite )
class BudgetFiscalYear( ):
    '''Class to describe the federal fiscal year'''
    __source = None
    __provider = None
    __budgetfiscalyearsid = None
    __input = None
    __bfy = None
    __efy = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = None
    __workdays = None
    __currentyear = None
    __currentmonth = None
    __currentday = None
    __holidays = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__budgetfiscalyearsid, int ):
            return self.__budgetfiscalyearsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__budgetfiscalyearsid = value

    @property
    def firstyear( self ):
        if isinstance( self.__bfy, str ) and len( self.__bfy ) == 4:
            return self.__bfy

    @firstyear.setter
    def firstyear( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def lastyear( self ):
        if isinstance( self.__efy, str) and len( self.__efy ) <= 4:
            return self.__efy

    @lastyear.setter
    def lastyear( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def currentyear( self ):
        if isinstance( self.__currentyear, int ):
            return self.__currentyear

    @currentyear.setter
    def currentyear( self, value ):
        if isinstance( value, int ):
            self.__currentyear = value

    @property
    def startdate( self ):
        if isinstance( self.__startdate, datetime ):
            return self.__startdate

    @startdate.setter
    def startdate( self, value ):
        if isinstance( value, datetime ):
            self.__startdate = value

    @property
    def enddate( self ):
        if isinstance( self.__enddate, datetime ):
            return self.__enddate

    @enddate.setter
    def enddate( self, value ):
        if isinstance( value, datetime ):
            self.__enddate = value

    @property
    def expiration( self ):
        if isinstance( self.__expiration, datetime):
            return self.__expiration

    @expiration.setter
    def expiration( self, value ):
        if isinstance( value, datetime ):
            self.__expiration = value

    @property
    def weekends( self ):
        if isinstance( self.__weekends, int ):
            return self.__weekends

    @weekends.setter
    def weekends( self, value ):
        if isinstance( value, int ):
            self.__weekends = value

    @property
    def workdays( self ):
        if isinstance( self.__workdays, float ):
            return self.__workdays

    @workdays.setter
    def workdays( self, value ):
        if isinstance( value, float ):
            self.__workdays = value

    @property
    def today( self ):
        if isinstance( self.__today, date ):
            return self.__today

    @today.setter
    def today( self, value ):
        if isinstance( value, date ):
            self.__today = value

    @property
    def date( self ):
        if isinstance( self.__date, date ):
            return self.__date

    @date.setter
    def date( self, value ):
        if isinstance( value, date ):
            self.__date = value

    @property
    def currentday( self ):
        if isinstance( self.__currentday, int ):
            return self.__currentday

    @currentday.setter
    def currentday( self, value ):
        if isinstance( value, int ) and (0 <= value <= 7):
            self.__currentday = value

    @property
    def currentmonth( self ):
        if isinstance( self.__currentmonth, int ):
            return self.__currentmonth

    @property
    def holidays( self ):
        if isinstance( self.__holidays, list ):
            return self.__holidays

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, date = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source  = Source.FiscalYears
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__today = datetime.today( )
        self.__currentday = datetime.today( ).day
        self.__currentmonth = datetime.today( ).month
        self.__date = date if isinstance( date, datetime ) else datetime.today( )
        self.__currentyear = datetime.today( ).year
        self.__startdate = datetime( datetime.today( ).year, 10, 1 ) if isinstance( self.__currentyear, int ) else None
        self.__enddate = datetime( datetime.today( ).year + 1, 9, 30 ) if isinstance( self.__currentyear, int ) else None
        self.__holidays = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                            'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                            'Memorial', 'Juneteenth', 'Independence', 'Labor' ]
        self.__fields = [ 'FiscalYearsId',
                          'BFY',
                          'EFY',
                          'StartDate',
                          'EndDate',
                          'Columbus',
                          'Veterans',
                          'Thanksgiving',
                          'Christmas',
                          'NewYears',
                          'MartinLutherKing',
                          'Presidents',
                          'Memorial',
                          'Juneteenth',
                          'Independence',
                          'Labor',
                          'ExpiringYear',
                          'ExpirationDate',
                          'CancellationDate',
                          'Workdays',
                          'Weekdays',
                          'Weekends',
                          'Availability' ]

    def __str__( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetFiscalYear'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetFiscalYear'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetObjectClasses( code, provider = Provider.SQLite  )
class BudgetObjectClasses( ):
    '''Defines the BudgetObjectClass Class'''
    __source = None
    __provider = None
    __budgetobjectclassesid = None
    __code = None
    __boc = None
    __name = None
    __value = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__accountsid, int ):
            return self.__accountsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__accountsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def value( self ):
        if isinstance( self.__value, object ):
            return self.__value

    @value.setter
    def value( self, value ):
        if isinstance( value, object ):
            self.__value = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetObjectClasses
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'BudgetObjectClassesId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetObjectClass'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'BudgetObjectClass'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetaryResourceExecution( bfy, efy, code, provider = Provider.SQLite )
class BudgetaryResourceExecution( ):
    '''BudgetaryResourceExecution( bfy, efy, code )
    initializes object representing MAX A-11 DE, SF-133'''
    __source = None
    __provider = None
    __budgetaryresourceexecutionid = None
    __bfy = None
    __efy = None
    __treasuryfundsymbol = None
    __ombaccountcode = None
    __ombaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__budgetaryresourceexecutionid, int ):
            return self.__budgetaryresourceexecutionid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__budgetaryresourceexecutionid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def treasuryfundsymbol( self ):
        if isinstance( self.__treasuryfundsymbol, str ) and self.__treasuryfundsymbol != '':
            return self.__treasuryfundsymbol

    @treasuryfundsymbol.setter
    def treasuryfundsymbol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryfundsymbol = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetResourceExecution
        self.__bfy = bfy if isinstance( bfy, str ) else None
        self.__efy = efy if isinstance( efy, str ) else None
        self.__ombaccountcode = code if isinstance( code, str ) and len( code ) == 4 else None
        self.__fields = [ 'BudgetaryResourceExecutionId',
                          'FiscalYear',
                          'BFY',
                          'EFY',
                          'LastUpdate',
                          'TreasurySymbol',
                          'OmbAccount',
                          'TreasuryAgencyCode',
                          'TreasuryAccountCode',
                          'STAT',
                          'CreditIndicator',
                          'LineNumber',
                          'LineDescription',
                          'SectionName',
                          'SectionNumber',
                          'LineType',
                          'FinancingAccounts',
                          'November',
                          'January',
                          'Feburary',
                          'April',
                          'May',
                          'June',
                          'August',
                          'October',
                          'Amount1',
                          'Amount2',
                          'Amount3',
                          'Amount4',
                          'Agency',
                          'Bureau' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            v = (self.__bfy, self.__efy, self.__ombaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetaryResourceExecution'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetaryResourceExecution'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetOutlays( account, provider = Provider.SQLite )
class BudgetOutlays( ):
    '''BudgetOutlays( bfy, omb )
    object provides OMB data'''
    __source = None
    __provider = None
    __budgetoutlaysid = None
    __reportyear = None
    __ombaccountcode = None
    __ombaccountname = None
    __linenumber = None
    __linesection = None
    __linename = None
    __linecategory = None
    __beacategory = None
    __beacategoryname = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__budgetoutlaysid, int ):
            return self.__budgetoutlaysid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__budgetoutlaysid = value

    @property
    def reportyear( self ):
        if isinstance( self.__reportyear, str ) and len( self.__reportyear ) == 4:
            return self.__reportyear

    @reportyear.setter
    def reportyear( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__reportyear = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def linesection( self ):
        if isinstance( self.__linesection, str ) and self.__linesection != '':
            return self.__linesection

    @linesection.setter
    def linesection( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linesection = value

    @property
    def linename( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @linename.setter
    def linename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linename = value

    @property
    def linecategory( self ):
        if isinstance( self.__linecategory, str ) and self.__linecategory != '':
            return self.__linecategory

    @linecategory.setter
    def linecategory( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linecategory = value

    @property
    def beacategory( self ):
        if isinstance( self.__beacategory, str ) and self.__beacategory != '':
            return self.__beacategory

    @beacategory.setter
    def beacategory( self, value ):
        if isinstance( value, str ) and value != '':
            self.__beacategory = value

    @property
    def beacategoryname( self ):
        if isinstance( self.__beacategoryname, str ) and self.__beacategoryname != '':
            return self.__beacategoryname

    @beacategoryname.setter
    def beacategoryname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__beacategoryname = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def prioryear( self ):
        if isinstance( self.__prioryear, float ):
            return self.__prioryear

    @prioryear.setter
    def prioryear( self, value ):
        if isinstance( value, float ):
            self.__prioryear = value

    @property
    def currentyear( self ):
        if isinstance( self.__currentyear, float ):
            return self.__currentyear

    @currentyear.setter
    def currentyear( self, value ):
        if isinstance( value, float ):
            self.__currentyear = value

    @property
    def budgetyear( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budgetyear.setter
    def budgetyear( self, value ):
        if isinstance( value, float ):
            self.__budgetyear = value

    @property
    def outyear1( self ):
        if isinstance( self.__outyear1, float ):
            return self.__outyear1

    @outyear1.setter
    def outyear1( self, value ):
        if isinstance( value, float ):
            self.__outyear1 = value

    @property
    def outyear2( self ):
        if isinstance( self.__outyear2, float ):
            return self.__outyear2

    @outyear2.setter
    def outyear2( self, value ):
        if isinstance( value, float ):
            self.__outyear2 = value

    @property
    def outyear3( self ):
        if isinstance( self.__outyear3, float ):
            return self.__outyear3

    @outyear3.setter
    def outyear3( self, value ):
        if isinstance( value, float ):
            self.__outyear3 = value

    @property
    def outyear4( self ):
        if isinstance( self.__outyear4, float ):
            return self.__outyear4

    @outyear4.setter
    def outyear4( self, value ):
        if isinstance( value, float ):
            self.__outyear4 = value

    @property
    def outyear5( self ):
        if isinstance( self.__outyear5, float ):
            return self.__outyear5

    @outyear5.setter
    def outyear5( self, value ):
        if isinstance( value, float ):
            self.__outyear5 = value

    @property
    def outyear6( self ):
        if isinstance( self.__outyear6, float ):
            return self.__outyear6

    @outyear6.setter
    def outyear6( self, value ):
        if isinstance( value, float ):
            self.__outyear6 = value

    @property
    def outyear7( self ):
        if isinstance( self.__outyear7, float ):
            return self.__outyear7

    @outyear7.setter
    def outyear7( self, value ):
        if isinstance( value, float ):
            self.__outyear7 = value

    @property
    def outyear8( self ):
        if isinstance( self.__outyear8, float ):
            return self.__outyear8

    @outyear8.setter
    def outyear8( self, value ):
        if isinstance( value, float ):
            self.__outyear8 = value

    @property
    def outyear9( self ):
        if isinstance( self.__outyear9, float ):
            return self.__outyear9

    @outyear9.setter
    def outyear9( self, value ):
        if isinstance( value, float ):
            self.__outyear9 = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetOutlays
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'BudgetOutlaysId',
                          'ReportYear',
                          'Category',
                          'AgencyName',
                          'LineNumber',
                          'LineSection',
                          'OmbAccount',
                          'LineTitle',
                          'AccountType',
                          'AuthorityTypeName',
                          'Line',
                          'AuthorityType',
                          'PriorYear',
                          'CurrentYear',
                          'BudgetYear',
                          'BudgetYear1',
                          'BudgetYear2',
                          'BudgetYear3',
                          'BudgetYear4',
                          'BudgetYear5',
                          'BudgetYear6',
                          'BudgetYear7',
                          'BudgetYear8',
                          'BudgetYear9' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'OmbAccountCode', ]
            v = (self.__ombaccountcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetOutlays'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'BudgetOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# CongressionalControls( bfy, fund, provider = Provider.SQLite )
class CongressionalControls( ):
    '''object representing congressional control data'''
    __source = None
    __provider = None
    __congressionalcontrolsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __subprojectcode = None
    __subprojectname = None
    __reprogrammingrestriction = None
    __increaserestriction = None
    __decreaserestriction = None
    __memorandumrequired = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__congressionalcontrolsid, int ):
            return self.__congressionalcontrolsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__congressionalcontrolsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def subprojectcode( self ):
        if isinstance( self.__subprojectcode, str ) and self.__subprojectcode != '':
            return self.__subprojectcode

    @subprojectcode.setter
    def subprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subprojectcode = value

    @property
    def subprojectname( self ):
        if isinstance( self.__subprojectname, str ) and self.__subprojectname != '':
            return self.__subprojectname

    @subprojectname.setter
    def subprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def reprogrammingrestriction( self ):
        if isinstance( self.__reprogrammingrestriction, bool ):
            return self.__reprogrammingrestriction

    @reprogrammingrestriction.setter
    def reprogrammingrestriction( self, value ):
        if isinstance( value, bool ):
            self.__reprogrammingrestriction = value

    @property
    def increaserestriction( self ):
        if isinstance( self.__increaserestriction, bool ):
            return self.__increaserestriction

    @increaserestriction.setter
    def increaserestriction( self, value ):
        if isinstance( value, bool ):
            self.__increaserestriction = value

    @property
    def decreaserestriction( self ):
        if isinstance( self.__decreaserestriction, bool ):
            return self.__decreaserestriction

    @decreaserestriction.setter
    def decreaserestriction( self, value ):
        if isinstance( value, bool ):
            self.__decreaserestriction = value

    @property
    def memorandumrequired( self ):
        if isinstance( self.__memorandumrequired, bool ):
            return self.__memorandumrequired

    @memorandumrequired.setter
    def memorandumrequired( self, value ):
        if isinstance( value, bool ):
            self.__memorandumrequired = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fundcode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CongressionalControls
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'CongressionalControlsId',
                           'FundCode',
                           'FundName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'SubProjectCode',
                           'SubProjectName',
                           'ReprogrammingRestriction',
                           'IncreaseRestriction',
                           'DecreaseRestriction',
                           'MemoRequirement' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'CongressionalControl'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )


# CompassLevel( bfy, efy, fund, provider = Provider.SQLite )
class CompassLevels( ):
    '''object representing Compass data levels 1-7'''
    __source = None
    __provider = None
    __compasslevelsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __appropriationcode = None
    __subappropriationcode = None
    __appropriationname = None
    __treasurysymbol = None
    __documenttype = None
    __lowername = None
    __description = None
    __postedcontrolflag = None
    __actualrecoverytranstype = None
    __commitmentspendingcontrolflag = None
    __budgetdefault = None
    __lowerchildexpenditurecontrolflag = None
    __lowerchildexpensespendingcontrolflag = None
    __ftecontrolflag = None
    __accrualspendigcontrolflag = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __lowercommitmentspendingcontrolflag = None
    __lowerobligationspendingcontrolflag = None
    __lowerexpenditurespendingcontrolflag = None
    __lowerexpensespendingcontrolflag = None
    __lowerpostedcontrolflag = None
    __lowerpostedtranstype = None
    __lowerpostedflag = None
    __lowerprecommitmentspendingcontrolflag = None
    __lowerrecoveriesspendingoption = None
    __lowerrecoveriesoption = None
    __lowerreimbursablespendingoption = None
    __date = None
    __totalauthority = None
    __originalauthority = None
    __carryoveravailabilitypercentage = None
    __carryoverin = None
    __carryoverout = None
    __fundsin = None
    __fundsout = None
    __recoverieswithdrawn = None
    __actualrecoveries = None
    __actualreimbursements = None
    __agreementreimbursables = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__compasslevelsid, int ):
            return self.__compasslevelsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__compasslevelsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def appropriationcode( self ):
        if isinstance( self.__appropriationcode, str ) \
                and self.__appropriationcode != '':
            return self.__appropriationcode

    @appropriationcode.setter
    def appropriationcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationcode = value

    @property
    def appropriationname( self ):
        if isinstance( self.__appropriationname, str ) \
                and self.__appropriationname != '':
            return self.__appropriationname

    @appropriationname.setter
    def appropriationname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationname = value

    @property
    def subappropriationcode( self ):
        if isinstance( self.__subappropriationcode, str ) \
                and self.__subappropriationcode != '':
            return self.__subappropriationcode

    @subappropriationcode.setter
    def subappropriationcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subappropriationcode = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, efy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CompassLevels
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'CompassLevelsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'FundCode',
                           'FundName',
                           'AppropriationCode',
                           'SubAppropriationCode',
                           'AppropriationName'
                           'TreasurySymbol',
                           'DocumentType',
                           'LowerName',
                           'Description',
                           'PostedControlFlag',
                           'ActualRecoveryTransType',
                           'CommitmentSpendingControlFlag',
                           'BudgetDefault'
                           'LowerChildExpenditureSpendingControlFlag',
                           'LowerChildExpenseSpendingControlFlag',
                           'FteControlFlag',
                           'AccrualSpendingControlFlag',
                           'ObligationSpendingControlFlag',
                           'PreCommitmentSpendingControlFlag',
                           'LowerCommitmentSpendingControlFlag',
                           'LowerObligationSpendingControlFlag',
                           'LowerExpenditureSpendingControlFlag',
                           'LowerExpenseSpendingControlFlag',
                           'LowerPostedControlFlag',
                           'LowerPostedTransType',
                           'LowerTransType',
                           'LowerPostedFlag',
                           'LowerPreCommitmentSpendingControlFlag',
                           'LowerRecoveriesSpendingOption',
                           'LowerRecoveriesOption',
                           'LowerReimbursableSpendingOption',
                           'Date',
                           'TotalAuthority',
                           'OriginalAmount',
                           'CarryoverAvailabilityPercentage',
                           'CarryIn',
                           'CarryOut',
                           'FundsIn',
                           'FundOut',
                           'RecoveriesWithdrawn',
                           'ActualRecoveries',
                           'ActualReimbursements',
                           'AgreementReimbursables' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'CompassLevels'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'CompassLevels'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Commitments( bfy, fund, account, boc, provider = Provider.SQLite )
class Commitments( ):
    '''Defines the CommitmentS class.'''
    __source = None
    __provider = None
    __opencommitmentsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__expendituresid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def referencedocumentnumber( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @referencedocumentnumber.setter
    def referencedocumentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__referencedocumentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if isinstance( value, int ):
            self.__age = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__foccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.OpenCommitments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'CommitmentsId',
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitments',
                           'Obligations',
                           'ULO',
                           'Expenditures' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Commitment'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Commitment'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# CarryoverOutlays( bfy, omb, provider = Provider.SQLite )
class CarryoverOutlays( ):
    ''' object provides OMB data '''
    __source = None
    __provider = None
    __carryoveroutlaysid = None
    __ombaccountcode = None
    __ombaccountname = None
    __linenumber = None
    __carryover = None
    __carryoveroutlays = None
    __budgetyear = None
    __budgetyearadjustment = None
    __currentyear = None
    __currentyearadjustment = None
    __delta = None
    __avaiablebalance = None
    __ulo = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None


    @property
    def id( self ):
        if isinstance( self.__carryoveroutlaysid, int ):
            return self.__carryoveroutlaysid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__carryoveroutlaysid = value

    @property
    def budgetyear( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budgetyear.setter
    def budgetyear( self, value ):
        if isinstance( value, float ):
            self.__budgetyear = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def carryover( self ):
        if isinstance( self.__carryover, float ):
            return self.__carryover

    @carryover.setter
    def carryover( self, value ):
        if isinstance( value, float ):
            self.__carryover = value

    @property
    def carryoveroutlays( self ):
        if isinstance( self.__carryoveroutlays, float ):
            return self.__carryoveroutlays

    @carryoveroutlays.setter
    def carryoveroutlays( self, value ):
        if isinstance( value, float ):
            self.__carryoveroutlays = value

    @property
    def ulo( self ):
        if isinstance( self.__ulo, float ) and self.__ulo > 0:
            return self.__ulo

    @ulo.setter
    def ulo( self, value ):
        if isinstance( value, float ) and value > 0:
            self.__ulo = value

    @property
    def delta( self ):
        if isinstance( self.__delta, float ) and self.__delta > 0:
            return self.__delta

    @delta.setter
    def delta( self, value ):
        if isinstance( value, float ) and value > 0:
            self.__delta = value

    @property
    def availablebalance( self ):
        if isinstance( self.__availablebalance, float ) and self.__availablebalance > 0:
            return self.__availablebalance

    @availablebalance.setter
    def availablebalance( self, value ):
        if isinstance( value, float ) and value > 0:
            self.__availablebalance = value

    @property
    def currentyear( self ):
        if isinstance( self.__currentyear, float ):
            return self.__currentyear

    @currentyear.setter
    def currentyear( self, value ):
        if isinstance( value, float ):
            self.__currentyear = value

    @property
    def currentyearadjustment( self ):
        if isinstance( self.__currentyearadjustment, float ):
            return self.__currentyearadjustment

    @currentyearadjustment.setter
    def currentyearadjustment( self, value ):
        if isinstance( value, float ):
            self.__currentyearadjustment = value

    @property
    def budgetyear( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budgetyear.setter
    def budgetyear( self, value ):
        if isinstance( value, float ):
            self.__budgetyear = value

    @property
    def budgetyearadjustment( self ):
        if isinstance( self.__budgetyearadjustment, float ):
            return self.__budgetyearadjustment

    @budgetyearadjustment.setter
    def budgetyearadjustment( self, value ):
        if isinstance( value, float ):
            self.__budgetyearadjustment = value

    @property
    def outyear1( self ):
        if isinstance( self.__outyear1, float ):
            return self.__outyear1

    @outyear1.setter
    def outyear1( self, value ):
        if isinstance( value, float ):
            self.__outyear1 = value

    @property
    def outyear2( self ):
        if isinstance( self.__outyear2, float ):
            return self.__outyear2

    @outyear2.setter
    def outyear2( self, value ):
        if isinstance( value, float ):
            self.__outyear2 = value

    @property
    def outyear3( self ):
        if isinstance( self.__outyear3, float ):
            return self.__outyear3

    @outyear3.setter
    def outyear3( self, value ):
        if isinstance( value, float ):
            self.__outyear3 = value

    @property
    def outyear4( self ):
        if isinstance( self.__outyear4, float ):
            return self.__outyear4

    @outyear4.setter
    def outyear4( self, value ):
        if isinstance( value, float ):
            self.__outyear4 = value

    @property
    def outyear5( self ):
        if isinstance( self.__outyear5, float ):
            return self.__outyear5

    @outyear5.setter
    def outyear5( self, value ):
        if isinstance( value, float ):
            self.__outyear5 = value

    @property
    def outyear6( self ):
        if isinstance( self.__outyear6, float ):
            return self.__outyear6

    @outyear6.setter
    def outyear6( self, value ):
        if isinstance( value, float ):
            self.__outyear6 = value

    @property
    def outyear7( self ):
        if isinstance( self.__outyear7, float ):
            return self.__outyear7

    @outyear7.setter
    def outyear7( self, value ):
        if isinstance( value, float ):
            self.__outyear7 = value

    @property
    def outyear8( self ):
        if isinstance( self.__outyear8, float ):
            return self.__outyear8

    @outyear8.setter
    def outyear8( self, value ):
        if isinstance( value, float ):
            self.__outyear8 = value

    @property
    def outyear9( self ):
        if isinstance( self.__outyear9, float ):
            return self.__outyear9

    @outyear9.setter
    def outyear9( self, value ):
        if isinstance( value, float ):
            self.__outyear9 = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, omb, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverOutlays
        self.__budgetyear = bfy if isinstance( bfy, str ) and bfy != '' else None
        self.__ombaccountcode = omb if isinstance( omb, str ) and omb != '' else None
        self.__fields = [ 'CarryoverOutlaysId',
                          'ReportYear',
                          'AgencyName',
                          'OmbAccountName',
                          'LINE',
                          'Carryover',
                          'CarryoverOutlays',
                          'Delta',
                          'AvailableBalance',
                          'ULO',
                          'CurrentYearAdjustment',
                          'BudgetYearAdjustment',
                          'CurrentYear',
                          'BudgetYear',
                          'OutYear1',
                          'OutYear2',
                          'OutYear3',
                          'OutYear4',
                          'OutYear5',
                          'OutYear6',
                          'OutYear7',
                          'OutYear8',
                          'OutYear9' ]

    def getdata( self ):
        try:
            source = Source.CarryoverOutlays
            provider = Provider.SQLite
            n = [ 'BudgetYear', 'OmbAccountCode' ]
            v = (self.__budgetyear, self.__ombaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverOutlays'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# CostArea( code, provider = Provider.SQLite )
class CostArea( ):
    __source = None
    __provider = None
    __code = None
    __fields = None

    @property
    def id( self ):
        if isinstance( self.__transfersid, int ):
            return self.__transfersid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__transfersid = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__provider = provider
        self.__fields = [ 'CostAreasId',
                          'Code',
                          'Name' ]


# CarryoverEstimates( bfy, provider = Provider.SQLite )
class CarryoverEstimates( ):
    '''CarryoverEstimates( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __carryoverestimatesid = None
    __budgetlevel = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __availablebalance = None
    __opencommitments = None
    __unobligatedauthority = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__allocationsid, int ):
            return self.__allocationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__allocationsid = value

    @property
    def budgetlevel( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != "":
            return self.__budgetlevel

    @budgetlevel.setter
    def budgetlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetlevel = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def availablebalance( self ):
        if isinstance( self.__availablebalance, float ):
            return self.__availablebalance

    @availablebalance.setter
    def availablebalance( self, value ):
        if isinstance( value, float ):
            self.__availablebalance = value

    @property
    def opencommitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @opencommitments.setter
    def opencommitments( self, value ):
        if isinstance( value, float ):
            self.__opencommitments = value

    @property
    def unobligatedauthority( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return self.__unobligatedauthority

    @unobligatedauthority.setter
    def unobligatedauthority( self, value ):
        if isinstance( value, float ):
            self.__unobligatedauthority = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value


    def __init__( self, bfy, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitments',
                           'UnobligatedAuthority' ]

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY' ]
            v = (self.__bfy, self.__efy)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimates'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverEstimates'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# CarryoverSurvey( bfy, efy, fund, provider = Provider.SQLite )
class CarryoverSurvey( ):
    '''CarryoverSurvey( bfy ) initializes object
    providing carryover survey data'''
    __source = None
    __provider = None
    __carryoversurveyid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__allocationsid, int ):
            return self.__allocationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__allocationsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CarryoverSurvey
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'CarryoverSurveyId',
                          'FundCode',
                          'FundName',
                          'Amount' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'FundCode', ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarryoverOutlays'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'CarrryoverOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# CapitalPlanningInvestmentCodes( code, provider = Provider.SQLite  )
class CapitalPlanningInvestmentCodes( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __capitalplanninginvestmentcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__capitalplanninginvestmentcodesid, int ):
            return self.__capitalplanninginvestmentcodesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__accountsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CapitalPlanningInvestmentCodes
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'CpicId',
                          'Type'
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = ( self.__code, )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ITProjectCode'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ITProjectCode'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# DataRuleDescription( schedule, line, rule, provider = Provider.SQLite )
class DataRuleDescription( ):
    ''' DataRuleDescription( schedule, line, rule )
    initializes object providing OMB MAX A11 rule data '''
    __source = None
    __provider = None
    __dataruledescriptionsid = None
    __schedule = None
    __linenumber = None
    __rulenumber = None
    __ruledescription = None
    __scheduleorder = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__dataruledescriptionsid, int ):
            return self.__dataruledescriptionsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__dataruledescriptionsid = value

    @property
    def schedule( self ):
        if isinstance( self.__schedule, str ) and self.__schedule != '':
            return self.__schedule

    @schedule.setter
    def schedule( self, value ):
        if isinstance( value, str ) and value != '':
            self.__schedule = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def linedescription( self ):
        if isinstance( self.__linedescription, str ) and self.__linedescription != '':
            return self.__linedescription

    @linedescription.setter
    def linedescription( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linedescription = value

    @property
    def rulenumber( self ):
        if isinstance( self.__rulenumber, str ) and self.__rulenumber != '':
            return self.__rulenumber

    @rulenumber.setter
    def rulenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rulenumber = value

    @property
    def ruledescription( self ):
        if isinstance( self.__ruledescription, str ) and self.__ruledescription != '':
            return self.__ruledescription

    @ruledescription.setter
    def ruledescription( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ruledescription = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, schedule, line, rule, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.DataRuleDescriptions
        self.__schedule = schedule if isinstance( schedule, str ) and schedule != '' else None
        self.__linenumber = line if isinstance( line, str ) and line != '' else None
        self.__rulenumber = rule if isinstance( rule, str ) and rule != '' else None
        self.__fields = [ 'DataRuleDescriptionsId',
                          'Schedule',
                          'LineNumber',
                          'RuleNumber',
                          'RuleDescription',
                          'ScheduleOrder' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Schedule', 'LineNumber', 'RuleNumber' ]
            v = (self.__schedule, self.__linenumber, self.__rulenumber)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'DataRuleDescription'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'DataRuleDescription'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Defacto( bfy, fund, provider = Provider.SQLite )
class Defacto( ):
    '''object representing defacto obligations'''
    __source = None
    __provider = None
    __defactosid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def budgeted( self ):
        if isinstance( self.__budgeted, float ):
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if isinstance( value, float ):
            self.__budgeted = value

    @property
    def posted( self ):
        if isinstance( self.__posted, float ):
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def opencommitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @opencommitments.setter
    def opencommitments( self, value ):
        if isinstance( value, float ):
            self.__opencommitments = value

    @property
    def obligations( self ):
        if isinstance( self.__obligations, float ):
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if isinstance( value, float ):
            self.__obligations = value

    @property
    def unliquidatedobligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidatedobligations.setter
    def unliquidatedobligations( self, value ):
        if isinstance( value, float ):
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if isinstance( value, float ):
            self.__expenditures = value

    @property
    def used( self ):
        if isinstance( self.__used, float ):
            return self.__used

    @used.setter
    def used( self, value ):
        if isinstance( value, float ):
            self.__used = value

    @property
    def available( self ):
        if isinstance( self.__avaialable, float ):
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if isinstance( value, float ):
            self.__avaialable = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.Defactos
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'DefactosId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitments',
                           'ULO',
                           'Expenditures',
                           'Obligations',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Defacto'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Defacto'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Deobligation( bfy, fund, account, boc, provider = Provider.SQLite )
class Deobligation( ):
    '''Deobligation( bfy, fund, account, boc )
    initializes object providing Deobligation data '''
    __source = None
    __provider = None
    __deobligationsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__deobligationsid, int ):
            return self.__deobligationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__deobligationsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def referencedocumentnumber( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @referencedocumentnumber.setter
    def referencedocumentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__referencedocumentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if isinstance( value, int ):
            self.__age = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Deobligations
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'DeobligationsId',
                           'BFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'AccountCode',
                           'NpmCode',
                           'NpmName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'OrgCode',
                           'OrgName',
                           'BocCode',
                           'BocName',
                           'DocumentNumber',
                           'FocCode',
                           'FocName',
                           'ProcessedDate',
                           'Amount' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Deobligations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Deobligations'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# DocumentControlNumber( dcn, provider = Provider.SQLite )
class DocumentControlNumber( ):
    ''' object provides DCN data'''
    __source = None
    __provider = None
    __documentcontrolnumbersid = None
    __rpiocode = None
    __rpioname = None
    __documenttype = None
    __documentnumber = None
    __documentprefix = None
    __documentcontrolnumber = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__documentcontrolnumbersid, int ):
            return self.__documentcontrolnumbersid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__documentcontrolnumbersid = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentprefix( self ):
        if isinstance( self.__documentprefix, str ) and self.__documentprefix != '':
            return self.__documentprefix

    @documentprefix.setter
    def documentprefix( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentprefix = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, dcn = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.DocumentControlNumbers
        self.__documentcontrolnumber = dcn if isinstance( dcn, str ) and dcn != '' else None
        self.__fields = [ 'DocumentControlNumbersId',
                           'RpioCode',
                           'RpioName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentPrefix',
                           'DocumentControlNumbe' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'DocumentControlNumber', ]
            v = (self.__dcn,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'DocumentControlNumber'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'DocumentControlNumber'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Expenditure( bfy, fund, account, boc, provider = Provider.SQLite )
class Expenditures( ):
    '''Expenditure( bfy, fund, account, code, provider = Provider.SQLite )
    initializes object providing Expenditure data'''
    __source = None
    __provider = None
    __expendituresid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__expendituresid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def referencedocumentnumber( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @referencedocumentnumber.setter
    def referencedocumentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__referencedocumentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if isinstance( value, int ):
            self.__age = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, account = None,
                  boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Expenditures
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'ExpendituresId',
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'Amount' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Expenditures'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Expenditures'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# FinanceObjectClass( code, provider = Provider.SQLite  )
class FinanceObjectClass( ):
    '''Defines the Finance Object Class'''
    __source = None
    __provider = None
    __financeobjectclassesid = None
    __code = None
    __name = None
    __boccode = None
    __bocname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__financeobjectclassesid, int ):
            return self.__financeobjectclassesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__financeobjectclassesid = id

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, code ):
        if isinstance( code, str ) and code != '':
            self.__code = code

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__data = cache

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FinanceObjectClasses
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'FinanceObjectClassesId',
                          'Code',
                          'Name',
                          'BocCode',
                          'BocName' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FinanceObjectClass'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FinanceObjectClass'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Fund( bfy, efy, code, provider = Provider.SQLite )
class Fund( ):
    '''Defines the Fund Class'''
    __source = None
    __provider = None
    __fundsid = None
    __code = None
    __name = None
    __bfy = None
    __efy = None
    __shortname = None
    __status = None
    __bpoa = None
    __epoa = None
    __main = None
    __multiyearindicator = None
    __sublevel = None
    __ata = None
    __aid = None
    __fundcategory = None
    __appropriationcode = None
    __appropriationname = None
    __fundgroup = None
    __noyear = None
    __carryover = None
    __cancelledyearspendingaccount = None
    __applyatalllevels = None
    __batsfund = None
    __batsenddate = None
    __batsoptionid = None
    __securityorg = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __ombaccountcode = None
    __ombaccountname = None
    __apportionmentaccountcode = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__fundsid, int ):
            return self.__fundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__fundsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def shortname( self ):
        if isinstance( self.__shortname, str ) and self.__shortname != '':
            return self.__shortname

    @shortname.setter
    def shortname( self, value ):
        if isinstance( value , str ) and value != '':
            self.__shortname = value

    @property
    def status( self ):
        if isinstance( self.__status, str ) and self.__status != '':
            return self.__status

    @status.setter
    def status( self, value ):
        if isinstance( value, str ) and value in [ 'ACTIVE', 'INACTIVE' ]:
            self.__status = value

    @property
    def bpoa( self ):
        if isinstance( self.__bpoa, str ) and self.__bpoa != '':
            return self.__bpoa

    @bpoa.setter
    def bpoa( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bpoa = value

    @property
    def epoa( self ):
        if isinstance( self.__epoa, str ) and self.__epoa != '':
            return self.__epoa

    @epoa.setter
    def epoa( self, value ):
        if isinstance( value, str ) and value != '':
            self.__epoa = value

    @property
    def main( self ):
        if isinstance( self.__main, str ) and self.__main != '':
            return self.__main

    @main.setter
    def main( self, value ):
        if isinstance( value, str ) and value != '':
           self.__main = value

    @property
    def multiyearindicator( self ):
        if isinstance( self.__multiyearindicator, str ) \
                and self.__multiyearindicator != '':
            return self.__multiyearindicator

    @multiyearindicator.setter
    def multiyearindicator( self, value ):
        if isinstance( value, str ) and value != '':
            self.__multiyearindicator = value

    @property
    def sublevel( self ):
        if isinstance( self.__sublevel, str ) and self.__sublevel != '':
            return self.__sublevel

    @sublevel.setter
    def sublevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sublevel = value

    @property
    def ata( self ):
        if isinstance( self.__ata, str ) and self.__ata != '':
            return self.__ata

    @ata.setter
    def ata( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ata = value

    @property
    def aid( self ):
        if isinstance( self.__aid, str ) and self.__aid != '':
            return self.__aid

    @aid.setter
    def aid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__aid = value

    @property
    def fundcategory( self ):
        if isinstance( self.__fundcategory, str ) and self.__fundcategory != '':
            return self.__fundcategory

    @fundcategory.setter
    def fundcategory( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcategory = value

    @property
    def appropriationcode( self ):
        if isinstance( self.__appropriationcode, str ) \
                and self.__appropriationcode != '':
            return self.__appropriationcode

    @appropriationcode.setter
    def appropriationcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationcode = value

    @property
    def appropriationname( self ):
        if isinstance( self.__appropriationname, str ) \
                and self.__appropriationname != '':
            return self.__appropriationname

    @appropriationname.setter
    def appropriationname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__appropriationname = name

    @property
    def fundgroup( self ):
        if isinstance( self.__fundgroup, str ) and self.__fundgroup != '':
            return self.__fundgroup

    @fundgroup.setter
    def fundgroup( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundgroup = value

    @property
    def noyear( self ):
        if isinstance( self.__noyear, str ) and self.__noyear != '':
            return self.__noyear

    @noyear.setter
    def noyear( self, value ):
        if isinstance( value, str ) and value != '':
            self.__noyear = value

    @property
    def carryover( self ):
        if isinstance( self.__carryover, str ) and self.__carryover != '':
            return self.__carryover

    @carryover.setter
    def carryover( self, value ):
        if isinstance( value, str ) and value != '':
            self.__carryover = value

    @property
    def cancelledyearspendingaccount( self ):
        if isinstance( self.__cancelledyearspendingaccount, str ) \
                and self.__cancelledyearspendingaccount != '':
            return self.__cancelledyearspendingaccount

    @cancelledyearspendingaccount.setter
    def cancelledyearspendingaccount( self, acct ):
        if isinstance( acct, str ) and acct != '':
            self.__cancelledyearspendingaccount = acct

    @property
    def applyatalllevels( self ):
        if isinstance( self.__applyatalllevels, str ) and self.__applyatalllevels != '':
            return self.__applyatalllevels

    @applyatalllevels.setter
    def applyatalllevels( self, value ):
        if isinstance( value, str ) and value != '':
           self.__applyatalllevels = value

    @property
    def batsfund( self ):
        if isinstance( self.__batsfund, str ) and self.__batsfund != '':
            return self.__batsfund

    @batsfund.setter
    def batsfund( self, value ):
        if isinstance( value, str ) and value != '':
            self.__batsfund = value

    @property
    def batsenddate( self ):
        if isinstance( self.__batsenddate, datetime ):
            return self.__batsenddate

    @batsenddate.setter
    def batsenddate( self, value ):
        if isinstance( value, datetime ):
            self.__batsenddate = value

    @property
    def batsoptionid( self ):
        if isinstance( self.__batsoptionid, int ):
            return self.__batsoptionid

    @batsoptionid.setter
    def batsoptionid( self, value ):
        if isinstance( value, int ):
            self.__batsoptionid = value

    @property
    def securityorg( self ):
        if isinstance( self.__securityorg, str ) and self.__securityorg != '':
            return self.__securityorg

    @securityorg.setter
    def securityorg( self, value ):
        if isinstance( value, str ) and value != '':
            self.__securityorg = value

    @property
    def treasuryaccountcode( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasuryaccountcode.setter
    def treasuryaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountcode = value

    @property
    def treasuryaccountname( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasuryaccountname.setter
    def treasuryaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountname = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def apportionmentaccountcode( self ):
        if isinstance( self.__apportionmentaccountcode, str ) \
                and self.__apportionmentaccountcode != '':
            return self.__apportionmentaccountcode

    @apportionmentaccountcode.setter
    def apportionmentaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__apportionmentaccountcode = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Funds
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'FundsId',
                          'BFY',
                          'EFY',
                          'Code',
                          'Name',
                          'ShortName',
                          'Status',
                          'SubLevelPrefix',
                          'ATA',
                          'BeginningPeriodOfAvailability',
                          'EndingPeriodOfAvailability',
                          'MAIN',
                          'A',
                          'AID',
                          'SUB',
                          'FundCategory',
                          'AppropriationCode',
                          'SubAppropriationCode',
                          'FundGroup',
                          'NoYear',
                          'Carryover',
                          'CancelledYearSpendingAccount',
                          'ApplyAtAllLevels',
                          'BatsFund',
                          'BatsEndDate',
                          'BatsOptionId',
                          'SecurityOrg' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'Code', ]
            v = (self.__bfy, self.__efy, self.__code)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Fund'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Fund'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# FederalHoliday( bfy, name, provider = Provider.SQLite )
class FederalHoliday( ):
    '''Defines the FederalHoliday class'''
    __source = None
    __provider = None
    __federalholidaysid = None
    __bfy = None
    __efy = None
    __name = None
    __newyearsday = None
    __martinlutherking = None
    __memorial = None
    __juneteenth = None
    __independence = None
    __washingtons = None
    __labor = None
    __columbus = None
    __veterans = None
    __thanksgiving = None
    __christmas = None
    __list = None
    __date = None
    __dayofweek = None
    __day = None
    __month = None
    __year = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__federalholidaysid, int ):
            return self.__federalholidaysid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__federalholidaysid = value

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if value is not None:
            self.__bfy = str( value )
            self.__data[ 'value' ] = self.__bfy

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value in self.__list:
            self.__name = value

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @property
    def month( self ):
        if self.__month is not None:
            return self.__month

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def list( self ):
        if self.__list is not None:
            return self.__list

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def observances( self ):
        if isinstance( self.__observance, dict ):
            return self.__observance

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, name, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FederalHolidays
        self.__list = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                        'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                        'Memorial', 'Juneteenth', 'Independence', 'Labor' ]
        self.__observance = { 'Columbus': 'The second Monday in October',
                              'Veterans': 'Veterans Day, November 11',
                              'Thanksgiving': 'The fourth Thursday in November',
                              'Christmas': 'Christmas Day, December 25',
                              'NewYearsDay': 'January 1',
                              'MartinLutherKing': 'The third Monday in January',
                              'Washingtons': 'The third Monday in February',
                              'Memorial': 'The last Monday in May.',
                              'Juneteenth': 'Juneteenth National Independence Day, June 19',
                              'Independence': 'Independence Day, July 4',
                              'Labor': 'The first Monday in September' }
        self.__bfy = bfy
        self.__year = int( bfy )
        self.__name = self.setname( name )
        self.__date = self.setdate( name )
        self.__dayofweek = self.__date.day
        self.__month = self.__date.month
        self.__day = self.__date.isoweekday()
        self.__fields = [ 'FederalHolidaysId',
                          'BFY',
                          'Columbus',
                          'Veterans',
                          'Thanksgiving',
                          'Christmas',
                          'NewYears',
                          'MartinLutherKing',
                          'Presidents',
                          'Memorial',
                          'Juneteenth',
                          'Independence',
                          'Labor' ]
        self.__data = None
        self.__frame = None

    def __str__( self ):
        if not self.__name == '':
            return self.__name

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'Name', ]
            v = (self.__bfy, self.__efy, self.__name,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )

    def columbusday( self ):
        '''The second Monday in October'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 10, 1 )
                __end = datetime( self.__year, 10, 31 )
                __delta = ( __start - __end ).days
                for i in range( 1, 31 ):
                    d = datetime( self.__year, 10, __start.day + i )
                    if ( 15 < d.day < 28 ) and datetime( self.__year, 10, d.day ).isoweekday( ) == 1:
                        self.__columbus = datetime( self.__year, 10, d.day )
                        return self.__columbus
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'columnbusday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def veteransday( self ):
        '''Veterans Day, November 11'''
        try:
            if self.__year is not None:
                self.__veterans = datetime( self.__year, 11, 11 )
                return self.__veterans
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'veteransday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def thanksgivingday( self ):
        '''The fourth Thursday in November'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 11, 15 )
                __end = datetime( self.__year, 11, 30 )
                __delta = ( __start - __end ).days
                for i in range( 15, 31 ):
                    d = datetime( self.__year, 11, i )
                    if ( 21 < d.day < 31 ) and datetime( self.__year, 11, d.day ).isoweekday( ) == 4:
                        self.__thanksgiving = datetime( self.__year, 11, d.day )
                        return self.__thanksgiving
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'thanksgivingday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def christmasday( self ):
        '''Christmas Day, December 25'''
        try:
            if self.__year is not None:
                self.__christmas = datetime( self.__year, 12, 25 )
                return self.__christmas
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'christmasday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def newyearsday( self ):
        '''January 1'''
        try:
            if self.__year is not None:
                self.__newyearsday = datetime( self.__year, 1, 1 )
                return self.__newyearsday
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'newyearsday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def martinlutherkingday( self ):
        '''The third Monday in January'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 1, 15 )
                __end = datetime( self.__year, 1, 31 )
                __delta = ( __start - __end ).days
                for i in range( __delta ):
                    d = datetime( self.__year, 1, __start.day + i )
                    if ( 15 < d.day < 31) and datetime( self.__year, 1, d.day ).isoweekday( ) == 1:
                        self.__martinlutherking = datetime( self.__year, 1, d.day )
                        return self.__martinlutherking
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'martinlutherkingday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def washingtonsday( self ):
        '''The third Monday in February'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 2, 15 )
                __end = datetime( self.__year, 2, 28 )
                __delta = ( __start - __end ).days
                for i in range( __delta ):
                    d = datetime( self.__year, 2, __start.day + i )
                    if (15 < d.day < 28) and datetime( self.__year, 2, d.day ).isoweekday( ) == 1:
                        self.__washingtons = datetime( self.__year, 2, d.day )
                        return self.__washingtons
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'washingtonsday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def memorialday( self ):
        '''The last Monday in May'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 5, 1 )
                __end = datetime( self.__year, 5, 31 )
                __delta = ( __start - __end ).days
                for i in range( 15, 31 ):
                    d = datetime( self.__year, 5, i )
                    if ( 21 < d.day < 31 ) and datetime( self.__year, 5, d.day ).isoweekday( ) == 1:
                        self.__memorial = datetime( self.__year, 5, d.day )
                        return self.__memorial
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'memorialday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def juneteenthday( self ):
        '''Juneteenth National Independence Day, June 19'''
        try:
            if self.__year is not None:
                self.__juneteenth = datetime( self.__year, 6, 19 )
                return self.__juneteenth
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'juneteenthday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def independence( self ):
        '''Independence Day, July 4'''
        try:
            if self.__year is not None:
                self.__independence = datetime( self.__year, 7, 4 )
                return self.__independence
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'independence( self )'
            err = ErrorDialog( exc )
            err.show( )

    def laborday( self ):
        '''The first Monday in September'''
        try:
            if self.__year is not None:
                __monday = list( )
                __month = dt.date( self.__year, 9, 1 ) - dt.date( self.__year, 9, 31 )
                for i in range( 1, __month.days - 1 ):
                    if datetime( self.__year, 9, i ).isoweekday( ) == 1:
                        __monday.append( datetime( self.__year, 9, i ) )
                y = __monday[ 0 ].date( ).year
                m = __monday[ 0 ].date( ).currentmonth
                d = __monday[ 0 ].date( ).currentday
                self.__labor = datetime( y, m, d )
                return self.__labor
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'laborday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def dayofweek( self ):
        try:
            if 0 < self.__day < 8 and  self.__day == 1:
                self.__dayofweek = 'Monday'
                return self.__dayofweek
            elif 0 <  self.__day < 8 and  self.__day == 2:
                self.__dayofweek = 'Tuesday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 3:
                self.__dayofweek = 'Wednesday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 4:
                self.__dayofweek = 'Thursday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 5:
                self.__dayofweek = 'Friday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 6:
                self.__dayofweek = 'Saturday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 7:
                self.__dayofweek = 'Sunday'
                return self.__dayofweek
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'dayofweek( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isweekday( self ):
        try:
            if 1 <= self.__date.isoweekday() <= 5:
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'isweekday( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isweekend( self ):
        try:
            if 5 < self.__date.isoweekday() <= 7:
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'isweekend( self )'
            err = ErrorDialog( exc )
            err.show( )

    def setdate( self, name ):
        try:
            if isinstance( name, str ) and name in self.__list:
                if name == 'Columbus':
                    self.__date = self.columbusday( )
                    return self.__date
                elif name == 'Veterans':
                    self.__date = self.veteransday( )
                    return self.__date
                elif name == 'Thanksgiving':
                    self.__date = self.thanksgivingday( )
                    return self.__date
                elif name == 'Christmas':
                    self.__date = self.christmasday( )
                    return self.__date
                elif name == 'NewYearsDay':
                    self.__date = self.newyearsday( )
                    return self.__date
                elif name == 'MartinLutherKing':
                    self.__date = self.martinlutherkingday( )
                    return self.__date
                elif name == 'Washingtons':
                    self.__date = self.washingtonsday( )
                    return self.__date
                elif name == 'Memorial':
                    self.__date = self.memorialday( )
                    return self.__date
                elif name == 'Juneteenth':
                    self.__date = self.juneteenthday( )
                    return self.__date
                elif name == 'Labor':
                    self.__date = self.laborday( )
                    return self.__date
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'setdate( self, value )'
            err = ErrorDialog( exc )
            err.show( )

    def setname( self, name ):
        try:
            if isinstance( name, str ) and name in self.__list:
                self.__name = name
                return self.__name
            else:
                self.__name = 'NS'
                return self.__name
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'FederalHoliday'
            exc.method = 'setname( self, value  ) '
            err = ErrorDialog( exc )
            err.show( )


# FullTimeEquivalent( bfy, fund, provider = Provider.SQLite )
class FullTimeEquivalent( ):
    '''object representing Operating Plan FTE'''
    __source = None
    __provider = None
    __fulltimeequivalentsid = None
    __operatingplansid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FullTimeEquivalents
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'FullTimeEquivalentsId', 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
                           'FundCode', 'OrgCode', 'AccountCode', 'BocCode', 'BocName',
                           'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
                           'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode', 'ProgramAreaCode',
                           'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName', 'ProgramProjectName',
                           'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName', 'ProgramAreaName',
                           'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
                           'ObjectiveCode', 'ObjectiveName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'FullTimeEquivalent'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'FullTimeEquivalent'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# GeneralLedgerAccounts( bfy, number, provider = Provider.SQLite )
class GeneralLedgerAccounts( ):
    __source = None
    __provider = None
    __generalledgeraccountsid = None
    __bfy = None
    __efy = None
    __treasurysymbol = None
    __fundcode = None
    __fundname = None
    __accountnumber = None
    __accountname = None
    __fields = None

    @property
    def id( self ):
        if isinstance( self.__ledgeraccountsid, int ):
            return self.__ledgeraccountsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__ledgeraccountsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def accountnumber( self ):
        if isinstance( self.__accountnumber, str ) and self.__accountnumber != '':
            return self.__accountnumber

    @accountnumber.setter
    def accountnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountnumber = value

    @property
    def accountname( self ):
        if isinstance( self.__accountname, str ) and self.__accountname != '':
            return self.__accountname

    @accountname.setter
    def accountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountname = value

    @property
    def treasurysymbol( self ):
        if isinstance( self.__treasuryaccount, str ) and self.__treasuryaccount != '':
            return self.__treasuryaccount

    @treasurysymbol.setter
    def treasurysymbol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, number, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__accountnumber = number if isinstance( number, str ) and number != '' else None
        self.__provider = provider
        self.__source = Source.GeneralLedgerAccounts
        self.__fields = [ 'GeneralLedgerAccountsId',
                          'BFY',
                          'EFY',
                          'FundCode',
                          'FundName',
                          'TreasurySymbol',
                          'AccountNumber',
                          'AccountName',
                          'BeginningBalance',
                          'CreditBalance',
                          'DebitBalance',
                          'ClosingAmount' ]


# Goal( code, provider = Provider.SQLite )
class Goal( ):
    '''Defines the Goal Class'''
    __source = None
    __provider = None
    __goalsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__goalsid, int ):
            return self.__goalsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__goalsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Goals
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'GoalsId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Goal'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )


# GrowthRates( bfy, id, provider = Provider.SQLite )
class GrowthRates( ):
    '''GrowthRates( bfy, id )
    initializes object providing OMB growth rate data'''
    __source = None
    __provider = None
    __growthratesid = None
    __rateid = None
    __description = None
    __budgetyear = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__growthratesid, int ):
            return self.__growthratesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__growthratesid = value

    @property
    def rateid( self ):
        if isinstance( self.__rateid, int ):
            return self.__rateid

    @rateid.setter
    def rateid( self, value ):
        if isinstance( value, int ):
            self.__rateid = value

    @property
    def description( self ):
        if isinstance( self.__description, str ) and self.__description != '':
            return self.__description

    @description.setter
    def description( self, value ):
        if isinstance( value, str ) and value != '':
            self.__description = value

    @property
    def budgetyear( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budgetyear.setter
    def budgetyear( self, value ):
        if isinstance( value, float ):
            self.__budgetyear = value

    @property
    def outyear1( self ):
        if isinstance( self.__outyear1, float ):
            return self.__outyear1

    @outyear1.setter
    def outyear1( self, value ):
        if isinstance( value, float ):
            self.__outyear1 = value

    @property
    def outyear2( self ):
        if isinstance( self.__outyear2, float ):
            return self.__outyear2

    @outyear2.setter
    def outyear2( self, value ):
        if isinstance( value, float ):
            self.__outyear2 = value

    @property
    def outyear3( self ):
        if isinstance( self.__outyear3, float ):
            return self.__outyear3

    @outyear3.setter
    def outyear3( self, value ):
        if isinstance( value, float ):
            self.__outyear3 = value

    @property
    def outyear4( self ):
        if isinstance( self.__outyear4, float ):
            return self.__outyear4

    @outyear4.setter
    def outyear4( self, value ):
        if isinstance( value, float ):
            self.__outyear4 = value

    @property
    def outyear5( self ):
        if isinstance( self.__outyear5, float ):
            return self.__outyear5

    @outyear5.setter
    def outyear5( self, value ):
        if isinstance( value, float ):
            self.__outyear5 = value

    @property
    def outyear6( self ):
        if isinstance( self.__outyear6, float ):
            return self.__outyear6

    @outyear6.setter
    def outyear6( self, value ):
        if isinstance( value, float ):
            self.__outyear6 = value

    @property
    def outyear7( self ):
        if isinstance( self.__outyear7, float ):
            return self.__outyear7

    @outyear7.setter
    def outyear7( self, value ):
        if isinstance( value, float ):
            self.__outyear7 = value

    @property
    def outyear8( self ):
        if isinstance( self.__outyear8, float ):
            return self.__outyear8

    @outyear8.setter
    def outyear8( self, value ):
        if isinstance( value, float ):
            self.__outyear8 = value

    @property
    def outyear9( self ):
        if isinstance( self.__outyear9, float ):
            return self.__outyear9

    @outyear9.setter
    def outyear9( self, value ):
        if isinstance( value, float ):
            self.__outyear9 = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, id, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.GrowthRates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rateid = id if isinstance( id, str ) and id != '' else None
        self.__fields = [ 'GrowthRatesId',
                          'RateId',
                          'Description',
                          'BudgetYearRate',
                          'OutYear1',
                          'OutYear2',
                          'OutYear3',
                          'OutYear4',
                          'OutYear5',
                          'OutYear6',
                          'OutYear7',
                          'OutYear8',
                          'OutYear9',
                          'Sort' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RateId', ]
            v = (self.__bfy, self.__rateid)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'GrowthRates'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'GrowthRates'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# HeadquartersAuthority( bfy, rpio, provider = Provider.SQLite )
class HeadquartersAuthority( ):
    '''object representing HQ Allocations'''
    __source = None
    __provider = None
    __headquartersauthorityid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, rpio = None, provider = Provider.SQLite ):
        self.__source = Source.HeadquartersAuthority
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None
        self.__fields = [ 'HeadquartersAuthorityId',
                           'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'BocCode',
                           'BocName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'HeadquartersAuthority'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'HeadquartersAuthority'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# HeadquartersOffice( code, provider = Provider.SQLite  )
class HeadquartersOffice( ):
    '''Defines a regional RPIO'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.___resourceplanningofficesid = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ):
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ):
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.HeadquartersOffices
        self.__rpiocode = code if isinstance( code, str ) and len( code ) == 2 else None
        self.__fields = [ 'HeadquartersOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]


    def __str__( self ):
        if isinstance( self.__code, str ):
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'RpioCode', ]
            v = (self.__rpiocode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HeadquartersOffice'
            exc.method = 'getdata( self ) '
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HeadquartersOffice'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# HumanResourceOrganization( code, provider = Provider.SQLite )
class HumanResourceOrganization( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __humanresourceorganizationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__humanresourceorganizationsid, int ):
            return self.__humanresourceorganizationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__humanresourceorganizationsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.HumanResourceOrganizations
        self.__code = code if isinstance( code, str ) else None
        self.__frame = DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HumanResourceOrganization'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'HumanResourceOrganization'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# MonthlyOutlays( bfy, efy, account, provider = Provider.SQLite )
class MonthlyOutlays( ):
    '''MonthlyOutlays( bfy, efy, omb ) initializes
    object providing OMB outlay data'''
    __source = None
    __provider = None
    __monthlyoutlaysid = None
    __reportyear = None
    __bfy = None
    __efy = None
    __linenumber = None
    __linename = None
    __taxationcode = None
    __treasuryagency = None
    __treasuryaccount = None
    __treasuryaccountname = None
    __subaccount = None
    __ombagency = None
    __ombbureau = None
    __ombaccount = None
    __ombaccountname = None
    __january = None
    __feburary = None
    __march = None
    __april = None
    __may = None
    __june = None
    __july = None
    __august = None
    __september = None
    __october = None
    __november = None
    __december = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__monthlyoutlaysid, int ):
            return self.__monthlyoutlaysid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__monthlyoutlaysid = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def linename( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @linename.setter
    def linename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linename = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def taxationcode( self ):
        if isinstance( self.__taxationcode, str ) and self.__taxationcode != '':
            return self.__taxationcode

    @taxationcode.setter
    def taxationcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__taxationcode = value

    @property
    def treasuryagency( self ):
        if isinstance( self.__treasuryagency, str ) and self.__treasuryagency != '':
            return self.__treasuryagency

    @treasuryagency.setter
    def treasuryagency( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryagency = value

    @property
    def treasuryaccount( self ):
        if isinstance( self.__treasuryaccount, str ) and self.__treasuryaccount != '':
            return self.__treasuryaccount

    @treasuryaccount.setter
    def treasuryaccount( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccount = value

    @property
    def ombaccount( self ):
        if isinstance( self.__ombaccount, str ) and self.__ombaccount != '':
            return self.__ombaccount

    @ombaccount.setter
    def ombaccount( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccount = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.MonthlyOutlays
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) <= 5 else None
        self.__fields = [ 'MonthlyOutlaysId',
                          'FiscalYear',
                          'LineNumber',
                          'LineTitle',
                          'TaxationCode',
                          'TreasuryAgency',
                          'TreasuryAccount',
                          'SubAccount',
                          'BFY',
                          'EFY',
                          'OmbAgency',
                          'OmbBureau',
                          'OmbAccount',
                          'AgencySequence',
                          'BureauSequence',
                          'AccountSequence',
                          'AgencyTitle',
                          'BureauTitle',
                          'OmbAccountTitle',
                          'TreasuryAccountTitle',
                          'October',
                          'November',
                          'December',
                          'January',
                          'Feburary',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            v = (self.__bfy, self.__efy, self.__ombaccountcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'MonthlyOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'MonthlyOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# NationalProgram( code value, provider = Provider.SQLite )
class NationalProgram( ):
    '''Defines the NationalProgram Class'''
    __source = None
    __provider = None
    __nationalprogramsid = None
    __code = None
    __name = None
    __rpio = None
    __title = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__nationalprogramsid, int ):
            return self.__nationalprogramsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__nationalprogramsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def rpio( self ):
        if isinstance( self.__rpio, str ) and self.__rpio != '':
            return self.__rpio

    @rpio.setter
    def rpio( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpio = value

    @property
    def title( self ):
        if isinstance( self.__title, str ) and self.__title != '':
            return self.__title

    @title.setter
    def title( self, value ):
        if isinstance( value, str ) and value != '':
            self.__title = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.NationalPrograms
        self.__code = code
        self.__fields = [ 'NationalProgramsId',
                          'Code',
                          'Name',
                          'RpioCode',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'NationalProgram'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'NationalProgram'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Objective( code, provider = Provider.SQLite )
class Objective( ):
    '''Defines the Objective Class'''
    __source = None
    __provider = None
    __objectivesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__objectivesid, int ):
            return self.__objectivesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__objectivesid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Objectives
        self.__code = code
        self.__fields = [ 'ObjectivesId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = Source.Objectives
            provider = Provider.SQLite
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Objective'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Objective'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Organization( code, provider = Provider.SQLite  )
class Organization( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __organizationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__organizationsid, int ):
            return self.__organizationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__organizationsid = id

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, code ):
        if isinstance( code, str ) and code != '':
            self.__code = code

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__data = cache

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Organizations
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'OrganizationsId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Organization'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )


# ObjectClassOutlays( account, provider = Provider.SQLite )
class ObjectClassOutlays( ):
    '''ObjectClassOutlays( bfy, omb )
    object provides OMB outlay data'''
    __source = None
    __provider = None
    __objectclassoutlaysid = None
    __reportyear = None
    __ombagencycode = None
    __ombaccountcode = None
    __ombaccountname = None
    __obligationtype = None
    __directreimbursabletitle = None
    __objectclassgroupnumber = None
    __objectclassgroupname = None
    __boccode = None
    __bocname = None
    __financeobjectclass = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__objectclassoutlaysid, int ):
            return self.__objectclassoutlaysid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__objectclassoutlaysid = value

    @property
    def reportyear( self ):
        if isinstance( self.__reportyear, str ) and len( self.__reportyear ) == 4:
            return self.__reportyear

    @reportyear.setter
    def reportyear( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__reportyear = value

    @property
    def ombagencycode( self ):
        if isinstance( self.__ombagencycode, str ) and self.__ombagencycode != '':
            return self.__ombagencycode

    @ombagencycode.setter
    def ombagencycode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombagencycode = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def obligationtype( self ):
        if isinstance( self.__obligationtype, str ) and self.__obligationtype != '':
            return self.__obligationtype

    @obligationtype.setter
    def obligationtype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__obligationtype = value

    @property
    def directreimbursabletitle( self ):
        if isinstance( self.__directreimbursabletitle, str ) and self.__directreimbursabletitle != '':
            return self.__directreimbursabletitle

    @directreimbursabletitle.setter
    def directreimbursabletitle( self, value ):
        if isinstance( value, str ) and value != '':
            self.__directreimbursabletitle = value

    @property
    def objectclassgroupnumber( self ):
        if isinstance( self.__objectclassgroupnumber, str ) and self.__objectclassgroupnumber != '':
            return self.__objectclassgroupnumber

    @objectclassgroupnumber.setter
    def objectclassgroupnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectclassgroupnumber = value

    @property
    def objectclassgroupname( self ):
        if isinstance( self.__objectclassgroupname, str ) and self.__objectclassgroupname != '':
            return self.__objectclassgroupname

    @objectclassgroupname.setter
    def objectclassgroupname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectclassgroupname = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def financeobjectclass( self ):
        if isinstance( self.__financeobjectclass, str ) and self.__financeobjectclass != '':
            return self.__financeobjectclass

    @financeobjectclass.setter
    def financeobjectclass( self, value ):
        if isinstance( value, str ) and value != '':
            self.__financeobjectclass = value

    @property
    def prioryear( self ):
        if isinstance( self.__prioryear, float ):
            return self.__prioryear

    @prioryear.setter
    def prioryear( self, value ):
        if isinstance( value, float ):
            self.__prioryear = value

    @property
    def currentyear( self ):
        if isinstance( self.__currentyear, float ):
            return self.__currentyear

    @currentyear.setter
    def currentyear( self, value ):
        if isinstance( value, float ):
            self.__currentyear = value

    @property
    def budgetyear( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budgetyear.setter
    def budgetyear( self, value ):
        if isinstance( value, float ):
            self.__budgetyear = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ObjectClassOutlays
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'ObjectClassOutlaysId',
                          'ReportYear',
                          'OmbAgencyCode',
                          'OmbAgencyName',
                          'OmbBureauCode',
                          'OmbBureauName',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'ObligationType',
                          'DirectReimbursableTitle',
                          'ObjectClassGroupNumber',
                          'ObjectClassGroupName',
                          'BocCode',
                          'BocName',
                          'FinanceObjectClass',
                          'PriorYear',
                          'CurrentYear',
                          'BudgetYear' ]

    def getdata( self ):
        try:
            source = Source.ObjectClassOutlays
            provider = Provider.SQLite
            n = [ 'OmbAccountCode', ]
            v = (self.__ombaccountcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlays'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# OperatingPlan( bfy, efy, fundcode, provider = Provider.SQLite )
class OperatingPlan( ):
    '''object representing Operating plan allocations'''
    __source = None
    __provider = None
    __operatingplansid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.OperatingPlans
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
                           'FundCode', 'OrgCode', 'AccountCode', 'RcCode', 'BocCode', 'BocName',
                           'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
                           'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode', 'ProgramAreaCode',
                           'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName', 'ProgramProjectName',
                           'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName', 'ProgramAreaName',
                           'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
                           'ObjectiveCode', 'ObjectiveName' ]

    def getdata( self ):
        try:
            src = self.__source
            pdr = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source = src, provider = pdr )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OperatingPlan'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OperatingPlan'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# OpenCommitment( bfy, fund, account, boc, provider = Provider.SQLite )
class OpenCommitment( ):
    ''' OpenCommitment( bfy, fund, account, boc )
    initializes object providing OpenCommitment data.'''
    __source = None
    __provider = None
    __opencommitmentsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__expendituresid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def referencedocumentnumber( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @referencedocumentnumber.setter
    def referencedocumentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__referencedocumentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if isinstance( value, int ):
            self.__age = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__foccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.OpenCommitments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'OpenCommitmentsId',
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitments',
                           'Obligations',
                           'ULO',
                           'Expenditures' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OpenCommitment'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'OpenCommitment'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Obligations( bfy, fund, account, boc, provider = Provider.SQLite )
class Obligations( ):
    '''Obligation( bfy, fund, account, boc )
    initializes object providing Obligation data'''
    __source = None
    __provider = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__obligationsid, int ):
            return self.__obligationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__obligationsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def referencedocumentnumber( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @referencedocumentnumber.setter
    def referencedocumentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__referencedocumentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if isinstance( value, int ):
            self.__age = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__foccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Obligations
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitments',
                           'Obligations',
                           'ULO',
                           'Expenditures' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Obligaions'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'Obligations'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ProgramFinancingScedule( bfy, account, provider = Provider.SQLite )
class ProgramFinancingSchedule( ):
    __source = None
    __provider = None
    __bfy = None
    __programfinancingscheduleid = None
    __reportyear = None
    __ledgeraccountcode = None
    __treasuryagencycode = None
    __ombaccountcode = None
    __ombaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __fundname = None
    __sectionnumber = None
    __sectionname = None
    __linenumber = None
    __linedescription = None
    __originalamount = None
    __budgetamount = None
    __agencyamount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def treasuryaccountcode( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasuryaccountcode.setter
    def treasuryaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountcode = value

    @property
    def treasuryaccountname( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasuryaccountname.setter
    def treasuryaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountname = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, account, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__ombaccountcode = account if isinstance( account, str ) and account != '' else None
        self.__provider = provider
        self.__source = Source.ProgramFinancingSchedule
        self.__fields = [ 'ProgramFinancingScheduleId',
                          'ReportYear',
                          'TreasuryAccountCode',
                          'LedgerAccountCode',
                          'SectionNumber',
                          'SectionName',
                          'LineNumber',
                          'LineDescription',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'FundName',
                          'OriginalAmount',
                          'BudgetAmount',
                          'AgencyAmount',
                          'Amount' ]


# PublicLaws( bfy, number, provider = Provider.SQLite )
class PublicLaws( ):
    __source = None
    __provider = None
    __publiclawsid = None
    __bfy = None
    __efy = None
    __lawnumber = None
    __enacteddate = None
    __congress = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__publiclawsid, int ):
            return self.__publiclawsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__publiclawsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def lawnumber( self ):
        if isinstance( self.__lawnumber, str ) and self.__lawnumber != '':
            return self.__lawnumber

    @lawnumber.setter
    def lawnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__lawnumber = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, number, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__lawnumber = number if isinstance( number, str ) and number != '' else None
        self.__provider = provider
        self.__source = Source.PublicLaws
        self.__fields = [ 'PublicLawsId',
                          'LawNumber',
                          'BillTitle',
                          'EnactedDate',
                          'Congress',
                          'BFY' ]


# PayrollActivity( bfy, fund, provider = Provider.SQLite )
class PayrollActivity( ):
    '''provides payroll data'''
    __source = None
    __provider = None
    __payrollactivityid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __rccode = None
    __rcname = None
    __subrccode = None
    __subrcname = None
    __hrorgcode = None
    __hrorgname = None
    __workcode = None
    __workcodename = None
    __payperiod = None
    __startdate = None
    __enddate = None
    __checkdate = None
    __foccode = None
    __focname = None
    __amount = None
    __hours = None
    __basepaid = None
    __basehours = None
    __benefits = None
    __overtimepaid = None
    __overtimehours = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__payrollactivityid, int ):
            return self.__payrollactivityid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__payrollactivityid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def subrccode( self ):
        if isinstance( self.__subrccode, str ) and self.__subrccode != '':
            return self.__subrccode

    @subrccode.setter
    def subrccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subrccode = value

    @property
    def subrcname( self ):
        if isinstance( self.__subrcname, str ) and self.__subrcname != '':
            return self.__subrcname

    @subrcname.setter
    def subrcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subrcname = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def hrorgcode( self ):
        if isinstance( self.__hrorgcode, str ) and self.__hrorgcode != '':
            return self.__hrorgcode

    @hrorgcode.setter
    def hrorgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__hrorgcode = value

    @property
    def hrorgname( self ):
        if isinstance( self.__hrorgname, str ) and self.__hrorgname != '':
            return self.__hrorgname

    @hrorgname.setter
    def hrorgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__hrorgname = value

    @property
    def workcode( self ):
        if isinstance( self.__workcode, str ) and self.__workcode != '':
            return self.__workcode

    @workcode.setter
    def workcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__workcode = value

    @property
    def workcodename( self ):
        if isinstance( self.__workcodename, str ) and self.__workcodename != '':
            return self.__workcodename

    @workcodename.setter
    def workcodename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__workcodename = value

    @property
    def payperiod( self ):
        if isinstance( self.__payperiod, int ):
            return self.__payperiod

    @payperiod.setter
    def payperiod( self, value ):
        if isinstance( value, int ):
            self.__payperiod = value

    @property
    def startdate( self ):
        if isinstance( self.__startdate, datetime ):
            return self.__startdate

    @startdate.setter
    def startdate( self, value ):
        if isinstance( value, datetime ):
            self.__startdate = value

    @property
    def enddate( self ):
        if isinstance( self.__enddate, datetime ):
            return self.__enddate

    @enddate.setter
    def enddate( self, value ):
        if isinstance( value, datetime ):
            self.__startdate = value

    @property
    def checkdate( self ):
        if isinstance( self.__checkdate, datetime ):
            return self.__checkdate

    @checkdate.setter
    def checkdate( self, value ):
        if isinstance( value, datetime ):
            self.__checkdate = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def hours( self ):
        if isinstance( self.__hours, float ):
            return self.__hours

    @hours.setter
    def hours( self, value ):
        if isinstance( value, float ):
            self.__hours = value

    @property
    def basepaid( self ):
        if isinstance( self.__basepaid, float ):
            return self.__basepaid

    @basepaid.setter
    def basepaid( self, value ):
        if isinstance( value, float):
            self.__basepaid = value

    @property
    def basehours( self ):
        if isinstance( self.__basehours, float ):
            return self.__basehours

    @basehours.setter
    def basehours( self, value ):
        if isinstance( value, float ):
            self.__basehours = value

    @property
    def benefits( self ):
        if isinstance( self.__benefits, float ):
            return self.__benefits

    @benefits.setter
    def benefits( self, value ):
        if isinstance( value, float ):
            self.__benefits = value

    @property
    def overtimepaid( self ):
        if isinstance( self.__overtimepaid, float ):
            return self.__overtimepaid

    @overtimepaid.setter
    def overtimepaid( self, value ):
        if isinstance( value, float ):
            self.__overtimepaid = value

    @property
    def overtimehours( self ):
        if isinstance( self.__overtimehours, float ):
            return self.__overtimehours

    @overtimehours.setter
    def overtimehours( self, value ):
        if isinstance( value, float ):
            self.__overtimehours = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.PayrollActivity
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'PayrollActivityId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'AhCode',
                           'AhName',
                           'RcCode',
                           'RcName',
                           'SubRcCode',
                           'SubRcName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'NpmCode',
                           'NpmName',
                           'FocCode',
                           'FocName',
                           'HrOrgCode',
                           'HrOrgName',
                           'WorkCode',
                           'WorkCodeName',
                           'PayPeriod',
                           'StartDate',
                           'EndDate',
                           'CheckDate',
                           'Amount',
                           'Hours',
                           'BasePaid',
                           'BaseHours',
                           'Benefits',
                           'OvertimePaid',
                           'OvertimeHours' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'PayrollActivity'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'PayrollActivity'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Project( code, provider = Provider.SQLite  )
class Project( ):
    '''Defines the Organization Class'''
    __source = None
    __projectsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__projectsid, int ):
            return self.__projectsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__accountsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Projects
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ProjectId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Project'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Project'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ProgramArea( code, provider = Provider.SQLite  )
class ProgramArea( ):
    '''defines the ProgramArea class'''
    __source = None
    __provider = None
    __programareasid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__programareasid, int ):
            return self.__programareasid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__accountsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ProgramAreas
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ProgramAreasId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramArea'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramArea'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ProgramProjects( code, provider = Provider.SQLite  )
class ProgramProjects( ):
    '''Defines the ProgramProject Class'''
    __source = None
    __provider = None
    __programprojectsid = None
    __code = None
    __name = None
    __programareacode = None
    __programareaname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__programprojectsid , int ):
            return self.__programprojectsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__programprojectsid  = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.____programareaname = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ProgramProjects
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ProgramProjectsId',
                          'Code',
                          'Name',
                          'ProgramAreaCode',
                          'ProgramAreaName' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramProjects'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )


# PayrollCostCodes( bfy, code, provider = Provider.SQLite )
class PayrollCostCodes( ):
    __source = None
    __provider = None
    __payrollcostcodesid = None
    __bfy = None
    __rpiocode = None
    __ahcode = None
    __rccode = None
    __rcname = None
    __workcode = None
    __workcodename = None
    __hrorgcode = None
    __hrorgname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__payrollcostcodesid, int ):
            return self.__payrollcostcodesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__payrollcostcodesid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def workcode( self ):
        if isinstance( self.__workcode, str ) and self.__workcode != '':
            return self.__workcode

    @workcode.setter
    def workcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__workcode = value

    @property
    def workcodename( self ):
        if isinstance( self.__workcodename, str ) and self.__workcodename != '':
            return self.__workcodename

    @workcodename.setter
    def workcodename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__workcodename = value

    @property
    def hrorgcode( self ):
        if isinstance( self.__hrorgcode, str ) and self.__hrorgcode != '':
            return self.__hrorgcode

    @hrorgcode.setter
    def hrorgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__hrorgcode = value

    @property
    def hrorgname( self ):
        if isinstance( self.__hrorgname, str ) and self.__hrorgname != '':
            return self.__hrorgname

    @hrorgname.setter
    def hrorgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__hrorgname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, rpio, provider = Provider.SQLite ):
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None
        self.__provider = provider
        self.__source = Source.PayrollCostCodes
        self.__fields = [ 'PayrollCostCodesId',
                           'RPIO',
                           'AhCode',
                           'BFY',
                           'RcCode',
                           'RcName',
                           'WorkCode',
                           'WorkCodeName',
                           'HrOrgCode',
                           'HrOrgName' ]


# ProgramResultsCode( bfy, efy, rpio, ah, account, boc, amount = 0.0, provider = Provider.SQLite )
class ProgramResultsCode( ):
    '''Defines the PRC class'''
    __source = None
    __provider = None
    __allocationsid = None
    __rpiocode = None
    __rpioname = None
    __bfy = None
    __efy = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __accountname = None
    __activitycode = None
    __activityname = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__allocationsid, int ):
            return self.__allocationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__allocationsid = id

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str) and len( year ) == 4:
            self.__bfy = year

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, year ):
        if isinstance( year, str) and len( year ) == 4:
            self.__efy = year

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpioname.setter
    def rpioname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__fundcode = code

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__fundname = name

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__ahcode = code

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__ahname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def activitycode( self ):
        if isinstance( self.__activitycode, str ) and self.__activitycode != '':
            return self.__activitycode

    @activitycode.setter
    def activitycode( self, value ):
        if isinstance( value, str ) and self.__activitycode != '':
            self.__activitycode = value

    @property
    def activityname( self ):
        if isinstance( self.__activityname, str ) and self.__activityname != '':
            return self.__activityname

    @activityname.setter
    def activityname( self, value ):
        if isinstance( value, str ) and self.__activityname != '':
            self.__activityname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value


    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, efy = None,
                  fund = None, rpio = None, ah = None,
                  account = None, boc = None,
                  amount = 0.0, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Allocations
        self.__accountcode = account
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__rpiocode = rpio
        self.__ahcode = ah
        self.__boccode = boc
        self.__amount = amount if isinstance( amount, float ) else 0.0
        self.__fields = [ 'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            command = SQL.SELECTALL
            names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
                      'AccountCode', 'BocCode', 'Amount' ]
            values = ( self.__bfy, self.__efy, self.__fundcode, self.__rpiocode,
                       self.__ahcode, self.__accountcode, self.__boccode, self.__amount )
            db = DataBuilder( provider, source, command, names, values )
            self.__data = db.createtable( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramResultsCode'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ProgramResultsCode'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ResponsibilityCenter( code, provider = Provider.SQLite  )
class ResponsibilityCenter( ):
    '''Defines the ResponsibilityCenter Class'''
    __source = None
    __provider = None
    __responsibilitycentersid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__responsibilitycentersid, int ):
            return self.__responsibilitycentersid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__accountsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResponsibilityCenters
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResponsibilityCentersId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
            provider = Provider.SQLite
            source = Source.ResponsibilityCenters
            command = SQL.SELECTALL
            names = [ 'Code', ]
            values = ( self.__code, )
            df = DataBuilder( provider, source, command, names, values )
            self.__data = df.createtable( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResponsibilityCenter'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResponsibilityCenter'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ResourcePlanningOffice( code, provider = Provider.SQLite  )
class ResourcePlanningOffice( ):
    '''defines the ResponsiblePlanningOffice class'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__resourceplanningofficesid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResourcePlanningOffices
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResourcePlanningOfficesId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResourcePlanningOffice'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'ResourcePlanningOffice'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# RegionalOffice( code, provider = Provider.SQLite  )
class RegionalOffice( ):
    '''Defines a regional RPIO'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.___resourceplanningofficesid = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str) and len( self.__rpio ) == 2:
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and len( value ) == 2:
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResourcePlanningOffices
        self.__rpiocode = code if isinstance( code, str ) and len( code ) == 2 else None
        self.__fields = [ 'RegionalOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]

    def __str__( self ):
        if isinstance( self.__code, str ):
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'RegionalOffice'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )


# ReimbursableSurvey( bfy, efy, fund, provider = Provider.SQLite )
class ReimbursableSurvey( ):
    '''ReimbursableSurvey( bfy, fund ) initializes
    object providing Reimbursable Authority data'''
    __source = None
    __provider = None
    __reimbursablesurveyid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__reimbursablesurveyid, int ):
            return self.__reimbursablesurveyid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__reimbursablesurveyid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ReimbursableSurvey
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'ReimbursableSurveyId',
                           'BFY',
                           'FundCode',
                           'FundName',
                           'Amount' ]

    def getdata( self ):
        try:
            src = self.__source
            pro = self.__provider
            n = [ 'BFY', 'FundCode', ]
            v = (self.__bfy, self.__fundcode)
            cfg = SqlConfig( names = n, values = v )
            cnx = Connection( source = src, provider = pro )
            sql = SqlStatement( cnx, cfg )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ReimbursableSurvey'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ReimbursableSurvey'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# ReimbursableAgreements( agreementnumber, provider = Provide.SQLite )
class ReimbursableAgreements( ):
    __source = None
    __provider = None
    __reimbursableagreementsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __rpiocode = None
    __agreementnumber = None
    __startdate = None
    __enddate = None
    __rccode = None
    __rcname = None
    __orgcode = None
    __siteprojectcode = None
    __accountcode = None
    __vendorcode = None
    __vendorname = None
    __amount = None
    __opencommitments = None
    __unliquidatedobligations = None
    __obligations = None
    __available = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__reimbursableagreementsid, int ):
            return self.__reimbursableagreementsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__reimbursableagreementsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def agreementnumber( self ):
        if isinstance( self.__agreementnumber, str ) and self.__agreementnumber != '':
            return self.__agreementnumber

    @agreementnumber.setter
    def agreementnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__agreementnumber = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def opencommitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @opencommitments.setter
    def opencommitments( self, value ):
        if isinstance( value, float ):
            self.__opencommitments = value

    @property
    def obligations( self ):
        if isinstance( self.__obligations, float ):
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if isinstance( value, float ):
            self.__obligations = value

    @property
    def unliquidatedobligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidatedobligations.setter
    def unliquidatedobligations( self, value ):
        if isinstance( value, float ):
            self.__unliquidatedobligations = value

    @property
    def available( self ):
        if isinstance( self.__avaialable, float ):
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if isinstance( value, float ):
            self.__avaialable = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, agreementnumber, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ReimbursableAgreements
        self.__fields = [ 'ReimbursableAgreementsId'
                          'BFY',
                          'EFY',
                          'FundCode',
                          'RpioCode',
                          'AgreementNumber',
                          'StartDate',
                          'EndDate',
                          'RcCode',
                          'RcName',
                          'OrgCode',
                          'SiteProjectCode',
                          'AccountCode',
                          'VendorCode',
                          'VendorName',
                          'Amount',
                          'OpenCommitments',
                          'Obligations',
                          'ULO',
                          'Available' ]

    def __str__( self ):
        if isinstance( self.__agreementnumber, str ) and self.__agreementnumber != '':
            return self.__agreementnumber

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', ]
            v = (self.__bfy,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlays'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'ObjectClassOutlays'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# RegionalAuthority( bfy, fund, provider = Provider.SQLite )
class RegionalAuthority( ):
    '''object representing Regional Allocations'''
    __source = None
    __provider = None
    __regionalauthorityid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__source = Source.RegionalAuthority
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'RegionalAuthorityId',
                           'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'BocCode',
                           'BocName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'RegionalAuthority'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'RegionalAuthority'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# StatusOfFunds( bfy, fund, provider = Provider.SQLite )
class StatusOfFunds( ):
    '''Object representing execution data'''
    __source = None
    __provider = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def budgeted( self ):
        if isinstance( self.__budgeted, float ):
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if isinstance( value, float ):
            self.__budgeted = value

    @property
    def posted( self ):
        if isinstance( self.__posted, float ):
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def opencommitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @opencommitments.setter
    def opencommitments( self, value ):
        if isinstance( value, float ):
            self.__opencommitments = value

    @property
    def obligations( self ):
        if isinstance( self.__obligations, float ):
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if isinstance( value, float ):
            self.__obligations = value

    @property
    def unliquidatedobligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidatedobligations.setter
    def unliquidatedobligations( self, value ):
        if isinstance( value, float ):
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if isinstance( value, float ):
            self.__expenditures = value

    @property
    def used( self ):
        if isinstance( self.__used, float ):
            return self.__used

    @used.setter
    def used( self, value ):
        if isinstance( value, float ):
            self.__used = value

    @property
    def available( self ):
        if isinstance( self.__avaialable, float ):
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if isinstance( value, float ):
            self.__avaialable = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.StatusOfFunds
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitments',
                           'ULO',
                           'Expenditures',
                           'Obligations',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfFunds'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfFunds'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# StatusOfSupplementalFunding( bfy, fund, provider = Provider.SQLite )
class StatusOfSupplementalFunding( ):
    '''Class representing Supplemental Funding execution data'''
    __source = None
    __provider = None
    __statusofsupplementalfundsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def budgeted( self ):
        if isinstance( self.__budgeted, float ):
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value ):
        if isinstance( value, float ):
            self.__budgeted = value

    @property
    def posted( self ):
        if isinstance( self.__posted, float ):
            return self.__posted

    @posted.setter
    def posted( self, value ):
        if isinstance( self.__posted, value ):
            self.__posted = value

    @property
    def opencommitments( self ):
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @opencommitments.setter
    def opencommitments( self, value ):
        if isinstance( value, float ):
            self.__opencommitments = value

    @property
    def obligations( self ):
        if isinstance( self.__obligations, float ):
            return self.__obligations

    @obligations.setter
    def obligations( self, value ):
        if isinstance( value, float ):
            self.__obligations = value

    @property
    def unliquidatedobligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidatedobligations.setter
    def unliquidatedobligations( self, value ):
        if isinstance( value, float ):
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ):
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value ):
        if isinstance( value, float ):
            self.__expenditures = value

    @property
    def used( self ):
        if isinstance( self.__used, float ):
            return self.__used

    @used.setter
    def used( self, value ):
        if isinstance( value, float ):
            self.__used = value

    @property
    def available( self ):
        if isinstance( self.__avaialable, float ):
            return self.__avaialable

    @available.setter
    def available( self, value ):
        if isinstance( value, float ):
            self.__avaialable = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, fund, provider = Provider.SQLite ):
        self.__source = Source.StatusOfSupplementalFunding
        self.__provider = Provider.SQLite
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitments',
                           'ULO',
                           'Expenditures',
                           'Obligations',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]


    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode' ]
            v = (self.__bfy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfSupplementalFunding'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StatusOfSupplementalFunding'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# StateGrantObligation( bfy, rpio, provider = Provider.SQLite )
class StateGrantObligation( ):
    '''object representing the BIS'''
    __source = None
    __provider = None
    __stategrantobligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __statecode = None
    __statename = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__stategrantobligationsid, int ):
            return self.__stategrantobligationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__stategrantobligationsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def statecode( self ):
        if isinstance( self.__statecode, str ) and self.__statecode != '':
            return self.__statecode

    @statecode.setter
    def statecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__statecode = value

    @property
    def statename( self ):
        if isinstance( self.__statename, str ) and self.__statename != '':
            return self.__statename

    @statename.setter
    def statename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__statename = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, rpio, provider = Provider.SQLite ):
        self.__source = Source.StateGrantObligations
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None
        self.__fields = [ 'StateGrantObligationsId',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'AhCode',
                           'AhName',
                           'OrgCode',
                           'OrgName',
                           'StateCode',
                           'StateName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'BocCode',
                           'BocName',
                           'Amount' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__rpiocode, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StateGrantObligation'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'StateGrantObligation'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# SpecialAccount( bfy, fund, account, boc, provider = Provider.SQLite )
class SpecialAccounts( ):
    '''' object providing SF Special Account data'''
    __source = None
    __provider = None
    __specialaccountsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __rpiocode = None
    __rpioname = None
    __specialaccountfundcode = None
    __specialaccountfundname = None
    __specialaccountnumber = None
    __specialaccountname = None
    __accountstatus = None
    __nplstatus = None
    __nplstatusname = None
    __nplstatuscode = None
    __siteid = None
    __cerclisid = None
    __sitecode = None
    __sitename = None
    __operableunit = None
    __pipelinecode = None
    __pipelinedescription = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __transactiontype = None
    __transactiontypename = None
    __availablebalance = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __disbursements = None
    __unpaidbalances = None
    __collections = None
    __cumulativereciepts = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__specialaccountsid, int ):
            return self.__specialaccountsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__specialaccountsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def specialaccountfundcode( self ):
        if isinstance( self.__specialaccountfundcode, str ) and self.__specialaccountfundcode != '':
            return self.__specialaccountfundcode

    @specialaccountfundcode.setter
    def specialaccountfundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__specialaccountfundcode = value

    @property
    def specialaccountfundname( self ):
        if isinstance( self.__specialaccountfundname, str ) and self.__specialaccountfundname != '':
            return self.__specialaccountfundname

    @specialaccountfundname.setter
    def specialaccountfundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__specialaccountfundname = value

    @property
    def specialaccountnumber( self ):
        if isinstance( self.__specialaccountnumber, str ) and self.__specialaccountnumber != '':
            return self.__specialaccountnumber

    @specialaccountnumber.setter
    def specialaccountnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__specialaccountnumber = value

    @property
    def specialaccountname( self ):
        if isinstance( self.__specialaccountnumber, str ) and self.__specialaccountnumber != '':
            return self.__specialaccountnumber

    @specialaccountname.setter
    def specialaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__specialaccountnumber = value

    @property
    def accountstatus( self ):
        if isinstance( self.__accountstatus, str ) and self.__accountstatus != '':
            return self.__accountstatus

    @accountstatus.setter
    def accountstatus( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountstatus = value

    @property
    def nplstatus( self ):
        if isinstance( self.__nplstatus, str ) and self.__nplstatus != '':
            return self.__nplstatus

    @nplstatus.setter
    def nplstatus( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatus = value

    @property
    def nplstatuscode( self ):
        if isinstance( self.__nplstatuscode, str ) and self.__nplstatuscode != '':
            return self.__nplstatuscode

    @nplstatuscode.setter
    def nplstatuscode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatuscode = value

    @property
    def nplstatusname( self ):
        if isinstance( self.__nplstatusname, str ) and self.__nplstatusname != '':
            return self.__nplstatusname

    @nplstatusname.setter
    def nplstatusname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatusname = value

    @property
    def siteid( self ):
        if isinstance( self.__siteid, str ) and self.__siteid != '':
            return self.__siteid

    @siteid.setter
    def siteid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__value = value

    @property
    def cerclisid( self ):
        if isinstance( self.__cerclisid, str ) and self.__cerclisid != '':
            return self.__cerclisid

    @cerclisid.setter
    def cerclisid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__cerclisid = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SpecialAccounts
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'SpecialAccountsId',
                           'BFY',
                           'RpioCode',
                           'FundCode',
                           'SpecialAccountFund',
                           'SpecialAccountNumber',
                           'SpecialAccountName',
                           'AccountStatus',
                           'NplStatusCode',
                           'NplStatusName',
                           'SiteId',
                           'CerclisId',
                           'SiteCode',
                           'SiteName',
                           'OperableUnit',
                           'PipelineCode',
                           'PipelineDescription',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'TransactionType',
                           'TransactionTypeName',
                           'FocCode',
                           'FocName',
                           'TransactionDate',
                           'AvailableBalance',
                           'OpenCommitments',
                           'Obligations',
                           'ULO',
                           'Disbursements',
                           'UnpaidBalances',
                           'Collections',
                           'CumulativeReceipts' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SpecialAccounts'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SpecialAccounts'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# SuperfundSite( bfy, rpio, provider = Provider.SQLite )
class SuperfundSites( ):
    ''' object providing SF Site data '''
    __source = None
    __provider = None
    __superfundsitesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __siteprojectname = None
    __city = None
    __state = None
    __ssid = None
    __epasiteid = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__specialaccountsid, int ):
            return self.__specialaccountsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__specialaccountsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpioname.setter
    def rpioname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpioname = value

    @property
    def city( self ):
        if isinstance( self.__nplstatus, str ) and self.__nplstatus != '':
            return self.__nplstatus

    @city.setter
    def city( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatus = value

    @property
    def state( self ):
        if isinstance( self.__nplstatuscode, str ) and self.__nplstatuscode != '':
            return self.__nplstatuscode

    @state.setter
    def state( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatuscode = value

    @property
    def siteprojectname( self ):
        if isinstance( self.__nplstatusname, str ) and self.__nplstatusname != '':
            return self.__nplstatusname

    @siteprojectname.setter
    def siteprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatusname = value

    @property
    def ssid( self ):
        if isinstance( self.__ssid, str ) and self.__ssid != '':
            return self.__ssid

    @ssid.setter
    def ssid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ssid = value

    @property
    def epasiteid( self ):
        if isinstance( self.__cerclisid, str ) and self.__cerclisid != '':
            return self.__cerclisid

    @epasiteid.setter
    def epasiteid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__cerclisid = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value


    def __init__( self, bfy = None, rpiocode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SuperfundSites
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpiocode if isinstance( rpiocode, str ) and rpiocode != '' else None
        self.__fields = [ 'SuperfundSitesId',
                           'RpioCode',
                           'RpioName',
                           'City',
                           'State',
                           'SSID',
                           'SiteProjectName',
                           'EpaSiteId' ]


    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'SuperfundSites'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SuperfundSites'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# SiteProject( code, provider = Provider.SQLite  )
class SiteProjectCodes( ):
    '''Defines the Site Project Code Class'''
    __source = None
    __provider = None
    __siteprojectcodesid = None
    __epaid = None
    __ssid = None
    __actioncode = None
    __operableunit = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteprojectcodesid, int ):
            return self.___siteprojectcodesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__siteprojectcodesid = value

    @property
    def ssid( self ):
        if isinstance( self.__ssid, str ) and self.__ssid != '':
            return self.__ssid

    @ssid.setter
    def ssid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ssid = value

    @property
    def actioncode( self ):
        if isinstance( self.__actioncode, str ):
            return self.__actioncode

    @actioncode.setter
    def actioncode( self, value ):
        if isinstance( self.__actioncode, str ) and self.__actioncode != '':
            self.__actioncode = value

    @property
    def operableunit( self ):
        if isinstance( self.__operableunit, str ) and self.__operableunit != '':
            return self.__operableunit

    @operableunit.setter
    def operableunit( self, value ):
        if isinstance( value, str ) and value != '':
            self.__operableunit =  value

    @property
    def epaid( self ):
        if isinstance( self.__epaid, str ) and self.__epaid != '':
            return self.__epaid

    @epaid.setter
    def epaid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__epaid =  value

    @property
    def code( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None:
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SiteProjectCodes
        self.__code = str( code )
        self.__ssid = self.__code[ 0: 4 ]
        self.__actioncode = self.__code[ 4:6 ]
        self.__operableunit = self.__code[ 6:9 ]

    def __str__( self ):
        if isinstance( self.__name, str ):
            return self.__name

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SiteProject'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SiteProject'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Appropriation( code, provider = Provider.SQLite )
class SubAppropriations( ):
    '''Defines the Appropriation Class'''
    __source = None
    __provider = None
    __subappropriationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__subappropriationsid , int ):
            return self.__appropriationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__appropriationsid  = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = name

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Appropriations
        self.__code = code if isinstance( code, str ) and code != '' else None
        self.__fields = [ 'SubAppropriationsId',
                           'Code',
                           'Name' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code' ]
            v = ( self.__code )
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SubAppropriations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Appropriation'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# SiteProjectCode( code, provider = Provider.SQLite  )
class SiteProjectCode( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __siteprojectcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteprojectcodesid, int ):
            return self.__siteprojectcodesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__siteprojectcodesid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SiteProjectCodes
        self.__code = code if isinstance( code, str ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SiteProjectCode'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'SiteProjectCode'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# StateOrganization( code, provider = Provider.SQLite  )
class StateOrganization( ):
    '''StateOrganization( fgrp ) class
    representing state codes'''
    __source = None
    __provider = None
    __stateorganizationsid = None
    __code = None
    __name = None
    __orgcode = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None

    @property
    def id( self ):
        if isinstance( self.__stateorganizationsid, int ):
            return self.__stateorganizationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__stateorganizationsid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StateOrganizations
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'StateOrganizationsId',
                          'Name',
                          'Code',
                          'RpioName',
                          'RpioCode' ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'StateOrganization'
            exc.method = 'getdata( self ) '
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'StateOrganization'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# StatusOfAppropriations( bfy, efy, fund, provider = Provider.SQLite )
class StatusOfAppropriations( ):
    '''StatusOfAppropriations( bfy, efy, fund )
    object representing Appropriation-level execution data'''
    __source = None
    __provider = None
    __statusofappropriationsid = None
    __bfy = None
    __efy = None
    __budgetlevel = None
    __appropriationfundcode = None
    __appropriationfundname = None
    __appropriationcreationdate = None
    __appropriationcode = None
    __subappropriationcode = None
    __appropriationdescription = None
    __fundgroup = None
    __fundgroupname = None
    __documenttype = None
    __transtype = None
    __actualrecoverytranstype = None
    __commitmentspendingcontrolflag = None
    __expensespendingcontrolflag = None
    __agreementlimit = None
    __estimatedrecoveriestranstype = None
    __estimatedreimbursementstranstype = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __postedcontrolflag = None
    __postedflag = None
    __recordcarryoveratlowerlevel = None
    __reimbursablespendingoption = None
    __recoveriesoption = None
    __recoveriesspendingoption = None
    __originalbudgetedamount = None
    __apportionmentsposted = None
    __totalauthority = None
    __totalbudgeted = None
    __totalpostedamount = None
    __fundswithdrawnprioryearamounts = None
    __fundinginamount = None
    __fundingoutamount = None
    __totalaccrualrecoveries = None
    __totalactualreimbursements = None
    __totalagreeementreimbursables = None
    __totalcarriedforwardin = None
    __totalcarriedforwardout = None
    __totalcommited = None
    __totalestimatedrecoveries = None
    __totalestimatedreimbursements = None
    __totalexpenses = None
    __totalexpenditureexpenses = None
    __totalexpenseaccruals = None
    __totalprecommitments = None
    __unliquidatedprecommitments = None
    __totalobligations = None
    __unliquidatedobligations = None
    __voidedamount = None
    __totalusedamount = None
    __availableamount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofappropriationsid, int ):
            return self.__statusofappropriationsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ) and value > -1:
            self.__statusofappropriationsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def budgetlevel( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != '':
            return self.__budgetlevel

    @budgetlevel.setter
    def budgetlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetlevel = value

    @property
    def appropriationfundcode( self ):
        if isinstance( self.__appropriationfundcode, str ) \
                and self.__appropriationfundcode != '':
            return self.__appropriationfundcode

    @appropriationfundcode.setter
    def appropriationfundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationfundcode = value

    @property
    def appropriationfundname( self ):
        if isinstance( self.__appropriationfundname, str ) \
                and self.__appropriationfundname != '':
            return self.__appropriationfundname

    @appropriationfundname.setter
    def appropriationfundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationfundname = value

    @property
    def appropriationcreationdate( self ):
        if isinstance( self.__appropriationcreationdate, datetime ):
            return self.__appropriationcreationdate

    @appropriationcreationdate.setter
    def appropriationcreationdate( self, value ):
        if isinstance( value, datetime ):
            self.__appropriationcreationdate = value

    @property
    def appropriationcode( self ):
        if isinstance( self.__appropriationcode, str ) \
                and self.__appropriationcode != '':
            return self.__appropriationcode

    @appropriationcode.setter
    def appropriationcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationcode = value

    @property
    def subappropriationcode( self ):
        if isinstance( self.__subappropriationcode, str ) \
                and self.__subappropriationcode != '':
            return self.__subappropriationcode

    @subappropriationcode.setter
    def subappropriationcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subappropriationcode = value

    @property
    def appropriationdescription( self ):
        if isinstance( self.__appropriationdescription, str ) \
                and self.__appropriationdescription != '':
            return self.__appropriationdescription

    @appropriationdescription.setter
    def appropriationdescription( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriationdescription = value

    @property
    def fundgroup( self ):
        if isinstance( self.__fundgroup, str ) \
                and self.__fundgroup != '':
            return self.__fundgroup

    @fundgroup.setter
    def fundgroup( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundgroup = value

    @property
    def fundgroupname( self ):
        if isinstance( self.__fundgroupname, str ) \
                and self.__fundgroupname != '':
            return self.__fundgroupname

    @fundgroupname.setter
    def fundgroupname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundgroupname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) \
                and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def transtype( self ):
        if isinstance( self.__transtype, str ) \
                and self.__transtype != '':
            return self.__transtype

    @transtype.setter
    def transtype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__transtype = value

    @property
    def actualrecoverytranstype( self ):
        if isinstance( self.__actualrecoverytranstype, str ) \
                and self.__actualrecoverytranstype != '':
            return self.__actualrecoverytranstype

    @actualrecoverytranstype.setter
    def actualrecoverytranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__actualrecoverytranstype = value

    @property
    def commitmentspendingcontrolflag( self ):
        if isinstance( self.__commitmentspendingcontrolflag, str ) \
                and self.__commitmentspendingcontrolflag != '':
            return self.__commitmentspendingcontrolflag

    @commitmentspendingcontrolflag.setter
    def commitmentspendingcontrolflag( self, value ):
        if isinstance( value, str ) and value != '':
            self.__commitmentspendingcontrolflag = value

    @property
    def agreementlimit( self ):
        if isinstance( self.__agreementlimit, str ) \
                and self.__agreementlimit != '':
            return self.__agreementlimit

    @agreementlimit.setter
    def agreementlimit( self, value ):
        if isinstance( value, str ) and value != '':
            self.__agreementlimit = value

    @property
    def estimatedrecoveriestranstype( self ):
        if isinstance( self.__estimatedrecoveriestranstype, str ) \
                and self.__estimatedrecoveriestranstype != '':
            return self.__estimatedrecoveriestranstype

    @estimatedrecoveriestranstype.setter
    def estimatedrecoveriestranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__estimatedrecoveriestranstype = value

    @property
    def estimatedreimbursementstranstype( self ):
        if isinstance( self.__estimatedreimbursementstranstype, str ) \
                and self.__estimatedreimbursementstranstype != '':
            return self.__estimatedreimbursementstranstype

    @estimatedreimbursementstranstype.setter
    def estimatedreimbursementstranstype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__estimatedreimbursementstranstype = value

    @property
    def expensespendingcontrolflag( self ):
        if isinstance( self.__expensespendingcontrolflag, str ) \
                and self.__expensespendingcontrolflag != '':
            return self.__expensespendingcontrolflag

    @expensespendingcontrolflag.setter
    def expensespendingcontrolflag( self, value ):
        if isinstance( value, str ) and value != '':
            self.__expensespendingcontrolflag = value

    @property
    def obligationspendingcontrolflag( self ):
        if isinstance( self.__obligationspendingcontrolflag, str ) \
                and self.__obligationspendingcontrolflag != '':
            return self.__obligationspendingcontrolflag

    @obligationspendingcontrolflag.setter
    def obligationspendingcontrolflag( self, value ):
        if isinstance( value, str ) and value != '':
            self.__obligationspendingcontrolflag = value

    @property
    def precommitmentspendingcontrolflag( self ):
        if isinstance( self.__precommitmentspendingcontrolflag, str ) \
                and self.__precommitmentspendingcontrolflag != '':
            return self.__precommitmentspendingcontrolflag

    @precommitmentspendingcontrolflag.setter
    def precommitmentspendingcontrolflag( self, value ):
        if isinstance( value, str ) and value != '':
            self.__precommitmentspendingcontrolflag = value

    @property
    def postedcontrolflag( self ):
        if isinstance( self.__postedcontrolflag, str ) \
                and self.__postedcontrolflag != '':
            return self.__postedcontrolflag

    @postedcontrolflag.setter
    def postedcontrolflag( self, value ):
        if isinstance( value, str ) and value != '':
            self.__expensespendingcontrolflag = value

    @property
    def postedflag( self ):
        if isinstance( self.__postedflag, str ) and self.__postedflag != '':
            return self.__postedflag

    @postedflag.setter
    def postedflag( self, value ):
        if isinstance( value, str ) and value != '':
            self.__postedflag = value

    @property
    def recordcarryoveratlowerlevel( self ):
        if isinstance( self.__recordcarryoveratlowerlevel, str ) \
                and self.__recordcarryoveratlowerlevel != '':
            return self.__recordcarryoveratlowerlevel

    @recordcarryoveratlowerlevel.setter
    def recordcarryoveratlowerlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recordcarryoveratlowerlevel = value

    @property
    def reimbursablespendingoption( self ):
        if isinstance( self.__reimbursablespendingoption, str ) \
                and self.__reimbursablespendingoption != '':
            return self.__reimbursablespendingoption

    @reimbursablespendingoption.setter
    def reimbursablespendingoption( self, value ):
        if isinstance( value, str ) and value != '':
            self.__reimbursablespendingoption = value

    @property
    def recoveriesoption( self ):
        if isinstance( self.__recoveriesoption, str ) \
                and self.__recoveriesoption != '':
            return self.__recoveriesoption

    @recoveriesoption.setter
    def recoveriesoption( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoveriesoption = value

    @property
    def recoveriesspendingoption( self ):
        if isinstance( self.__recoveriesspendingoption, str ) \
                and self.__recoveriesspendingoption != '':
            return self.__recoveriesspendingoption

    @recoveriesspendingoption.setter
    def recoveriesspendingoption( self, value ):
        if isinstance( value, str ) and value != '':
            self.__recoveriesspendingoption = value

    @property
    def originalbudgetedamount( self ):
        if isinstance( self.__originalbudgetedamount, float ):
            return self.__originalbudgetedamount

    @originalbudgetedamount.setter
    def originalbudgetedamount( self, value ):
        if isinstance( value, float ):
            self.__originalbudgetedamount = value

    @property
    def apportionmentsposted( self ):
        if isinstance( self.__apportionmentsposted, float ):
            return self.__apportionmentsposted

    @apportionmentsposted.setter
    def apportionmentsposted( self, value ):
        if isinstance( value, float ):
            self.__apportionmentsposted = value

    @property
    def totalauthority( self ):
        if isinstance( self.__totalauthority, float ):
            return self.__totalauthority

    @totalauthority.setter
    def totalauthority( self, value ):
        if isinstance( value, float ):
            self.__totalauthority = value

    @property
    def totalbudgeted( self ):
        if isinstance( self.__totalbudgeted, float ):
            return self.__totalbudgeted

    @totalbudgeted.setter
    def totalbudgeted( self, value ):
        if isinstance( value, float ):
            self.__totalbudgeted = value

    @property
    def totalpostedamount( self ):
        if isinstance( self.__totalpostedamount, float ):
            return self.__totalpostedamount

    @totalpostedamount.setter
    def totalpostedamount( self, value ):
        if isinstance( value, float ):
            self.__totalpostedamount = value

    @property
    def fundswithdrawnprioryearamounts( self ):
        if isinstance( self.__fundswithdrawnprioryearamounts, float ):
            return self.__fundswithdrawnprioryearamounts

    @fundswithdrawnprioryearamounts.setter
    def fundswithdrawnprioryearamounts( self, value ):
        if isinstance( value, float ):
            self.__fundswithdrawnprioryearamounts = value

    @property
    def fundinginamount( self ):
        if isinstance( self.__fundinginamount, float ):
            return self.__fundinginamount

    @fundinginamount.setter
    def fundinginamount( self, value ):
        if isinstance( value, float ):
            self.__fundinginamount = value

    @property
    def fundingoutamount( self ):
        if isinstance( self.__fundingoutamount, float ):
            return self.__fundingoutamount

    @fundingoutamount.setter
    def fundingoutamount( self, value ):
        if isinstance( value, float ):
            self.__fundingoutamount = value

    @property
    def totalaccrualrecoveries( self ):
        if isinstance( self.__totalaccrualrecoveries, float ):
            return self.__totalaccrualrecoveries

    @totalaccrualrecoveries.setter
    def totalaccrualrecoveries( self, value ):
        if isinstance( value, float ):
            self.__totalaccrualrecoveries = value

    @property
    def totalactualreimbursements( self ):
        if isinstance( self.__totalactualreimbursements, float ):
            return self.__totalactualreimbursements

    @totalactualreimbursements.setter
    def totalactualreimbursements( self, value ):
        if isinstance( value, float ):
            self.__totalactualreimbursements = value

    @property
    def totalagreementreimbursables( self ):
        if isinstance( self.__totalagreementreimbursables, float ):
            return self.__totalagreementreimbursables

    @totalagreementreimbursables.setter
    def totalagreementreimbursables( self, value ):
        if isinstance( value, float ):
            self.__totalagreementreimbursables = value

    @property
    def totalcarriedforwardin( self ):
        if isinstance( self.__totalcarriedforwardin, float ):
            return self.__totalcarriedforwardin

    @totalcarriedforwardin.setter
    def totalcarriedforwardin( self, value ):
        if isinstance( value, float ):
            self.__totalcarriedforwardin = value

    @property
    def totalcarriedforwardout( self ):
        if isinstance( self.__totalcarriedforwardout, float ):
            return self.__totalcarriedforwardout

    @totalcarriedforwardout.setter
    def totalcarriedforwardout( self, value ):
        if isinstance( value, float ):
            self.__totalcarriedforwardout = value

    @property
    def totalestimatedrecoveries( self ):
        if isinstance( self.__totalestimatedrecoveries, float ):
            return self.__totalestimatedrecoveries

    @totalestimatedrecoveries.setter
    def totalestimatedrecoveries( self, value ):
        if isinstance( value, float ):
            self.__totalestimatedrecoveries = value

    @property
    def totalestimatedreimbursements( self ):
        if isinstance( self.__totalestimatedreimbursements, float ):
            return self.__totalestimatedreimbursements

    @totalestimatedreimbursements.setter
    def totalestimatedreimbursements( self, value ):
        if isinstance( value, float ):
            self.__totalestimatedreimbursements = value

    @property
    def totalexpenses( self ):
        if isinstance( self.__totalexpenses, float ):
            return self.__totalexpenses

    @totalexpenses.setter
    def totalexpenses( self, value ):
        if isinstance( value, float ):
            self.__totalexpenses = value

    @property
    def totalexpenditureexpenses( self ):
        if isinstance( self.__totalexpenditureexpenses, float ):
            return self.__totalexpenditureexpenses

    @totalexpenditureexpenses.setter
    def totalexpenditureexpenses( self, value ):
        if isinstance( value, float ):
            self.__totalexpenditureexpenses = value

    @property
    def totalexpenseaccruals( self ):
        if isinstance( self.__totalexpenseaccruals, float ):
            return self.__totalexpenseaccruals

    @totalexpenseaccruals.setter
    def totalexpenseaccruals( self, value ):
        if isinstance( value, float ):
            self.__totalexpenseaccruals = value

    @property
    def totalprecommitments( self ):
        if isinstance( self.__totalprecommitments, float ):
            return self.__totalprecommitments

    @totalprecommitments.setter
    def totalprecommitments( self, value ):
        if isinstance( value, float ):
            self.__totalprecommitments = value

    @property
    def unliquidatedprecommitments( self ):
        if isinstance( self.__unliquidatedprecommitments, float ):
            return self.__unliquidatedprecommitments

    @unliquidatedprecommitments.setter
    def unliquidatedprecommitments( self, value ):
        if isinstance( value, float ):
            self.__unliquidatedprecommitments = value

    @property
    def totalobligations( self ):
        if isinstance( self.__totalobligations, float ):
            return self.__totalobligations

    @totalobligations.setter
    def totalobligations( self, value ):
        if isinstance( value, float ):
            self.__totalobligations = value

    @property
    def unliquidatedobligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidatedobligations.setter
    def unliquidatedobligations( self, value ):
        if isinstance( value, float ):
            self.__unliquidatedobligations = value

    @property
    def voidedamount( self ):
        if isinstance( self.__voidedamount, float ):
            return self.__voidedamount

    @voidedamount.setter
    def voidedamount( self, value ):
        if isinstance( value, float ):
            self.__voidedamount = value

    @property
    def totalusedamount( self ):
        if isinstance( self.__totalusedamount, float ):
            return self.__totalusedamount

    @totalusedamount.setter
    def totalusedamount( self, value ):
        if isinstance( value, float ):
            self.__totalusedamount = value

    @property
    def availableamount( self ):
        if isinstance( self.__availableamount, float ):
            return self.__availableamount

    @availableamount.setter
    def availableamount( self, value ):
        if isinstance( value, float ):
            self.__availableamount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fund, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfAppropriations
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__appropriationfundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields =[ 'StatusOfAppropriationsId',
                           'BFY',
                           'EFY',
                           'BudgetLevel',
                           'AppropriationFundCode',
                           'AppropriationFundName',
                           'Availability',
                           'TreasurySymbol',
                           'AppropriationCreationDate',
                           'AppropriationCode',
                           'SubAppropriationCode',
                           'AppropriationDescription',
                           'FundGroup',
                           'FundGroupName',
                           'DocumentType',
                           'TransType',
                           'ActualRecoveryTransType',
                           'CommitmentSpendingControlFlag',
                           'AgreementLimit',
                           'EstimatedRecoveriesTransType',
                           'EstimatedReimbursmentsTransType',
                           'ExpenseSpendingControlFlag',
                           'ObligationSpendingControlFlag',
                           'PreCommitmentSpendingControlFlag',
                           'PostedControlFlag',
                           'PostedFlag',
                           'RecordCarryoverAtLowerLevel',
                           'ReimbursableSpendingOption',
                           'RecoveriesOption',
                           'RecoveriesSpendingOption',
                           'OriginalBudgetedAmount',
                           'ApportionmentsPosted',
                           'TotalAuthority',
                           'TotalBudgeted',
                           'TotalPostedAmount',
                           'FundsWithdrawnPriorYearsAmount',
                           'FundingInAmount',
                           'FundingOutAmount',
                           'TotalAccrualRecoveries',
                           'TotalActualReimbursements',
                           'TotalAgreementReimbursables',
                           'TotalCarriedForwardIn',
                           'TotalCarriedForwardOut',
                           'TotalCommitted',
                           'TotalEstimatedRecoveries',
                           'TotalEstimatedReimbursements',
                           'TotalExpenses',
                           'TotalExpenditureExpenses',
                           'TotalExpenseAccruals',
                           'TotalPreCommitments',
                           'UnliquidatedPreCommitments',
                           'TotalObligations',
                           'ULO',
                           'VoidedAmount',
                           'TotalUsedAmount',
                           'AvailableAmount' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'EFY', 'AppropriationFundCode', ]
            v = (self.__bfy, self.__efy, self.__appropriationfundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'StatusOfAppropriations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'StatusOfAppropriations'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# SpendingRates( account, provider = Provider.SQLite )
class SpendingRates( ):
    '''SpendingRates( code ) initializes
    object providing OMB spending rate data'''
    __source = None
    __provider = None
    __spendingratesid = None
    __ombagencycode = None
    __ombagencyname = None
    __treasuryagencycode = None
    __treasuryagencyname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __ombaccountcode = None
    __ombaccountname = None
    __ombaccounttitle = None
    __subfunction = None
    __linenumber = None
    __linename = None
    __category = None
    __subcategory = None
    __subcategoryname = None
    __jurisdiction = None
    __yearofauthority = None
    __budgetauthority = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __outyear10 = None
    __outyear11 = None
    __totalspendout = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__spendingratesid, int ):
            return self.__spendingratesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__spendingratesid = value

    @property
    def treasuryagencycode( self ):
        if isinstance( self.__treasuryagencycode, str ) and self.__treasuryagencycode != '':
            return self.__treasuryagencycode

    @treasuryagencycode.setter
    def treasuryagencycode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryagencycode = value

    @property
    def treasuryagencyname( self ):
        if isinstance( self.__treasuryagencyname, str ) and self.__treasuryagencyname != '':
            return self.__treasuryagencyname

    @treasuryagencyname.setter
    def treasuryagencyname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryagencyname = value

    @property
    def treasuryaccountcode( self ):
        if isinstance( self.__treasuryaccountcode, str ) and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasuryaccountcode.setter
    def treasuryaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountcode = value

    @property
    def treasuryaccountname( self ):
        if isinstance( self.__treasuryaccountname, str ) and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasuryaccountname.setter
    def treasuryaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountname = value

    @property
    def ombagencycode( self ):
        if isinstance( self.__ombagencycode, str ) and self.__ombagencycode != '':
            return self.__ombagencycode

    @ombagencycode.setter
    def ombagencycode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombagencycode = value

    @property
    def ombagencyname( self ):
        if isinstance( self.__ombagencyname, str ) and self.__ombagencyname != '':
            return self.__ombagencyname

    @ombagencyname.setter
    def ombagencyname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombagencyname = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def subfunction( self ):
        if isinstance( self.__subfunction, str ) and self.__subfunction != '':
            return self.__subfunction

    @subfunction.setter
    def subfunction( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subfunction = value

    @property
    def category( self ):
        if isinstance( self.__category, str ) and self.__category != '':
            return self.__category

    @category.setter
    def category( self, value ):
        if isinstance( value, str ) and value != '':
            self.__category = value

    @property
    def subcategory( self ):
        if isinstance( self.__subcategory, str ) and self.__subcategory != '':
            return self.__subcategory

    @subcategory.setter
    def subcategory( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subcategory = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def linename( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @linename.setter
    def linename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linename = value

    @property
    def yearofauthority( self ):
        if isinstance( self.__yearofauthority, str ) and self.__yearofauthority != '':
            return self.__yearofauthority

    @yearofauthority.setter
    def yearofauthority( self, value ):
        if isinstance( value, str ) and value != '':
            self.__yearofauthority = value

    @property
    def budgetauthority( self ):
        if isinstance( self.__budgetauthority, float ):
            return self.__budgetauthority

    @budgetauthority.setter
    def budgetauthority( self, value ):
        if isinstance( value, float ):
            self.__budgetauthority = value

    @property
    def outyear1( self ):
        if isinstance( self.__outyear1, float ):
            return self.__outyear1

    @outyear1.setter
    def outyear1( self, value ):
        if isinstance( value, float ):
            self.__outyear1 = value

    @property
    def outyear2( self ):
        if isinstance( self.__outyear2, float ):
            return self.__outyear2

    @outyear2.setter
    def outyear2( self, value ):
        if isinstance( value, float ):
            self.__outyear2 = value

    @property
    def outyear3( self ):
        if isinstance( self.__outyear3, float ):
            return self.__outyear3

    @outyear3.setter
    def outyear3( self, value ):
        if isinstance( value, float ):
            self.__outyear3 = value

    @property
    def outyear4( self ):
        if isinstance( self.__outyear4, float ):
            return self.__outyear4

    @outyear4.setter
    def outyear4( self, value ):
        if isinstance( value, float ):
            self.__outyear4 = value

    @property
    def outyear5( self ):
        if isinstance( self.__outyear5, float ):
            return self.__outyear5

    @outyear5.setter
    def outyear5( self, value ):
        if isinstance( value, float ):
            self.__outyear5 = value

    @property
    def outyear6( self ):
        if isinstance( self.__outyear6, float ):
            return self.__outyear6

    @outyear6.setter
    def outyear6( self, value ):
        if isinstance( value, float ):
            self.__outyear6 = value

    @property
    def outyear7( self ):
        if isinstance( self.__outyear7, float ):
            return self.__outyear7

    @outyear7.setter
    def outyear7( self, value ):
        if isinstance( value, float ):
            self.__outyear7 = value

    @property
    def outyear8( self ):
        if isinstance( self.__outyear8, float ):
            return self.__outyear8

    @outyear8.setter
    def outyear8( self, value ):
        if isinstance( value, float ):
            self.__outyear8 = value

    @property
    def outyear9( self ):
        if isinstance( self.__outyear9, float ):
            return self.__outyear9

    @outyear9.setter
    def outyear9( self, value ):
        if isinstance( value, float ):
            self.__outyear9 = value

    @property
    def outyear10( self ):
        if isinstance( self.__outyear10, float ):
            return self.__outyear10

    @outyear10.setter
    def outyear10( self, value ):
        if isinstance( value, float ):
            self.__outyear10 = value

    @property
    def outyear11( self ):
        if isinstance( self.__outyear11, float ):
            return self.__outyear11

    @outyear11.setter
    def outyear11( self, value ):
        if isinstance( value, float ):
            self.__outyear11 = value

    @property
    def totalspendout( self ):
        if isinstance( self.__totalspendout, float ):
            return self.__totalspendout

    @totalspendout.setter
    def totalspendout( self, value ):
        if isinstance( value, float ):
            self.__totalspendout = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SpendingRates
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'SpendingRatesId',
                          'OmbAgencyCode',
                          'OmbAgencyName',
                          'OmbBureauCode',
                          'OmbBureauName',
                          'TreausuryAgencyCode',
                          'TreausuryAccountCode',
                          'TreausuryAccountName',
                          'AccountTitle',
                          'Subfunction',
                          'Line',
                          'LineNumber',
                          'Category',
                          'Subcategory',
                          'SubcategoryName',
                          'AccountCode',
                          'Jurisdiction',
                          'YearOfAuthority',
                          'BudgetAuthority',
                          'OutYear1',
                          'OutYear2',
                          'OutYear3',
                          'OutYear4',
                          'OutYear5',
                          'OutYear6',
                          'OutYear7',
                          'OutYear8',
                          'OutYear9',
                          'OutYear10',
                          'OutYear11',
                          'TotalSpendout' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            command = SQL.SELECTALL
            names = [ 'OmbAccountCode', ]
            values = ( self.__ombaccountcode, )
            data = DataBuilder( provider, source, command, names, values )
            self.__data = data.createtable( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'SpendingRates'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'SpendingRates'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# StatusOfSupplementalFunds( bfy, efy, fundcode, provider = Provider.SQLite )
class StatusOfSupplementalFunds( ):
    __statusofsupplementalfundsid = None
    __source = None
    __provider = None
    __fields = None
    __data = None
    __frame = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None

    @property
    def id( self ):
        if isinstance( self.__statusofsupplementalfundsid, int ):
            return self.__statusofsupplementalfundsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__statusofsupplementalfundsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfSupplementalFunding
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields =[ 'StatusOfSupplementalFundsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitments',
                           'ULO',
                           'Expenditures',
                           'Obligations',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]


# StatusOfJobsActFunding( bfy, efy, fundcode, provider = Provider.SQLite )
class StatusOfJobsActFunding( ):
    __source = None
    __provider = None
    __statusofjobsactfundingid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __fields = None
    __data  = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofjobsactfundingid, int ):
            return self.__statusofjobsactfundingid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__statusofjobsactfundingid= value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__provider = provider
        self.__source = Source.StatusOfJobsActFunding
        self.__fields = [ 'StatusOfJobsActFundingId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'NpmCode',
                           'NpmName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitments',
                           'ULO',
                           'Expenditures',
                           'Obligations',
                           'Used',
                           'Available' ]


# StatusOfEarmarks( bfy, efy, fundcode, provider = Provider.SQLite )
class StatusOfEarmarks( ):
    __source = None
    __provider = None
    __statusofearmarksid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __fields = None
    __data  = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__statusofearmarksid, int ):
            return self.__statusofearmarksid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__statusofearmarksid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__provider = provider
        self.__source = Source.StatusOfEarmarks
        self.__fields = [ 'StatusOfEarmarksId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'NpmCode',
                           'NpmName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitments',
                           'ULO',
                           'Expenditures',
                           'Obligations',
                           'Used',
                           'Available' ]


# SiteActivity( bfy, rpio, provider = Provider.SQLite  )
class SiteActivity( ):
    '''provides data on superfund site spending'''
    __source = None
    __provider = None
    __siteactivityid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __city = None
    __siteprojectcode = None
    __stieprojectname = None
    __ssid = None
    __actioncode = None
    __operableunit = None
    __congress = None
    __startdate = None
    __enddate = None
    __lastactivitydate = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __foccode = None
    __focname = None
    __requested = None
    __accepted = None
    __closed = None
    __outstanding = None
    __refunded = None
    __reversal = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteactivityid, int ):
            return self.__siteactivityid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__siteactivityid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def epasiteid( self ):
        if isinstance( self.__epasiteid, str ) and self.__epasiteid != '':
            return self.__epasiteid

    @epasiteid.setter
    def epasiteid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__epasiteid = value

    @property
    def projecttype( self ):
        if isinstance( self.__projecttype, str ) and self.__projecttype != '':
            return self.__projecttype

    @projecttype.setter
    def projecttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__projecttype = value

    @property
    def siteprojectcode( self ):
        if isinstance( self.__siteprojectcode, str ) and self.__siteprojectcode != '':
            return self.__siteprojectcode

    @siteprojectcode.setter
    def siteprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__siteprojectcode = value

    @property
    def siteprojectname( self ):
        if isinstance( self.__siteprojectname, str ) and self.__siteprojectname != '':
            return self.__siteprojectname

    @siteprojectname.setter
    def siteprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__siteprojectname = value

    @property
    def ssid( self ):
        if isinstance( self.__ssid, str ) and self.__ssid != '':
            return self.__ssid

    @ssid.setter
    def ssid( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ssid = value

    @property
    def actioncode( self ):
        if isinstance( self.__actioncode, str ) and self.__actioncode != '':
            return self.__actioncode

    @actioncode.setter
    def actioncode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__actioncode = code

    @property
    def operableunit( self ):
        if isinstance( self.__operableunit, str ) and self.__operableunit != '':
            return self.__operableunit

    @operableunit.setter
    def operableunit( self, value ):
        if isinstance( value, str ) and value != '':
            self.__operableunit = value

    @property
    def state( self ):
        if isinstance( self.__state, str ) and self.__state != '':
            return self.__state

    @state.setter
    def state( self, value ):
        if isinstance( value, str ) and value != '':
            self.__state = value

    @property
    def city( self ):
        if isinstance( self.__city, str ) and self.__city != '':
            return self.__city

    @city.setter
    def city( self, value ):
        if isinstance( value, str ) and value != '':
            self.__city = value

    @property
    def congress( self ):
        if isinstance( self.__congress, str ) and self.__congress != '':
            return self.__congress

    @congress.setter
    def congress( self, value ):
        if isinstance( value, str ) and value != '':
            self.__congress = value

    @property
    def startdate( self ):
        if isinstance( self.__startdate, str ) and self.__startdate != '':
            return self.__startdate

    @startdate.setter
    def startdate( self, value ):
        if isinstance( value, str ) and value != '':
            self.__startdate = value

    @property
    def enddate( self ):
        if isinstance( self.__enddate, str ) and self.__enddate != '':
            return self.__enddate

    @enddate.setter
    def enddate( self, value ):
        if isinstance( value, str ) and value != '':
            self.__enddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, str ) and self.__lastactivitydate != '':
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, str ) and value != '':
            self.__lastactivitydate = value

    @property
    def requested( self ):
        if isinstance( self.__requested, float ):
            return self.__requested

    @requested.setter
    def requested( self, value ):
        if isinstance( value, float ):
            self.__requested = value

    @property
    def accepted( self ):
        if isinstance( self.__accepted, float ):
            return self.__accepted

    @accepted.setter
    def accepted( self, value ):
        if isinstance( value, float ):
            self.__accepted = value

    @property
    def closed( self ):
        if isinstance( self.__closed, float ):
            return self.__closed

    @closed.setter
    def closed( self, value ):
        if isinstance( value, float ):
            self.__closed = value

    @property
    def refunded( self ):
        if isinstance( self.__refunded, float ):
            return self.__refunded

    @refunded.setter
    def refunded( self, value ):
        if isinstance( value, float ):
            self.__refunded = value

    @property
    def reversal( self ):
        if isinstance( self.__reversal, float ):
            return self.__reversal

    @reversal.setter
    def reversal( self, value ):
        if isinstance( value, float ):
            self.__reversal = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, rpio = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SiteActivity
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None
        self.__fields = [ 'SiteActivityId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'FundCode',
                           'FundName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'BocCode',
                           'BocName',
                           'OrgCode',
                           'OrgName',
                           'FocCode',
                           'FocName',
                           'EpaSiteId',
                           'SiteProjectCode',
                           'SSID',
                           'ActionCode',
                           'OperableUnit',
                           'SiteProjectName',
                           'State',
                           'City',
                           'CongressionalDistrict',
                           'ProjectType',
                           'StartDate',
                           'LastActivity',
                           'EndDate',
                           'Requested',
                           'Accepted',
                           'Closed',
                           'Outstanding',
                           'Refunded',
                           'Reversal' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'RpioCode' ]
            v = (self.__bfy, self.__rpiocode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SiteActivity'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'SiteActivity'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# TreasurySymbols( bfy, efy, code, provider = Provider.SQLite )
class TreasurySymbols( ):
    '''TreasurySymbol( value )
    creates object that represents a TAFS'''
    __source = None
    __provider = None
    __treasurysymbolsid = None
    __ombagencycode = None
    __treasuryagencycode = None
    __bfy = None
    __efy = None
    __ombaccountcode = None
    __ombaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__treasurysymbolsid, int ):
            return self.__treasurysymbolsid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__treasurysymbolsid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def treasuryaccountcode( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasuryaccountcode.setter
    def treasuryaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountcode = value

    @property
    def treasuryaccountname( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasuryaccountname.setter
    def treasuryaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccountname = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__soruce = Source.FundSymbols
        self.__bfy = bfy if isinstance( bfy, str ) else None
        self.__efy = efy if isinstance( efy, str ) else None
        self.__treasuryaccountcode = code if isinstance( code, str ) else None
        self.__fields = [ 'TreasurySymbolsId',
                          'BFY',
                          'EFY',
                          'FundCode',
                          'FundName',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'ApportionmentAccountCode' ]

    def __str__( self ):
        if isinstance( self.__treasuryaccountname, str ) and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            command = SQL.SELECTALL
            n = [ 'BFY', 'EFY', 'TreasuryAccountCode' ]
            v = (self.__bfy, self.__efy, self.__treasuryaccountcode)
            dbcfg = DbConfig( source, provider )
            sqlcfg = SqlConfig( names = n, values = v )
            cnx = Connection( dbcfg )
            sql = SqlStatement( dbcfg, sqlcfg )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'TreasurySymbol'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'TreasurySymbol'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# Transfer( documentnumber, provider = Provider.SQLite )
class Transfer( ):
    ''' Transfer( documentnumber ) initializes object
    representing EPA reprogrammings'''
    __source = None
    __provider = None
    __transfersid = None
    __documenttype = None
    __documentnumber = None
    __processeddate = None
    __budgetlevel = None
    __rpiocode = None
    __rpioname = None
    __bfy = None
    __efy = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__transfersid, int ):
            return self.__transfersid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__transfersid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__efy = value

    @property
    def budgetlevel( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != '':
            return self.__budgetlevel

    @budgetlevel.setter
    def budgetlevel( self, value ):
        if isinstance( value, str ) and value != '':
            self.__budgetlevel = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpioname.setter
    def rpioname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def activitycode( self ):
        if isinstance( self.__activitycode, str ) and self.__activitycode != '':
            return self.__activitycode

    @activitycode.setter
    def activitycode( self, value ):
        if isinstance( value, str ) and self.__activitycode != '':
            self.__activitycode = value

    @property
    def activityname( self ):
        if isinstance( self.__activityname, str ) and self.__activityname != '':
            return self.__activityname

    @activityname.setter
    def activityname( self, value ):
        if isinstance( value, str ) and self.__activityname != '':
            self.__activityname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, documentnumber, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Transfers
        self.__documentnumber = documentnumber if isinstance( documentnumber, str ) else None
        self.__fields = [ 'TransfersId',
                           'BudgetLevel',
                           'DocPrefix',
                           'DocType',
                           'BFY',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'ReprogrammingNumber',
                           'ControlNumber',
                           'ProcessedDate',
                           'Quarter',
                           'Line',
                           'Subline',
                           'AhCode',
                           'AhName',
                           'OrgCode',
                           'OrgName',
                           'RcCode',
                           'RcName',
                           'AccountCode',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'ProgramProjectName',
                           'ProgramProjectCode',
                           'FromTo',
                           'BocCode',
                           'BocName',
                           'NpmCode',
                           'Amount',
                           'ResourceType',
                           'Purpose',
                           'ExtendedPurpose' ]

    def getdata( self ):
        try:
            src = self.__source
            pdr = self.__provider
            command = SQL.SELECTALL
            n = [ 'DocumentNumber', ]
            v = (self.__documentnumber,)
            dconfig = DbConfig( source = src, provider = pdr )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Transfer'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'Transfer'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# TransType( bfy, fundcode, provider = Provider.SQLite )
class TransType( ):
    __source = None
    __provider = None
    __transtypesid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __doctype = None
    __appropriationbill = None
    __continuingresolution = None
    __rescissioncurrentyear = None
    __rescissionprioryear = None
    __sequesterreduction = None
    __sequesterreturn = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__transtypesid, int ):
            return self.__transtypesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__transtypesid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def appropriation( self ):
        if isinstance( self.__appropriation, str ) and self.__appropriation != '':
            return self.__appropriation

    @appropriation.setter
    def appropriation( self, value ):
        if isinstance( value, str ) and value != '':
            self.__appropriation = value

    @property
    def treasurysymbol( self ):
        if isinstance( self.__treasuryaccount, str ) and self.__treasuryaccount != '':
            return self.__treasuryaccount

    @treasurysymbol.setter
    def treasurysymbol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, fundcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.TransTypes
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'TransTypesId',
                          'FundCode',
                          'Appropriation',
                          'BFY',
                          'EFY',
                          'TreasurySymbol',
                          'DocType',
                          'AppropriationBill',
                          'ContinuingResolution',
                          'RescissionCurrentYear',
                          'RescissionPriorYear',
                          'SequesterReduction',
                          'SequesterReturn' ]


# UnobligatedAuthority( account, provider = Provider.SQLite )
class UnobligatedAuthority( ):
    '''UnobligatedAuthority( bfy, omb )
    object provides OMB data'''
    __source = None
    __provider = None
    __unobligatedauthorityid = None
    __reportyear = None
    __ombaccountcode = None
    __ombaccountname = None
    __ombaccounttitle = None
    __linenumber = None
    __linename = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__unobligatedauthorityid, int ):
            return self.__unobligatedauthorityid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__unobligatedauthorityid = value

    @property
    def reportyear( self ):
        if isinstance( self.__reportyear, str ) and len( self.__reportyear ) == 4:
            return self.__reportyear

    @reportyear.setter
    def reportyear( self, value ):
        if isinstance( value, str ) and len( value ) == 4:
            self.__reportyear = value

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linenumber = value

    @property
    def linename( self ):
        if isinstance( self.__linename, str ) and self.__linename != '':
            return self.__linename

    @linename.setter
    def linename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__linename = value

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountcode = value

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ombaccountname = value

    @property
    def prioryear( self ):
        if isinstance( self.__prioryear, float ):
            return self.__prioryear

    @prioryear.setter
    def prioryear( self, value ):
        if isinstance( value, float ):
            self.__prioryear = value

    @property
    def currentyear( self ):
        if isinstance( self.__currentyear, float ):
            return self.__currentyear

    @currentyear.setter
    def currentyear( self, value ):
        if isinstance( value, float ):
            self.__currentyear = value

    @property
    def budgetyear( self ):
        if isinstance( self.__budgetyear, float ):
            return self.__budgetyear

    @budgetyear.setter
    def budgetyear( self, value ):
        if isinstance( value, float ):
            self.__budgetyear = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnobligatedAuthority
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None
        self.__fields = [ 'UnobligatedAuthorityId',
                          'ReportYear',
                          'AgencyCode',
                          'BureauCode',
                          'AccountCode',
                          'OmbAccount',
                          'OmbAccountName',
                          'LineName',
                          'LineNumber',
                          'BudgetYear',
                          'PriorYear',
                          'CurrentYear',
                          'AgencyName',
                          'BureauName' ]

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'OmbAccountCode', ]
            v = (self.__ombaccountcode,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedAuthority'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedAuthority'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# UnobligatedBalance( bfy, efy, fundcode, provider = Provider.SQLite )
class UnobligatedBalances( ):
    '''object provides OMB data on unobligated
    balances by Fund Code and General Ledger Account'''
    __source = None
    __provider = None
    __unobligatedbalancesid = None
    __bfy = None
    __efy = None
    __treasurysymbol = None
    __fundcode = None
    __fundname = None
    __accountnumber = None
    __accountname = None
    __amount = None
    __fields = None
    __frame = None
    __data = None

    @property
    def id( self ):
        if isinstance( self.__unobligatedbalancesid, int ):
            return self.__unobligatedbalancesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__unobligatedbalancesid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def accountnumber( self ):
        if isinstance( self.__accountnumber, str ) and self.__accountnumber != '':
            return self.__accountnumber

    @accountnumber.setter
    def accountnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountnumber = value

    @property
    def accountname( self ):
        if isinstance( self.__accountname, str ) and self.__accountname != '':
            return self.__accountname

    @accountname.setter
    def accountname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountname = value

    @property
    def treasurysymbol( self ):
        if isinstance( self.__treasuryaccount, str ) and self.__treasuryaccount != '':
            return self.__treasuryaccount

    @treasurysymbol.setter
    def treasurysymbol( self, value ):
        if isinstance( value, str ) and value != '':
            self.__treasuryaccount = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy, efy, fundcode, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnobligatedBalances
        self.__bfy = bfy if isinstance( bfy, str ) and bfy != '' else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields =[ 'UnobligatedBalancesId',
                           'BudgetYear',
                           'BFY',
                           'EFY',
                           'TreasurySymbol',
                           'FundCode',
                           'FundName',
                           'AccountNumber',
                           'AccountName',
                           'Amount' ]

    def getdata( self ):
        try:
            source = Source.CarryoverOutlays
            provider = Provider.SQLite
            n = [ 'BFY', 'EFY', 'FundCode' ]
            v = (self.__bfy, self.__efy, self.__fundcode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedBalances'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Reporting'
            exc.cause = 'UnobligatedBalances'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# UnliquidatedObligation( bfy, fund, account, boc, provider = Provider.SQLite )
class UnliquidatedObligation( ):
    '''UnliquidatedObligation( bfy, fund, account, boc )
    initializes object providing ULO data'''
    __source = None
    __provider = None
    __unliquidatedobligationsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__expendituresid = value

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bfy = value

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value ):
        if isinstance( value, str ) and value != '':
            self.__efy = value

    @property
    def rpiocode( self ):
        if isinstance( self.__rpiocode, str ) and self.__rpiocode != '':
            return self.__rpiocode

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rpiocode = value

    @property
    def ahcode( self ):
        if isinstance( self.__ahcode, str ) and self.__ahcode != '':
            return self.__ahcode

    @ahcode.setter
    def ahcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahcode = value

    @property
    def ahname( self ):
        if isinstance( self.__ahname, str ) and self.__ahname != '':
            return self.__ahname

    @ahname.setter
    def ahname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__ahname = value

    @property
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundcode = value

    @property
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__fundname = value

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgcode = value

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__orgname = value

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

    @accountcode.setter
    def accountcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountcode = value

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__boccode = value

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__bocname = value

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rcname = value

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documenttype = value

    @property
    def documentnumber( self ):
        if isinstance( self.__documentnumber, str ) and self.__documentnumber != '':
            return self.__documentnumber

    @documentnumber.setter
    def documentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentnumber = value

    @property
    def documentcontrolnumber( self ):
        if isinstance( self.__documentcontrolnumber, str ) and self.__documentcontrolnumber != '':
            return self.__documentcontrolnumber

    @documentcontrolnumber.setter
    def documentcontrolnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__documentcontrolnumber = value

    @property
    def referencedocumentnumber( self ):
        if isinstance( self.__referencedocumentnumber,
                str ) and self.__referencedocumentnumber != '':
            return self.__referencedocumentnumber

    @referencedocumentnumber.setter
    def referencedocumentnumber( self, value ):
        if isinstance( value, str ) and value != '':
            self.__referencedocumentnumber = value

    @property
    def processeddate( self ):
        if isinstance( self.__processeddate, datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ):
        if isinstance( self.__age, int ):
            return self.__age

    @age.setter
    def age( self, value ):
        if isinstance( value, int ):
            self.__age = value

    @property
    def vendorcode( self ):
        if isinstance( self.__vendorcode, str ) and self.__vendorcode != '':
            return self.__vendorcode

    @vendorcode.setter
    def vendorcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorcode = value

    @property
    def vendorname( self ):
        if isinstance( self.__vendorname, str ) and self.__vendorname != '':
            return self.__vendorname

    @vendorname.setter
    def vendorname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__vendorname = value

    @property
    def foccode( self ):
        if isinstance( self.__foccode, str ) and self.__foccode != '':
            return self.__foccode

    @foccode.setter
    def foccode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rccode = value

    @property
    def focname( self ):
        if isinstance( self.__focname, str ) and self.__focname != '':
            return self.__focname

    @focname.setter
    def focname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__focname = value

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def programprojectcode( self ):
        if isinstance( self.__programprojectcode, str ) and self.__programprojectcode != '':
            return self.__programprojectcode

    @programprojectcode.setter
    def programprojectcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectcode = value

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programprojectname = value

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareacode = value

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__programareaname = value

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalcode = value

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__goalname = value

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @objectivecode.setter
    def objectivecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivecode = value

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__objectivename = value

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmcode = value

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @npmname.setter
    def npmname( self, value ):
        if isinstance( value, str ) and value != '':
            self.__npmname = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnliquidatedObligations
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'UnliquidatedObligationsId'
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitments',
                           'Obligations',
                           'ULO',
                           'Expenditures' ]

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            v = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'UnliquidatedObligations'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Control'
            exc.cause = 'UnliquidatedObligations'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )


# WorkCode( code, provider = Provider.SQLite )
class WorkCode( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __workcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__workcodesid, int ):
            return self.__workcodesid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__workcodesid = value

    @property
    def code( self ):
        if isinstance( self.__code, str) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, value ):
        if isinstance( value, str ) and value != '':
            self.__code = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, value ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ):
        if isinstance( self.__frame, DataFrame ):
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, DataFrame ):
            self.__frame = value

    @property
    def fields( self ):
        if isinstance( self.__fields, list ) and len( self.__fields ) > 0:
            return self.__fields

    @fields.setter
    def fields( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.WorkCodes
        self.__code = code if isinstance( code, str ) else None
        self.__frame = DataFrame
        self.__fields = None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        try:
            source = self.__source
            provider = self.__provider
            n = [ 'Code', ]
            v = (self.__code,)
            dconfig = DbConfig( source, provider )
            sconfig = SqlConfig( names = n, values = v )
            cnx = Connection( dconfig )
            sql = SqlStatement( dconfig, sconfig )
            sqlite = cnx.connect( )
            cursor = sqlite.cursor( )
            query = sql.getcommandtext( )
            data = cursor.execute( query )
            self.__data =  [ i for i in data.fetchall( ) ]
            cursor.close( )
            sqlite.close( )
            return self.__data
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'WorkCode'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getframe( self ):
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            src = self.__source
            data = BudgetData( src )
            return data.getframe( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Execution'
            exc.cause = 'WorkCode'
            exc.method = 'getframe( self )'
            err = ErrorDialog( exc )
            err.show( )

