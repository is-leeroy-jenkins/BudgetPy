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
    Actuals = auto( )
    Allocations = auto( )
    ApplicationTables = auto( )
    CarryoverEstimates = auto( )
    CarryoverSurvey = auto( )
    Changes = auto( )
    CongressionalReprogrammings = auto( )
    Deobligations = auto( )
    Defactos = auto( )
    DocumentControlNumbers = auto( )
    DataRuleDescriptions = auto( )
    HumanResourceOrganizations = auto( )
    Obligations = auto( )
    OperatingPlans = auto( )
    OperatingPlanUpdates = auto( )
    ObjectClassOutlays = auto( )
    CarryoverOutlays = auto( )
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
    StateGrantObligations = auto( )
    SuperfundSites = auto( )
    PayrollAuthority = auto( )
    PayrollActivity = auto( )
    TransTypes = auto( )
    ProgramFinancingSchedule = auto( )
    PayrollRequests = auto( )
    FullTimeEquivalents = auto( )
    CarryoverRequests = auto( )
    CompassLevels = auto( )
    AdministrativeRequests = auto( )
    OpenCommitments = auto( )
    Expenditures = auto( )
    UnliquidatedObligations = auto( )
    UnobligatedAuthority = auto( )
    MonthlyOutlays = auto( )
    CongressionalControls = auto( )
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
    SELECT = 0
    SELECTALL = 1
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
    ControlPanel = auto( )
    Calculator = auto( )


class PNG( Enum ):
    '''Enumeration of images'''
    NS = auto( )
    Attachment = auto( )
    Access = auto( )
    Adobe = auto( )
    Authority = auto( )
    Appropriation = auto( )
    Add = auto( )
    BFY = auto( )
    Browse = auto( )
    BOC = auto( )
    Budget = auto( )
    Calculator = auto( )
    ControlPanel = auto( )
    CategoricalGrants = auto( )
    Cancel = auto( )
    Calendar = auto( )
    Chart = auto( )
    CSV = auto( )
    Chrome = auto( )
    Contracts = auto( )
    Database = auto( )
    DatabaseAdd = auto( )
    DatabaseDelete = auto( )
    DatabaseRefresh = auto( )
    DatabaseVerify = auto( )
    DatabaseSql = auto( )
    Datagrid = auto( )
    Delete = auto( )
    EFY = auto( )
    Edge = auto( )
    Edit = auto( )
    Excel = auto( )
    Export = auto( )
    Expenses = auto( )
    Filter = auto( )
    File = auto( )
    FileAdd = auto( )
    FileBrowse = auto( )
    FileCopy = auto( )
    FileEdit = auto( )
    FileVerify = auto( )
    FileTransfer = auto( )
    FileWriter = auto( )
    FileReader = auto( )
    FileDelete = auto( )
    FileSearch = auto( )
    First = auto( )
    Folder = auto( )
    FolderBrowse = auto( )
    FolderCopy = auto( )
    FolderDownload = auto( )
    FolderOpen = auto( )
    FolderCompress = auto( )
    Function = auto( )
    FTE = auto( )
    G0 = auto( )
    Google = auto( )
    Grants = auto( )
    Guidance = auto( )
    Home = auto( )
    Import = auto( )
    Left = auto( )
    Last = auto( )
    LUST = auto( )
    Levels = auto( )
    LogOut = auto( )
    Ledger = auto( )
    Menu = auto( )
    Next = auto( )
    No = auto( )
    OK = auto( )
    Play = auto( )
    Print = auto( )
    Previous = auto( )
    PDF = auto( )
    Recycle = auto( )
    Redo = auto( )
    Right = auto( )
    Remove = auto( )
    Refresh = auto( )
    Row = auto( )
    RowCopy = auto( )
    RowEdit = auto( )
    RowDelete = auto( )
    RowInsert = auto( )
    Recert = auto( )
    Save = auto( )
    Scan = auto( )
    Sigma = auto( )
    Spreadsheet = auto( )
    Sort = auto( )
    Statistics = auto( )
    Sharepoint = auto( )
    Site = auto( )
    SiteTravel = auto( )
    Text = auto( )
    Table = auto( )
    TableAdd = auto( )
    TableDelete = auto( )
    TableSettings = auto( )
    Travel = auto( )
    TSCA = auto( )
    Undo = auto( )
    WCF = auto( )
    WIFIA = auto( )
    Windows = auto( )
    Word = auto( )
    XML = auto( )
    Yes = auto( )


class RPIO( Enum ):
    '''Enumeration of Resource Planning and Implementation Offices'''
    NS = 0
    R1 = 01
    R2 = 02
    R3 = 03
    R4 = 04
    R5 = 05
    R6 = 06
    R7 = 07
    R8 = 08
    R9 = 09
    R10 = 10
    OA = 11
    OITA = 13
    OMS = 16
    OCFO = 17
    OCSPP = 20
    OAR = 27
    OW = 30
    OIG = 35
    OGC = 39
    OLEM = 75
    OECA = 77
