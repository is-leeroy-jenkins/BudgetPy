from Execution import *
from Static import *
from Ninja import *


# OperatingPlan( bfy, fund )
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
    __data = None
    __frame = None

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

    @rpioname.setter
    def rpioname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__rpioname = name

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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.OperatingPlans
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# FullTimeEquivalent( bfy, fund )
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
    __data = None
    __frame = None

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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.FullTimeEquivalents
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# StatusOfFunds( bfy, fund )
class StatusOfFunds( ):
    '''Object representing execution data'''
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.StatusOfFunds
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# Defacto( bfy, fund )
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Defactos
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# StatusOfSupplementalFunds( bfy, fund )
class StatusOfSupplementalFunds( ):
    '''object representing Supplemental Funds execution data'''
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.StatusOfSupplementalFunding
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# StateGrantObligation( bfy, rpio )
class StateGrantObligation( ):
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
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __statecode = None
    __statename = None
    __amount = None
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    def __init__( self, bfy, rpio ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.StateGrantObligations
        command = Command.SELECTALL
        names = [ 'BFY', 'RpioCode', ]
        values = ( self.__bfy, self.__rpiocode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# Allocation( bfy, fund )
class Allocations( ):
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Allocations
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# RegionalAuthority( bfy, fund )
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.RegionalAuthority
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# HeadquartersAuthority( bfy, rpio )
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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, rpio ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.HeadquartersAuthority
        command = Command.SELECTALL
        names = [ 'BFY', 'RpioCode', ]
        values = ( self.__bfy, self.__rpiocode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# PayrollActivity( bfy, fund )
class PayrollActivity( ):
    '''provides payroll data'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__payrollactivityid, int ):
            return self.__payrollactivityid

    @id.setter
    def id( self, pid ):
        if isinstance( pid, int ):
            self.__payrollactivityid = pid

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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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
    def subrccode( self ):
        if isinstance( self.__subrccode, str ) and self.__subrccode != '':
            return self.__subrccode

    @subrccode.setter
    def subrccode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__subrccode = code

    @property
    def subrcname( self ):
        if isinstance( self.__subrcname, str ) and self.__subrcname != '':
            return self.__subrcname

    @subrcname.setter
    def subrcname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__subrcname = name

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
    def hrorgcode( self ):
        if isinstance( self.__hrorgcode, str ) and self.__hrorgcode != '':
            return self.__hrorgcode

    @hrorgcode.setter
    def hrorgcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__hrorgcode = code

    @property
    def hrorgname( self ):
        if isinstance( self.__hrorgname, str ) and self.__hrorgname != '':
            return self.__hrorgname

    @hrorgname.setter
    def hrorgname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__hrorgname = name

    @property
    def workcode( self ):
        if isinstance( self.__workcode, str ) and self.__workcode != '':
            return self.__workcode

    @workcode.setter
    def workcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__workcode = code

    @property
    def workcodename( self ):
        if isinstance( self.__workcodename, str ) and self.__workcodename != '':
            return self.__workcodename

    @workcodename.setter
    def workcodename( self, name ):
        if isinstance( name, str ) and name != '':
            self.__workcodename = name

    @property
    def payperiod( self ):
        if isinstance( self.__payperiod, int ):
            return self.__payperiod

    @payperiod.setter
    def payperiod( self, pd ):
        if isinstance( pd, int ):
            self.__payperiod = pd

    @property
    def startdate( self ):
        if isinstance( self.__startdate, dt.datetime ):
            return self.__startdate

    @startdate.setter
    def startdate( self, sd ):
        if isinstance( sd, dt.datetime ):
            self.__startdate = sd

    @property
    def enddate( self ):
        if isinstance( self.__enddate, dt.datetime ):
            return self.__enddate

    @enddate.setter
    def enddate( self, ed ):
        if isinstance( ed, dt.datetime ):
            self.__startdate = ed

    @property
    def checkdate( self ):
        if isinstance( self.__checkdate, dt.datetime ):
            return self.__checkdate

    @checkdate.setter
    def checkdate( self, cd ):
        if isinstance( cd, dt.datetime ):
            self.__checkdate = cd

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None


    def getdata( self ):
        provider = Provider.SQLite
        source = Source.PayrollActivity
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# SiteActivity( bfy, rpio  )
class SiteActivity( ):
    '''provides data on superfund site spending'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__siteactivityid, int ):
            return self.__siteactivityid

    @id.setter
    def id( self, pid ):
        if isinstance( pid, int ):
            self.__siteactivityid = pid

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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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
    def epasiteid( self ):
        if isinstance( self.__epasiteid, str ) and self.__epasiteid != '':
            return self.__epasiteid

    @epasiteid.setter
    def epasiteid( self, code ):
        if isinstance( code, str ) and code != '':
            self.__epasiteid = code

    @property
    def projecttype( self ):
        if isinstance( self.__projecttype, str ) and self.__projecttype != '':
            return self.__projecttype

    @projecttype.setter
    def projecttype( self, code ):
        if isinstance( code, str ) and code != '':
            self.__projecttype = code

    @property
    def siteprojectcode( self ):
        if isinstance( self.__siteprojectcode, str ) and self.__siteprojectcode != '':
            return self.__siteprojectcode

    @siteprojectcode.setter
    def siteprojectcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__siteprojectcode = code

    @property
    def siteprojectname( self ):
        if isinstance( self.__siteprojectname, str ) and self.__siteprojectname != '':
            return self.__siteprojectname

    @siteprojectname.setter
    def siteprojectname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__siteprojectname = code

    @property
    def ssid( self ):
        if isinstance( self.__ssid, str ) and self.__ssid != '':
            return self.__ssid

    @ssid.setter
    def ssid( self, code ):
        if isinstance( code, str ) and code != '':
            self.__ssid = code

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
    def operableunit( self, code ):
        if isinstance( code, str ) and code != '':
            self.__operableunit = code

    @property
    def state( self ):
        if isinstance( self.__state, str ) and self.__state != '':
            return self.__state

    @state.setter
    def state( self, code ):
        if isinstance( code, str ) and code != '':
            self.__state = code

    @property
    def city( self ):
        if isinstance( self.__city, str ) and self.__city != '':
            return self.__city

    @city.setter
    def city( self, code ):
        if isinstance( code, str ) and code != '':
            self.__city = code

    @property
    def congress( self ):
        if isinstance( self.__congress, str ) and self.__congress != '':
            return self.__congress

    @congress.setter
    def congress( self, code ):
        if isinstance( code, str ) and code != '':
            self.__congress = code

    @property
    def startdate( self ):
        if isinstance( self.__startdate, str ) and self.__startdate != '':
            return self.__startdate

    @startdate.setter
    def startdate( self, code ):
        if isinstance( code, str ) and code != '':
            self.__startdate = code

    @property
    def enddate( self ):
        if isinstance( self.__enddate, str ) and self.__enddate != '':
            return self.__enddate

    @enddate.setter
    def enddate( self, code ):
        if isinstance( code, str ) and code != '':
            self.__enddate = code

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, str ) and self.__lastactivitydate != '':
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, code ):
        if isinstance( code, str ) and code != '':
            self.__lastactivitydate = code

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

    def __init__( self, bfy, rpio ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rpiocode = rpio if isinstance( rpio, str ) and rpio != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.SiteActivity
        command = Command.SELECTALL
        names = [ 'BFY', 'RpioCode', ]
        values = ( self.__bfy, self.__rpiocode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# Acutals( bfy, fund  )
class Actuals( ):
    '''Object representing expenditure data'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__actualsid, int ):
            return self.__actualsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ) and id > -1:
            self.__id = id

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
            self.__fundname = name

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
        if isinstance( self.__accountcode, str ) and self.__accountcode != '':
            return self.__accountcode

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

    @objectivecode.setter
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

    @npmname.setter
    def npmname( self, code ):
        if isinstance( code, str ) and code != '':
            self.__npmname = code

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Actuals
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# AppropriationDocument( bfy, fund )
class AppropriationDocument( ):
    '''object representing Level 1 documents'''
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
    def fundcode( self ):
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    @fundcode.setter
    def fundcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__fundcode = code

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
        if isinstance( self.__documentdate, dt.datetime ):
            return self.__documentdate

    @documentdate.setter
    def documentdate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__documentdate = value

    @property
    def lastdocumentdate( self ):
        if isinstance( self.__lastdocumentdate, dt.datetime ):
            return self.__lastdocumentdate

    @lastdocumentdate.setter
    def lastdocumentdate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.AppropriationDocuments
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# BudgetDocument( bfy, fund )
class BudgetDocument( ):
    '''object representing Level 2-3 documents'''
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
        if isinstance( self.__documentdate, dt.datetime ):
            return self.__documentdate

    @documentdate.setter
    def documentdate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__documentdate = value

    @property
    def lastdocumentdate( self ):
        if isinstance( self.__lastdocumentdate, dt.datetime ):
            return self.__lastdocumentdate

    @lastdocumentdate.setter
    def lastdocumentdate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, efy, fundcode ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.BudgetDocuments
        command = Command.SELECTALL
        names = [ 'BFY', 'EFY', 'FundCode', ]
        values = ( self.__bfy, self.__efy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# BudgetControl( code )
class BudgetControl( ):
    '''object representing compass control data'''
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

    def __init__( self, bfy, efy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.BudgetControls
        command = Command.SELECTALL
        names = [ 'BFY', 'EFY', 'FundCode', ]
        values = ( self.__bfy, self.__efy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# CongressionalControl( bfy, fund )
class CongressionalControl( ):
    '''object representing congressional control data'''
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

    def __init__( self, bfy, fundcode ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.CongressionalControls
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', ]
        values = ( self.__bfy, self.__fundcode )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


# CompassLevel( bfy, efy, fund )
class CompassLevels( ):
    '''object representing Compass data levels 1-7'''
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

    def __init__( self, bfy, efy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.CompassLevels
        command = Command.SELECTALL
        names = [ 'BFY', 'EFY', 'FundCode' ]
        values = ( self.__bfy, self.__efy, self.__fundcode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# Commitment( bfy, fund, account, boc )
class Commitment( ):
    '''Defines the CommitmentS class.'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__expendituresid = iid

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
        if isinstance( self.__processeddate, dt.datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, dt.datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__data = {
                'amount':   self.__amount,
                'account':  None,
                'document': None,
                'org':      None,
                'bfy':      None,
                'fund':     None,
                'boc':      None }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.OpenCommitments
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# DocumentControlNumber( dcn )
class DocumentControlNumber( ):
    ''' object provides DCN data'''
    __documentcontrolnumbersid = None
    __rpiocode = None
    __rpioname = None
    __documenttype = None
    __documentnumber = None
    __documentprefix = None
    __documentcontrolnumber = None

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

    def __init__( self, dcn ):
        self.__documentcontrolnumber = dcn if isinstance( dcn, str ) and dcn != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.OpenCommitments
        command = Command.SELECTALL
        names = [ 'DocumentControlNumber', ]
        values = ( self.__documentcontrolnumber, )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# HumanResourceOrganization( code )
class HumanResourceOrganization( ):
    ''' object providing HR Org data'''
    __humanresourceorganizationsid = None
    __code = None
    __name = None

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
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ) and value != '':
            self.__name = value

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) and code != '' else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.HumanResourceOrganizations
        command = Command.SELECTALL
        names = [ 'Code', ]
        values = (self.__code, )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# OpenCommitment( bfy, fund, account, boc )
class OpenCommitment( ):
    ''' OpenCommitment( bfy, fund, account, boc )
    initializes object providing OpenCommitment data.'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__expendituresid = iid

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
        if isinstance( self.__processeddate, dt.datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, dt.datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__data = {
                'amount':   self.__amount,
                'account':  None,
                'document': None,
                'org':      None,
                'bfy':      None,
                'fund':     None,
                'boc':      None }
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.OpenCommitments
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# Obligation( bfy, fund, account, boc )
class Obligation( ):
    '''Obligation( bfy, fund, account, boc )
    initializes object providing Obligation data'''
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
        if isinstance( self.__processeddate, dt.datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, dt.datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Obligations
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# Deobligation( bfy, fund, account, boc )
class Deobligation( ):
    '''Deobligation( bfy, fund, account, boc )
    initializes object providing Deobligation data '''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__expendituresid = iid

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
        if isinstance( self.__processeddate, dt.datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, dt.datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Deobligations
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data



# UnliquidatedObligation( bfy, fund, account, boc )
class UnliquidatedObligation( ):
    '''UnliquidatedObligation( bfy, fund, account, boc )
    initializes object providing ULO data'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__expendituresid = iid

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
        if isinstance( self.__processeddate, dt.datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, dt.datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.UnliquidatedObligations
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data



# Expenditure( bfy, fund, account, code )
class Expenditures:
    '''Expenditure( bfy, fund, account, code )
    initializes object providing Expenditure data'''
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
    __data = None
    __frame = None

    @property
    def id( self ):
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__expendituresid = iid

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
        if isinstance( self.__processeddate, dt.datetime ):
            return self.__processeddate

    @processeddate.setter
    def processeddate( self, value ):
        if isinstance( value, dt.datetime ):
            self.__processeddate = value

    @property
    def lastactivitydate( self ):
        if isinstance( self.__lastactivitydate, dt.datetime ):
            return self.__lastactivitydate

    @lastactivitydate.setter
    def lastactivitydate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Expenditures
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data



class SpecialAccounts( ):
    '''' object providing SF Special Account data'''
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

    @property
    def id( self ):
        if isinstance( self.__specialaccountsid, int ):
            return self.__specialaccountsid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__specialaccountsid = iid

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

    @specialaccountfundcode.setter
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

    @acccountstatus.setter
    def accountstatus( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accountstatus = value

    @property
    def nplstatus( self ):
        if isinstance( self.__nplstatus, str ) and self.__nplstatus != '':
            return self.__nplstatus

    @acccountstatus.setter
    def nplstatus( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatus = value

    @property
    def nplstatuscode( self ):
        if isinstance( self.__nplstatuscode, str ) and self.__nplstatuscode != '':
            return self.__nplstatuscode

    @acccountstatus.setter
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



    def __init__( self, bfy, fund, account, boc ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.SpecialAccounts
        command = Command.SELECTALL
        names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
        values = ( self.__bfy, self.__accountcode, self.__boccode )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data




class SuperfundSites( ):
    ''' object providing SF Site data '''
    __superfundsitesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __specialaccountfund = None
    __specialaccountnumber = None
    __specialaccountname = None
    __accountstatus = None
    __nplstatuscode = None
    __nplstatusname = None
    __siteid = None
    __cerclisid = None
    __sitecode = None
    __sitename = None
    __operableunit = None
    __pipelinecode = None
    __pipelinedescription = None
    __accountcode = None
    __bocccode = None
    __bocname = None
    __transactiontype = None
    __transactiontypename = None
    __foccode = None
    __focname = None
    __transactiondate = None
    __availablebalance = None
    __opencommitments = None
    __obligations = None
    __disbursements = None
    __cumulativereciepts = None
    __unpaidbalances = None
    __collections = None
    __unliquidatedobligations = None

    @property
    def id( self ):
        if isinstance( self.__specialaccountsid, int ):
            return self.__specialaccountsid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__specialaccountsid = iid

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
    def nplstatus( self ):
        if isinstance( self.__nplstatus, str ) and self.__nplstatus != '':
            return self.__nplstatus

    @acccountstatus.setter
    def nplstatus( self, value ):
        if isinstance( value, str ) and value != '':
            self.__nplstatus = value

    @property
    def nplstatuscode( self ):
        if isinstance( self.__nplstatuscode, str ) and self.__nplstatuscode != '':
            return self.__nplstatuscode

    @acccountstatus.setter
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
    def sitecode( self ):
        if isinstance( self.__sitecode, str ) and self.__sitecode != '':
            return self.__sitecode

    @sitecode.setter
    def sitecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__value = value

    @property
    def sitename( self ):
        if isinstance( self.__sitename, str ) and self.__sitename != '':
            return self.__sitename

    @sitename.setter
    def sitename( self, value ):
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
    def pipelinecode( self ):
        if isinstance( self.__pipelinecode, str ) and self.__pipelinecode != '':
            return self.__pipelinecode

    @pipelinecode.setter
    def pipelinecode( self, value ):
        if isinstance( value, str ) and value != '':
            self.__pipelinecode = value

    @property
    def pipelinename( self ):
        if isinstance( self.__pipelinename, str ) and self.__pipelinename!= '':
            return self.__pipelinename

    @pipelinename.setter
    def pipelinename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__pipelinename = value

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
    def transactiontype( self ):
        if isinstance( self.__transactiontype, str ) and self.__transactiontype != '':
            return self.__transactiontype

    @transactiontype.setter
    def transactiontype( self, value ):
        if isinstance( value, str ) and value != '':
            self.__transactiontype = value

    @property
    def transactiontypename( self ):
        if isinstance( self.__transactiontypename, str ) and self.__transactiontypename != '':
            return self.__transactiontypename

    @transactiontype.setter
    def transactiontypename( self, value ):
        if isinstance( value, str ) and value != '':
            self.__transactiontypename = value
