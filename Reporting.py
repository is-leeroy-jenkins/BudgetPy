

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

class Apportionment( ):
    '''Apportionment( code ) creates
    object representing Letters Of Apportionment'''

    __treasurysymbol = None
    __ombaccount = None
    __ombagency = None
    __treasuryagency = None
    __linenumber = None
    __linedescription = None
    __sectionnumber = None
    __sectiondescription = None
    __subline = None
    __amount = None

class BudgetaryResourceExecution( ):
    '''BudgetaryResourceExecution( code ) initializes
    object representing MAX A-11 DE, SF-133'''

    __treasurysymbol = None