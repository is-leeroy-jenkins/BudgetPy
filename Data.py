import datetime

class Unit():
    '''Defines the Data class'''
    __id = -1
    __code = None

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id
        else:
            return -1

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    def __init__( self, code, index = None ):
        self.__id = int( index )
        self.__code = str( code )

    def __str__( self ):
        if self.__code is not None:
            return self.__code
        else:
            return 'NS'

class Element( Unit ):
    '''Defines the basic budget data unit'''
    __name = None
    __value = None

    @property
    def name( self ):
        if self.__name is not None:
            return str( self.__name )
        else:
            return 'NS'

    @property
    def value( self ):
        if self.__value is not None:
            return self.__value
        else:
            return 'NS'

    def __init__( self, code, name ):
        super().__init__( str( code ) )
        self.__code = str( code )
        self.__name = str( name )
        self.__value = self.__code

    def __str__( self ):
        if self.__name is not None:
            return self.__name

class Account():
    '''defines the Account Code class'''
    __index = None
    __code = None
    __name = None
    __goal = None
    __objective = None
    __npm = None
    __programproject = None

    @property
    def id( self ):
        if not self.__index < 0:
            return int( self.__index )
        else:
            return -1

    @property
    def code( self ):
        if self.__code:
            return str( self.__code )
        else:
            return 'NS'

    @property
    def name( self ):
        if self.__name:
            return str( self.__name )
        else:
            return 'NS'

    @property
    def goal( self ):
        if self.__goal is not None:
            return self.__goal
        else:
            return 'NS'

    @property
    def objective( self ):
        if self.__objective is not None:
            return self.__objective
        else:
            return 'NS'

    @property
    def npm( self ):
        if self.__npm is not None:
            return self.__npm
        else:
            return 'NS'

    @property
    def programproject( self ):
        if self.__programproject is not None:
            return self.__programproject
        else:
            return 'NS'

    def __init__( self, code, name = None, index = None ):
        self.__index = int( index )
        self.__code = str( code )
        self.__name = str( name )
        self.__goal = list( code )[ 0 ]
        self.__objective = str( list( code )[ 1:3 ] )
        self.__npm = list( code )[ 3 ]
        self.__programproject = str( list( code )[ 4:6 ] )

    def __str__( self ):
        if self.__code is not None:
            return self.__code

class Activity():
    '''Defines the Activity Class'''
    __id = None
    __code = None
    __name = None

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id
        else:
            return -1

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name
        else:
            return 'NS'

    def __init__( self, code, name = None, index = None ):
        self.__id = int( index )
        self.__code = str( code )
        self.__name = str( name )

    def __str__( self ):
        return self.__code

class AllowanceHolder():
    '''Defines the AllowanceHolder Class'''
    __id = None
    __code = None
    __name = None

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id
        else:
            return -1

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name
        else:
            return 'NS'

    def __init__( self, code, name = None, index = None ):
        self.__id = int( index )
        self.__code = code
        self.__name = name

    def __str__( self ):
        if self.__code is not None:
            return self.__code

class Appropriation():
    '''Defines the Appropriation Class'''
    __code = None
    __name = None
    __title = None
    __bfy = None

    @property
    def id( self ):
        if self.__id > 0:
            return self.__id
        else:
            return -1

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name
        else:
            return 'NS'

    @property
    def fiscalyear( self ):
        if self.__bfy is not None:
            return self.__bfy
        else:
            return 'NS'

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title
        else:
            return 'NS'

    def __init__( self, code, name = None,
                  bfy = None, title = None,
                  index = None ):
        self.__id = int( index )
        self.__code = str( code )
        self.__bfy = str( bfy )
        self.__name = str( name )
        self.__title = str( title )

    def __str__( self ):
        return self.__code

class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __base = None
    __fiscalyear = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = 0
    __workdays = 0
    __year = None
    __month = ''
    __day = ''
    __holidays = { }

    @property
    def fiscalyear( self ):
        if self.__fiscalyear is not None:
            return self.__fiscalyear

    @property
    def calendaryear( self ):
        if self.__year:
            return str( self.__year )

    @property
    def startdate( self ):
        if isinstance( self.__startdate, datetime.datetime ):
            return datetime.date( self.__startdate.year, self.__startdate.month,
                self.__startdate.day )

    @property
    def enddate( self ):
        if isinstance( self.__enddate, datetime.datetime ):
            return datetime.datetime( self.__enddate.year, self.__enddate.month,
                self.__enddate.day )

    @property
    def expiration( self ):
        if isinstance( self.__expiration, datetime.datetime ):
            return datetime.datetime( self.__expiration.year, self.__expiration.month,
                self.__expiration.day )

    @property
    def weekends( self ):
        if self.__weekends is not None:
            return self.__weekends

    @property
    def workdays( self ):
        if self.__workdays is not None:
            return float( self.__workdays )

    @property
    def date( self ):
        if isinstance( self.__date, datetime.datetime):
            return datetime.date( self.__date.year, self.__month,
                self.__date.day )

    @property
    def day( self ):
        if self.__day is not None:
            return str( self.__day )

    @property
    def month( self ):
        if self.__month is not None:
            return str( self.__month )

    @property
    def holidays( self ):
        if self.__holidays is not None:
            return self.__holidays

    def __init__( self, year ):
        self.__base = str( year )
        self.__fiscalyear = self.__base[ 3: ]
        self.__date = datetime.date
        self.__year = int( year )
        self.__today = datetime.date
        self.__day = self.__today.day
        self.__month = self.__today.month

    def __str__( self ):
        return str( self.__year )

class BudgetObjectClass():
    '''Defines the BudgetObjectClass Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class Division():
    '''Defines the Division Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class FinanceObjectClass():
    '''Defines the FinanceObjectClass Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class Fund():
    '''Defines the Fund Class'''
    __code = None
    __name = None
    __title = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class Goal():
    '''Defines the Goal Class'''
    __code = ''
    __name = ''

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class NationalProgram():
    '''Defines the NationalProgram Class'''
    __code = None
    __name = None
    __rpio = None
    __title = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    def __init__( self, code, name = None,
                 rpio = None, title = None):
        self.__code = code
        self.__name = name
        self.__rpio = rpio
        self.__title = title

    def __str__( self ):
        return self.__code

class Objective():
    '''Defines the Objective Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class Organization():
    '''Defines the Organization Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return str( self.__code )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class Project():
    '''Defines the Organization Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        if self.__code:
            return self.__code

class ItProjectCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class SiteProjectCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class HumanResourceOrganization():
    '''Defines the Organization Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class WorkCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class ProgramArea():
    '''defines the ProgramArea class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class ProgramProject():
    '''Defines the ProgramProject Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = None ):
        self.__code = str( code )
        self.__name = str( name )

    def __str__( self ):
        return self.__code

class ResponsibilityCenter():
    '''Defines the ResponsibilityCenter Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class ResourcePlanningImplementationOffice():
    '''defines the ResponsiblePlanningOffice class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class ProgramResultsCode():
    '''Defines the PRC class'''
    __id = -1
    __rpio = None
    __bfy = None
    __ah = None
    __fund = None
    __org = None
    __account = None
    __activity = None
    __rc = None
    __boc = None
    __amount = 0

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id
        else:
            return - 1

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @property
    def fund( self ):
        if self.__fund.code is not None:
            return Fund( self.__fund.code )

    @property
    def ah( self ):
        if self.__ah is not None:
            return AllowanceHolder( self.__ah )

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @property
    def activity( self ):
        if self.__account is not None:
            self.__activity = str( self.__account[ 5:2 ] )
            return Activity( self.__activity )

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @property
    def rc( self ):
        if self.__rc is not None:
            return self.__rc

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    def __init__( self, code, rpio = None, bfy = None,
                  ah = None, fund = None,
                  boc = None, org = None,
                  amount = 0 ):
        '''Initializes the PRC class'''

        self.__rpio = ResourcePlanningImplementationOffice( rpio )
        self.__bfy = BudgetFiscalYear( bfy )
        self.__ah = AllowanceHolder( ah )
        self.__fund = Fund( fund )
        self.__account = Account( code )
        self.__org = Organization( org )
        self.__boc = BudgetObjectClass( boc )
        self.__amount = amount

    def __str__( self ):
        if self.__account.code is not None:
            return self.__account.code

class RegionalOffice():
    '''Defines a regional RPIO'''
    __rpio = None
    __name = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, rpio, name = None ):
        self.__rpio = rpio
        self.__name = name

    def __str__(self):
        if self.__rpio is not None:
            return str( self.__rpio )

class HeadQuartersOffice():
    '''Defines the HQ class'''
    __rpio = None
    __name = None
    __title = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    def __init__( self, rpio, name = None,
                  title = None):
        self.__rpio = rpio
        self.__name = name
        self.__title = title

    def __str__( self ):
        if self.__name is not None:
            return str( self.__name )

class Holiday():
    '''Defines the Holiday class'''
    __bfy = None
    __name = None
    __date = None
    __day = None

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    def __init__( self, bfy, date = None,
                  name = None, day = None ):
        self.__bfy = bfy
        self.__name = name
        self.__day = day
        self.__date = date

    def __str__(self):
        if self.__name is not None:
            return str( self.__name )

class Commitment:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    def __init__(self, amount, account = None,
                 document = None, bfy = None,
                 org = None, boc = None):
        self.__amount = amount
        self.__account = account
        self.__document = document
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class OpenCommitment:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    def __init__( self, amount, account = None,
                  doc = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = doc
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class Obligation:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class DeObligation:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class ULO:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class Expenditure:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )