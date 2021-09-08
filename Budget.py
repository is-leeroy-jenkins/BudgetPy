import datetime

class Unit():
    '''Defines the Data class'''
    __id = None
    __code = None

    def __init__( self, code, index = None ):
        self.__id = int( index )
        self.__code = str( code )

    def __str__( self ):
        if self.__code is not None:
            return self.__code
        else:
            return 'NS'

class Data( Unit ):
    '''Defines the basic budget data unit'''
    __name = None
    __value = None

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name
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
    def goal( self ):
        if self.__goal is not None:
            return self.__goal
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
        self.__objective = list( code )[ 1:3 ]
        self.__npm = list( code )[ 3 ]
        self.__programproject = list( code )[ 4:6 ]

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
    __code = ''
    __name = ''

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

    def __init__( self, code, name = None, bfy = None, index = None ):
        self.__id = int( index )
        self.__bfy = str( bfy )
        self.__code = str( code )
        self.__name = str( name )

    def __str__( self ):
        return self.__code

class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __base = None
    __fiscalyear = None
    __today = None
    __date = None
    __year = None
    __start_date = None
    __end_date = None
    __expiration = None
    __weekends = 0
    __workdays = 0
    __day = ''
    __month = ''
    __federal_holidays = { }

    def __init__( self, year ):
        self.__base = str( year )
        self.__fiscalyear = self.__base[ 3: ]
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
