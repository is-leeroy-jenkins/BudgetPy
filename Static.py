'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Static.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Static.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2023  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Static.py
  </summary>
  ******************************************************************************************
  '''
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
    '''
    Constructor:  BOC.Member

    Purpose:  Enumeration of object class codes'''

    PAYROLL = 10
    FTE = 17
    EXPENSES = 36
    CONTRACTS = 37
    WCF = 38
    GRANTS = 41

class NPM( Enum ):
    '''
    Constructor:  NPM.Member

    Purpose:  Enumeration of NPM Codes'''
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    H = 7
    J = 8
    M = 9
    Y = 10
    W = 11

class Source( Enum ):
    '''
    Constructor:  Source.Member

    Purpose:  Enumeration of table_name column_names
    '''
    NS = auto( )
    Actuals = auto( )
    AdministrativeRequests = auto( )
    Allocations = auto( )
    AmericanRescuePlan = auto( )
    AnnualCarryoverEstimates = auto( )
    AnnualReimbursableEstimates = auto( )
    AppropriationAvailableBalances = auto( )
    AppropriationDocuments = auto( )
    AppropriationLevelAuthority = auto( )
    BudgetDocuments = auto( )
    CarryoverApportionments = auto( )
    CarryoverRequests = auto( )
    Changes = auto( )
    CompassLevels = auto( )
    CongressionalReprogrammings = auto( )
    Defactos = auto( )
    Deobligations = auto( )
    DocumentControlNumbers = auto( )
    Earmarks = auto( )
    Expenditures = auto( )
    FullTimeEquivalents = auto( )
    PayPeriods = auto( )
    PayrollAuthority = auto( )
    PayrollRequests = auto( )
    PRC = auto( )
    QueryDefinitions = auto( )
    RegionalAuthority = auto( )
    RecoveryAct = auto( )
    ReimbursableAgreements = auto( )
    ReimbursableFunds = auto( )
    Reports = auto( )
    HeadquartersAuthority = auto( )
    InflationReductionActCarryoverEstimates = auto( )
    JobsActCarryoverEstimates = auto( )
    MonthlyLedgerAccountBalances = auto( )
    MonthlyActuals = auto( )
    ObligationActivity = auto( )
    Obligations = auto( )
    Outlays = auto( )
    OpenCommitments = auto( )
    SiteActivity = auto( )
    SpecialAccounts = auto( )
    SpendingRates = auto( )
    SpendingDocuments = auto( )
    StateGrantObligations = auto( )
    StatusOfAppropriations = auto( )
    StatusOfBudgetaryResources = auto( )
    StatusOfEarmarks = auto( )
    StatusOfFunds = auto( )
    StatusOfJobsActFunding = auto( )
    StatusOfInflationReductionActFunds = auto( )
    StatusOfSupplementalFunding = auto( )
    SuperfundSites = auto( )
    SupplementalCarryoverEstimates = auto( )
    TransferActivity = auto( )
    Transfers = auto( )
    UnliquidatedObligations = auto( )
    UnobligatedBalances = auto( )
    '''Reference Models: data tables used to describe 
    elements of the account code structure'''
    AccountingEvents = auto( )
    Accounts = auto( )
    ActivityCodes = auto( )
    AllowanceHolders = auto( )
    ApportionmentData = auto( )
    ApplicationTables = auto( )
    Appropriations = auto( )
    BudgetaryResourceExecution = auto( )
    BudgetContacts = auto( )
    BudgetControls = auto( )
    BudgetObjectClasses = auto( )
    CapitalPlanningInvestmentCodes = auto( )
    ColumnSchema = auto( )
    CompassErrors = auto( )
    CongressionalControls = auto( )
    CostAreas = auto( )
    DataRuleDescriptions = auto( )
    Documents = auto( )
    FederalHolidays = auto( )
    FinanceObjectClasses = auto( )
    FiscalYears = auto( )
    FundCategories = auto( )
    Funds = auto( )
    FundSymbols = auto( )
    GeneralLedgerAccounts = auto( )
    Goals = auto( )
    GrowthRates = auto( )
    GsPayScales = auto( )
    HeadquartersOffices = auto( )
    Images = auto( )
    Messages = auto( )
    MonthlyOutlays = auto( )
    NationalPrograms = auto( )
    Objectives = auto( )
    OperatingPlans = auto( )
    OperatingPlanUpdates = auto( )
    Organizations = auto( )
    ProgramAreas = auto( )
    ProgramProjectDescriptions = auto( )
    ProgramProjects = auto( )
    Projects = auto( )
    Providers = auto( )
    PublicLaws = auto( )
    ReferenceTables = auto( )
    RegionalOffices = auto( )
    ResourcePlanningOffices = auto( )
    Resources = auto( )
    ResponsibilityCenters = auto( )
    SchemaTypes = auto( )
    StateOrganizations = auto( )
    SubAppropriations = auto( )
    TransTypes = auto( )
    URL = auto( )

class Provider( Enum ):
    '''
    Constructor:  Provider.Member

    Purpose:  Enumeration of data providers
    '''
    SQLite = 0
    Access = 1
    SqlServer = 2
    Excel = 3
    CSV = 4

class Model( Enum ):
    '''
    Constructor:  Model.Member

    Purpose:  Enumeration of model types
    '''
    Data = auto( )
    Reference = auto( )

class ParamStyle( Enum ):
    '''
    Constructor:  ParamStyle( )

    Purpose:  Enumeration of parameter styles
    '''
    format = 1
    number = 2
    pyformat = 3
    name = 4
    qmark = 5
    NS = 6

class SQL( Enum ):
    '''
    Constructor:  SQL.Member

    Purpose:   Enumeration of sql commands
    '''
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

class APP( Enum ):
    '''
    Constructor:  APP.Member

    Purpose:  Enumeration of auxiliary applications
    '''
    SQLite = auto( )
    Access = auto( )
    Excel = auto( )
    Linq = auto( )
    Edge = auto( )
    Chrome = auto( )
    ControlPanel = auto( )
    Calculator = auto( )

class PNG( Enum ):
    '''
    Constructor:  PNG.Member

    Pupose:  Enumeration of images
    '''
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
    Recertification = auto( )
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

class ICO( Enum ):
    '''
    Constructor:  ICO.Member

    Purpose:  Enumeration of ICO files
    '''
    NS = auto( )
    Access = auto( )
    Browse = auto( )
    CSV = auto( )
    Database = auto( )
    Error = auto( )
    Excel = auto( )
    Ninja = auto( )
    Notification = auto( )
    PDF = auto( )
    Text = auto( )

class RPIO( Enum ):
    '''
    Constructor:  RPIO.Member

    Pupose:  Enumeration of Resource Planning and Implementation Offices
    '''
    NS = 0
    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    R6 = 6
    R7 = 7
    R8 = 8
    R9 = 9
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

class ACCDB( Enum ):
    '''
    Constructor:  ACCDB.Member

    Purpose:  Enumeration of access database types used in the application
    '''
    INTEGER = auto( )
    NUMBER = auto( )
    AUTONUMBER = auto( )
    CURRENCY = auto( )
    DATETIME = auto( )
    HYPERLINK = auto( )
    SHORTTEXT = auto( )
    LONGTEXT = auto( )
    RICHTEXT = auto( )
    ATTACHMENT = auto( )
    CALCULATED = auto( )

class DB( Enum ):
    '''
    Constructor:  DB.Member

    Purpose:  Enumeration of SQLite database types used in the application
    '''
    REAL = auto( )
    TEXT = auto( )
    INTEGER = auto( )
    BLOB = auto( )

class MDF( Enum ):
    '''
    Constructor:  MDF.Member

    Purpose:  Enumeration of SQL Server database types used in the application
    '''
    BIT = auto( )
    INT = auto( )
    DECIMAL = auto( )
    MONEY = auto( )
    DATE = auto( )
    TIME = auto( )
    DATETIME = auto( )
    FLOAT = auto( )
    CHAR = auto( )
    TEXT = auto( )
    NCHAR = auto( )
    NTEXT = auto( )
    VARCHAR = auto( )
    NVARCHAR = auto( )
    BINARY = auto( )
    VARBINARY = auto( )
    IMAGE = auto( )
    DATETIMEOFFSET = auto( )
