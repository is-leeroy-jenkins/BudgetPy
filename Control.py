from Execution import *


class Apportionment( ):
    '''Apportionment( code ) creates
    object representing Letters Of Apportionment'''

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
    __data = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__bfy = yr

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__efy = yr

    @property
    def treasuryfundsymbol( self ):
        if isinstance( self.__treasuryfundsymbol, TreasuryAccountFundSymbol ):
            return self.__treasuryfundsymbol

    @treasuryfundsymbol.setter
    def treasuryfundsymbol( self, tafs ):
        if isinstance( tafs, TreasuryAccountFundSymbol ):
            self.__treasuryfundsymbol = tafs

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
    def ombagency( self ):
        if isinstance( self.__ombagency, str ) \
                and self.__ombagency != '':
            return self.__ombagency

    @ombagency.setter
    def ombagency( self, agency ):
        if isinstance( agency, str ) and agency != '':
            self.__ombagency = agency

    @property
    def treasuryagency( self ):
        if isinstance( self.__treasuryagency, str ) \
                and self.__treasuryagency != '':
            return self.__treasuryagency

    @treasuryagency.setter
    def treasuryagency( self, agency ):
        if isinstance( agency, str ) and agency != '':
            self.__treasuryagency = agency

    @property
    def linenumber( self ):
        if isinstance( self.__linenumber, str ) \
                and self.__linenumber != '':
            return self.__linenumber

    @linenumber.setter
    def linenumber( self, nbr ):
        if isinstance( nbr, str ) and nbr != '':
            self.__linenumber = nbr

    @property
    def linedescription( self ):
        if isinstance( self.__linedescription, str ) \
                and self.__linedescription != '':
            return self.__linedescription

    @linedescription.setter
    def linedescription( self, desc ):
        if isinstance( desc, str ) and desc != '':
            self.__linedescription = desc

    @property
    def sectionnumber( self ):
        if isinstance( self.__sectionnumber, str ) \
                and self.__sectionnumber != '':
            return self.__sectionnumber

    @sectionnumber.setter
    def sectionnumber( self, section ):
        if isinstance( section, str ) and section != '':
            self.__sectionnumber = section

    @property
    def sectiondescription( self ):
        if isinstance( self.__sectiondescription, str ) \
                and self.__sectiondescription != '':
            return self.__sectiondescription

    @sectiondescription.setter
    def sectiondescription( self, description ):
        if isinstance( description, str ) and description != '':
            self.__sectiondescription = description

    @property
    def subline( self ):
        if isinstance( self.__subline, str ) \
                and self.__subline != '':
            return self.__subline

    @subline.setter
    def subline( self, line ):
        if isinstance( line, str ) and line != '':
            self.__subline = line

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value

    def __init__( self, bfy, efy, ombaccount ):
        self.__bfy = bfy if isinstance( bfy, str ) else None
        self.__efy = efy if isinstance( efy, str ) else None
        self.__ombaccountcode = ombaccount if isinstance( ombaccount, str ) else None


class BudgetaryResourceExecution( ):
    '''BudgetaryResourceExecution( code ) initializes
    object representing MAX A-11 DE, SF-133'''

    __bfy = None
    __efy = None
    __treasuryfundsymbol = None
    __ombaccountcode = None
    __ombaccountname = None

    @property
    def bfy( self ):
        if isinstance( self.__bfy, str ) and self.__bfy != '':
            return self.__bfy

    @bfy.setter
    def bfy( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__bfy = yr

    @property
    def efy( self ):
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, yr ):
        if isinstance( yr, str ) and yr != '':
            self.__efy = yr

    @property
    def treasuryfundsymbol( self ):
        if isinstance( self.__treasuryfundsymbol, TreasuryAccountFundSymbol ):
            return self.__treasuryfundsymbol

    @treasuryfundsymbol.setter
    def treasuryfundsymbol( self, tafs ):
        if isinstance( tafs, TreasuryAccountFundSymbol ):
            self.__treasuryfundsymbol = tafs

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

    def __init__( self, bfy, efy, ombaccount ):
        self.__bfy = bfy if isinstance( bfy, str ) else None
        self.__efy = efy if isinstance( efy, str ) else None
        self.__ombaccountcode = ombaccount if isinstance( ombaccount, str ) else None


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


class FullTimeEquivalents( ):
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


class Defactos( ):
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
        if isinstance( self.__appropriationcode, str ) \
                and self.__appropriationcode != '':
            return self.__appropriationcode

    @appropriationcode.setter
    def appropriationcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__appropriationcode = code

    @property
    def subappropriationcode( self ):
        if isinstance( self.__subappropriationcode, str ) \
                and self.__subappropriationcode != '':
            return self.__subappropriationcode

    @subappropriationcode.setter
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
            self.__appropriationdescription = desc

    @property
    def fundgroup( self ):
        if isinstance( self.__fundgroup, str ) \
                and self.__fundgroup != '':
            return self.__fundgroup

    @fundgroup.setter
    def fundgroup( self, code ):
        if isinstance( code, str ) and code != '':
            self.__fundgroup = code

    @property
    def fundgroupname( self ):
        if isinstance( self.__fundgroupname, str ) \
                and self.__fundgroupname != '':
            return self.__fundgroupname

    @fundgroupname.setter
    def fundgroupname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__fundgroupname = name

    @property
    def documenttype( self ):
        if isinstance( self.__documenttype, str ) \
                and self.__documenttype != '':
            return self.__documenttype

    @documenttype.setter
    def documenttype( self, code ):
        if isinstance( code, str ) and code != '':
            self.__documenttype = code

    @property
    def transtype( self ):
        if isinstance( self.__transtype, str ) \
                and self.__transtype != '':
            return self.__transtype

    @transtype.setter
    def transtype( self, code ):
        if isinstance( code, str ) and code != '':
            self.__transtype = code

    @property
    def actualrecoverytranstype( self ):
        if isinstance( self.__actualrecoverytranstype, str ) \
                and self.__actualrecoverytranstype != '':
            return self.__actualrecoverytranstype

    @actualrecoverytranstype.setter
    def actualrecoverytranstype( self, code ):
        if isinstance( code, str ) and code != '':
            self.__actualrecoverytranstype = code

    @property
    def commitmentspendingcontrolflag( self ):
        if isinstance( self.__commitmentspendingcontrolflag, str ) \
                and self.__commitmentspendingcontrolflag != '':
            return self.__commitmentspendingcontrolflag

    @commitmentspendingcontrolflag.setter
    def commitmentspendingcontrolflag( self, flag ):
        if isinstance( flag, str ) and flag != '':
            self.__commitmentspendingcontrolflag = flag

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
    def estimatedrecoveriestranstype( self, code ):
        if isinstance( code, str ) and code != '':
            self.__estimatedrecoveriestranstype = code

    @property
    def estimatedreimbursementstranstype( self ):
        if isinstance( self.__estimatedreimbursementstranstype, str ) \
                and self.__estimatedreimbursementstranstype != '':
            return self.__estimatedreimbursementstranstype

    @estimatedreimbursementstranstype.setter
    def estimatedreimbursementstranstype( self, code ):
        if isinstance( code, str ) and code != '':
            self.__estimatedreimbursementstranstype = code

    @property
    def expensespendingcontrolflag( self ):
        if isinstance( self.__expensespendingcontrolflag, str ) \
                and self.__expensespendingcontrolflag != '':
            return self.__expensespendingcontrolflag

    @expensespendingcontrolflag.setter
    def expensespendingcontrolflag( self, flag ):
        if isinstance( flag, str ) and flag != '':
            self.__expensespendingcontrolflag = flag

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
    def originalbudgetedamount( self, amount ):
        if isinstance( amount, float ):
            self.__originalbudgetedamount = amount

    @property
    def apportionmentsposted( self ):
        if isinstance( self.__apportionmentsposted, float ):
            return self.__apportionmentsposted

    @apportionmentsposted.setter
    def apportionmentsposted( self, amount ):
        if isinstance( amount, float ):
            self.__apportionmentsposted = amount

    @property
    def totalauthority( self ):
        if isinstance( self.__totalauthority, float ):
            return self.__totalauthority

    @totalauthority.setter
    def totalauthority( self, amount ):
        if isinstance( amount, float ):
            self.__totalauthority = amount

    @property
    def totalbudgeted( self ):
        if isinstance( self.__totalbudgeted, float ):
            return self.__totalbudgeted

    @totalbudgeted.setter
    def totalbudgeted( self, amount ):
        if isinstance( amount, float ):
            self.__totalbudgeted = amount

    @property
    def totalpostedamount( self ):
        if isinstance( self.__totalpostedamount, float ):
            return self.__totalpostedamount

    @totalpostedamount.setter
    def totalpostedamount( self, amount ):
        if isinstance( amount, float ):
            self.__totalpostedamount = amount

    @property
    def fundswithdrawnprioryearamounts( self ):
        if isinstance( self.__fundswithdrawnprioryearamounts, float ):
            return self.__fundswithdrawnprioryearamounts

    @fundswithdrawnprioryearamounts.setter
    def fundswithdrawnprioryearamounts( self, amount ):
        if isinstance( amount, float ):
            self.__fundswithdrawnprioryearamounts = amount

    @property
    def fundinginamount( self ):
        if isinstance( self.__fundinginamount, float ):
            return self.__fundinginamount

    @fundinginamount.setter
    def fundinginamount( self, amount ):
        if isinstance( amount, float ):
            self.__fundinginamount = amount

    @property
    def fundingoutamount( self ):
        if isinstance( self.__fundingoutamount, float ):
            return self.__fundingoutamount

    @fundingoutamount.setter
    def fundingoutamount( self, amount ):
        if isinstance( amount, float ):
            self.__fundingoutamount = amount

    @property
    def totalaccrualrecoveries( self ):
        if isinstance( self.__totalaccrualrecoveries, float ):
            return self.__totalaccrualrecoveries

    @totalaccrualrecoveries.setter
    def totalaccrualrecoveries( self, amount ):
        if isinstance( amount, float ):
            self.__totalaccrualrecoveries = amount

    @property
    def totalactualreimbursements( self ):
        if isinstance( self.__totalactualreimbursements, float ):
            return self.__totalactualreimbursements

    @totalactualreimbursements.setter
    def totalactualreimbursements( self, amount ):
        if isinstance( amount, float ):
            self.__totalactualreimbursements = amount

    @property
    def totalagreementreimbursables( self ):
        if isinstance( self.__totalagreementreimbursables, float ):
            return self.__totalagreementreimbursables

    @totalagreementreimbursables.setter
    def totalagreementreimbursables( self, amount ):
        if isinstance( amount, float ):
            self.__totalagreementreimbursables = amount

    @property
    def totalcarriedforwardin( self ):
        if isinstance( self.__totalcarriedforwardin, float ):
            return self.__totalcarriedforwardin

    @totalcarriedforwardin.setter
    def totalcarriedforwardin( self, amount ):
        if isinstance( amount, float ):
            self.__totalcarriedforwardin = amount

    @property
    def totalcarriedforwardout( self ):
        if isinstance( self.__totalcarriedforwardout, float ):
            return self.__totalcarriedforwardout

    @totalcarriedforwardout.setter
    def totalcarriedforwardout( self, amount ):
        if isinstance( amount, float ):
            self.__totalcarriedforwardout = amount

    @property
    def totalestimatedrecoveries( self ):
        if isinstance( self.__totalestimatedrecoveries, float ):
            return self.__totalestimatedrecoveries

    @totalestimatedrecoveries.setter
    def totalestimatedrecoveries( self, amount ):
        if isinstance( amount, float ):
            self.__totalestimatedrecoveries = amount

    @property
    def totalestimatedreimbursements( self ):
        if isinstance( self.__totalestimatedreimbursements, float ):
            return self.__totalestimatedreimbursements

    @totalestimatedreimbursements.setter
    def totalestimatedreimbursements( self, amount ):
        if isinstance( amount, float ):
            self.__totalestimatedreimbursements = amount

    @property
    def totalexpenses( self ):
        if isinstance( self.__totalexpenses, float ):
            return self.__totalexpenses

    @totalexpenses.setter
    def totalexpenses( self, amount ):
        if isinstance( amount, float ):
            self.__totalexpenses = amount

    @property
    def totalexpenditureexpenses( self ):
        if isinstance( self.__totalexpenditureexpenses, float ):
            return self.__totalexpenditureexpenses

    @totalexpenditureexpenses.setter
    def totalexpenditureexpenses( self, amount ):
        if isinstance( amount, float ):
            self.__totalexpenditureexpenses = amount

    @property
    def totalexpenseaccruals( self ):
        if isinstance( self.__totalexpenseaccruals, float ):
            return self.__totalexpenseaccruals

    @totalexpenseaccruals.setter
    def totalexpenseaccruals( self, amount ):
        if isinstance( amount, float ):
            self.__totalexpenseaccruals = amount

    @property
    def totalprecommitments( self ):
        if isinstance( self.__totalprecommitments, float ):
            return self.__totalprecommitments

    @totalprecommitments.setter
    def totalprecommitments( self, amount ):
        if isinstance( amount, float ):
            self.__totalprecommitments = amount

    @property
    def unliquidatedprecommitments( self ):
        if isinstance( self.__unliquidatedprecommitments, float ):
            return self.__unliquidatedprecommitments

    @unliquidatedprecommitments.setter
    def unliquidatedprecommitments( self, amount ):
        if isinstance( amount, float ):
            self.__unliquidatedprecommitments = amount

    @property
    def totalobligations( self ):
        if isinstance( self.__totalobligations, float ):
            return self.__totalobligations

    @totalobligations.setter
    def totalobligations( self, amount ):
        if isinstance( amount, float ):
            self.__totalobligations = amount

    @property
    def unliquidatedobligations( self ):
        if isinstance( self.__unliquidatedobligations, float ):
            return self.__unliquidatedobligations

    @unliquidatedobligations.setter
    def unliquidatedobligations( self, amount ):
        if isinstance( amount, float ):
            self.__unliquidatedobligations = amount

    @property
    def voidedamount( self ):
        if isinstance( self.__voidedamount, float ):
            return self.__voidedamount

    @voidedamount.setter
    def voidedamount( self, amount ):
        if isinstance( amount, float ):
            self.__voidedamount = amount

    @property
    def totalusedamount( self ):
        if isinstance( self.__totalusedamount, float ):
            return self.__totalusedamount

    @totalusedamount.setter
    def totalusedamount( self, amount ):
        if isinstance( amount, float ):
            self.__totalusedamount = amount

    @property
    def availableamount( self ):
        if isinstance( self.__availableamount, float ):
            return self.__availableamount

    @availableamount.setter
    def availableamount( self, amount ):
        if isinstance( amount, float ):
            self.__availableamount = amount


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
    __accountcode = None
    __rccode = None
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
    __carryout = None
    __carryin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None


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
    __fundcode = None
    __fundname = None
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
    __carryout = None
    __carryin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None


class BudgetControls( ):
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


class CongressionalControls( ):
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


class Commitments( ):
    '''Defines the commitment class.'''
    __commitmentsid = None
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
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
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

    def __init__( self, amount ):
        self.__amount = amount if isinstance( amount, float ) else None
        self.__frame = pd.DataFrame

    def __str__( self ):
        if isinstance( self.__amount, float ):
            return str( self.__amount )


class OpenCommitments( ):
    '''Defines the commitment class.'''
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
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
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

    def __init__( self, amount ):
        self.__amount = float( amount )
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


class Obligations( ):
    '''Defines the commitment class.'''
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
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
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
    def id( self, cid ):
        if isinstance( cid, int ):
            self.__obligationsid = cid

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

    def __init__( self, amount ):
        self.__amount = float( amount )
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


class Deobligations( ):
    '''Defines the commitment class.'''
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
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
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
        if isinstance( self.__deobligationsid, int ):
            return self.__deobligationsid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__deobligationsid = iid

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


class UnliquidatedObligations( ):
    '''Defines the commitment class.'''
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
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
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
        if isinstance( self.__unliquidatedobligationsid, int ):
            return self.__unliquidatedobligationsid

    @id.setter
    def id( self, iid ):
        if isinstance( iid, int ):
            self.__unliquidatedobligationsid = iid

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

    def __init__( self, amount ):
        self.__amount = float( amount )
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


class Expenditures:
    '''Defines the commitment class.'''
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
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
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

    def __init__( self, amount ):
        self.__amount = float( amount )
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
