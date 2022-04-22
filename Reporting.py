from Execution import *
from Static import *
from Ninja import *


''' Apportionment( bfy, efy, code ) '''
class Apportionment( ):
    '''Apportionment( value ) creates
    object representing Letters Of Apportionment'''
    __apportionmentsid = None
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
        if isinstance( self.__treasuryfundsymbol, str ) and self.__treasuryfundsymbol != "":
            return self.__treasuryfundsymbol

    @treasuryfundsymbol.setter
    def treasuryfundsymbol( self, tafs ):
        if isinstance( tafs, str ) and tafs != '':
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


''' BudgetaryResourceExecution( bfy, efy, code ) '''
class BudgetaryResourceExecution( ):
    '''BudgetaryResourceExecution( value ) initializes
    object representing MAX A-11 DE, SF-133'''
    __budgetaryresourceexecutionid = None
    __bfy = None
    __efy = None
    __treasuryfundsymbol = None
    __ombaccountcode = None
    __ombaccountname = None

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
        if isinstance( self.__treasuryfundsymbol, str ) and self.__treasuryfundsymbol != '':
            return self.__treasuryfundsymbol

    @treasuryfundsymbol.setter
    def treasuryfundsymbol( self, tafs ):
        if isinstance( tafs, str ) and tafs != '':
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


''' CarryoverEstimates( bfy, efy, code ) '''
class CarryoverEstimates( ):
    '''CarryoverEstimates( bfy ) initializes object bfy
    providing Carryover Estimate data for'''
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
    def accountcode( self, code ):
        if isinstance( code, str ) and code != '':
            self.__accountcode = code

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
    def orgcode( self ):
        if isinstance( self.__orgcode, str ) and self.__orgcode != '':
            return self.__orgcode

    @orgcode.setter
    def orgcode( self, code ):
        if isinstance( code, str) and code != '':
            self.__orgcode = code

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
        '''Initializes the PRC class'''
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None

    def __str__( self ):
        if isinstance( self.__code ) and self.__code != '':
            return self.__code

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Allocations
        command = Command.SELECTALL
        names = [ 'BFY',  ]
        values = ( self.__bfy, )
        df = DataFactory( provider, source, command, names, values )
        self.__data = df.create( )
        return self.__data


''' CarryoverSurvey( bfy, efy, code ) '''
class CarryoverSurvey( ):
    '''CarryoverSurvey( bfy ) initializes object
    providing carryover survey data'''
    __carryoversurveyid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
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
    def fundname( self ):
        if isinstance( self.__fundname, str ) and self.__fundname != '':
            return self.__fundname

    @fundname.setter
    def fundname( self, name ):
        if isinstance( name, str ) and name != '':
            self.__fundname = name

    @property
    def amount( self ):
        if isinstance( self.__amount, float):
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if isinstance( value, float ):
            self.__amount = value


''' StatusOfAppropriations( bfy, efy, code ) '''
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


''' MonthlyOutlays( bfy, efy, code ) '''
class MonthlyOutlays( ):
    '''object provides OMB outlay data'''
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


class SpendingRates( ):
    '''object provides OMB spending rate data'''
    __spendingratesid = None


class ReimbursableSurvey( ):
    '''object provides Reimbursable Authority data'''
    __reimbursablesurveyid = None


class ObjectClassOutlays( ):
    '''object provides OMB outlay data'''
    __objectclassoutlaysid = None


class UnobligatedAuthority( ):
    '''object provides OMB data'''
    __unobligatedauthorityid = None


class GrossBudgetAuthorityOutlays( ):
    '''object provides OMB data'''
    __grossbudgetauthorityoutlaysid = None


class GrowthRates( ):
    ''' object provides OMB data'''
    __growthratesid = None


class DataRuleDescriptions( ):
    ''' object provides OMB MAX A11 rule data '''
    __dataruledescriptionsid = None


class CarryoverOutlays( ):
    ''' object provides OMB data '''
    __carryoveroutlaysid = None