

class TreasuryAccountFundSymbol( ):
    '''TreasuryAccountFundSymbol( code )
    creates object that represents a TAFS'''

    __ombagencycode = None
    __treasuryagencycode = None
    __bfy = None
    __efy = None
    __ombaccountcode = None
    __ombaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None

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

    def __init__( self, bfy, efy, trescode ):
        self.__bfy = bfy if isinstance( bfy, str ) else None
        self.__efy = efy if isinstance( efy, str ) else None
        self.__treasuryaccountcode = trescode if isinstance( trescode, str ) else None

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
    def sectionnumber( self, secno ):
        if isinstance( secno, str ) and secno != '':
            self.__sectionnumber = secno

    @property
    def sectiondescription( self ):
        if isinstance( self.__sectiondescription, str ) \
                and self.__sectiondescription != '':
            return self.__sectiondescription

    @sectiondescription.setter
    def sectiondescription( self, secdesc ):
        if isinstance( secdesc, str ) and secdesc != '':
            self.__sectiondescription = secdesc

    @property
    def subline( self ):
        if isinstance( self.__subline, str )\
                and self.__subline != '':
            return self.__subline

    @subline.setter
    def subline( self, sub ):
        if isinstance( sub, str ) and sub != '':
            self.__subline = sub

    @property
    def amount( self ):
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, amt ):
        if isinstance( amt, float ):
            self.__amount = amt

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
