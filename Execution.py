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


# Account( code  )
class Account( ):
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

    def __init__( self, code ):
        self.__source = Source.Accounts
        self.__provider = Provider.SQLite
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


# Activity( code   )
class Activity( ):
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

    def __init__( self, code ):
        self.__source = Source.ActivityCodes
        self.__provider = Provider.SQLite
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


# AllowanceHolder( code   )
class AllowanceHolder( ):
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

    def __init__( self, code ):
        self.__source = Source.AllowanceHolders
        self.__provider = Provider.SQLite
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


# Appropriation( code   )
class Appropriation( ):
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


# Appropriation( code   )
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

    def __init__( self, code ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
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


# BudgetFiscalYear( bfy, efy, date = None )
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

    def __init__( self, bfy, efy, date = None ):
        self.__source  = Source.FiscalYears
        self.__provider = Provider.SQLite
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



# BudgetObjectClass( code  )
class BudgetObjectClass( ):
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

    def __init__( self, code ):
        self.__source = Source.BudgetObjectClasses
        self.__provider = Provider.SQLite
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



# FinanceObjectClass( code  )
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

    def __init__( self, code ):
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



# Fund( bfy, efy, code )
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
            self.__fundsid

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
        if isinstance( self.__multiyearindicator) \
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
        if isinstance( self.__applyatalllevels, str ) and self.__applyatalllevels != '':
            return self.__applyatalllevels

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

    def __init__( self, bfy, efy, code ):
        self.__source = Source.Funds
        self.__provider = Provider.SQLite
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



# Goal( code )
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

    def __init__( self, code ):
        self.__source = Source.Goals
        self.__provider = Provider.SQLite
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



# NationalProgram( code value )
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

    def __init__( self, code ):
        self.__source = Source.NationalPrograms
        self.__provider = Provider.SQLite
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



# Objective( code  )
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

    def __init__( self, code ):
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



# Organization( code  )
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

    def __init__( self, code ):
        self.__source = Source.Organizations
        self.__provider = Provider.SQLite
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


# Project( code  )
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

    def __init__( self, code ):
        self.__source = Source.Projects
        self.__provider = Provider.SQLite
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



# CapitalPlanningInvestmentCode( code  )
class CapitalPlanningInvestmentCode( ):
    '''Defines the Organization Class'''
    __source = None
    __provider = None
    __cpicid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__cpicid, int ):
            return self.__cpicid

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

    def __init__( self, code ):
        self.__source = Source.CPIC
        self.__provider = Provider.SQLite
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



# SiteProjectCode( code  )
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

    def __init__( self, code ):
        self.__source = Source.SiteProjectCodes
        self.__provider = Provider.SQLite
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



# StateOrganization( code  )
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

    def __init__( self, code ):
        self.__source = Source.StateOrganizations
        self.__provider = Provider.SQLite
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



# HeadquartersOffice( code  )
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

    def __init__( self, code ):
        self.__source = Source.HeadquartersOffices
        self.__provider = Provider.SQLite
        self.__rpiocode = code if isinstance( code, str ) and len( code ) == 2 else None
        self.__fields = [ 'HeadquartersOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]


    def __str__( self ):
        if isinstance( self.__code ):
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



# HumanResourceOrganization( code  )
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

    def __init__( self, code ):
        self.__source = Source.HumanResourceOrganizations
        self.__provider = Provider.SQLite
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



# ProgramArea( code  )
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

    def __init__( self, code ):
        self.__source = Source.ProgramAreas
        self.__provider = Provider.SQLite
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



# ProgramProject( code  )
class ProgramProject( ):
    '''Defines the ProgramProject Class'''
    __source = None
    __provider = None
    __programprojectsid = None
    __code = None
    __name = None
    __description = None
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
    def description( self ):
        if isinstance( self.__description, str ) and self.__description != '':
            return self.__description

    @description.setter
    def description( self, value ):
        if isinstance( value, str ) and value != '':
            self.__description = value

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

    def __init__( self, code ):
        self.__source = Source.ProgramProjects
        self.__provider = Provider.SQLite
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ProgramProjectId',
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
            exc.cause = 'ProgramProject'
            exc.method = 'getdata( self )'
            err = ErrorDialog( exc )
            err.show( )



# ResponsibilityCenter( code  )
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

    def __init__( self, code ):
        self.__source = Source.ResponsibilityCenters
        self.__provider = Provider.SQLite
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResponsibilityCentersId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ):
        if isinstance( self.__code ) and self.__code != '':
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



# ResourcePlanningOffice( code  )
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

    def __init__( self, code ):
        self.__source = Source.ResourcePlanningOffices
        self.__provider = Provider.SQLite
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResourcePlanningOfficesId',
                          'Code',
                          'Name' ]

    def __str__( self ):
        if isinstance( self.__code ) and self.__code != '':
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


# ProgramResultsCode( bfy, efy, rpio, ah, account, boc )
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
                  account = None, boc = None, amount = 0.0 ):
        '''Initializes the PRC class'''
        self.__source = Source.Allocations
        self.__provider = Provider.SQLite
        self.__accountcode = account
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__rpiocode = rpio
        self.__ahcode = ah
        self.__boccode = boc
        self.__amount = amount
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
        if isinstance( self.__code ) and self.__code != '':
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


# RegionalOffice( code  )
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

    def __init__( self, code ):
        self.__source = Source.ResourcePlanningOffices
        self.__provider = Provider.SQLite
        self.__rpiocode = code if isinstance( code, str ) and len( code ) == 2 else None
        self.__fields = [ 'RegionalOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]

    def __str__( self ):
        if isinstance( self.__code ):
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


# SiteProject( code  )
class SiteProject( ):
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

    def __init__( self, code ):
        self.__source = Source.SiteProjectCodes
        self.__provider = Provider.SQLite
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



# FederalHoliday( bfy, name )
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

    def __init__( self, bfy, name ):
        self.__source = Source.FederalHolidays
        self.__provider = Provider.SQLite
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


# TreasurySymbol( bfy, efy, code )
class TreasurySymbol( ):
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

    def __init__( self, bfy, efy, code ):
        self.__soruce = Source.FundSymbols
        self.__provider = Provider.SQLite
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



class PayrollCostCode( ):
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

    def __init__( self ):
        self.__source = Source.PayrollCostCodes
        self.__provider = Provider.SQLite
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



# WorkCode( code )
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

    def __init__( self, code ):
        self.__source = Source.WorkCodes
        self.__provider = Provider.SQLite
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



# Transfer( documentnumber )
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

    def __init__( self, rpnumber = None ):
        self.__source = Source.Transfers
        self.__provider = Provider.SQLite
        self.__documentnumber = rpnumber if isinstance( rpnumber, str ) else None
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



# CostArea( code )
class CostArea( ):
    __source = None
    __provider = None
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

    def __init__( self ):
        self.__fields = [ 'CostAreasId',
                          'Code',
                          'Name' ]
