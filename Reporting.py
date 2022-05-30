from Control import *

# Apportionment( bfy, efy, code )
class Apportionment( ):
    '''Apportionment( bfy, efy, omb )
    initializes object representing Letters Of Apportionment'''
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

    def __init__( self, bfy, efy, omb ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__ombaccountcode = omb if isinstance( omb, str ) and len( omb ) == 4 else None

    def getdata( self ):
        source = Source.Apportionments
        provider = Provider.SQLite
        n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
        v = ( self.__bfy, self.__efy, self.__ombaccountcode )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# BudgetaryResourceExecution( bfy, efy, code )
class BudgetaryResourceExecution( ):
    '''BudgetaryResourceExecution( bfy, efy, code )
    initializes object representing MAX A-11 DE, SF-133'''
    __budgetaryresourceexecutionid = None
    __bfy = None
    __efy = None
    __treasuryfundsymbol = None
    __ombaccountcode = None
    __ombaccountname = None
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

    def __init__( self, bfy, efy, code ):
        self.__bfy = bfy if isinstance( bfy, str ) else None
        self.__efy = efy if isinstance( efy, str ) else None
        self.__ombaccountcode = code if isinstance( code, str ) and len( code ) == 4 else None

    def getdata( self ):
        source = Source.BudgetResourceExecution
        provider = Provider.SQLite
        n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
        v = ( self.__bfy, self.__efy, self.__ombaccountcode )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# CarryoverEstimates( bfy )
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

    def __init__( self, bfy ):
        '''Initializes the PRC class'''
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None

    def __str__( self ):
        if isinstance( self.__unobligatedauthority, float ):
            return str( self.__unobligatedauthority )

    def getdata( self ):
        source = Source.UnobligatedAuthority
        provider = Provider.SQLite
        n = [ 'BFY', 'EFY' ]
        v = ( self.__bfy, self.__efy )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# CarryoverSurvey( bfy, efy, fund )
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

    def __init__( self, bfy, efy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        source = Source.CarryoverSurvey
        provider = Provider.SQLite
        n = [ 'BFY', 'EFY', 'FundCode', ]
        v = ( self.__bfy, self.__efy, self.__fundcode )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# StatusOfAppropriations( bfy, efy, fund )
class StatusOfAppropriations( ):
    '''StatusOfAppropriations( bfy, efy, fund )
    object representing Appropriation-level execution data'''
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
        if isinstance( self.__appropriationcreationdate, dt.datetime ):
            return self.__appropriationcreationdate

    @appropriationcreationdate.setter
    def appropriationcreationdate( self, value ):
        if isinstance( value, dt.datetime ):
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

    def __init__( self, bfy, efy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__appropriationfundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        source = Source.StatusOfAppropriations
        provider = Provider.SQLite
        n = [ 'BFY', 'EFY', 'AppropriationFundCode', ]
        v = ( self.__bfy, self.__efy, self.__appropriationfundcode )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# MonthlyOutlays( bfy, efy, account )
class MonthlyOutlays( ):
    '''MonthlyOutlays( bfy, efy, omb ) initializes
    object providing OMB outlay data'''
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

    def __init__( self, bfy, efy, account ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) <= 5 else None

    def getdata( self ):
        source = Source.MonthlyOutlays
        provider = Provider.SQLite
        n = [ 'BFY', 'EFY', 'OmbAccountCode', ]
        v = ( self.__bfy, self.__efy, self.__ombaccountcode )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# SpendingRates( account )
class SpendingRates( ):
    '''SpendingRates( code ) initializes
    object providing OMB spending rate data'''
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

    def __init__( self, account ):
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None

    def getdata( self ):
        provider = Provider.SQLite
        source = Source.Apportionments
        command = SQL.SELECTALL
        names = [ 'OmbAccountCode', ]
        values = ( self.__ombaccountcode, )
        data = DataFactory( provider, source, command, names, values )
        self.__data = data.create( )
        return self.__data


# ReimbursableSurvey( bfy, fund )
class ReimbursableSurvey( ):
    '''ReimbursableSurvey( bfy, fund ) initializes
    object providing Reimbursable Authority data'''
    __reimbursablesurveyid = None
    __bfy = None
    __fundcode = None
    __fundname = None
    __amount = None
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

    def __init__( self, bfy, efy, fund ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None

    def getdata( self ):
        source = Source.ReimbursableSurvey
        provider = Provider.SQLite
        n = [ 'BFY', 'FundCode', ]
        v = ( self.__bfy, self.__fundcode )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# ObjectClassOutlays( account )
class ObjectClassOutlays( ):
    '''ObjectClassOutlays( bfy, omb )
    object provides OMB outlay data'''
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

    def __init__( self, account ):
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None

    def getdata( self ):
        source = Source.ObjectClassOutlays
        provider = Provider.SQLite
        n = [ 'OmbAccountCode', ]
        v = ( self.__ombaccountcode, )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# UnobligatedAuthority( account )
class UnobligatedAuthority( ):
    '''UnobligatedAuthority( bfy, omb )
    object provides OMB data'''
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

    def __init__( self, account ):
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None

    def getdata( self ):
        source = Source.MonthlyOutlays
        provider = Provider.SQLite
        n = [ 'OmbAccountCode', ]
        v = ( self.__ombaccountcode, )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# BudgetOutlays( account )
class BudgetOutlays( ):
    '''BudgetOutlays( bfy, omb )
    object provides OMB data'''
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

    def __init__( self, account ):
        self.__ombaccountcode = account if isinstance( account, str ) and len( account ) == 4 else None

    def getdata( self ):
        source = Source.BudgetOutlays
        provider = Provider.SQLite
        n = [ 'OmbAccountCode', ]
        v = ( self.__ombaccountcode, )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# GrowthRates( bfy, id )
class GrowthRates( ):
    '''GrowthRates( bfy, id )
    initializes object providing OMB growth rate data'''
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

    def __init__( self, bfy, id ):
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__rateid = id if isinstance( id, str ) and id != '' else None

    def getdata( self ):
        source = Source.MonthlyOutlays
        provider = Provider.SQLite
        n = [ 'BFY', 'RateId', ]
        v = ( self.__bfy, self.__rateid )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


# DataRuleDescription( schedule, line, rule )
class DataRuleDescription( ):
    ''' DataRuleDescription( schedule, line, rule )
    initializes object providing OMB MAX A11 rule data '''
    __dataruledescriptionsid = None
    __schedule = None
    __linenumber = None
    __rulenumber = None
    __ruledescription = None
    __scheduleorder = None

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

    def __init__( self, schedule, line, rule ):
        self.__schedule = schedule if isinstance( schedule, str ) and schedule != '' else None
        self.__linenumber = line if isinstance( line, str ) and line != '' else None
        self.__rulenumber = rule if isinstance( rule, str ) and rule != '' else None

    def getdata( self ):
        source = Source.DataRuleDescriptions
        provider = Provider.SQLite
        n = [ 'Schedule', 'LineNumber', 'RuleNumber' ]
        v = ( self.__schedule, self.__linenumber, self.__rulenumber )
        dconfig = DataConfig( source, provider )
        sconfig = SqlConfig( names = n, values = v )
        cnx = DataConnection( dconfig )
        sql = SqlStatement( dconfig, sconfig )
        sqlite = cnx.connect( )
        cursor = sqlite.cursor( )
        query = sql.getcommandtext( )
        data = cursor.execute( query )
        self.__data =  [ i for i in data.fetchall( ) ]
        cursor.close( )
        sqlite.close( )
        return self.__data


class CarryoverOutlays( ):
    ''' object provides OMB data '''
    __carryoveroutlaysid = None

    @property
    def id( self ):
        if isinstance( self.__carryoveroutlaysid, int ):
            return self.__carryoveroutlaysid

    @id.setter
    def id( self, value ):
        if isinstance( value, int ):
            self.__carryoveroutlaysid = value


