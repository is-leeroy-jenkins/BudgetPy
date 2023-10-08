CREATE TABLE dbo.AccountingEvents
(
	AccountingEventsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name nvarchar(80) NULL DEFAULT ('NS'),
    CONSTRAINT AccountingEventsPrimaryKeyPrimaryKey PRIMARY KEY
    (
        AccountingEvents ASC
    )
) ;

CREATE TABLE dbo.Accounts
(
	AccountsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	ActivityCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ActivityName NVARCHAR(80) NULL DEFAULT ('NS'),
	AgencyActivity NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT AccountsPrimaryKey PRIMARY KEY 
    (
        AccountsId ASC
    )
) ;

CREATE TABLE dbo.ActivityCodes
(
	ActivityId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NOT NULL,
	Name NVARCHAR(50) NULL DEFAULT ('NS'),
	Description NVARCHAR(50) NULL DEFAULT ('NS'),
    CONSTRAINT ActivityCodesPrimaryKey PRIMARY KEY 
    (
        ActivityId ASC
    )
) ;

CREATE TABLE dbo.Actuals
(
	ActualsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationName NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAppropriationName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioActivityCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioActivityName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Balance FLOAT NULL DEFAULT (0.0),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalCode NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalName NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL ('NS'),
    CONSTRAINT ActualsPrimaryKey PRIMARY KEY 
    (
        ActualsId ASC
    )
) ;

CREATE TABLE dbo.AdministrativeRequests
(
	AdministrativeRequestsId INT NOT NULL UNIQUE,
	RequestId FLOAT NULL DEFAULT (0.0),
	Analyst NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	Status NVARCHAR(80) NULL DEFAULT ('NS'),
	OriginalRequestDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	Duration FLOAT NULL DEFAULT (0.0),
	BudgetFormulationSystem NVARCHAR(80) NULL DEFAULT ('NS'),
	Comments NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	RequestDocument NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	RequestType NVARCHAR(80) NULL DEFAULT ('NS'),
	TypeCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Decision NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT AdministrativeRequestsPrimaryKey PRIMARY KEY 
    (
        AdministrativeRequestsId ASC
    )
) ;

CREATE TABLE dbo.AggregateOutlays
(
	MonthlyAggregatesId INT NOT NULL UNIQUE,
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	MainAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	October FLOAT NULL DEFAULT (0.0),
	November FLOAT NULL DEFAULT (0.0),
	December FLOAT NULL DEFAULT (0.0),
	January FLOAT NULL DEFAULT (0.0),
	Feburary FLOAT NULL DEFAULT (0.0),
	March FLOAT NULL DEFAULT (0.0),
	April FLOAT NULL DEFAULT (0.0),
	May FLOAT NULL DEFAULT (0.0),
	June FLOAT NULL DEFAULT (0.0),
	July FLOAT NULL DEFAULT (0.0),
	August FLOAT NULL DEFAULT (0.0),
	September FLOAT NULL DEFAULT (0.0),
    CONSTRAINT AggregateOutlaysPrimaryKey PRIMARY KEY 
    (
        MonthlyAggregatesId ASC
    )
) ;

CREATE TABLE dbo.Allocations
(
	AllocationsId INT NOT NULL UNIQUE,
	StatusOfFundsId int NOT NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT AllocationsPrimaryKey PRIMARY KEY 
    (
        AllocationsId ASC
    )
);

CREATE TABLE dbo.AllowanceHolders
(
	AllowanceHoldersId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT AllowanceHoldersPrimaryKey PRIMARY KEY 
	(
		AllowanceHoldersId ASC
	)
);

CREATE TABLE dbo.AmericanRescuePlanCarryoverEstimates
(
	AmericanRescuePlanCarryoverEstimatesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Estimate FLOAT NULL DEFAULT (0.0),
	CONSTRAINT AmericanRescuePlanCarryoverEstimatesPrimaryKey PRIMARY KEY 
	(
		AmericanRescuePlanCarryoverEstimatesId ASC
	)
) ;

CREATE TABLE dbo.AnnualCarryoverEstimates
(
	AnnualCarryoverEstimatesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Estimate FLOAT NULL DEFAULT (0.0),
	CONSTRAINT AnnualCarryoverEstimatesPrimaryKey PRIMARY KEY 
	(
		AnnualCarryoverEstimatesId ASC
	)
);

CREATE TABLE dbo.AnnualReimbursableEstimates
(
	AnnualReimbursableEstimatesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Estimate FLOAT NULL DEFAULT (0.0),
	CONSTRAINT AnnualReimbursableEstimatesPrimaryKey PRIMARY KEY 
	(
		AnnualReimbursableEstimatesId ASC
	)
);

CREATE TABLE dbo.ApplicationTables
(
	ApplicationTablesId INT NOT NULL UNIQUE,
	TableName NVARCHAR(80) NULL DEFAULT ('NS'),
	Model NVARCHAR(80) NULL DEFAULT ('NS'),
	Title NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT ApplicationTablesPrimaryKey PRIMARY KEY 
	(
		ApplicationTablesId ASC
	) 
);

CREATE TABLE dbo.ApportionmentData
(
	ApportionmentDataId INT NOT NULL UNIQUE,
	FiscalYear NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	AvailabilityType NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	ApprovalDate DATETIME NULL,
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	LineName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT ApportionmentDataPrimaryKey PRIMARY KEY 
	(
		ApportionmentDataId ASC
	)
);

CREATE TABLE dbo.AppropriationAvailableBalances
(
	AppropriationAvailableBalancesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	OriginalAmount FLOAT NULL DEFAULT (0.0),
	Authority FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	CarryoverIn FLOAT NULL DEFAULT (0.0),
	CarryoverOut FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	CONSTRAINT AppropriationAvailableBalancesPrimaryKey PRIMARY KEY 
	(
		AppropriationAvailableBalancesId ASC
	)
);

CREATE TABLE dbo.AppropriationDocuments
(
	AppropriationDocumentsId INT NOT NULL UNIQUE,
	FiscalYear NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationFund NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentDate DATETIME NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetingControls NVARCHAR(80) NULL DEFAULT ('NS'),
	PostingControls NVARCHAR(80) NULL DEFAULT ('NS'),
	PreCommitmentControls NVARCHAR(80) NULL DEFAULT ('NS'),
	CommitmentControls NVARCHAR(80) NULL DEFAULT ('NS'),
	ObligationControls NVARCHAR(80) NULL DEFAULT ('NS'),
	AccrualControls NVARCHAR(80) NULL DEFAULT ('NS'),
	ExpenditureControls NVARCHAR(80) NULL DEFAULT ('NS'),
	ExpenseControls NVARCHAR(80) NULL DEFAULT ('NS'),
	ReimbursementControls NVARCHAR(80) NULL DEFAULT ('NS'),
	ReimbursableAgreementControls NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	CarryoverOut FLOAT NULL DEFAULT (0.0),
	CarryoverIn FLOAT NULL DEFAULT (0.0),
	Reimbursements FLOAT NULL DEFAULT (0.0),
	Recoveries FLOAT NULL DEFAULT (0.0),
	CONSTRAINT AppropriationDocumentsPrimaryKey PRIMARY KEY 
	(
		AppropriationDocumentsId ASC
	)
);

CREATE TABLE dbo.AppropriationLevelAuthority
(
	AppropriationLevelAuthority INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	CarryoverOut FLOAT NULL DEFAULT (0.0),
	CarryoverIn FLOAT NULL DEFAULT (0.0),
	Reimbursements FLOAT NULL DEFAULT (0.0),
	Recoveries FLOAT NULL DEFAULT (0.0),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT AppropriationLevelAuthorityPrimaryKey PRIMARY KEY 
	(
		AppropriationLevelAuthority ASC
	) 
) ;

CREATE TABLE dbo.Appropriations
(
	AppropriationsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT AppropriationsPrimaryKey PRIMARY KEY 
	(
		AppropriationsId ASC
	)
) ;

CREATE TABLE dbo.BudgetAuthorityAndOutlays
(
	BudgetAuthorityAndOutlaysId INT NOT NULL UNIQUE,
	ReportYear NVARCHAR(80) NULL DEFAULT ('NS'),
	Category NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	LineName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountType NVARCHAR(80) NULL DEFAULT ('NS'),
	AuthorityType NVARCHAR(80) NULL DEFAULT ('NS'),
	PriorYear FLOAT NULL DEFAULT (0.0),
	CurrentYear FLOAT NULL DEFAULT (0.0),
	BudgetYear FLOAT NULL DEFAULT (0.0),
	OutYear1 FLOAT NULL DEFAULT (0.0),
	OutYear2 FLOAT NULL DEFAULT (0.0),
	OutYear3 FLOAT NULL DEFAULT (0.0),
	OutYear4 FLOAT NULL DEFAULT (0.0),
	OutYear5 FLOAT NULL DEFAULT (0.0),
	OutYear6 FLOAT NULL DEFAULT (0.0),
	OutYear7 FLOAT NULL DEFAULT (0.0),
	OutYear8 FLOAT NULL DEFAULT (0.0),
	OutYear9 FLOAT NULL DEFAULT (0.0),
	CONSTRAINT BudgetAuthorityAndOutlaysPrimaryKey PRIMARY KEY 
	(
		BudgetAuthorityAndOutlaysId ASC
	)
);

CREATE TABLE dbo.BudgetContacts
(
	BudgetContactsId INT NOT NULL UNIQUE,
	FirstName NVARCHAR(80) NULL DEFAULT ('NS'),
	LastName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Section NVARCHAR(80) NULL DEFAULT ('NS'),
	JobTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	Street NVARCHAR(80) NULL DEFAULT ('NS'),
	City NVARCHAR(80) NULL DEFAULT ('NS'),
	State NVARCHAR(80) NULL DEFAULT ('NS'),
	ZipCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Account NVARCHAR(80) NULL DEFAULT ('NS'),
	EmailAddress NVARCHAR(80) NULL DEFAULT ('NS'),
	EmailType NVARCHAR(80) NULL DEFAULT ('NS'),
	DisplayName NVARCHAR(80) NULL DEFAULT ('NS'),
	OfficeLocation NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT BudgetContactsPrimaryKey PRIMARY KEY 
	(
		BudgetContactsId ASC
	)
);

CREATE TABLE dbo.BudgetControls
(
	BudgetControlsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetedTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	PostedTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	EstimatedReimbursementsTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	SpendingAdjustmentTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	EstimatedRecoveriesTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	ActualRecoveriesTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	StatusReserveTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	ProfitLossTransType NVARCHAR(80) NULL DEFAULT ('NS'),
	EstimatedReimbursementsSpendingOption NVARCHAR(80) NULL DEFAULT ('NS'),
	EstimatedReimursementsBudgetingOption NVARCHAR(80) NULL DEFAULT ('NS'),
	TrackAgreementLowerLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetEstimatedLowerLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	EstimatedRecoveriesSpendingOption NVARCHAR(80) NULL DEFAULT ('NS'),
	EstimatedRecoveriesBudgetingOption NVARCHAR(80) NULL DEFAULT ('NS'),
	RecoveryNextLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	RecoveryBudgetMismatch NVARCHAR(80) NULL DEFAULT ('NS'),
	ProfitLossSpendingOption NVARCHAR(80) NULL DEFAULT ('NS'),
	ProfitLossBudgetOption NVARCHAR(80) NULL DEFAULT ('NS'),
	RecoveriesCarryInLowerLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	RecoveriesCarryInLowerLevelControl NVARCHAR(80) NULL DEFAULT ('NS'),
	RecoveriesCarryInAmountControl NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetedControl NVARCHAR(80) NULL DEFAULT ('NS'),
	PostedControl NVARCHAR(80) NULL DEFAULT ('NS'),
	PreCommitmentSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	CommitmentSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	ObligationSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	AccrualSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	ExpenditureSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	ExpenseSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	ReimbursableSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	ReimbursableAgreementSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	FteBudgetingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	FteSpendingControl NVARCHAR(80) NULL DEFAULT ('NS'),
	TransactionTypeControl NVARCHAR(80) NULL DEFAULT ('NS'),
	AuthorityDistributionControl NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT BudgetControlsPrimaryKey PRIMARY KEY 
	(
		BudgetControlsId ASC
	)
);

CREATE TABLE dbo.BudgetDocuments
(
	BudgetDocumentsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentDate DATETIME NULL,
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	CarryoverOut FLOAT NULL DEFAULT (0.0),
	CarryoverIn FLOAT NULL DEFAULT (0.0),
	Recoveries FLOAT NULL DEFAULT (0.0),
	Reimbursements FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT BudgetDocumentsPrimaryKey PRIMARY KEY 
	(
		BudgetDocumentsId ASC
	)
);

CREATE TABLE dbo.BudgetObjectClasses
(
	BudgetObjectClassesId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT BudgetObjectClassesPrimaryKey PRIMARY KEY 
	(
		BudgetObjectClassesId ASC
	)
);

CREATE TABLE dbo.CapitalPlanningInvestmentCodes
(
	CapitalPlanningInvestmentCodesId INT NOT NULL UNIQUE,
	Type NVARCHAR(80) NULL DEFAULT ('NS'),
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT CapitalPlanningInvestmentCodesPrimaryKey PRIMARY KEY 
	(
		CapitalPlanningInvestmentCodesId ASC
	)
) ;

CREATE TABLE dbo.CarryoverApportionments
(
	CarryoverApportionmentsId INT NOT NULL UNIQUE,
	BudgetAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	Group NVARCHAR(80) NULL DEFAULT ('NS'),
	Description NVARCHAR(80) NULL DEFAULT ('NS'),
	LineName NVARCHAR(80) NULL DEFAULT ('NS'),
	AuthorityType NVARCHAR(80) NULL DEFAULT ('NS'),
	Request FLOAT NULL DEFAULT (0.0),
	Balance FLOAT NULL DEFAULT (0.0),
	Deobligations FLOAT NULL DEFAULT (0.0),
	Amount FLOAT NULL DEFAULT (0.0),
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	LineSplit NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT CarryoverApportionmentsPrimaryKey PRIMARY KEY 
	(
		CarryoverApportionmentsId ASC
	) 
);

CREATE TABLE dbo.CarryoverRequests
(
	CarryoverRequestsId INT NOT NULL UNIQUE,
	Analyst NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Status NVARCHAR(80) NULL DEFAULT ('NS'),
	OriginalRequestDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	BudgetFormulationSystem NVARCHAR(80) NULL DEFAULT ('NS'),
	Comments NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	RequestDocument NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	Duration FLOAT NULL DEFAULT (0.0),
	CONSTRAINT CarryoverRequestsPrimaryKey PRIMARY KEY 
	(
		CarryoverRequestsId ASC
	)
);

CREATE TABLE dbo.Changes
(
	ChangesId INT NOT NULL UNIQUE,
	TableName NVARCHAR(80) NULL DEFAULT ('NS'),
	FieldName NVARCHAR(80) NULL DEFAULT ('NS'),
	Action NVARCHAR(80) NULL DEFAULT ('NS'),
	OldValue NVARCHAR(80) NULL DEFAULT ('NS'),
	NewValue NVARCHAR(80) NULL DEFAULT ('NS'),
	TimeStamp DATETIME NULL,
	Message NVARCHAR(80) NULL DEFAULT ('NS'),
	CONSTRAINT ChangesPrimaryKey PRIMARY KEY 
	(
		ChangesId ASC
	)
) ;

CREATE TABLE dbo.ColumnSchema
(
	ColumnSchemaId INT NOT NULL UNIQUE,
	DataType NVARCHAR(80) NULL DEFAULT ('NS'),
	ColumnName NVARCHAR(80) NULL DEFAULT ('NS'),
	TableName NVARCHAR(80) NULL DEFAULT ('NS'),
	ColumnCaption NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ColumnSchemaPrimaryKey PRIMARY KEY 
    (
        ColumnSchemaId ASC
    )
) 

CREATE TABLE dbo.CompassErrors
(
	CompassErrorsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Message NVARCHAR(80) NULL DEFAULT ('NS'),
	Severity NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT CompassErrorsPrimaryKey PRIMARY KEY 
    (
        CompassErrorsId ASC
    )
) ;

CREATE TABLE dbo.CompassLevels
(
	CompassLevelsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasurySymbol NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	Authority FLOAT NULL DEFAULT (0.0),
	CarryoverIn FLOAT NULL DEFAULT (0.0),
	CarryoverOut FLOAT NULL DEFAULT (0.0),
	Recoveries FLOAT NULL DEFAULT (0.0),
	Reimbursements FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT CompassLevelsPrimaryKey PRIMARY KEY 
    (
        CompassLevelsId ASC
    )
)

CREATE TABLE dbo.CongressionalControls
(
	CongressionalControlsId INT NOT NULL UNIQUE,
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	SubProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SubProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ReprogrammingRestriction NVARCHAR(80) NULL DEFAULT ('NS'),
	IncreaseRestriction NVARCHAR(80) NULL DEFAULT ('NS'),
	DecreaseRestriction NVARCHAR(80) NULL DEFAULT ('NS'),
	MemoRequirement NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT CongressionalControlsPrimaryKey PRIMARY KEY 
    (
        CongressionalControlsId ASC
    )
) ;

CREATE TABLE dbo.CongressionalProjects
(
	CongressionalEarmarksId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	StateCode NVARCHAR(80) NULL DEFAULT ('NS'),
	StateName NVARCHAR(80) NULL DEFAULT ('NS'),
	Project NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT CongressionalProjectsPrimaryKey PRIMARY KEY 
    (
        CongressionalEarmarksId ASC
    )
);

CREATE TABLE dbo.CostAreas
(
	CostAreasId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT CostAreasPrimaryKey PRIMARY KEY 
    (
        CostAreasId ASC
    )
);

CREATE TABLE dbo.DataRuleDescriptions
(
	DataRuleDescriptionsId INT NOT NULL UNIQUE,
	Schedule NVARCHAR(80) NULL DEFAULT ('NS'),
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	RuleNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	RuleDescription NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	ScheduleOrder NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT DataRuleDescriptionsPrimaryKey PRIMARY KEY 
    (
        DataRuleDescriptionsId ASC
    )
) ;

CREATE TABLE dbo.Defactos
(
	DefactosId INT NOT NULL UNIQUE,
	StatusOfFundsId int NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	ULO FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT DefactosPrimaryKey PRIMARY KEY 
    (
        DefactosId ASC
    )
) ;

CREATE TABLE dbo.Deobligations
(
	DeobligationsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	FocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProcessedDate DATETIME NULL,
	Amount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT DeobligationsPrimaryKey PRIMARY KEY 
    (
        DeobligationsId ASC
    )
);

CREATE TABLE dbo.DocumentControlNumbers
(
	DocumentControlNumbersId INT NOT NULL UNIQUE,
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentPrefix NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT DocumentControlNumbersPrimaryKey PRIMARY KEY 
    (
        DocumentControlNumbersId ASC
    )
);

CREATE TABLE dbo.Documents
(
	DocumentsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Category NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	System NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT DocumentsPrimaryKey PRIMARY KEY 
    (
        DocumentsId ASC
    )
) ;

CREATE TABLE dbo.EarmarkCodes
(
	EarmarkCodesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT EarmarkCodesPrimaryKey PRIMARY KEY 
    (
        EarmarkCodesId ASC
    )
) ;

CREATE TABLE dbo.Earmarks
(
	EarmarksId INT NOT NULL UNIQUE,
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	StateCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Description NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	ProjectOfficerLastName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectOfficerFirstName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectOfficerPhoneNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectOfficerMailCode NVARCHAR(80) NULL DEFAULT ('NS'),
	CommitmentDate DATETIME NULL,
	ObligationDate DATETIME NULL,
	ProjectStatus NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectOfficerComments NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT EarmarksPrimaryKey PRIMARY KEY 
    (
        EarmarksId ASC
    )
) ;

CREATE TABLE dbo.Expenditures
(
	ExpendituresId INT NOT NULL UNIQUE,
	ObligationsId int NULL,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	ProcessedDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	Age FLOAT NULL DEFAULT (0.0),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	FocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FocName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorCode NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
    CONSTRAINT ExpendituresPrimaryKey PRIMARY KEY 
    (
        ExpendituresId ASC
    )
) ;

CREATE TABLE dbo.FederalHolidays
(
	FederalHolidaysId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	ColumbusDay DATETIME NULL,
	VeteransDay DATETIME NULL,
	ThanksgivingDay DATETIME NULL,
	ChristmasDay DATETIME NULL,
	NewYearsDay DATETIME NULL,
	MartinLutherKingDay DATETIME NULL,
	WashingtonsDay DATETIME NULL,
	MemorialDay DATETIME NULL,
	JuneteenthDay DATETIME NULL,
	IndependenceDay DATETIME NULL,
	LaborDay DATETIME NULL,
    CONSTRAINT FederalHolidaysPrimaryKey PRIMARY KEY 
    (
        FederalHolidaysId ASC
    )
) ;

CREATE TABLE dbo.FinanceObjectClasses
(
	FinanceObjectClassesId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT FinanceObjectClassesPrimaryKey PRIMARY KEY 
    (
        FinanceObjectClassesId ASC
    )
) ;

CREATE TABLE dbo.FiscalYears
(
	FiscalYearsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NOT NULL,
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	StartDate NVARCHAR(80) NULL DEFAULT ('NS'),
	ColumbusDay DATETIME NULL,
	VeteransDay DATETIME NULL,
	ThanksgivingDay DATETIME NULL,
	ChristmasDay DATETIME NULL,
	NewYearsDay DATETIME NULL,
	MartinLutherKingDay DATETIME NULL,
	WashingtonsDay DATETIME NULL,
	MemorialDay DATETIME NULL,
	JuneteenthDay DATETIME NULL,
	IndependenceDay DATETIME NULL,
	LaborDay DATETIME NULL,
	ExpiringYear NVARCHAR(80) NULL DEFAULT ('NS'),
	ExpirationDate NVARCHAR(80) NULL DEFAULT ('NS'),
	WorkDays FLOAT NULL DEFAULT (0.0),
	WeekDays FLOAT NULL DEFAULT (0.0),
	WeekEnds FLOAT NULL DEFAULT (0.0),
	EndDate NVARCHAR(80) NULL DEFAULT ('NS'),
	Availability NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT FiscalYearsPrimaryKey PRIMARY KEY 
    (
        FiscalYearsId ASC
    )
) ;

CREATE TABLE dbo.FullTimeEquivalents
(
	FullTimeEquivialentsId INT NOT NULL UNIQUE,
	OperatingPlansId int NULL,
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	ITProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectTypeName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProjectTypeCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ActivityCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ActivityName NVARCHAR(80) NULL DEFAULT ('NS'),
	LocalCode NVARCHAR(80) NULL DEFAULT ('NS'),
	LocalCodeName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	CostAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	CostAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalCode NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalName NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT FullTimeEquivalentsPrimaryKey PRIMARY KEY 
    (
        FullTimeEquivialentsId ASC
    )
);

CREATE TABLE dbo.FundCategories
(
	FundCategoriesId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	ShortName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT FundCategoriesPrimaryKey PRIMARY KEY 
    (
        FundCategoriesId ASC
    )
);

CREATE TABLE dbo.Funds
(
	FundsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	ShortName NVARCHAR(80) NULL DEFAULT ('NS'),
	Status NVARCHAR(80) NULL DEFAULT ('NS'),
	StartDate NVARCHAR(80) NULL DEFAULT ('NS'),
	EndDate NVARCHAR(80) NULL DEFAULT ('NS'),
	SubLevelPrefix NVARCHAR(80) NULL DEFAULT ('NS'),
	AllocationTransferAgency NVARCHAR(80) NULL DEFAULT ('NS'),
	AgencyIdentifier NVARCHAR(80) NULL DEFAULT ('NS'),
	BeginningPeriodOfAvailability NVARCHAR(80) NULL DEFAULT ('NS'),
	EndingPeriodOfAvailability NVARCHAR(80) NULL DEFAULT ('NS'),
	MultiyearIndicator NVARCHAR(80) NULL DEFAULT ('NS'),
	MainAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCategory NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundGroup NVARCHAR(80) NULL DEFAULT ('NS'),
	NoYear NVARCHAR(80) NULL DEFAULT ('NS'),
	Carryover NVARCHAR(80) NULL DEFAULT ('NS'),
	CanceledYearSpendingAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	ApplyAtAllLevels NVARCHAR(80) NULL DEFAULT ('NS'),
	BatsFund NVARCHAR(80) NULL DEFAULT ('NS'),
	BatsEndDate NVARCHAR(80) NULL DEFAULT ('NS'),
	BatsOptionId NVARCHAR(80) NULL DEFAULT ('NS'),
	SecurityOrg NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT FundsPrimaryKey PRIMARY KEY 
    (
        FundsId ASC
    )
);

CREATE TABLE dbo.FundSymbols
(
	FundSymbolsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT FundSymbolsPrimaryKey PRIMARY KEY 
    (
        FundSymbolsId ASC
    )
) ;

CREATE TABLE dbo.GeneralLedgerAccounts
(
	GeneralLedgerAccountsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	Number NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	ShortName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountClassification NVARCHAR(80) NULL DEFAULT ('NS'),
	NormalBalance NVARCHAR(80) NULL DEFAULT ('NS'),
	RealOrClosingAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	CashAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	SummaryAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	ReportableAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	CostAllocationIndicator NVARCHAR(80) NULL DEFAULT ('NS'),
	FederalNonFederal NVARCHAR(80) NULL DEFAULT ('NS'),
	AttributeValue NVARCHAR(80) NULL DEFAULT ('NS'),
	Usage NVARCHAR(80) NULL DEFAULT ('NS'),
	Deposit NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT GeneralLedgerAccountsPrimaryKey PRIMARY KEY 
    (
        GeneralLedgerAccountsId ASC
    )
) ;

CREATE TABLE dbo.Goals
(
	GoalsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    Title NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT GoalsPrimaryKey PRIMARY KEY 
    (
        GoalsId ASC
    )
);

CREATE TABLE dbo.GsPayScales
(
	GsPayScalesId INT NOT NULL UNIQUE,
	LOCNAME NVARCHAR(80) NULL DEFAULT ('NS'),
	GRADE FLOAT NULL DEFAULT (0.0),
	ANNUAL1 FLOAT NULL DEFAULT (0.0),
	HOURLY1 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME1 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL2 FLOAT NULL DEFAULT (0.0),
	HOURLY2 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME2 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL3 FLOAT NULL DEFAULT (0.0),
	HOURLY3 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME3 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL4 FLOAT NULL DEFAULT (0.0),
	HOURLY4 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME4 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL5 FLOAT NULL DEFAULT (0.0),
	HOURLY5 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME5 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL6 FLOAT NULL DEFAULT (0.0),
	HOURLY6 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME6 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL7 FLOAT NULL DEFAULT (0.0),
	HOURLY7 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME7 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL8 FLOAT NULL DEFAULT (0.0),
	HOURLY8 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME8 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL9 FLOAT NULL DEFAULT (0.0),
	HOURLY9 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME9 NVARCHAR(80) NULL DEFAULT ('NS'),
	ANNUAL10 FLOAT NULL DEFAULT (0.0),
	HOURLY10 NVARCHAR(80) NULL DEFAULT ('NS'),
	OVERTIME10 NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT GsPayScalesPrimaryKey PRIMARY KEY 
    (
        GsPayScalesId ASC
    )
);

CREATE TABLE dbo.HeadquartersAuthority
(
	HeadquartersAuthorityId INT NOT NULL UNIQUE,
	AllocationsId int NULL,
	StatusOfFundsId int NULL,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT HeadquartersAuthorityPrimaryKey PRIMARY KEY 
    (
        HeadquartersAuthorityId ASC
    )
) ;

CREATE TABLE dbo.HeadquartersOffices
(
	HeadquartersOfficesId INT NOT NULL UNIQUE,
	ResourcePlanningOfficesId int NULL,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT HeadquartersOfficesPrimaryKey PRIMARY KEY 
    (
        HeadquartersOfficesId ASC
    )
) ;

CREATE TABLE dbo.Images
(
	ImagesId INT NOT NULL UNIQUE,
	FileName NVARCHAR(80) NULL DEFAULT ('NS'),
	FilePath NVARCHAR(80) NULL DEFAULT ('NS'),
	FileExtension NVARCHAR(80) NULL DEFAULT ('NS'),
	ImageFile image NULL,
	Attachments NVARCHAR(MAX) NULL DEFAULT ('NS'),,
    CONSTRAINT ImagesPrimaryKey PRIMARY KEY 
    (
        ImagesId ASC
    )
);

CREATE TABLE dbo.InflationReductionActCarryoverEstimates
(
	InflationReductionActCarryoverEstimatesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Estimate FLOAT NULL DEFAULT (0.0),
    CONSTRAINT InflationReductionActCarryoverEstimatesPrimaryKey PRIMARY KEY 
    (
        InflationReductionActCarryoverEstimatesId ASC
    ) 
) ;

CREATE TABLE dbo.JobsActCarryoverEstimates
(
	JobsActCarryoverEstimatesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Estimate FLOAT NULL DEFAULT (0.0),
    CONSTRAINT JobsActCarryoverEstimatesPrimaryKey PRIMARY KEY 
    (
        JobsActCarryoverEstimatesId ASC
    )
) ;

CREATE TABLE dbo.MarginalOutlays
(
	MonthlyMarginalsId INT NOT NULL UNIQUE,
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	MainAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	October FLOAT NULL DEFAULT (0.0),
	November FLOAT NULL DEFAULT (0.0),
	December FLOAT NULL DEFAULT (0.0),
	January FLOAT NULL DEFAULT (0.0),
	Feburary FLOAT NULL DEFAULT (0.0),
	March FLOAT NULL DEFAULT (0.0),
	April FLOAT NULL DEFAULT (0.0),
	May FLOAT NULL DEFAULT (0.0),
	June FLOAT NULL DEFAULT (0.0),
	July FLOAT NULL DEFAULT (0.0),
	August FLOAT NULL DEFAULT (0.0),
	September FLOAT NULL DEFAULT (0.0),
    CONSTRAINT MarginalOutlaysPrimaryKey PRIMARY KEY 
    (
        MonthlyMarginalsId ASC
    )
) ;

CREATE TABLE dbo.Messages
(
	MessageId INT NOT NULL UNIQUE,
	Message NVARCHAR(80) NULL DEFAULT ('NS'),
	Type NVARCHAR(80) NULL DEFAULT ('NS'),
	Form NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT MessagesPrimaryKey PRIMARY KEY 
    (
        MessageId ASC
    )
);

CREATE TABLE dbo.MonthlyActuals
(
	MonthlyActualsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationName NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAppropriationName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioActivityCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	NetOutlays FLOAT NULL DEFAULT (0.0),
	GrossOutlays FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
    CONSTRAINT MonthlyActualsPrimaryKey PRIMARY KEY 
    (
        MonthlyActualsId ASC
    )
) ;

CREATE TABLE dbo.MonthlyLedgerAccountBalances
(
	MonthlyLedgerAccountBalancesId INT NOT NULL UNIQUE,
	FiscalYear NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	LedgerAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	LedgerName NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasurySymbol NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasurySymbolName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	FiscalMonth NVARCHAR(80) NULL DEFAULT ('NS'),
	CreditBalance FLOAT NULL DEFAULT (0.0),
	DebitBalance FLOAT NULL DEFAULT (0.0),
	YearToDateAmount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT MonthlyLedgerAccountBalancesPrimaryKey PRIMARY KEY 
    (
        MonthlyLedgerAccountBalancesId ASC
    )
) ;

CREATE TABLE dbo.MonthlyOutlays
(
	MonthlyOutlaysId INT NOT NULL UNIQUE,
	FiscalYear NVARCHAR(80) NULL DEFAULT ('NS'),
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	LineTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	TaxationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAgencyCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAgencyCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetBureauCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AgencySequence NVARCHAR(80) NULL DEFAULT ('NS'),
	BureauSequence NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountSequence NVARCHAR(80) NULL DEFAULT ('NS'),
	AgencyTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	BureauTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	October FLOAT NULL DEFAULT (0.0),
	November FLOAT NULL DEFAULT (0.0),
	December FLOAT NULL DEFAULT (0.0),
	January FLOAT NULL DEFAULT (0.0),
	Feburary FLOAT NULL DEFAULT (0.0),
	March FLOAT NULL DEFAULT (0.0),
	April FLOAT NULL DEFAULT (0.0),
	May FLOAT NULL DEFAULT (0.0),
	June FLOAT NULL DEFAULT (0.0),
	July FLOAT NULL DEFAULT (0.0),
	August FLOAT NULL DEFAULT (0.0),
	September FLOAT NULL DEFAULT (0.0),
    CONSTRAINT MonthlyOutlaysPrimaryKey PRIMARY KEY 
    (
        MonthlyOutlaysId ASC
    )
) ;

CREATE TABLE dbo.NationalPrograms
(
	NationalProgramsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NOT NULL,
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Title NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT NationalProgramsPrimaryKey PRIMARY KEY 
    (
        NationalProgramsId ASC
    )
);

CREATE TABLE dbo.Objectives
(
	ObjectivesId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Title NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ObjectivesPrimaryKey PRIMARY KEY 
    (
        ObjectivesId ASC
    )
) ;

CREATE TABLE dbo.Obligations
(
	ObligationsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	ApportionmentAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProcessedDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	Age FLOAT NULL DEFAULT (0.0),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	FocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FocName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorCode NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorName NVARCHAR(80) NULL DEFAULT ('NS'),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
    CONSTRAINT ObligationsPrimaryKey PRIMARY KEY 
    (
        ObligationsId ASC
    )
);

CREATE TABLE dbo.OpenCommitments
(
	OpenCommitmentsId INT NOT NULL UNIQUE,
	ObligationsId int NULL,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	ProcessedDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	Age FLOAT NULL DEFAULT (0.0),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	FocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FocName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorCode NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT OpenCommitmentsPrimaryKey PRIMARY KEY 
    (
        OpenCommitmentsId ASC
    )
);

CREATE TABLE dbo.OperatingPlans
(
	OperatingPlansId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ActivityCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ActivityName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalCode NVARCHAR(80) NULL DEFAULT ('NS'),
	GoalName NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ObjectiveName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	Version NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT OperatingPlansPrimaryKey PRIMARY KEY 
    (
        OperatingPlansId ASC
    )
);

CREATE TABLE dbo.Organizations
(
	OrganizationsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	PreventNewUse NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Status NVARCHAR(80) NULL DEFAULT ('NS'),
	SecurityOrg NVARCHAR(80) NULL DEFAULT ('NS'),
	Usage NVARCHAR(80) NULL DEFAULT ('NS'),
	UseAsCostOrg NVARCHAR(80) NULL DEFAULT ('NS'),
	SubCodeRequired NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SubRcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Description NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT OrganizationsPrimaryKey PRIMARY KEY 
    (
        OrganizationsId ASC
    )
);

CREATE TABLE dbo.Outlays
(
	CompassOutlaysId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasurySymbol NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProcessedDate NVARCHAR(80) NULL DEFAULT ('NS'),
	LastActivityDate NVARCHAR(80) NULL DEFAULT ('NS'),
	TotalObligations FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	ObligationsPaid FLOAT NULL DEFAULT (0.0),
    CONSTRAINT CompassOutlaysPrimaryKey PRIMARY KEY 
    (
        CompassOutlaysId ASC
    )
);

CREATE TABLE dbo.PayPeriods
(
	PayPeriodsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	Number NVARCHAR(80) NULL DEFAULT ('NS'),
	Period NVARCHAR(80) NULL DEFAULT ('NS'),
	Type NVARCHAR(80) NULL DEFAULT ('NS'),
	SecurityOrg NVARCHAR(80) NULL DEFAULT ('NS'),
	StartDate DATETIME NULL,
	EndDate DATETIME NULL,
	SplitPayPeriod NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT PayPeriodsPrimaryKey PRIMARY KEY 
    (
        PayPeriodsId ASC
    )
); 

CREATE TABLE dbo.PayrollAuthority
(
	PayrollAuthorityId INT NOT NULL UNIQUE,
	AllocationsId int NULL,
	StatusOfFundsId int NULL,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT PayrollAuthorityPrimaryKey PRIMARY KEY 
    (
        PayrollAuthorityId ASC
    )
);

CREATE TABLE dbo.PayrollRequests
(
	PayrollRequestsId INT NOT NULL UNIQUE,
	ControlTeamAnalyst NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Status NVARCHAR(80) NULL DEFAULT ('NS'),
	OriginalRequestDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	BFS NVARCHAR(80) NULL DEFAULT ('NS'),
	Comments NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	RequestDocument NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	Duration FLOAT NULL DEFAULT (0.0),
    CONSTRAINT PayrollRequestsPrimaryKey PRIMARY KEY 
    (
        PayrollRequestsId ASC
    )
);  

CREATE TABLE dbo.PRC
(
	PrcId INT NOT NULL UNIQUE,
	StatusOfFundsId int NULL,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT PRCPrimaryKey PRIMARY KEY 
    (
        PrcId ASC
    )
) ;

CREATE TABLE dbo.ProgramAreas
(
	ProgramAreasId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ProgramAreasPrimaryKey PRIMARY KEY 
    (
        ProgramAreasId ASC
    )
) ;

CREATE TABLE dbo.ProgramProjects
(
	ProgramProjectsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ProgramProjectsPrimaryKey PRIMARY KEY 
    (
        ProgramProjectsId ASC
    )
) ;

CREATE TABLE dbo.Projects
(
	ProjectsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ProjectsPrimaryKey PRIMARY KEY 
    (
        ProjectsId ASC
    )
) ;

CREATE TABLE dbo.Providers
(
	ProvidersId INT NOT NULL UNIQUE,
	ProviderName NVARCHAR(80) NULL DEFAULT ('NS'),
	FileExtension NVARCHAR(80) NULL DEFAULT ('NS'),
	Connection NVARCHAR(80) NULL DEFAULT ('NS'),
	Properties NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ProvidersPrimaryKey PRIMARY KEY 
    (
        ProvidersId ASC
    )
);

CREATE TABLE dbo.PublicLaws
(
	PublicLawsId INT NOT NULL UNIQUE,
	LawNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	BillTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	EnactedDate DATETIME NULL,
	Congress NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT PublicLawsPrimaryKey PRIMARY KEY 
    (
        PublicLawsId ASC
    )
) ;

CREATE TABLE dbo.QueryDefinitions
(
	QueryDefinitionsId INT NOT NULL UNIQUE,
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Type NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT QueryDefinitionsPrimaryKey PRIMARY KEY 
    (
        QueryDefinitionsId ASC
    )
);

CREATE TABLE dbo.RecoveryAct
(
	RecoveryActId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT RecoveryActPrimaryKey PRIMARY KEY 
    (
        RecoveryActId ASC
    )
) ;

CREATE TABLE dbo.RegionalAuthority
(
	RegionalAuthorityId INT NOT NULL UNIQUE,
	AllocationsId int NULL,
	StatusOfFundsId int NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL
) ;

CREATE TABLE dbo.RegionalOffices
(
	RegionalOfficesId INT NOT NULL UNIQUE,
	ResourcePlanningOfficesId int NULL,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT RegionalOfficesPrimaryKey PRIMARY KEY 
    (
        RegionalOfficesId ASC
    )
);

CREATE TABLE dbo.ReimbursableAgreements
(
	ReimbursableAgreementsId INT NOT NULL UNIQUE,
	RPIO NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	AgreementNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	StartDate DATETIME NULL,
	EndDate DATETIME NULL,
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SiteProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorCode NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	ULO FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
    CONSTRAINT ReimbursableAgreementsPrimaryKey PRIMARY KEY 
    (
        ReimbursableAgreementsId ASC
    )
) ;

CREATE TABLE dbo.ReimbursableFunds
(
	ReimbursableFundsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AgreeementNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount money NULL,
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
    CONSTRAINT ReimbursableFundsPrimaryKey PRIMARY KEY 
    (
        ReimbursableFundsId ASC
    )
) ;

CREATE TABLE dbo.ReportingLines
(
	ReportingLinesId int NOT NULL UNIQUE,
	Number NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Caption NVARCHAR(80) NULL DEFAULT ('NS'),
	Category NVARCHAR(80) NULL DEFAULT ('NS'),
	Range NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ReportingLinesPrimaryKeyPrimaryKey PRIMARY KEY 
    (
        ReportingLinesId ASC
    )
) ;

CREATE TABLE dbo.Reports
(
	ReportsId INT NOT NULL UNIQUE,
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Title NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ReportsPrimaryKey PRIMARY KEY 
    (
        ReportsId ASC
    )
) ;

CREATE TABLE dbo.ResourcePlanningOffices
(
	ResourcePlanningOfficesId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ResourcePlanningOfficesPrimaryKey PRIMARY KEY 
    (
        ResourcePlanningOfficesId ASC
    )
);

CREATE TABLE dbo.Resources
(
	ResourcesId INT NOT NULL UNIQUE,
	Identifier NVARCHAR(80) NULL DEFAULT ('NS'),
	Type NVARCHAR(80) NULL DEFAULT ('NS'),
	Location NVARCHAR(80) NULL DEFAULT ('NS'),
	FileExtension NVARCHAR(80) NULL DEFAULT ('NS'),
	Caption NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ResourcesPrimaryKey PRIMARY KEY 
    (
        ResourcesId ASC
    ) 
) ;

CREATE TABLE dbo.ResponsibilityCenters
(
	ResponsibilityCentersId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Title NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT ResponsibilityCentersPrimaryKey PRIMARY KEY 
    (
        ResponsibilityCentersId ASC
    )
) ;

CREATE TABLE dbo.SchemaTypes
(
	SchemaTypesId INT NOT NULL UNIQUE,
	TypeName NVARCHAR(80) NULL DEFAULT ('NS'),
	Database NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT SchemaTypesPrimaryKey PRIMARY KEY 
    (
        SchemaTypesId ASC
    )
) ;

CREATE TABLE dbo.SpendingDocuments
(
	SpendingDocumentsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasurySymbol NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioActivityCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	PurchaseRequestNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	OriginalActionDate DATETIME NULL,
	LastActionDate DATETIME NULL,
	Commitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Deobligations FLOAT NULL DEFAULT (0.0),
	UnliqudatedObligations FLOAT NULL DEFAULT (0.0),
    CONSTRAINT SpendingDocumentsPrimaryKey PRIMARY KEY 
    (
        SpendingDocumentsId ASC
    )
) ;

CREATE TABLE dbo.SpendingRates
(
	SpendingRatesId INT NOT NULL UNIQUE,
	OmbAgencyCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OmbAgencyName NVARCHAR(80) NULL DEFAULT ('NS'),
	OmbBureauCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OmbBureauName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreausuryAgencyCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreausuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreausuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountTitle NVARCHAR(80) NULL DEFAULT ('NS'),
	Subfunction NVARCHAR(80) NULL DEFAULT ('NS'),
	Line NVARCHAR(80) NULL DEFAULT ('NS'),
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	Category NVARCHAR(80) NULL DEFAULT ('NS'),
	Subcategory NVARCHAR(80) NULL DEFAULT ('NS'),
	SubcategoryName NVARCHAR(80) NULL DEFAULT ('NS'),
	MainAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	Jurisdiction NVARCHAR(80) NULL DEFAULT ('NS'),
	YearOfAuthority NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAuthority FLOAT NULL DEFAULT (0.0),
	OutYear1 FLOAT NULL DEFAULT (0.0),
	OutYear2 FLOAT NULL DEFAULT (0.0),
	OutYear3 FLOAT NULL DEFAULT (0.0),
	OutYear4 FLOAT NULL DEFAULT (0.0),
	OutYear5 FLOAT NULL DEFAULT (0.0),
	OutYear6 FLOAT NULL DEFAULT (0.0),
	OutYear7 FLOAT NULL DEFAULT (0.0),
	OutYear8 FLOAT NULL DEFAULT (0.0),
	OutYear9 FLOAT NULL DEFAULT (0.0),
	OutYear10 FLOAT NULL DEFAULT (0.0),
	OutYear11 FLOAT NULL DEFAULT (0.0),
	TotalSpendout FLOAT NULL DEFAULT (0.0),
    CONSTRAINT SpendingRatesPrimaryKey PRIMARY KEY 
    (
        SpendingRatesId ASC
    )
);

CREATE TABLE dbo.StateGrantObligations
(
	StateGrantObligationsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	Approp Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Approp Code Short TItle NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	StateCode NVARCHAR(80) NULL DEFAULT ('NS'),
	StateName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	WholeDollars FLOAT NULL DEFAULT (0.0),
    CONSTRAINT StateGrantObligationsPrimaryKey PRIMARY KEY 
    (
        StateGrantObligationsId ASC
    )
) ;

CREATE TABLE dbo.StateOrganizations
(
	StateOrganizationsId INT NOT NULL UNIQUE,
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT StateOrganizationsPrimaryKey PRIMARY KEY 
    (
        StateOrganizationsId ASC
    )
); 

CREATE TABLE dbo.StatusOfAmericanRescuePlanFunds
(
	StatusOfAmericanRescuePlanFundsId INT NOT NULL UNIQUE,
	StatusOfFundsId INT NOT NULL UNIQUE,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName nvarchar(max) NULL
);

CREATE TABLE dbo.StatusOfAppropriations
(
	StatusOfAppropriationsId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	Availability NVARCHAR(80) NULL DEFAULT ('NS'),
	TransType NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasurySymbol NVARCHAR(80) NULL DEFAULT ('NS'),
	OriginalAmount FLOAT NULL DEFAULT (0.0),
	Authority FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	CarryoverOut FLOAT NULL DEFAULT (0.0),
	CarryoverIn FLOAT NULL DEFAULT (0.0),
	TransferIn FLOAT NULL DEFAULT (0.0),
	TransferOut FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT StatusOfAppropriationsPrimaryKey PRIMARY KEY 
    (
        StatusOfAppropriationsId ASC
    )
) ;

CREATE TABLE dbo.StatusOfBudgetaryResources
(
	StatusOfBudgetaryResourcesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BeginningPeriodOfAvailability NVARCHAR(80) NULL DEFAULT ('NS'),
	EndingPeriodOfAvailability NVARCHAR(80) NULL DEFAULT ('NS'),
	SectionNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	SectionName NVARCHAR(80) NULL DEFAULT ('NS'),
	LineNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	LineName NVARCHAR(80) NULL DEFAULT ('NS'),
	November FLOAT NULL DEFAULT (0.0),
	December FLOAT NULL DEFAULT (0.0),
	January FLOAT NULL DEFAULT (0.0),
	Feburary FLOAT NULL DEFAULT (0.0),
	March FLOAT NULL DEFAULT (0.0),
	April FLOAT NULL DEFAULT (0.0),
	May FLOAT NULL DEFAULT (0.0),
	June FLOAT NULL DEFAULT (0.0),
	July FLOAT NULL DEFAULT (0.0),
	August FLOAT NULL DEFAULT (0.0),
	September FLOAT NULL DEFAULT (0.0),
	October FLOAT NULL DEFAULT (0.0),
	LastUpdate DATETIME NULL,
    CONSTRAINT StatusOfBudgetaryResourcesPrimaryKey PRIMARY KEY 
    (
        StatusOfBudgetaryResourcesId ASC
    )
);

CREATE TABLE dbo.StatusOfEarmarks
(
	StatusOfEarmarksId INT NOT NULL UNIQUE,
	StatusOfFundsId int NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	ULO FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT StatusOfEarmarksPrimaryKey PRIMARY KEY 
    (
        StatusOfEarmarksId ASC
    )
) ;

CREATE TABLE dbo.StatusOfFunds
(
	StatusOfFundsId INT NOT NULL UNIQUE,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
    CONSTRAINT StatusOfFundsPrimaryKey PRIMARY KEY 
    (
        StatusOfFundsId ASC
    )
) ;

CREATE TABLE dbo.StatusOfInflationReductionActFunds
(
	StatusOfSupplementalFundingId INT NOT NULL UNIQUE,
	StatusOfFundsId int NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	ULO FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Balance FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT StatusOfInflationReductionActFundsPrimaryKey PRIMARY KEY 
    (
        StatusOfSupplementalFundingId ASC
    )
) ;

CREATE TABLE dbo.StatusOfJobsActFunds
(
	StatusOfJobsActFundingId INT NOT NULL UNIQUE,
	StatusOfFundsId int NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	ULO FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Balance FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT StatusOfJobsActFundingPrimaryKey PRIMARY KEY 
    (
        StatusOfJobsActFundingId ASC
    )
); 

CREATE TABLE dbo.StatusOfSpecialAccountFunds
(
	StatusOfSpecialAccountFundsId INT NOT NULL UNIQUE,
	Fiscal Year NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SpecialAccountNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	SpecialAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	SpecialAccountStatus NVARCHAR(80) NULL DEFAULT ('NS'),
	NplStatusCode NVARCHAR(80) NULL DEFAULT ('NS'),
	StatusDescription NVARCHAR(80) NULL DEFAULT ('NS'),
	EpaSiteId NVARCHAR(80) NULL DEFAULT ('NS'),
	CerclisSiteId NVARCHAR(80) NULL DEFAULT ('NS'),
	SiteCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SiteName NVARCHAR(80) NULL DEFAULT ('NS'),
	OperableUnit NVARCHAR(80) NULL DEFAULT ('NS'),
	PipelineCode NVARCHAR(80) NULL DEFAULT ('NS'),
	PipelineDescription NVARCHAR(80) NULL DEFAULT ('NS'),
	TransactionDescription NVARCHAR(80) NULL DEFAULT ('NS'),
	InterestDate NVARCHAR(80) NULL DEFAULT ('NS'),
	TrustfundTransfers int NULL,
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT NULL DEFAULT (0.0),
	Disbursements FLOAT NULL DEFAULT (0.0),
	UnpaidBalance int NULL,
	CumulativeReceipts FLOAT NULL DEFAULT (0.0),
	NetReceipts int NULL,
	Interest int NULL,
	CollectionsAndInterest FLOAT NULL DEFAULT (0.0),
	AvailableBalance float NULL,
    CONSTRAINT StatusOfJobsActFundingPrimaryKey PRIMARY KEY 
    (
        StatusOfJobsActFundingId ASC
    )
);

CREATE TABLE dbo.StatusOfSuperfundSites
(
	StatusOfSuperfundSitesId INT NOT NULL UNIQUE,
	FiscalYear NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	StateCode NVARCHAR(80) NULL DEFAULT ('NS'),
	StateName NVARCHAR(80) NULL DEFAULT ('NS'),
	CountyName NVARCHAR(80) NULL DEFAULT ('NS'),
	CityName NVARCHAR(80) NULL DEFAULT ('NS'),
	StreetAddress NVARCHAR(80) NULL DEFAULT ('NS'),
	ZipCode NVARCHAR(80) NULL DEFAULT ('NS'),
	SiteId NVARCHAR(80) NULL DEFAULT ('NS'),
	SiteName NVARCHAR(80) NULL DEFAULT ('NS'),
	Obligations FLOAT NULL DEFAULT (0.0),
	Deobligations FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
    CONSTRAINT StatusOfSuperfundSitesPrimaryKey PRIMARY KEY 
    (
        StatusOfSuperfundSitesId ASC
    )
);

CREATE TABLE dbo.StatusOfSupplementalFunds
(
	StatusOfSupplementalFundingId INT NOT NULL UNIQUE,
	StatusOfFundsId int NULL,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	LowerName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Budgeted FLOAT NULL DEFAULT (0.0),
	Posted FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	ULO FLOAT NULL DEFAULT (0.0),
	Expenditures FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Used FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Balance FLOAT NULL DEFAULT (0.0),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT StatusOfSupplementalFundsPrimaryKey PRIMARY KEY 
    (
        StatusOfSupplementalFundingId ASC
    )
);

CREATE TABLE dbo.SubAppropriations
(
	SubAppropriationsId INT NOT NULL UNIQUE,
	Code NVARCHAR(80) NULL DEFAULT ('NS'),
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT SubAppropriationsPrimaryKey PRIMARY KEY 
    (
        SubAppropriationsId ASC
    )
); 

CREATE TABLE dbo.SuperfundSites
(
	SuperfundSitesId INT NOT NULL UNIQUE,
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	City NVARCHAR(80) NULL DEFAULT ('NS'),
	State NVARCHAR(80) NULL DEFAULT ('NS'),
	SSID NVARCHAR(80) NULL DEFAULT ('NS'),
	SiteProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	EpaSiteId NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT SuperfundSitesPrimaryKey PRIMARY KEY 
    (
        SuperfundSitesId ASC
    )
);

CREATE TABLE dbo.SupplementalCarryoverEstimates
(
	SupplementalCarryoverEstimatesID INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	OpenCommitments FLOAT NULL DEFAULT (0.0),
	Obligations FLOAT NULL DEFAULT (0.0),
	Available FLOAT NULL DEFAULT (0.0),
	Estimate FLOAT NULL DEFAULT (0.0),
    CONSTRAINT SupplementalCarryoverEstimatesPrimaryKey PRIMARY KEY 
    (
        SupplementalCarryoverEstimatesID ASC
    )
);

CREATE TABLE dbo.TransferActivity
(
	TransferActivityId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	FromTo NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProcessedDate DATETIME NULL,
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	Net NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT TransferActivityPrimaryKey PRIMARY KEY 
    (
        TransferActivityId ASC
    )
);

CREATE TABLE dbo.Transfers
(
	TransfersId INT NOT NULL UNIQUE,
	BudgetLevel NVARCHAR(80) NULL DEFAULT ('NS'),
	DocPrefix NVARCHAR(80) NULL DEFAULT ('NS'),
	DocType NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	ReprogrammingNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	ControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	ProcessedDate DATETIME NULL,
	Quarter NVARCHAR(80) NULL DEFAULT ('NS'),
	Line NVARCHAR(80) NULL DEFAULT ('NS'),
	Subline NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramAreaName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FromTo NVARCHAR(80) NULL DEFAULT ('NS'),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
	Purpose NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	ResourceType NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT TransfersPrimaryKey PRIMARY KEY 
    (
        TransfersId ASC
    )
);

CREATE TABLE dbo.TransTypes
(
	TransTypesId INT NOT NULL UNIQUE,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	DocType NVARCHAR(80) NULL DEFAULT ('NS'),
	AppropriationBill NVARCHAR(80) NULL DEFAULT ('NS'),
	ContinuingResolution NVARCHAR(80) NULL DEFAULT ('NS'),
	RescissionCurrentYear NVARCHAR(80) NULL DEFAULT ('NS'),
	RescissionPriorYear NVARCHAR(80) NULL DEFAULT ('NS'),
	SequesterReduction NVARCHAR(80) NULL DEFAULT ('NS'),
	SequesterReturn NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT TransTypesPrimaryKey PRIMARY KEY 
    (
        TransTypesId ASC
    )
) ;

CREATE TABLE dbo.TreasurySymbols
(
	TreasurySymbolsId INT NOT NULL UNIQUE,
	ShortKey NVARCHAR(80) NULL DEFAULT ('NS'),
	AllocationTransferAgency NVARCHAR(80) NULL DEFAULT ('NS'),
	AgencyIdentifier NVARCHAR(80) NULL DEFAULT ('NS'),
	BeginningPeriodOfAvailability NVARCHAR(80) NULL DEFAULT ('NS'),
	EndingPeriodOfAvailability NVARCHAR(80) NULL DEFAULT ('NS'),
	AvailabilityType NVARCHAR(80) NULL DEFAULT ('NS'),
	MainAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	SubAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	Lapsed NVARCHAR(80) NULL DEFAULT ('NS'),
	UseCancelledYearSpendingAccounts NVARCHAR(80) NULL DEFAULT ('NS'),
	AgencyTreasurySymbol NVARCHAR(80) NULL DEFAULT ('NS'),
	InUse NVARCHAR(80) NULL DEFAULT ('NS'),
	PreventNewUse NVARCHAR(80) NULL DEFAULT ('NS'),
	Status NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT TreasurySymbolsPrimaryKey PRIMARY KEY 
    (
        TreasurySymbolsId ASC
    )
);

CREATE TABLE dbo.UnliquidatedObligations
(
	UnliquidatedObligationsId INT NOT NULL UNIQUE,
	ObligationsId int NULL,
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RpioName NVARCHAR(80) NULL DEFAULT ('NS'),
	AhCode NVARCHAR(80) NULL DEFAULT ('NS'),
	AhName NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgCode NVARCHAR(80) NULL DEFAULT ('NS'),
	OrgName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectCode NVARCHAR(80) NULL DEFAULT ('NS'),
	ProgramProjectName NVARCHAR(80) NULL DEFAULT ('NS'),
	RcCode NVARCHAR(80) NULL DEFAULT ('NS'),
	RcName NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentType NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	DocumentControlNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(MAX) NULL DEFAULT ('NS'),,
	ProcessedDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	Age FLOAT NULL DEFAULT (0.0),
	BocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BocName NVARCHAR(80) NULL DEFAULT ('NS'),
	FocCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FocName NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmCode NVARCHAR(80) NULL DEFAULT ('NS'),
	NpmName NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorCode NVARCHAR(80) NULL DEFAULT ('NS'),
	VendorName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT UnliquidatedObligationsPrimaryKey PRIMARY KEY 
    (
        UnliquidatedObligationsId ASC
    )
);

CREATE TABLE dbo.UnobligatedBalances
(
	UnobligatedBalancesId INT NOT NULL UNIQUE,
	BudgetYear NVARCHAR(80) NULL DEFAULT ('NS'),
	BFY NVARCHAR(80) NULL DEFAULT ('NS'),
	EFY NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccount NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(80) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(80) NULL DEFAULT ('NS'),
	FundName NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountNumber NVARCHAR(80) NULL DEFAULT ('NS'),
	AccountName NVARCHAR(80) NULL DEFAULT ('NS'),
	Amount FLOAT NULL DEFAULT (0.0),
    CONSTRAINT UnobligatedBalancesPrimaryKey PRIMARY KEY 
    (
        UnobligatedBalancesId ASC
    )
);

CREATE TABLE dbo.URL
(
	SourceId INT NOT NULL UNIQUE,
	Name NVARCHAR(80) NULL DEFAULT ('NS'),
	Location NVARCHAR(80) NULL DEFAULT ('NS'),
	Address NVARCHAR(80) NULL DEFAULT ('NS'),
    CONSTRAINT URLPrimaryKey PRIMARY KEY 
    (
        SourceId ASC
    )
);
