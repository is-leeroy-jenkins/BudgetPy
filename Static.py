from enum import Enum, auto


class EXT( Enum ):
    '''Enumeration of database file extensions'''
    NS = auto( )
    DB = auto( )
    ACCDB = auto( )
    XLS = auto( )
    XLSM = auto( )
    XLSX = auto( )
    MDF = auto( )
    HTML = auto( )
    HTM = auto( )
    XHTML = auto( )
    XML = auto( )
    PNG = auto( )
    JPEG = auto( )
    SVG = auto( )


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
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    H = 7
    J = 8
    M = 9
    NS = 10


class Source( Enum ):
    '''enumeration of table names'''
    NS = auto( )
    Allocations = auto( )
    ApplicationTables = auto( )
    CarryoverEstimates = auto( )
    CarryoverSurvey = auto( )
    Changes = auto( )
    CongressionalReprogrammings = auto( )
    Deobligations = auto( )
    Defactos = auto( )
    DocumentControlNumbers = auto( )
    HumanResourceOrganizations = auto( )
    Obligations = auto( )
    OperatingPlans = auto( )
    OperatingPlanUpdates = auto( )
    ObjectClassOutlays = auto( )
    CarryoverOutlays = auto( )
    UnobligatedAuthority = auto( )
    QueryDefinitions = auto( )
    RegionalAuthority = auto( )
    SpendingRates = auto( )
    GrowthRates = auto( )
    ReimbursableAgreements = auto( )
    ReimbursableFunds = auto( )
    ReimbursableSurvey = auto( )
    Reports = auto( )
    BudgetControls = auto( )
    AppropriationDocuments = auto( )
    Apportionments = auto( )
    BudgetDocuments = auto( )
    BudgetOutlays = auto( )
    BudgetResourceExecution = auto( )
    Reprogrammings = auto( )
    SiteActivity = auto( )
    SiteProjectCodes = auto( )
    StatusOfFunds = auto( )
    Supplementals = auto( )
    Transfers = auto( )
    HeadquartersAuthority = auto( )
    TravelObligations = auto( )
    StatusOfAppropriations = auto( )
    StatusOfJobsActFunding = auto( )
    StatusOfSupplementalFunding = auto( )
    SuperfundSites = auto( )
    PayrollAuthority = auto( )
    TransTypes = auto( )
    ProgramFinancingSchedule = auto( )
    PayrollRequests = auto( )
    CarryoverRequests = auto( )
    CompassLevels = auto( )
    AdministrativeRequests = auto( )
    OpenCommitments = auto( )
    Expenditures = auto( )
    UnliquidatedObligations = auto( )
    UnobligatedAuthority = auto( )
    '''Reference Models'''
    Accounts = auto( )
    ActivityCodes = auto( )
    AllowanceHolders = auto( )
    Appropriations = auto( )
    BudgetObjectClasses = auto( )
    CostAreas = auto( )
    CPIC = auto( )
    Divisions = auto( )
    Documents = auto( )
    FederalHolidays = auto( )
    FinanceObjectClasses = auto( )
    FiscalYears = auto( )
    FiscalYearsBackUp = auto( )
    Funds = auto( )
    FundSymbols = auto( )
    Goals = auto( )
    GsPayScale = auto( )
    HeadquartersOffices = auto( )
    Images = auto( )
    Messages = auto( )
    NationalPrograms = auto( )
    Objectives = auto( )
    Organizations = auto( )
    ProgramAreas = auto( )
    ProgramDescriptions = auto( )
    ProgramProjects = auto( )
    Projects = auto( )
    Providers = auto( )
    PublicLaws = auto( )
    ReferenceTables = auto( )
    RegionalOffices = auto( )
    ResourcePlanningOffices = auto( )
    ResponsibilityCenters = auto( )
    SchemaTypes = auto( )
    Sources = auto( )
    StateOrganizations = auto( )
    WorkCodes = auto( )


class Provider( Enum ):
    '''enumeration of data providers'''
    SQLite = 0
    SqlServer = 1
    Access = 2
    Excel = 3
    CSV = 4
    NS = 5


class ParamStyle( Enum ):
    '''Enumeration of paramstyles'''
    format = 1
    number = 2
    pyformat = 3
    name = 4
    qmark = 5
    NS = 6


class Command( Enum ):
    '''enumeration of sql commands'''
    ALL = 0
    SELECT = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
    DROPTABLE = 5
    DROPVIEW = 6
    CREATETABLE = 7
    CREATEVIEW = 8
    ALTERTABLE = 9
    ALTERCOLUMN = 10


class Client( Enum ):
    '''Enumeration of auxiliary applications'''
    NS = auto( )
    SQLite = auto( )
    Access = auto( )
    Excel = auto( )
    Linq = auto( )
    Edge = auto( )
    Chrome = auto( )
