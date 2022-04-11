import datetime as dt
import pandas as pd
from enum import Enum, auto
from collections import namedtuple as ntuple
from Ninja import *


class BOC( Enum ):
    '''Enumeration of object class codes'''
    NS = 0
    PAYROLL = 10
    FTE = 17
    EXPENSES = 36
    CONTRACTS = 37
    WCF = 38
    GRANTS = 41


class NPM( Enum ):
    '''Enumeration of NPM Codes'''
    NS = auto( )
    A = auto( )
    B = auto( )
    C = auto( )
    D = auto( )
    E = auto( )
    F = auto( )
    H = auto( )
    J = auto( )
    M = auto( )


class Unit( ):
    '''Unit( name, value ) initializes object
    representing fundemental unit of data
    in the Budget Execution application'''
    __id = None

    @property
    def id( self ):
        if isinstance( self.__index, int ):
            return self.__index

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__index = id

    def __init__( self, id ):
        self.__id = id if isinstance( id, int ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Element( Unit ):
    '''Element class represents fundemental program unit'''
    __id = None
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


class Account( ):
    '''defines the Account Code class'''
    __accountsid = None
    __code = None
    __name = None
    __goal = None
    __objective = None
    __npm = None
    __programproject = None
    __record = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__accountsid, int ):
            return self.__accountsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

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
    def goal( self ):
        if isinstance( self.__goal, str ):
            return self.__goal

    @goal.setter
    def goal( self, goal ):
        if isinstance( goal, str ):
            self.__goal = goal
            self.__record[ 'goal' ] = self.__goal

    @property
    def objective( self ):
        if isinstance( self.__objective, str ):
            return self.__objective

    @objective.setter
    def objective( self, obj ):
        if obj is not None:
            self.__objective = str( obj )
            self.__record[ 'objective' ] = self.__objective

    @property
    def npm( self ):
        if self.__npm is not None:
            return self.__npm

    @npm.setter
    def npm( self, code ):
        if isinstance( code, str ):
            self.__npm = code
            self.__record[ 'npm' ] = self.__npm

    @property
    def programproject( self ):
        if isinstance( self.__programproject, str ):
            return self.__programproject

    @programproject.setter
    def programproject( self, code ):
        if isinstance( code, str ):
            self.__programproject = code
            self.__record[ 'programproject' ] = self.__programproject

    @property
    def data( self ):
        if isinstance( self.__record, list ):
            return self.__record

    @data.setter
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__record = cache

    @property
    def table( self ):
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__goal = self.__code[ 0 ]
        self.__objective = self.__code[ 1:3 ]
        self.__npm = self.__code[ 3 ]
        self.__programproject = self.__code[ 4:6 ]

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Accounts
        command = Command.SELECT
        names = [ 'Code', ]
        values = ( self.__code, )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


class Activity( ):
    '''Defines the Activity Class'''
    __activitycodesid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__activitycodesid, int ):
            return self.__activitycodesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__activitycodesid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__data = self.getdata( )

    def getdata( self ):
        names = [ 'Code', ]
        values = ( self.__code, )
        sqlconfig = SqlConfig( Command.SELECTALL, names, values )
        dbconfig = DataConfig( Source.ActivityCodes, Provider.SQLite )
        connection = DataConnection( dbconfig )
        sql = SqlStatement( dbconfig, sqlconfig )
        query = SQLiteQuery( connection, sql )
        self.__data = query.getdata( )
        return self.__data

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class AllowanceHolder( ):
    '''Defines the AllowanceHolder Class'''
    __allowancholdersid = None
    __code = None
    __name = None
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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( self.__code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Appropriation( ):
    '''Defines the Appropriation Class'''
    __appropriationsid = None
    __fund = None
    __code = None
    __name = None
    __title = None
    __bfy = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__appropriationsid , int ):
            return self.__appropriationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__appropriationsid  = id

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
    def fiscalyear( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @fiscalyear.setter
    def fiscalyear( self, bfy ):
        if isinstance( bfy, str) and bfy != '':
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if isinstance( code, str ) and code != '':
            self.__fund = Fund( code )

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, title ):
        if isinstance( title, str ) and title != '':
            self.__title = title

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__fund = Fund( self.__code )

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class BudgetFiscalYear( ):
    '''Class to describe the federal fiscal year'''
    __budgetfiscalyearid = None
    __base = None
    __bfy = None
    __efy = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = 0
    __workdays = 0
    __year = None
    __month = None
    __day = None
    __holidays = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__budgetfiscalyearid, int ):
            return self.__budgetfiscalyearid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__budgetfiscalyearid = id

    @property
    def startyear( self ):
        if isinstance( self.__base, str ) and self.__bfy != '':
            return self.__bfy

    @startyear.setter
    def startyear( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__bfy = yr

    @property
    def endyear( self ):
        if isinstance( self.__efy, str) and self.__efy != '':
            return self.__efy

    @endyear.setter
    def endyear( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__efy = yr

    @property
    def calendaryear( self ):
        if isinstance( self.__year, int ):
            return self.__year

    @calendaryear.setter
    def calendaryear( self, cyr ):
        if isinstance( cyr, int ):
            self.__year = cyr

    @property
    def startdate( self ):
        if isinstance( self.__startdate, dt.datetime ):
            return self.__startdate

    @startdate.setter
    def startdate( self, start ):
        if isinstance( start, dt.datetime ):
            self.__startdate = start

    @property
    def enddate( self ):
        if isinstance( self.__enddate, dt.datetime ):
            return self.__enddate

    @enddate.setter
    def enddate( self, end ):
        if isinstance( end, dt.datetime ):
            self.__enddate = end

    @property
    def expiration( self ):
        if isinstance( self.__expiration, dt.datetime):
            return self.__expiration

    @expiration.setter
    def expiration( self, exp ):
        if isinstance( exp, dt.datetime ):
            self.__expiration = exp

    @property
    def weekends( self ):
        if isinstance( self.__weekends, int ):
            return self.__weekends

    @weekends.setter
    def weekends( self, end ):
        if isinstance( end, int ):
            self.__weekends = end

    @property
    def workdays( self ):
        if isinstance( self.__workdays, float ):
            return self.__workdays

    @workdays.setter
    def workdays( self, work ):
        if isinstance( work, float ):
            self.__workdays = work

    @property
    def date( self ):
        if isinstance( self.__date, dt.datetime ):
            return self.__date

    @date.setter
    def date( self, today ):
        if isinstance( today, dt.datetime ):
            self.__date = today

    @property
    def day( self ):
        if isinstance( self.__day, int ):
            return self.__day

    @day.setter
    def day( self, today ):
        if isinstance( today, int ):
            self.__day = today

    @property
    def month( self ):
        if isinstance( self.__month, int ):
            return self.__month

    @property
    def holidays( self ):
        if isinstance( self.__holidays, list ):
            return self.__holidays

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, bfy ):
        self.__today = dt.datetime.today()
        self.__date = self.__today
        self.__base = bfy if isinstance( bfy, str ) else str( self.__today.year )
        self.__year = int( self.__base ) if isinstance( self.__base, str ) else None
        self.__day = self.__date.day
        self.__month = self.__date.month
        self.__startdate = dt.datetime( self.__year, 10, 1 ) if isinstance( self.__year, int ) else None
        self.__bfy = bfy if isinstance( bfy, str ) else str( self.__today.year )
        self.__enddate = dt.datetime( self.__year + 1, 9, 30 ) if isinstance( self.__year, int ) else None
        self.__efy = str( self.__enddate.year ) if isinstance( self.__enddate, dt.datetime ) else None
        self.__frame = pd.DataFrame
        self.__holidays = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                            'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                            'Memorial', 'Juneteenth', 'Independence', 'Labor' ]

    def __str__( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy


class BudgetObjectClass( ):
    '''Defines the BudgetObjectClass Class'''
    __budgetobjectclassesid = None
    __code = None
    __boc = None
    __name = None
    __value = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__accountsid, int ):
            return self.__accountsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

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
    def value( self ):
        if isinstance( self.__value, object ):
            return self.__value

    @value.setter
    def value( self, val ):
        if isinstance( val, object ):
            self.__value = val

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, boc ):
        self.__boc = boc if isinstance( boc, BOC ) else BOC.NS
        self.__code = self.__boc.value
        self.__name = self.__boc.name
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Division( ):
    '''Defines the Division Class'''
    __code = None
    __name = None
    __data = None

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

    def __init__( self, code ):
        self.__code =  code if isinstance( code, str ) else None
        self.__data = { 'fund': self.__code }

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class FinanceObjectClass( ):
    '''Defines the Finance Object Class'''
    __financeobjectclassesid = None
    __code = None
    __name = None
    __data = None
    __frame = Nonec

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
            self.__code = ode

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Fund( ):
    '''Defines the Fund Class'''
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
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__fundsid, int ):
            self.__fundsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__fundsid = id

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
    def shortname( self ):
        if isinstance( self.__title, str ) and self.__title != '':
            return self.__title

    @title.setter
    def shortname( self, title ):
        if isinstance( title , str ) and title != '':
            self.__title = title

    @property
    def status( self ):
        if isinstance( self.__status, str ) and self.__status != '':
            return self.__status

    @status.setter
    def status( self, stat ):
        if isinstance( stat, str ) and stat in [ 'ACTIVE', 'INACTIVE' ]:
            self.__status = stat

    @property
    def BPOA( self ):
        if isinstance( self.__bpoa, str ) and self.__bpoa != '':
            return self.__bpoa

    @BPOA.setter
    def BPOA( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__bpoa = yr
    @property
    def EPOA( self ):
        if isinstance( self.__epoa, str ) and self.__epoa != '':
            return self.__epoa

    @EPOA.setter
    def EPOA( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__epoa = yr
    @property
    def main( self ):
        if isinstance( self.__main, str ) and self.__main != '':
            return self.__main

    @main.setter
    def main( self, code ):
        if isinstance( code, str ) and code != '':
           self.__main = code

    @property
    def multiyearindicator( self ):
        if isinstance( self.__multiyearindicator) \
                and self.__multiyearindicator != '':
            return self.__multiyearindicator

    @multiyearindicator.setter
    def multiyearindicator( self, multi ):
        if isinstance( multi, str ) and multi != '':
            self.__multiyearindicator = multi

    @property
    def sublevel( self ):
        if isinstance( self.__sublevel, str ) and self.__sublevel != '':
            return self.__sublevel

    @sublevel.setter
    def sublevel( self, sub ):
        if isinstance( sub, str ) and sub != '':
            self.__sublevel = sub
    @property
    def ATA( self ):
        if isinstance( self.__ata, str ) and self.__ata != '':
            return self.__ata

    @ATA.setter
    def ATA( self, ata ):
        if isinstance( ata, str ) and ata != '':
            self.__ata = ata

    @property
    def AID( self ):
        if isinstance( self.__aid, str ) and self.__aid != '':
            return self.__aid

    @AID.setter
    def AID( self, aid ):
        if isinstance( aid, str ) and aid != '':
            self.__aid = aid

    @property
    def fundcategory( self ):
        if isinstance( self.__fundcategory, str ) and self.__fundcategory != '':
            return self.__fundcategory

    @fundcategory.setter
    def fundcategory( self, catg ):
        if isinstance( catg, str ) and catg != '':
            self.__fundcategory = catg

    @property
    def appropriationcode( self ):
        if isinstance( self.__appropriationcode, str ) \
                and self.__appropriationcode != '':
            return self.__appropriationcode

    @appropriationcode.setter
    def appropriationcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__appropriationcode = code

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
    def fundgroup( self, group ):
        if isinstance( group, str ) and group != '':
            self.__fundgroup = group

    @property
    def noyear( self ):
        if isinstance( self.__noyear, str ) and self.__noyear != '':
            return self.__noyear

    @noyear.setter
    def noyear( self, noyr ):
        if isinstance( noyr, str ) and noyr != '':
            self.__noyear = noyr

    @property
    def carryover( self ):
        if isinstance( self.__carryover, str ) and self.__carryover != '':
            return self.__carryover

    @carryover.setter
    def carryover( self, carry ):
        if isinstance( carry, str ) and carry != '':
            self.__carryover = carry

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
    def applyatalllevels( self, all ):
        if isinstance( self.__applyatalllevels, str ) and self.__applyatalllevels != '':
            return self.__applyatalllevels

    @property
    def batsfund( self ):
        if isinstance( self.__batsfund, str ) and self.__batsfund != '':
            return self.__batsfund

    @batsfund.setter
    def batsfund( self, bats ):
        if isinstance( bats, str ) and bats != '':
            self.__batsfund = bats

    @property
    def batsenddate( self ):
        if isinstance( self.__batsenddate, dt.datetime ):
            return self.__batsenddate

    @batsenddate.setter
    def batsenddate( self, end):
        if isinstance( end, dt.datetime ):
            self.__batsenddate = end

    @property
    def batsoptionid( self ):
        if isinstance( self.__batsoptionid, int ):
            return self.__batsoptionid

    @batsoptionid.setter
    def batsoptionid( self, optid ):
        if isinstance( optid, int ):
            self.__batsoptionid = optid

    @property
    def securityorg( self ):
        if isinstance( self.__securityorg, str ) and self.__securityorg != '':
            return self.__securityorg

    @securityorg.setter
    def securityorg( self, sec ):
        if isinstance( sec, str ) and sec != '':
            self.__securityorg = sec

    @property
    def treasuryaccountcode( self ):
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasuryaccountcode.setter
    def treasuryaccountcode( self, tres ):
        if isinstance( tres, str ) and tres != '':
            self.__treasuryaccountcode = tres

    @property
    def treasuryaccountname( self ):
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasuryaccountname.setter
    def treasuryaccountname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__treasuryaccountname = name

    @property
    def ombaccountcode( self ):
        if isinstance( self.__ombaccountcode, str ) and self.__ombaccountcode != '':
            return self.__ombaccountcode

    @ombaccountcode.setter
    def ombaccountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__ombaccountcode = code

    @property
    def ombaccountname( self ):
        if isinstance( self.__ombaccountname, str ) and self.__ombaccountname != '':
            return self.__ombaccountname

    @ombaccountname.setter
    def ombaccountname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__ombaccountname = name

    @property
    def apportionmentaccountcode( self ):
        if isinstance( self.__apportionmentaccountcode, str ) \
                and self.__apportionmentaccountcode != '':
            return self.__apportionmentaccountcode

    @apportionmentaccountcode.setter
    def apportionmentaccountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__apportionmentaccountcode = code

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Goal( ):
    '''Defines the Goal Class'''
    __goalsid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__goalsid, int ):
            return self.__goalsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__goalsid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class NationalProgram( ):
    '''Defines the NationalProgram Class'''
    __nationalprogramsid = None
    __code = None
    __name = None
    __rpio = None
    __title = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__nationalprogramsid, int ):
            return self.__nationalprogramsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__nationalprogramsid = id

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
    def rpio( self ):
        if isinstance( self.__rpio, str ) and self.__rpio != '':
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpio = code

    @property
    def title( self ):
        if isinstance( self.__title, str ) and self.__title != '':
            return self.__title

    @title.setter
    def title( self, name ):
        if isinstance( name, str ) and name != '':
            self.__title = name

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Objective( ):
    '''Defines the Objective Class'''
    __objectivesid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__objectivesid, int ):
            return self.__objectivesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__objectivesid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = Objective( str( code ) )
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Organization( ):
    '''Defines the Organization Class'''
    __organizationsid = None
    __code = None
    __name = None
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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class Project( ):
    '''Defines the Organization Class'''
    __projectsid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__projectsid, int ):
            return self.__projectsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class ItProjectCode( ):
    '''Defines the Organization Class'''
    __cpicid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__cpicid, int ):
            return self.__cpicid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class SiteProjectCode( ):
    '''Defines the Organization Class'''
    __siteprojectcodesid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteprojectcodesid, int ):
            return self.__siteprojectcodesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__siteprojectcodesid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class StateOrganization( ):
    '''StateOrganization( fgrp ) class
    representing state codes'''
    __stateorganizationsid = None
    __code = None
    __name = None
    __orgcode = None
    __rpiocode = None
    __rpioname = None
    __data = None

    @property
    def id( self ):
        if isinstance( self.__stateorganizationsid, int ):
            return self.__stateorganizationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__stateorganizationsid = id

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

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class HumanResourceOrganization( ):
    '''Defines the Organization Class'''
    __humanresourceorganizationsid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__humanresourceorganizationsid, int ):
            return self.__humanresourceorganizationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__humanresourceorganizationsid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class WorkCode( ):
    '''Defines the Organization Class'''
    __workcodesid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__workcodesid, int ):
            return self.__workcodesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__workcodesid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class ProgramArea( ):
    '''defines the ProgramArea class'''
    __programareasid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__programareasid, int ):
            return self.__programareasid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class ProgramProject( ):
    '''Defines the ProgramProject Class'''
    __programprojectsid = None
    __code = None
    __name = None
    __description = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__programprojectsid , int ):
            return self.__programprojectsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__programprojectsid  = id

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
    def description( self ):
        if isinstance( self.__description, str ) and self.__description != '':
            return self.__description

    @description.setter
    def description( self, text ):
        if isinstance( text, str ) and text != '':
            self.__description = text

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code


class ResponsibilityCenter( ):
    '''Defines the ResponsibilityCenter Class'''
    __responsibilitycentersid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__responsibilitycentersid, int ):
            return self.__responsibilitycentersid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code ) and self.__code != '':
            return self.__code


class ResourcePlanningOffice( ):
    '''defines the ResponsiblePlanningOffice class'''
    __resourceplanningofficesid = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__resourceplanningofficesid = id

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code ) and self.__code != '':
            return self.__code


class ProgramResultsCode( ):
    '''Defines the PRC class'''
    __allocationsid = None
    __rpio = None
    __bfy = None
    __ah = None
    __fund = None
    __org = None
    __account = None
    __activity = None
    __rc = None
    __boc = None
    __amount = None
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
    def rpio( self ):
        if isinstance( self.__rpio, ResourcePlanningOffice ):
            return self.__rpio

    @rpio.setter
    def rpio( self, rp ):
        if isinstance( rp, ResourcePlanningOffice ):
            self.__rpio = rp

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, BudgetFiscalYear ):
            self.__bfy = year

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fu ):
        if isinstance( fu, Fund ):
            self.__fund = fu

    @property
    def ah( self ):
        if isinstance( self.__ah, AllowanceHolder ):
            return self.__ah

    @ah.setter
    def ah( self, ah ):
        if isinstance( ah, AllowanceHolder ):
            self.__ah = ah

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, acct ):
        if isinstance( acct, Account ):
            self.__account = acct

    @property
    def activity( self ):
        if isinstance( self.__activity, Activity ):
            return self.__activity

    @activity.setter
    def activity( self, act ):
        if isinstance( act, Activity ):
            self.__activity = act

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organziation):
            self.__org = org

    @property
    def rc( self ):
        if isinstance( self.__rc, ResponsibilityCenter ):
            return self.__rc

    @rc.setter
    def rc( self, rcc ):
        if isinstance( rcc, ResponsibilityCenter ):
            self.__rc = rcc

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code, amount = 0 ):
        '''Initializes the PRC class'''
        self.__account = Account( str( code ) )
        self.__bfy = BudgetFiscalYear( dt.datetime.year )
        self.__amount = amount
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code ) and self.__code != '':
            return self.__code


class RegionalOffice( ):
    '''Defines a regional RPIO'''
    __resourceplanningofficesid = None
    __rpio = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.___resourceplanningofficesid = id

    @property
    def rpio( self ):
        if isinstance( self.__rpio, ResourcePlanningOffice ):
            return self.__rpio

    @rpio.setter
    def rpio( self, rpo ):
        if isinstance( rpo, ResourcePlanningOffice ):
            self.__rpio = rpo

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, rpio ):
        self.__rpio = rpio if isinstance( rpio, ResourcePlanningOffice ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__code ):
            return self.__code


class SiteProject( ):
    '''Defines the Site Project Code Class'''
    __siteprojectcodesid = None
    __epaid = None
    __ssid = None
    __actioncode = None
    __operableunit = None
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteprojectcodesid, int ):
            return self.___siteprojectcodesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__siteprojectcodesid = id

    @property
    def ssid( self ):
        if isinstance( self.__ssid, str ) and self.__ssid != '':
            return self.__ssid

    @ssid.setter
    def ssid( self, ssid ):
        if isinstance( ssid, str ) and ssid != '':
            self.__ssid = ssid

    @property
    def actioncode( self ):
        if isinstance( self.__actioncode, str ):
            return self.__actioncode

    @actioncode.setter
    def actioncode( self, code ):
        if isinstance( self.__actioncode, str ) and self.__actioncode != '':
            self.__actioncode = code

    @property
    def operableunit( self ):
        if isinstance( self.__operableunit, str ) and self.__operableunit != '':
            return self.__operableunit

    @operableunit.setter
    def operableunit( self, unit ):
        if isinstance( unit, str ) and unit != '':
            self.__operableunit =  unit

    @property
    def epaid( self ):
        if isinstance( self.__epaid, str ) and self.__epaid != '':
            return self.__epaid

    @epaid.setter
    def epaid( self, eid ):
        if isinstance( eid, str ) and eid != '':
            self.__epaid =  eid

    @property
    def code( self ):
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    @code.setter
    def code( self, code ):
        if isinstance( code, str ) and code != '':
            self.__code = code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, code ):
        self.__code = str( code )
        self.__ssid = self.__code[ 0: 4 ]
        self.__actioncode = self.__code[ 4:6 ]
        self.__operableunit = self.__code[ 6:9 ]
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__name, str ):
            return self.__name


class HeadquartersOffice( ):
    '''Defines the HQ class'''
    __resourceplanningofficesid = None
    __rpio = None
    __name = None
    __title = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__resourceplanningofficesid, int ):
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if code is not None:
            self.__rpio = str( code )
            self.__data[ 'rpio' ] = ResourcePlanningOffice( self.__rpio )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, title ):
        if title is not None:
            self.__title = str( title )
            self.__data[ 'title' ] = self.__title

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, rpio ):
        self.__rpio = rpio if isinstance( rpio, str ) else None

    def __str__( self ):
        if isinstance( self.__rpio, str ):
            return self.__rpio


class FederalHoliday( ):
    '''Defines the FederalHoliday class'''
    __federalholidaysid = None
    __bfy = None
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__federalholidaysid, int ):
            return self.__accountsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__accountsid = id

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = str( year )
            self.__data[ 'bfy' ] = self.__bfy

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name in self.__list:
            self.__name = name

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
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__data = cache

    @property
    def list( self ):
        if self.__list is not None:
            return self.__list

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    @property
    def observance( self ):
        if self.__observance is not None:
            return self.__observance

    def columbusday( self ):
        '''The second Monday in October'''
        if self.__year is not None:
            __start = dt.datetime( self.__year, 10, 1 )
            __end = dt.datetime( self.__year, 10, 31 )
            __delta = ( __start - __end ).days
            for i in range( 1, 31 ):
                d = dt.datetime( self.__year, 10, __start.day + i )
                if ( 15 < d.day < 28 ) and dt.datetime( self.__year, 10, d.day ).isoweekday( ) == 1:
                    self.__columbus = dt.datetime( self.__year, 10, d.day )
                    return self.__columbus

    def veteransday( self ):
        '''Veterans Day, November 11'''
        if self.__year is not None:
            self.__veterans = dt.datetime( self.__year, 11, 11 )
            return self.__veterans

    def thanksgivingday( self ):
        '''The fourth Thursday in November'''
        if self.__year is not None:
            __start = dt.datetime( self.__year, 11, 15 )
            __end = dt.datetime( self.__year, 11, 30 )
            __delta = ( __start - __end ).days
            for i in range( 15, 31 ):
                d = dt.datetime( self.__year, 11, i )
                if ( 21 < d.day < 31 ) and dt.datetime( self.__year, 11, d.day ).isoweekday( ) == 4:
                    self.__thanksgiving = dt.datetime( self.__year, 11, d.day )
                    return self.__thanksgiving

    def christmasday( self ):
        '''Christmas Day, December 25'''
        if self.__year is not None:
            self.__christmas = dt.datetime( self.__year, 12, 25 )
            return self.__christmas

    def newyearsday( self ):
        '''January 1'''
        if self.__year is not None:
            self.__newyearsday = dt.datetime( self.__year, 1, 1 )
            return self.__newyearsday

    def martinlutherkingday( self ):
        '''The third Monday in January'''
        if self.__year is not None:
            __start = dt.datetime( self.__year, 1, 15 )
            __end = dt.datetime( self.__year, 1, 31 )
            __delta = ( __start - __end ).days
            for i in range( __delta ):
                d = dt.datetime( self.__year, 1, __start.day + i )
                if ( 15 < d.day < 31) and dt.datetime( self.__year, 1, d.day ).isoweekday( ) == 1:
                    self.__martinlutherking = dt.datetime( self.__year, 1, d.day )
                    return self.__martinlutherking

    def washingtonsday( self ):
        '''The third Monday in February'''
        if self.__year is not None:
            __start = dt.datetime( self.__year, 2, 15 )
            __end = dt.datetime( self.__year, 2, 28 )
            __delta = ( __start - __end ).days
            for i in range( __delta ):
                d = dt.datetime( self.__year, 2, __start.day + i )
                if (15 < d.day < 28) and dt.datetime( self.__year, 2, d.day ).isoweekday( ) == 1:
                    self.__washingtons = dt.datetime( self.__year, 2, d.day )
                    return self.__washingtons

    def memorialday( self ):
        '''The last Monday in May'''
        if self.__year is not None:
            __start = dt.datetime( self.__year, 5, 1 )
            __end = dt.datetime( self.__year, 5, 31 )
            __delta = ( __start - __end ).days
            for i in range( 15, 31 ):
                d = dt.datetime( self.__year, 5, i )
                if ( 21 < d.day < 31 ) and dt.datetime( self.__year, 5, d.day ).isoweekday( ) == 1:
                    self.__memorial = dt.datetime( self.__year, 5, d.day )
                    return self.__memorial

    def juneteenthday( self ):
        '''Juneteenth National Independence Day, June 19'''
        if self.__year is not None:
            self.__juneteenth = dt.datetime( self.__year, 6, 19 )
            return self.__juneteenth

    def independence( self ):
        '''Independence Day, July 4'''
        if self.__year is not None:
            self.__independence = dt.datetime( self.__year, 7, 4 )
            return self.__independence

    def laborday( self ):
        '''The first Monday in September'''
        if self.__year is not None:
            __monday = list( )
            __month = dt.date( self.__year, 9, 1 ) - dt.date( self.__year, 9, 31 )
            for i in range( 1, __month.days - 1 ):
                if dt.datetime( self.__year, 9, i ).isoweekday( ) == 1:
                    __monday.append( dt.datetime( self.__year, 9, i ) )
            y = __monday[ 0 ].date( ).year
            m = __monday[ 0 ].date( ).month
            d = __monday[ 0 ].date( ).day
            self.__labor = dt.datetime( y, m, d )
            return self.__labor

    def dayofweek( self ):
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

    def isweekday( self ):
        if 1 <= self.__date.isoweekday() <= 5:
            return True
        else:
            return False

    def isweekend( self ):
        if 5 < self.__date.isoweekday() <= 7:
            return True
        else:
            return False

    def setdate( self, name ):
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

    def setname( self, name ):
        if isinstance( name, str ) and name in self.__list:
            self.__name = name
            return self.__name
        else:
            self.__name = 'NS'
            return self.__name

    def __str__( self ):
        if not self.__name == '':
            return self.__name

    def __init__( self, bfy, name ):
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
        self.__data = { 'bfy': self.__bfy,
                        'name': self.__name }
        self.__frame = pd.DataFrame


class OperatingPlan( ):
    '''object representing Operating plan allocations'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class FullTimeEquivalent( ):
    '''object representing Operating Plan FTE'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class StatusOfFunds( ):
    '''Object representing exeuction data'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class Defacto( ):
    '''object representing defacto obligations'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class StatusOfAppropriations( ):
    '''object representing Appropriation-level execution data'''
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
    __agreementlimit = None
    __estimatedrecoveriestranstype = None
    __estimatedreimbursementstranstype = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __postedcontrolflag = None
    __postedflag= None
    __recordcarryoveratlowerlevel = None
    __reimbursablespendingoption = None
    __recoveriesoption = None
    __recoveriesspendingoption = None
    __originalbudgetedamount = None
    __apportionmentsposted = None
    __totalauthority = None
    __totalbudgeted = None
    __totalpostedamount = None
    __fundswithdrawnprioryearsamount = None
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
    __totaleexpenseaccruals = None
    __totaleprecommitments = None
    __unliquidatedprecommitments = None
    __totalobligations = None
    __unliquidatedobligations = None
    __voidedamount = None
    __totalusedamount = None
    __availableamount = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__efy = year

    @property
    def budgetlevel( self ):
        if isinstance( self.__budgetlevel, str ) and self.__budgetlevel != '':
            return self.__budgetlevel

    @budgetlevel.setter
    def budgetlevel( self, level ):
        if isinstance( level, str ) and level != '':
            self.__budgetlevel = level

    @property
    def appropriationfundcode( self ):
        if isinstance( self.__appropriationfundcode, str ) \
                and self.__appropriationfundcode != '':
            return self.__appropriationfundcode

    @appropriationfundcode.setter
    def appropriationfundcode( self, code ):
        if isinstance( code, str ) and code != '':
           self.__appropriationfundcode = code

    @property
    def appropriationfundname( self ):
        if isinstance( self.__appropriationfundname, str ) \
                and self.__appropriationfundname != '':
            return self.__appropriationfundname

    @appropriationfundname.setter
    def appropriationfundname( self, name ):
        if isinstance( name, str ) and name != '':
           self.__appropriationfundname = name

    @property
    def appropriationcreationdate( self ):
        if isinstance( self.__appropriationcreationdate, dt.datetime ):
            return self.__appropriationcreationdate

    @appropriationcreationdate.setter
    def appropriationcreationdate( self, date ):
        if isinstance( date, dt.datetime ):
           self.__appropriationcreationdate = date

    @property
    def appropriationcode( self ):
        if isinstance( self.__appropriationode, str ) \
                and self.__appropriationcode != '':
            return self.__appropriationode

    @appropriationode.setter
    def appropriationcode( self, code ):
        if isinstance( code, str ) and code != '':
           self.__appropriationcode = code

    @property
    def subappropriationcode( self ):
        if isinstance( self.__subappropriationode, str ) \
                and self.__subappropriationcode != '':
            return self.__subappropriationode

    @subappropriationode.setter
    def subappropriationcode( self, code ):
        if isinstance( code, str ) and code != '':
           self.__subappropriationcode = code

    @property
    def appropriationdescription( self ):
        if isinstance( self.__appropriationdescription, str ) \
                and self.__appropriationdescription != '':
            return self.__appropriationdescription

    @appropriationdescription.setter
    def appropriationdescription( self, desc ):
        if isinstance( desc, str ) and desc != '':
           self.__appropriationdescription = de

    @property
    def fundgroup( self ):
        if isinstance( self.__fundgroup, str ) \
                and self.__fundgroup != '':
            return self.__fundgroup

    @fundgroup.setter
    def fundgroup( self, fgrp ):
        if isinstance( fgrp, str ) and fgrp != '':
            self.__fundgroup = fgrp

    @property
    def fundgroupname( self ):
        if isinstance( self.__fundgroupname, str ) \
                and self.__fundgroupname != '':
            return self.__fundgroupname

    @fundgroupname.setter
    def fundgroupname( self, fgrp ):
        if isinstance( fgrp, str ) and fgrp != '':
            self.__fundgroupname = fgrp

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) \
                and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, dtyp ):
        if isinstance( dtyp, str ) and dtyp != '':
            self.__documenttype = dtyp

    @property
    def transtype( self ):
        if isinstance( self.__transtype, str ) \
                and self.__transtype != '':
            return self.__transtype

    @transtype.setter
    def transtype( self, ttyp ):
        if isinstance( ttyp, str ) and ttyp != '':
            self.__transtype = ttyp

    @property
    def actualrecoverytranstype( self ):
        if isinstance( self.__actualrecoverytranstype, str ) \
                and self.__actualrecoverytranstype != '':
            return self.__actualrecoverytranstype

    @actualrecoverytranstype.setter
    def actualrecoverytranstype( self, artyp ):
        if isinstance( artyp, str ) and artyp != '':
            self.__actualrecoverytranstype = artyp

    @property
    def commitmentspendingcontrolflag( self ):
        if isinstance( self.__commitmentspendingcontrolflag, str ) \
                and self.__commitmentspendingcontrolflag != '':
            return self.__commitmentspendingcontrolflag

    @commitmentspendingcontrolflag.setter
    def commitmentspendingcontrolflag( self, csflag ):
        if isinstance( csflag, str ) and csflag != '':
            self.__commitmentspendingcontrolflag = csflag

    @property
    def agreementlimit( self ):
        if isinstance( self.__agreementlimit, str ) \
                and self.__agreementlimit != '':
            return self.__agreementlimit

    @agreementlimit.setter
    def agreementlimit( self, lim ):
        if isinstance( lim, str ) and lim != '':
            self.__agreementlimit = lim

    @property
    def estimatedrecoveriestranstype( self ):
        if isinstance( self.__estimatedrecoveriestranstype, str ) \
                and self.__estimatedrecoveriestranstype != '':
            return self.__estimatedrecoveriestranstype

    @estimatedrecoveriestranstype.setter
    def estimatedrecoveriestranstype( self, ttyp ):
        if isinstance( ttyp, str ) and ttyp != '':
            self.__estimatedrecoveriestranstype = ttyp

    @property
    def estimatedreimbursementstranstype( self ):
        if isinstance( self.__estimatedreimbursementstranstype, str ) \
                and self.__estimatedreimbursementstranstype != '':
            return self.__estimatedreimbursementstranstype

    @estimatedreimbursementstranstype.setter
    def estimatedreimbursementstranstype( self, etyp ):
        if isinstance( etyp, str ) and etyp != '':
            self.__estimatedreimbursementstranstype = etyp

    @property
    def expensespendingcontrolflag( self ):
        if isinstance( self.__expensespendingcontrolflag, str ) \
                and self.__expensespendingcontrolflag != '':
            return self.__expensespendingcontrolflag

    @expensespendingcontrolflag.setter
    def expensespendingcontrolflag( self, esflag ):
        if isinstance( esflag, str ) and esflag != '':
            self.__expensespendingcontrolflag = esflag

    @property
    def obligationspendingcontrolflag( self ):
        if isinstance( self.__obligationspendingcontrolflag, str ) \
                and self.__obligationspendingcontrolflag != '':
            return self.__obligationspendingcontrolflag

    @obligationspendingcontrolflag.setter
    def obligationspendingcontrolflag( self, oflag ):
        if isinstance( oflag, str ) and oflag != '':
            self.__obligationspendingcontrolflag = oflag

    @property
    def precommitmentspendingcontrolflag( self ):
        if isinstance( self.__precommitmentspendingcontrolflag, str ) \
                and self.__precommitmentspendingcontrolflag != '':
            return self.__precommitmentspendingcontrolflag

    @precommitmentspendingcontrolflag.setter
    def precommitmentspendingcontrolflag( self, pflag ):
        if isinstance( pflag, str ) and pflag != '':
            self.__precommitmentspendingcontrolflag = pflag

    @property
    def postedcontrolflag( self ):
        if isinstance( self.__postedcontrolflag, str ) \
                and self.__postedcontrolflag != '':
            return self.__postedcontrolflag

    @postedcontrolflag.setter
    def postedcontrolflag( self, pcflag ):
        if isinstance( pcflag, str ) and pcflag != '':
            self.__expensespendingcontrolflag = pcflag

    @property
    def postedflag( self ):
        if isinstance( self.__postedflag, str ) and self.__postedflag != '':
            return self.__postedflag

    @postedflag.setter
    def postedflag( self, flag ):
        if isinstance( flag, str ) and flag != '':
            self.__postedflag = flag

    @property
    def recordcarryoveratlowerlevel( self ):
        if isinstance( self.__recordcarryoveratlowerlevel, str ) \
                and self.__recordcarryoveratlowerlevel != '':
            return self.__recordcarryoveratlowerlevel

    @recordcarryoveratlowerlevel.setter
    def recordcarryoveratlowerlevel( self, ttyp ):
        if isinstance( ttyp, str ) and ttyp != '':
            self.__recordcarryoveratlowerlevel = ttyp

    @property
    def reimbursablespendingoption( self ):
        if isinstance( self.__reimbursablespendingoption, str ) \
                and self.__reimbursablespendingoption != '':
            return self.__reimbursablespendingoption

    @reimbursablespendingoption.setter
    def reimbursablespendingoption( self, ttyp ):
        if isinstance( ttyp, str ) and ttyp != '':
            self.__reimbursablespendingoption = ttyp

    @property
    def recoveriesoption( self ):
        if isinstance( self.__recoveriesoption, str ) \
                and self.__recoveriesoption != '':
            return self.__recoveriesoption

    @recoveriesoption.setter
    def recoveriesoption( self, ttyp ):
        if isinstance( ttyp, str ) and ttyp != '':
            self.__recoveriesoption = ttyp

    @property
    def recoveriesspendingoption( self ):
        if isinstance( self.__recoveriesspendingoption, str ) \
                and self.__recoveriesspendingoption != '':
            return self.__recoveriesspendingoption

    @recoveriesspendingoption.setter
    def recoveriesspendingoption( self, ttyp ):
        if isinstance( ttyp, str ) and ttyp != '':
            self.__recoveriesspendingoption = ttyp

    @property
    def originalbudgetedamount( self ):
        if isinstance( self.__originalbudgetedamount, float ):
            return self.__originalbudgetedamount

    @originalbudgetedamount.setter
    def originalbudgetedamount( self, amount  ):
        if isinstance( amount , float):
            self.__originalbudgetedamount = amount

    @property
    def apportionmentsposted( self ):
        if isinstance( self.__apportionmentsposted, float ):
            return self.__apportionmentsposted

    @apportionmentsposted.setter
    def apportionmentsposted( self, amount  ):
        if isinstance( amount , float ):
            self.__apportionmentsposted = amount

    @property
    def totalauthority( self ):
        if isinstance( self.__totalauthority, float ):
            return self.__totalauthority

    @totalauthority.setter
    def totalauthority( self, amount ):
        if isinstance( amount, float ):
            self.__totalauthority = amount


class StatusOfSupplementalFunds( ):
    '''object representing Supplemental Funds execution data'''
    __statusofSupplementalfundsid = None
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class StateGrantObligations( ):
    '''object representing the BIS'''
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
    __accoutcode = None
    __rcccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __statecode = None
    __statename = None
    __amount = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

    @property
    def statecode( self ):
        if isinstance( self.__statecode, str ) and self.__statecode != '':
            return self.__statecode

    @statecode.setter
    def statecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__statecode = code

    @property
    def statename( self ):
        if isinstance( self.__statename, str ) and self.__statename != '':
            return self.__statename

    @statename.setter
    def statename( self, name ):
        if isinstance( name, str ) and name != '':
            self.__statename = name

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value


class Allocation( ):
    '''object representing operating plan data'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

    @property
    def rccode( self ):
        if isinstance( self.__rccode, str ) and self.__rccode != '':
            return self.__rccode

    @rccode.setter
    def rccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rccode = code

    @property
    def rcname( self ):
        if isinstance( self.__rcname, str ) and self.__rcname != '':
            return self.__rcname

    @rcname.setter
    def rcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rcname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class RegionalAuthority( ):
    '''object representing Regional Allocations'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class HeadquartersAuthority( ):
    '''object representing HQ Allocations'''
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
    __accoutcode = None
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

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, str ) and year != '':
            self.__bfy = year

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
    def rpiocode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__rpiocode = code

    @property
    def rpioname( self ):
        if isinstance( self.__rpioname, str ) and self.__rpioname != '':
            return self.__rpioname

    @rpiocode.setter
    def rpiocode( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpiocode = name

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
            self.__name = name

    @property
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__orgcode = code

    @property
    def orgname( self ):
        if isinstance( self.__orgname, str ) and self.__orgname != '':
            return self.__orgname

    @orgname.setter
    def orgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__orgname = name

    @property
    def accountcode( self ):
        if isinstance( self.__accountcode, str ) and self.__accoutcode != '':
            return self.__accoutcode

    @accountcode.setter
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

    @property
    def boccode( self ):
        if isinstance( self.__boccode, str ) and self.__boccode != '':
            return self.__boccode

    @boccode.setter
    def boccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__boccode = code

    @property
    def bocname( self ):
        if isinstance( self.__bocname, str ) and self.__bocname != '':
            return self.__bocname

    @bocname.setter
    def bocname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__bocname = name

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
    def programprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programprojectcode = code

    @property
    def programprojectname( self ):
        if isinstance( self.__programprojectname, str ) and self.__programprojectname != '':
            return self.__programprojectname

    @programprojectname.setter
    def programprojectname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programprojectname = name

    @property
    def programareacode( self ):
        if isinstance( self.__programareacode, str ) and self.__programareacode != '':
            return self.__programareacode

    @programareacode.setter
    def programareacode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__programareacode = code

    @property
    def programareaname( self ):
        if isinstance( self.__programareaname, str ) and self.__programareaname != '':
            return self.__programareaname

    @programareaname.setter
    def programareaname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__programareaname = name

    @property
    def goalcode( self ):
        if isinstance( self.__goalcode, str ) and self.__goalcode != '':
            return self.__goalcode

    @goalcode.setter
    def goalcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalcode = code

    @property
    def goalname( self ):
        if isinstance( self.__goalname, str ) and self.__goalname != '':
            return self.__goalname

    @goalname.setter
    def goalname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__goalname = code

    @property
    def objectivecode( self ):
        if isinstance( self.__objectivecode, str ) and self.__objectivecode != '':
            return self.__objectivecode

    @gobjectivecode.setter
    def objectivecode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivecode = code

    @property
    def objectivename( self ):
        if isinstance( self.__objectivename, str ) and self.__objectivename != '':
            return self.__objectivename

    @objectivename.setter
    def objectivename( self, code ):
        if isinstance( code, str ) and code != '':
            self.__objectivename = code

    @property
    def npmcode( self ):
        if isinstance( self.__npmcode, str ) and self.__npmcode != '':
            return self.__npmcode

    @npmcode.setter
    def npmcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmcode = code

    @property
    def npmname( self ):
        if isinstance( self.__npmname, str ) and self.__npmname != '':
            return self.__npmname

    @objectivename.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code


class Actuals( ):
    '''Object representing expendtiure data'''
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
    __accoutcode = None
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


class AppropriationDocument( ):
    '''object representing Level 1 documents'''
    __appropriationdocumentsid = None


class BudgetDocument( ):
    '''object representing Level 2-3 documents'''
    __budgetdocumentsid = None


class BudgetControl( ):
    '''object representing compass control data'''


class CongressionalControl( ):
    '''object representing congressional control data'''
    __congressionalcontrolsid = None


class CompassLevel( ):
    '''object representing Compass data levels 1-7'''
    __compasslevelsid = None


class Commitment( ):
    '''Defines the commitment class.'''
    __commitmentsid = None
    __obligationsid = None
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__commitmentsid , int ):
            return self.__commitmentsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__commitmentsid  = id

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float):
            self.__amount = value

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, code ):
        if isinstance( code, Account ):
            self.__account = code

    @property
    def document( self ):
        if isinstance( self.__document, str ) and self.__document != '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if isinstance( doc, str ) and doc != '':
            self.__document = doc

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organization ):
            self.__org = org

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, bfy ):
        if isinstance( bfy, BudgetFiscalYear ):
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame


    def __init__( self, amount ):
        self.__amount = amount if isinstance( amount, float ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )


class OpenCommitment( ):
    '''Defines the commitment class.'''
    __opencommitmentsid = None
    __obligationsid = None
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__opencommitmentsid, int ):
            return self.__opencommitmentsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__opencommitmentsid = id

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, acct ):
        if isinstance( acct, Account ):
            self.__account = acct

    @property
    def document( self ):
        if isinstance( self.__document, str ) and self.__document != '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if isinstance( doc, str ) and doc != '':
            self.__document = doc

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organization ):
            self.__org = org

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, bfy ):
        if isinstance( bfy, BudgetFiscalYear ):
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

    @property
    def data( self ):
        if isinstance( self.__data, list ):
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__data = cache

    @data.setter
    def data( self, cache ):
        if isinstance( cache, list ):
            self.__record = cache

    @property
    def table( self ):
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )


class Obligation( ):
    '''Defines the commitment class.'''
    __obligationsid = None
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__obligationsid, int ):
            return self.__obligationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__obligationsid = id

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, acct ):
        if isinstance( acct, Account ):
            self.__account = acct

    @property
    def document( self ):
        if isinstance( self.__document, str ) and self.__document != '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if isinstance( doc, str ) and doc != '':
            self.__document = doc

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organization ):
            self.__org = org

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, bfy ):
        if isinstance( bfy, BudgetFiscalYear ):
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )


class Deobligation( ):
    '''Defines the commitment class.'''
    __deobligationsid = None
    __obligationsid = None
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__deobligationsid, int ):
            return self.__deobligationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__deobligationsid = id

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, acct ):
        if isinstance( acct, Account ):
            self.__account = acct

    @property
    def document( self ):
        if isinstance( self.__document, str ) and self.__document != '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if isinstance( doc, str ) and doc != '':
            self.__document = doc

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organization ):
            self.__org = org

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, bfy ):
        if isinstance( bfy, BudgetFiscalYear ):
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

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
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )


class UnliquidatedObligation( ):
    '''Defines the commitment class.'''
    __unliquidatedobligationsid = None
    __obligationsid = None
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__unliquidatedobligationsid, int ):
            return self.__unliquidatedobligationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__unliquidatedobligationsid = id

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, acct ):
        if isinstance( acct, Account ):
            self.__account = acct

    @property
    def document( self ):
        if isinstance( self.__document, str ) and self.__document != '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if isinstance( doc, str ) and doc != '':
            self.__document = doc

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organization ):
            self.__org = org

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, bfy ):
        if isinstance( bfy, BudgetFiscalYear ):
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

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
        if isinstance( self.__frame, pd.DataFrame ):
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )


class Expenditure:
    '''Defines the commitment class.'''
    __expendituresid = None
    __obligationsid = None
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__expendituresid = id

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    @property
    def account( self ):
        if isinstance( self.__account, Account ):
            return self.__account

    @account.setter
    def account( self, acct ):
        if isinstance( acct, Account ):
            self.__account = acct

    @property
    def document( self ):
        if isinstance( self.__document, str ) and self.__document != '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if isinstance( doc, str ) and doc != '':
            self.__document = doc

    @property
    def org( self ):
        if isinstance( self.__org, Organization ):
            return self.__org

    @org.setter
    def org( self, org ):
        if isinstance( org, Organization ):
            self.__org = org

    @property
    def bfy( self ):
        if isinstance( self.__bfy, BudgetFiscalYear ):
            return self.__bfy

    @bfy.setter
    def bfy( self, bfy ):
        if isinstance( bfy, BudgetFiscalYear ):
            self.__bfy = bfy

    @property
    def fund( self ):
        if isinstance( self.__fund, Fund ):
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if isinstance( self.__boc, BudgetObjectClass ):
            return self.__boc

    @boc.setter
    def boc( self, boc ):
        if isinstance( boc, BudgetObjectClass ):
            self.__boc = boc

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
        if self.__frame is not None:
            return self.__frame

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )
