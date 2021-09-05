import datetime

class Unit():
    '''Defines the Data class'''
    __code = None

    def __init__( self, code ):
        self.__code = code

    def __str__(self):
        if self.__code is not None:
            return self.__code

class Data( Unit ):
    '''Defines the basic budget data unit'''
    __name = ''
    __value = ''

    @property
    def name( self ):
        if self.__name != '':
            return self.__name

    @property
    def value( self ):
        if self.__value != '':
            return self.__value

    def __init__( self, code, name, value ):
        super().__init__( code )
        self.__name = name
        self.__value = value

    def __str__( self ):
        return self.__name

class Account():
    '''defines the Account Code class'''
    __code = ''
    __name = None
    __goal = ''
    __objective = ''
    __npm = ''
    __program_project = ''

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if not self.__name == '':
            return self.__code
        else:
            return 'NS'

    @property
    def goal( self ):
        if not self.__goal == '':
            return self.__goal
        else:
            return 'NS'

    @property
    def npm( self ):
        if not self.__npm == '':
            return self.__npm
        else:
            return 'NS'

    @property
    def program_project( self ):
        if not self.__program_project == '':
            return self.__program_project
        else:
            return 'NS'

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name
        self.__goal = list( code )[ 0 ]
        self.__objective = list( code )[ 1:3 ]
        self.__npm = list( code )[ 3 ]
        self.__program_project = list( code )[ 4:6 ]

    def __str__( self ):
        if not self.__code == '':
            return self.__code

class Activity():
    '''Defines the Activity Class'''
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

class AllowanceHolder():
    '''Defines the AllowanceHolder Class'''
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
        self.__ah_code = code
        self.__a_name = name

    def __str__( self ):
        return self.__ah_code

class Appropriation():
    '''Defines the Appropriation Class'''
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

class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __fiscal_year = ''
    __today = ''
    __date = None
    __year = ''
    __start_date = ''
    __end_date = ''
    __expiration = ''
    __weekends = 0
    __workdays = 0
    __day = ''
    __month = ''
    __federal_holidays = { }

    def __init__( self, year ):
        self.__year = year
        self.__today = datetime.date
        self.__day = self.__today.day
        self.__month = self.__today.month

    def __str__( self ):
        return self.__fiscal_year

class BudgetObjectClass():
    '''Defines the BudgetObjectClass Class'''
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

class Division():
    '''Defines the Division Class'''
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

class FinanceObjectClass():
    '''Defines the FinanceObjectClass Class'''
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

class Fund():
    '''Defines the Fund Class'''
    __code = ''
    __name = ''
    __title = ''

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
    __code = ''
    __name = ''
    __rpio = ''
    __title = ''

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

class Objective():
    '''Defines the Objective Class'''
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

class Organization():
    '''Defines the Organization Class'''
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

class ProgramArea():
    '''defines the ProgramArea class'''
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

class ProgramProject():
    '''Defines the ProgramProject Class'''
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

class ResponsibilityCenter():
    '''Defines the ResponsibilityCenter Class'''
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

class ResourceImplementationPlanningOffice():
    '''defines the ResponsiblePlanningOffice class'''
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

class ProgramResultsCode():
    '''Defines the PRC class'''
    __id = -1
    __rpio = None
    __bfy = None
    __ah = None
    __fund = None
    __org = None
    __account = None
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
    def ah( self ):
        if self.__ah is not None:
            return self.__ah

    def __init__( self, rpio = None, bfy = None,
                  ah = None, fund = None, code = None,
                  boc = None, org = None ):
        '''Initializes the PRC class'''

        self.__rpio = ResourceImplementationPlanningOffice( rpio )
        self.__bfy = BudgetFiscalYear( bfy )
        self.__ah_code = AllowanceHolder( ah )
        self.__fund = Fund( fund )
        self.__account = Account( code )
        self.__org = Organization( org )
        self.__boc = BudgetObjectClass( boc )
