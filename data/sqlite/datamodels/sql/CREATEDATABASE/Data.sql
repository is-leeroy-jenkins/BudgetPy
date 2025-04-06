BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Allocations"
(
	"AllocationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"StatusOfFundsId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetLevel" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	'AllocationsId' AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ApplicationTables"
(
	"ApplicationTableId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"TableName"
	TEXT
(
	255
) NOT NULL DEFAULT 'NS',
	"Model" TEXT
(
	255
) NOT NULL DEFAULT 'NS',
	CONSTRAINT "PrimaryKeyApplicationTables" PRIMARY KEY
(
	"ApplicationTableId"
)
	);

CREATE TABLE IF NOT EXISTS "AppropriationDocuments"
(
	"AppropriationDocumentsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Fund" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastDocumentDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetLevel" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetingControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PostingControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PreCommitmentControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CommitmentControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObligationControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccrualControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpenditureControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpenseControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReimbursementControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReimbursableAgreementControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Budgeted" REAL NULL DEFAULT 0.0,
	"Posted" REAL NULL DEFAULT 0.0,
	"CarryOut" REAL NULL DEFAULT 0.0,
	"CarryIn" REAL NULL DEFAULT 0.0,
	"EstimatedReimbursements" REAL NULL DEFAULT 0.0,
	"EstimatedRecoveries" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"AppropriationDocumentsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "BackUpAllocations"
(
	"BackupAllocationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"AllocationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RPIO" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" DOUBLE,
	"AllocationRatio" INTEGER,
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Division" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DivisionName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ChangeDate" DATETIME,
	CONSTRAINT "ForeignKeyBackUpAllocations" FOREIGN KEY
(
	"AllocationsId"
) REFERENCES "Allocations",
	CONSTRAINT "PrimaryKeyBackUpAllocations" PRIMARY KEY
(
	"BackupAllocationsId"
)
	);

CREATE TABLE IF NOT EXISTS "BudgetDocuments"
(
	"BudgetDocumentsId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetLevel" INTEGER,
	"DocumentDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastDocumentDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReimbursableAgreementControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetingControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PostingControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PreCommitmentControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CommitmentControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObligationControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpenditureControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpenseControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccrualControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReimbursementControls" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Budgeted" REAL NULL DEFAULT 0.0,
	"Posted" REAL NULL DEFAULT 0.0,
	"CarryOut" REAL NULL DEFAULT 0.0,
	"CarryIn" REAL NULL DEFAULT 0.0,
	"EstimatedRecoveries" REAL NULL DEFAULT 0.0,
	"EstimatedReimbursements" REAL NULL DEFAULT 0.0
	);

CREATE TABLE IF NOT EXISTS "CarryoverOutlays"
(
	"CarryoverOutlaysId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ReportYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencyName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LINE" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Carryover" REAL NULL DEFAULT 0.0,
	"CarryoverOutlays" REAL NULL DEFAULT 0.0,
	"Delta" REAL NULL DEFAULT 0.0,
	"AvailableBalance" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"CurrentYearAdjustment" REAL NULL DEFAULT 0.0,
	"BudgetYearAdjustment" REAL NULL DEFAULT 0.0,
	"CurrentYear" REAL NULL DEFAULT 0.0,
	"BudgetYear" REAL NULL DEFAULT 0.0,
	"OutYear1" REAL NULL DEFAULT 0.0,
	"OutYear2" REAL NULL DEFAULT 0.0,
	"OutYear3" REAL NULL DEFAULT 0.0,
	"OutYear4" REAL NULL DEFAULT 0.0,
	"OutYear5" REAL NULL DEFAULT 0.0,
	"OutYear6" REAL NULL DEFAULT 0.0,
	"OutYear7" REAL NULL DEFAULT 0.0,
	"OutYear8" REAL NULL DEFAULT 0.0,
	"OutYear9" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"CarryoverOutlaysId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Changes"
(
	"ChangesId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"TableName"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"FieldName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActionType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OldValue" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NewValue" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ChangeDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Message" TEXT
(
	80
) NULL DEFAULT 'NS',
	CONSTRAINT "PrimaryKeyChanges" PRIMARY KEY
(
	"ChangesId"
)
	);

CREATE TABLE IF NOT EXISTS "DataRuleDescriptions"
(
	"DataRuleDescriptionsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Schedule"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RuleNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RuleDescription" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ScheduleOrder" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"DataRuleDescriptionsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "DocumentControlNumbers"
(
	"DocumentControlNumbersId"
	INTEGER
	NOT
	NULL,
	"RpioCode"
	TEXT
	NOT
	NULL
	DEFAULT
	'NS',
	"RpioName"
	TEXT
	NOT
	NULL
	DEFAULT
	'NS',
	"DocumentType"
	TEXT
	NOT
	NULL
	DEFAULT
	'NS',
	"DocumentNumber"
	TEXT
	NOT
	NULL
	DEFAULT
	'NS',
	"DocumentPrefix"
	TEXT
	NOT
	NULL
	DEFAULT
	'NS',
	"DocumentControlNumber"
	TEXT
	NOT
	NULL
	DEFAULT
	'NS',
	PRIMARY
	KEY
(
	"DocumentControlNumbersId"
)
	);

CREATE TABLE IF NOT EXISTS "ExecutionTables"
(
	"ExecutionTablesId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"TableName"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"TableType" TEXT
(
	50
),
	CONSTRAINT "PrimaryKeyExecutionTables" PRIMARY KEY
(
	"ExecutionTablesId"
)
	);

CREATE TABLE IF NOT EXISTS "GrowthRates"
(
	"GrowthRatesId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"RateId"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"DESCRIPTION" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetYearRate" REAL NULL DEFAULT 0.0,
	"OutYear1" REAL NULL DEFAULT 0.0,
	"OutYear2" REAL NULL DEFAULT 0.0,
	"OutYear3" REAL NULL DEFAULT 0.0,
	"OutYear4" REAL NULL DEFAULT 0.0,
	"OutYear5" REAL NULL DEFAULT 0.0,
	"OutYear6" REAL NULL DEFAULT 0.0,
	"OutYear7" REAL NULL DEFAULT 0.0,
	"OutYear8" REAL NULL DEFAULT 0.0,
	"OutYear9" REAL NULL DEFAULT 0.0,
	"Sort" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"GrowthRatesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "MonthlyOutlays"
(
	"MonthlyOutlaysId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"FiscalYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TaxationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAgency" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAgency" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbBureau" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencySequence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BureauSequence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountSequence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencyTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BureauTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccountTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"October" REAL NULL DEFAULT 0.0,
	"November" REAL NULL DEFAULT 0.0,
	"December" REAL NULL DEFAULT 0.0,
	"January" REAL NULL DEFAULT 0.0,
	"Feburary" REAL NULL DEFAULT 0.0,
	"March" REAL NULL DEFAULT 0.0,
	"April" REAL NULL DEFAULT 0.0,
	"May" REAL NULL DEFAULT 0.0,
	"June" REAL NULL DEFAULT 0.0,
	"July" REAL NULL DEFAULT 0.0,
	"August" REAL NULL DEFAULT 0.0,
	"September" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"MonthlyOutlaysId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ReferenceTables"
(
	"ReferenceTablesId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"TableName"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Type" TEXT
(
	80
) NULL DEFAULT 'NS',
	CONSTRAINT "PrimaryKeyReferenceTables" PRIMARY KEY
(
	"ReferenceTablesId"
)
	);

CREATE TABLE IF NOT EXISTS "QueryDefinitions"
(
	"QueryDefinitionsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Name"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Type" TEXT
(
	80
) NULL DEFAULT 'NS',
	CONSTRAINT "PrimaryKeyQueryDefinitions" PRIMARY KEY
(
	"QueryDefinitionsId"
)
	);

CREATE TABLE IF NOT EXISTS "ReimbursableAgreements"
(
	"ReimbursableAgreementsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"RPIO"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgreementNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StartDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndDate" INTEGER,
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DivisionName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"ReimbursableAgreementsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ReimbursableSurvey"
(
	"ReimbursableSurveyId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"ReimbursableSurveyId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Actuals"
(
	"ActualsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubAppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubAppropriationName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioActivityCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioActivityName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ULO" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"Balance" REAL NULL DEFAULT 0.0,
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ActualsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "StatusOfFunds"
(
	"StatusOfFundsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"Budgeted" REAL NULL DEFAULT 0.0,
	"Posted" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Expenditures" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"Used" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"StatusOfFundsId"
)
	);

CREATE TABLE IF NOT EXISTS "PayrollActivity"
(
	"PayrollActivityId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubRcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubRcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"HrOrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"HrOrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"WorkCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"WorkCodeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PayPeriod" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StartDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CheckDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"Hours" REAL NULL DEFAULT 0.0,
	"BasePaid" REAL NULL DEFAULT 0.0,
	"BaseHours" REAL NULL DEFAULT 0.0,
	"Benefits" REAL NULL DEFAULT 0.0,
	"OvertimePaid" REAL NULL DEFAULT 0.0,
	"OvertimeHours" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"PayrollActivityId"
)
	);

CREATE TABLE IF NOT EXISTS "SiteActivity"
(
	"SiteActivityId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EpaSiteId" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SSID" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActionCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OperableUnit" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"State" TEXT
(
	80
) NULL DEFAULT 'NS',
	"City" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CongressionalDistrict" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StartDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastActivity" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Requested" REAL NULL DEFAULT 0.0,
	"Accepted" REAL NULL DEFAULT 0.0,
	"Closed" REAL NULL DEFAULT 0.0,
	"Outstanding" REAL NULL DEFAULT 0.0,
	"Refunded" REAL NULL DEFAULT 0.0,
	"Reversal" REAL
	);

CREATE TABLE IF NOT EXISTS "CongressionalReprogrammings"
(
	"CongressionalTransferId"
	INTEGER,
	"ReprogrammingNumber"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"Description" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExtendedDescription" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FromTo" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Cycle" TEXT
	);

CREATE TABLE IF NOT EXISTS "StatusOfAppropriations"
(
	"StatusOfAppropriationsId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetLevel" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationFundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationFundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Availability" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationCreationDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubAppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationDescription" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundGroup" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundGroupName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActualRecoveryTransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CommitmentSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgreementLimit" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EstimatedRecoveriesTransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EstimatedReimbursmentsTransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpenseSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObligationSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PreCommitmentSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PostedControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PostedFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RecordCarryoverAtLowerLevel" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReimbursableSpendingOption" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RecoveriesOption" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RecoveriesSpendingOption" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OriginalBudgetedAmount" REAL NULL DEFAULT 0.0,
	"ApportionmentsPosted" REAL NULL DEFAULT 0.0,
	"TotalAuthority" REAL NULL DEFAULT 0.0,
	"TotalBudgeted" REAL NULL DEFAULT 0.0,
	"TotalPostedAmount" REAL NULL DEFAULT 0.0,
	"FundsWithdrawnPriorYearsAmount" REAL NULL DEFAULT 0.0,
	"FundingInAmount" REAL NULL DEFAULT 0.0,
	"FundingOutAmount" REAL NULL DEFAULT 0.0,
	"TotalAccrualRecoveries" REAL NULL DEFAULT 0.0,
	"TotalActualReimbursements" REAL NULL DEFAULT 0.0,
	"TotalAgreementReimbursables" REAL NULL DEFAULT 0.0,
	"TotalCarriedForwardIn" REAL NULL DEFAULT 0.0,
	"TotalCarriedForwardOut" REAL NULL DEFAULT 0.0,
	"TotalCommitted" REAL NULL DEFAULT 0.0,
	"TotalEstimatedRecoveries" REAL NULL DEFAULT 0.0,
	"TotalEstimatedReimbursements" REAL NULL DEFAULT 0.0,
	"TotalExpenses" REAL NULL DEFAULT 0.0,
	"TotalExpenditureExpenses" REAL NULL DEFAULT 0.0,
	"TotalExpenseAccruals" REAL NULL DEFAULT 0.0,
	"TotalPreCommitments" REAL NULL DEFAULT 0.0,
	"UnliquidatedPreCommitments" REAL NULL DEFAULT 0.0,
	"TotalObligations" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"VoidedAmount" REAL NULL DEFAULT 0.0,
	"TotalUsedAmount" REAL NULL DEFAULT 0.0,
	"AvailableAmount" REAL
	);

CREATE TABLE IF NOT EXISTS "GrossBudgetAuthorityOutlays"
(
	"GrossBudgetAuthorityOutlaysId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ReportYear"
	TEXT
	DEFAULT
	'NS',
	"AgencyName"
	TEXT
	DEFAULT
	'NS',
	"OmbAccount"
	TEXT
	DEFAULT
	'NS',
	"Line"
	TEXT
	DEFAULT
	'NS',
	"LineNumber"
	TEXT
	DEFAULT
	'NS',
	"LineSection"
	TEXT
	DEFAULT
	'NS',
	"LineName"
	TEXT
	DEFAULT
	'NS',
	"BeaCategory"
	TEXT
	DEFAULT
	'NS',
	"BeaCategoryName"
	TEXT
	DEFAULT
	'NS',
	"LineCategory"
	TEXT
	DEFAULT
	'NS',
	"PriorYear"
	NUMERIC
	DEFAULT
	0,
	"CurrentYear"
	NUMERIC
	DEFAULT
	0,
	"BudgetYear"
	NUMERIC
	DEFAULT
	0,
	"OutYear1"
	NUMERIC
	DEFAULT
	0,
	"OutYear2"
	NUMERIC
	DEFAULT
	0,
	"OutYear3"
	NUMERIC
	DEFAULT
	0,
	"OutYear4"
	NUMERIC
	DEFAULT
	0,
	"OutYear5"
	NUMERIC
	DEFAULT
	0,
	"OutYear6"
	NUMERIC
	DEFAULT
	0,
	"OutYear7"
	NUMERIC
	DEFAULT
	0,
	"OutYear8"
	NUMERIC
	DEFAULT
	0,
	"OutYear9"
	NUMERIC
	DEFAULT
	0,
	PRIMARY
	KEY
(
	"GrossBudgetAuthorityOutlaysId"
	AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "UnobligatedAuthority"
(
	"UnobligatedAuthorityId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ReportYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencyCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencyName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BureauCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BureauName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetYear" REAL NULL DEFAULT 0.0,
	"PriorYear" REAL NULL DEFAULT 0.0,
	"CurrentYear" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"UnobligatedAuthorityId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "UnliquidatedObligations"
(
	"UnliquidatedObligationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ObligationsId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentControlNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReferenceDocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastActivityDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Age" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"UnliquidatedObligationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "BudgetaryResourceExecution"
(
	"BudgetaryResourceExecutionId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"FiscalYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastUpdate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAgencyCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"STAT" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CreditIndicator" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineDescription" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SectionName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SectionNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FinancingAccounts" TEXT
(
	80
) NULL DEFAULT 'NS',
	"November" REAL NULL DEFAULT 0.0,
	"January" REAL NULL DEFAULT 0.0,
	"Feburary" REAL NULL DEFAULT 0.0,
	"April" REAL NULL DEFAULT 0.0,
	"May" REAL NULL DEFAULT 0.0,
	"June" REAL NULL DEFAULT 0.0,
	"August" REAL NULL DEFAULT 0.0,
	"October" REAL NULL DEFAULT 0.0,
	"Amount1" REAL NULL DEFAULT 0.0,
	"Amount2" REAL NULL DEFAULT 0.0,
	"Amount3" REAL NULL DEFAULT 0.0,
	"Amount4" REAL NULL DEFAULT 0.0,
	"Agency" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Bureau" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"BudgetaryResourceExecutionId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ProgramFinancingSchedule"
(
	"ProgramFinancingScheduleId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ReportYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAgencyCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LedgerAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SectionNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SectionName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineDescription" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAgencyCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbFundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccountTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencySequence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountSequence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OriginalAmount" REAL NULL DEFAULT 0.0,
	"BudgetAmount" REAL NULL DEFAULT 0.0,
	"AgencyAmount" REAL NULL DEFAULT 0.0,
	"Amount" REAL NULL DEFAULT 0.0,
	"AgencyName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ProgramFinancingScheduleId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Transfers"
(
	"TransfersId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocPrefix" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReprogrammingNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ControlNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Quarter" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Line" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Subline" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FromTo" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC DEFAULT 0,
	"ResourceType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Purpose" TEXT
(
	80
) DEFAULT 'NOT SPECIFIED',
	"ExtendedPurpose" TEXT
(
	80
) DEFAULT 'NOT SPECIFIED',
	PRIMARY KEY
(
	"TransfersId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Deobligations"
(
	"DeobligationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC DEFAULT 0,
	PRIMARY KEY
(
	"DeobligationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Obligations"
(
	"ObligationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentControlNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReferenceDocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastActivityDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Age" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OpenCommitments" NUMERIC DEFAULT 0,
	"Obligations" NUMERIC DEFAULT 0,
	"ULO" NUMERIC DEFAULT 0,
	"Expenditures" NUMERIC DEFAULT 0,
	PRIMARY KEY
(
	"ObligationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Expenditures"
(
	"ExpendituresId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ObligationsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentControlNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReferenceDocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastActivityDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Age" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC DEFAULT 0,
	PRIMARY KEY
(
	"ExpendituresId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "OpenCommitments"
(
	"OpenCommitmentsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ObligationsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentControlNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReferenceDocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastActivityDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Age" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"VendorName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC DEFAULT 0,
	PRIMARY KEY
(
	'OpenCommitmentsId' AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "SubAppropriations"
(
	"SubAppropriationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"SubAppropriationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ApportionmentData"
(
	"ApportionmentDataId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"FiscalYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAppropriationFundSymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAppropriationFundSymbolName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApportionmentAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApportionmentAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AvailabilityType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApprovalDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"ApportionmentDataId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "AppropriationAvailableBalances"
(
	"AppropriationAvailableBalancesId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationFundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationFundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Availability" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TotalAuthority" REAL NULL DEFAULT 0.0,
	"TotalUsed" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"AppropriationAvailableBalancesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Appropriations"
(
	"AppropriationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"AppropriationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "UnobligatedBalances"
(
	"UnobligatedBalancesId"
	INTEGER,
	"BudgetYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC NULL DEFAULT 0.0
	);

CREATE TABLE IF NOT EXISTS "Funds"
(
	"FundsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Code" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ShortName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Status" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StartDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubLevelPrefix" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ATA" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AID" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BeginningPeriodOfAvailability" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndingPeriodOfAvailability" TEXT
(
	80
) NULL DEFAULT 'NS',
	"A" TEXT
(
	80
) NULL DEFAULT 'NS',
	"MAIN" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SUB" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCategory" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubAppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundGroup" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NoYear" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Carryover" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CanceledYearSpendingAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApplyAtAllLevels" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BatsFund" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BatsEndDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BatsOptionId" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SecurityOrg" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApportionmentAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"FundsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "FundSymbols"
(
	"FundSymbolsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApportionmentAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"FundSymbolsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "StateOrganizations"
(
	"StateOrganizationsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Name"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Code" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"StateOrganizationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "StateGrantObligations"
(
	"StateGrantObligationsId"
	INTEGER
	NOT
	NULL,
	"RpioCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StateCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StateName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC
	);

CREATE TABLE IF NOT EXISTS "StatusOfEarmarks"
(
	"StatusOfEarmarksId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"StatusOfFundsId"
	INTEGER,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Budgeted" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Posted" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Expenditures" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"Used" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"StatusOfEarmarksId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "NetTransfers"
(
	"PrcId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Net" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC
	);

CREATE TABLE IF NOT EXISTS "NetObligations"
(
	"NetObligationsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"NetObligationsId"
)
	);

CREATE TABLE IF NOT EXISTS "NetDeobligations"
(
	"NetDeobligationsId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProcessedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"NetDeobligationsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "NetAuthority"
(
	"PrcId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Authority" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"Committed" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"Obligated" REAL NULL DEFAULT 0.0,
	"UnliquidatedObligations" REAL NULL DEFAULT 0.0,
	"Unliquidated" REAL NULL DEFAULT 0.0,
	"Used" REAL NULL DEFAULT 0.0,
	"Utilization" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	"Availability" REAL NULL DEFAULT 0.0,
	"Outlays" REAL NULL DEFAULT 0.0,
	"Outlaid" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"PrcId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "MonthlyLedgerAccountBalances"
(
	"MonthlyLedgerAccountBalancesId"
	INTEGER
	NOT
	NULL,
	"FiscalYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LedgerAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LedgerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApportionmentAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbolName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FiscalMonth" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CreditBalance" REAL NULL DEFAULT 0.0,
	"DebitBalance" REAL NULL DEFAULT 0.0,
	"YearToDateAmount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"MonthlyLedgerAccountBalancesId"
)
	);

CREATE TABLE IF NOT EXISTS "CompassOutlays"
(
	"CompassOutlaysId"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"MonthProcessed" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TotalObligations" REAL NULL DEFAULT 0.0,
	"UnliquidatedObligations" REAL NULL DEFAULT 0.0,
	"ObligationsPaid" NUMERIC
	);

CREATE TABLE IF NOT EXISTS "AppropriationLevelAuthority"
(
	"AppropriationBalancesId"
	INTEGER
	NOT
	NULL,
	"BudgetAccountCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FiscalYear" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Budgeted" REAL NULL DEFAULT 0.0,
	"Posted" REAL NULL DEFAULT 0.0,
	"CarryOut" REAL NULL DEFAULT 0.0,
	"CarryIn" REAL NULL DEFAULT 0.0,
	"EstimatedReimbursements" REAL NULL DEFAULT 0.0,
	"EstimatedRecoveries" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"AppropriationBalancesId"
)
	);

CREATE TABLE IF NOT EXISTS "FundCategories"
(
	"FundCategoriesId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ShortName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"FundCategoriesId"
)
	);

CREATE TABLE IF NOT EXISTS "CarryoverApportionments"
(
	"CarryoverApportionmentsId"
	INTEGER
	NOT
	NULL,
	"BudgetAccount"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Group" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Description" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AuthorityType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Request" REAL NULL DEFAULT 0.0,
	"Balance" REAL NULL DEFAULT 0.0,
	"Deobligations" REAL NULL DEFAULT 0.0,
	"Amount" REAL NULL DEFAULT 0.0,
	"LineNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LineSplit" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ApportionmentAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"CarryoverApportionmentsId"
)
	);

CREATE TABLE IF NOT EXISTS "CompassLevels"
(
	"CompassLevelsId"
	INTEGER
	NOT
	NULL,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubAppropriationCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Description" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PostedControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActualRecoveryTransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CommitmentSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetDefault" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerChildExpenditureSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerChildExpenseSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FteControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccrualSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObligationSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PreCommitmentSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerCommitmentSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerObligationSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerExpenditureSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerExpenseSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerPostedControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerPostedTransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerTransType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerPostedFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerPreCommitmentSpendingControlFlag" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerRecoveriesSpendingOption" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerRecoveriesOption" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerReimbursableSpendingOption" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Date" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TotalAuthority" REAL NULL DEFAULT 0.0,
	"OriginalAmount" REAL NULL DEFAULT 0.0,
	"CarryoverAvailabilityPercentage" REAL NULL DEFAULT 0.0,
	"CarryIn" REAL NULL DEFAULT 0.0,
	"CarryOut" REAL NULL DEFAULT 0.0,
	"FundsIn" REAL NULL DEFAULT 0.0,
	"FundOut" REAL NULL DEFAULT 0.0,
	"RecoveriesWithdrawn" REAL NULL DEFAULT 0.0,
	"ActualRecoveries" REAL NULL DEFAULT 0.0,
	"ActualReimbursements" REAL NULL DEFAULT 0.0,
	"AgreementReimbursables" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"CompassLevelsId"
)
	);

CREATE TABLE IF NOT EXISTS "AmericanRescuePlan"
(
	"AmericanRescuePlanId"
	INTEGER,
	"StatusOfFundsId"
	INTEGER,
	"BudgetLevel"
	INTEGER,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" INTEGER,
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"Budgeted" REAL NULL DEFAULT 0.0,
	"Posted" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Expenditures" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"Used" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS'
	);

CREATE TABLE IF NOT EXISTS "AllowanceHolders"
(
	"AllowanceHoldersId"
	INTEGER,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS'
	);

CREATE TABLE IF NOT EXISTS "AnnualCarryoverEstimates"
(
	"AnnualCarryoverEstimatesId"
	INTEGER,
	"BFY"
	INTEGER,
	"EFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" INTEGER,
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OpenCommitments" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Obligations" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Available" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Estimate" TEXT
	);

CREATE TABLE IF NOT EXISTS "AnnualReimbursableEstimates"
(
	"ReimbursableEstimatesId"
	INTEGER,
	"BFY"
	INTEGER,
	"EFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" INTEGER,
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OpenCommitments" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Obligations" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Available" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Estimate" TEXT
	);

CREATE TABLE IF NOT EXISTS "BudgetObjectClasses"
(
	"BudgetObjectClassesId"
	INTEGER,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
	);

CREATE TABLE IF NOT EXISTS "Accounts"
(
	"AccountsId"
	INTEGER,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgencyActivity" TEXT
(
	80
) NULL DEFAULT 'NS'
	);

CREATE TABLE IF NOT EXISTS "ActivityCodes"
(
	"ActivityId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Description" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ActivityId"
)
	);

CREATE TABLE IF NOT EXISTS "CapitalPlanningInvestmentCodes"
(
	"CapitalPlanningInvestmentCodesId"
	INTEGER
	NOT
	NULL,
	"Type"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Code" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"CapitalPlanningInvestmentCodesId"
)
	);

CREATE TABLE IF NOT EXISTS "CongressionalControls"
(
	"CongressionalControlsId"
	INTEGER
	NOT
	NULL,
	"FundCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ReprogrammingRestriction" TEXT
(
	80
) NULL DEFAULT 'NS',
	"IncreaseRestriction" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DecreaseRestriction" TEXT
(
	80
) NULL DEFAULT 'NS',
	"MemoRequirement" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"CongressionalControlsId"
)
	);

CREATE TABLE IF NOT EXISTS "CostAreas"
(
	"CostAreasId"
	INTEGER,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
	);

CREATE TABLE IF NOT EXISTS "Defactos"
(
	"DefactosId"
	INTEGER
	NOT
	NULL,
	"StatusOfFundsId"
	INTEGER,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"Budgeted" REAL NULL DEFAULT 0.0,
	"Posted" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Expenditures" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"Used" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"DefactosId"
)
	);

CREATE TABLE IF NOT EXISTS "Documents"
(
	"DocumentsId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Category" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"System" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"DocumentsId"
)
	);

CREATE TABLE IF NOT EXISTS "FederalHolidays"
(
	"FederalHolidaysId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Columbus" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Veterans" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Thanksgiving" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Christmas" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NewYears" TEXT
(
	80
) NULL DEFAULT 'NS',
	"MartinLutherKing" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Washingtons" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Memorial" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Juneteenth" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Independence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Labor" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"FederalHolidaysId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "FiscalYears"
(
	"BudgetFiscalYearsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StartDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Columbus" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Christmas" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Thanksgiving" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Veterans" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Labor" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Independence" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Juneteenth" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Memorial" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Washingtons" TEXT
(
	80
) NULL DEFAULT 'NS',
	"MartinLutherKing" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NewYears" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpiringYear" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ExpirationDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CancellationDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"WorkDays" INTEGER,
	"WeekDays" INTEGER,
	"WeekEnds" INTEGER,
	"Availability" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"BudgetFiscalYearsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "FinanceObjectClasses"
(
	"FinanceObjectClassesId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"FinanceObjectClassesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "FullTimeEquivalents"
(
	"FullTimeEquivialentsId"
	INTEGER
	NOT
	NULL,
	"OperatingPlansId"
	INTEGER,
	"RpioCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"ITProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectTypeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectTypeCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LocalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LocalCodeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CostAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CostAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"FullTimeEquivialentsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "HeadquartersOffices"
(
	"HeadquartersOfficesId"
	INTEGER
	NOT
	NULL,
	"ResourcePlanningOfficesId"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Code" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"HeadquartersOfficesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "LedgerAccounts"
(
	"LedgerAccountsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasurySymbol" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BeginningBalance" REAL NULL DEFAULT 0.0,
	"CreditBalance" REAL NULL DEFAULT 0.0,
	"DebitBalance" REAL NULL DEFAULT 0.0,
	"ClosingAmount" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"LedgerAccountsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "NationalPrograms"
(
	"NationalProgramsId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Title" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"NationalProgramsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "OperatingPlans"
(
	"OperatingPlansId"
	INTEGER
	NOT
	NULL,
	"RpioCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"ITProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectTypeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProjectTypeCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActivityName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LocalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LocalCodeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CostAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CostAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"GoalName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectiveName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"OperatingPlansId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ProgramAreas"
(
	"ProgramAreasId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ProgramAreasId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ProgramProjects"
(
	"ProgramProjectsId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ProgramProjectsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "Projects"
(
	"ProjectsId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ProjectsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "PublicLaws"
(
	"PublicLawsId"
	INTEGER
	NOT
	NULL,
	"LawNumber"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BillTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EnactedDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Congress" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"PublicLawsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ResourcePlanningOffices"
(
	"ResourcePlanningOfficesId"
	INTEGER
	NOT
	NULL,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"ResourcePlanningOfficesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "RegionalOffices"
(
	"RegionalOfficesId"
	INTEGER
	NOT
	NULL,
	"ResourcePlanningOfficesId"
	INTEGER,
	"Code"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Name" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"RegionalOfficesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ReimbursableFunds"
(
	"ReimbursableFundsId"
	INTEGER
	NOT
	NULL,
	"RpioCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentControlNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AgreeementNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Available" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"ReimbursableFundsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "SpecialAccounts"
(
	"SpecialAccountsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SpecialAccountFund" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SpecialAccountNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SpecialAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountStatus" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NplStatusCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NplStatusName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteId" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CerclisId" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OperableUnit" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PipelineCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PipelineDescription" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TransactionType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TransactionTypeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TransactionDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AvailableBalance" REAL NULL DEFAULT 0.0,
	"OpenCommitments" REAL NULL DEFAULT 0.0,
	"Obligations" REAL NULL DEFAULT 0.0,
	"ULO" REAL NULL DEFAULT 0.0,
	"Disbursements" REAL NULL DEFAULT 0.0,
	"UnpaidBalances" REAL NULL DEFAULT 0.0,
	"Collections" REAL NULL DEFAULT 0.0,
	"CumulativeReceipts" REAL NULL DEFAULT 0.0,
	PRIMARY KEY
(
	"SpecialAccountsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "SiteProjectCodes"
(
	"SiteProjectCodesId"
	INTEGER,
	"RpioCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"State" TEXT
(
	80
) NULL DEFAULT 'NS',
	"CongressionalDistrict" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EpaSiteId" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SiteProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SSID" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ActionCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OperableUnit" TEXT
	);

CREATE TABLE IF NOT EXISTS "TransTypes"
(
	"TransTypesId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AppropriationBill" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ContinuingResolution" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RescissionCurrentYear" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RescissionPriorYear" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SequesterReduction" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SequesterReturn" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"TransTypesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "BudgetControls"
(
	"BudgetControlsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Code"
	TEXT
	DEFAULT
	'NS',
	"Name"
	TEXT
	DEFAULT
	'NS',
	"BudgetedTransType"
	TEXT
	DEFAULT
	'NS',
	"PostedTransType"
	TEXT
	DEFAULT
	'NS',
	"EstimatedReimbursementsTransType"
	TEXT
	DEFAULT
	'NS',
	"SpendingAdjustmentTransType"
	TEXT
	DEFAULT
	'NS',
	"EstimatedRecoveriesTransType"
	TEXT
	DEFAULT
	'NS',
	"ActualRecoveriesTransType"
	TEXT
	DEFAULT
	'NS',
	"StatusReserveTransType"
	TEXT
	DEFAULT
	'NS',
	"ProfitLossTransType"
	TEXT
	DEFAULT
	'NS',
	"EstimatedReimbursementsSpendingOption"
	TEXT
	DEFAULT
	'NS',
	"EstimatedReimursementsBudgetingOption"
	TEXT
	DEFAULT
	'NS',
	"TrackAgreementLowerLevel"
	TEXT
	DEFAULT
	'NS',
	"BudgetEstimatedLowerLevel"
	TEXT
	DEFAULT
	'NS',
	"EstimatedRecoveriesSpendingOption"
	TEXT
	DEFAULT
	'NS',
	"EstimatedRecoveriesBudgetingOption"
	TEXT
	DEFAULT
	'NS',
	"RecoveryNextLevel"
	TEXT
	DEFAULT
	'NS',
	"RecoveryBudgetMismatch"
	TEXT
	DEFAULT
	'NS',
	"ProfitLossSpendingOption"
	TEXT
	DEFAULT
	'NS',
	"ProfitLossBudgetOption"
	TEXT
	DEFAULT
	'NS',
	"RecoveriesCarryInLowerLevel"
	TEXT
	DEFAULT
	'NS',
	"RecoveriesCarryInLowerLevelControl"
	TEXT
	DEFAULT
	'NS',
	"RecoveriesCarryInAmountControl"
	TEXT
	DEFAULT
	'NS',
	"BudgetedControl"
	TEXT
	DEFAULT
	'NS',
	"PostedControl"
	TEXT
	DEFAULT
	'NS',
	"PreCommitmentSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"CommitmentSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"ObligationSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"AccrualSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"ExpenditureSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"ExpenseSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"ReimbursableSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"ReimbursableAgreementSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"FteBudgetingControl"
	TEXT
	DEFAULT
	'NS',
	"FteSpendingControl"
	TEXT
	DEFAULT
	'NS',
	"TransactionTypeControl"
	TEXT
	DEFAULT
	'NS',
	"AuthorityDistributionControl"
	TEXT
	DEFAULT
	'NS',
	PRIMARY
	KEY
(
	"BudgetControlsId"
	AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "ObjectClassOutlays"
(
	"ObjectClassOutlaysId"
	INTEGER,
	"ReportYear"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAgencyCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAgencyName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbBureauCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbBureauName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OmbAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObligationType" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DirectReimbursableTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectClassGroupNumber" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ObjectClassGroupName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FinanceObjectClass" TEXT
(
	80
) NULL DEFAULT 'NS',
	"PriorYear" NUMERIC NULL DEFAULT 0.0,
	"CurrentYear" NUMERIC NULL DEFAULT 0.0,
	"BudgetYear" INTEGER DEFAULT 0.0
	);

CREATE TABLE IF NOT EXISTS "PayPeriods"
(
	"PayPeriodsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"Period"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"PayPeriod" TEXT
(
	80
) NULL DEFAULT 'NS',
	"StartDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EndDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"PayPeriodsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "PayrollAuthority"
(
	"PayrollAuthorityId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"AllocationsId"
	INTEGER
	NOT
	NULL,
	"StatusOfFundsId"
	INTEGER
	NOT
	NULL,
	"BFY"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetLevel" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC NULL DEFAULT 0.0,
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"PayrollAuthorityId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "PayrollCostCodes"
(
	"PayrollCostCodesId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"RpioCode"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubRcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"SubRcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"HrOrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"HrOrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"WorkCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"WorkCodeName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"PayrollCostCodesId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "PayrollRequests"
(
	"PayrollRequestsId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"ControlTeamAnalyst"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"DocumentTitle" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC NULL DEFAULT 0.0,
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Status" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OriginalRequestDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LastActivityDate" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFS" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Comments" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RequestDocument" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Duration" INTEGER DEFAULT 0,
	PRIMARY KEY
(
	"PayrollRequestsId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "StatusOfJobsActFunding"
(
	"StatusOfJobsActFundingId"
	INTEGER
	UNIQUE,
	"StatusOfFundsId"
	INTEGER,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC NULL DEFAULT 0.0,
	"Budgeted" NUMERIC NULL DEFAULT 0.0,
	"Posted" NUMERIC NULL DEFAULT 0.0,
	"OpenCommitments" NUMERIC NULL DEFAULT 0.0,
	"ULO" NUMERIC NULL DEFAULT 0.0,
	"Expenditures" NUMERIC NULL DEFAULT 0.0,
	"Obligations" NUMERIC NULL DEFAULT 0.0,
	"Used" NUMERIC NULL DEFAULT 0.0,
	"Available" NUMERIC NULL DEFAULT 0.0,
	"Balance" NUMERIC NULL DEFAULT 0.0,
	"TreasuryAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"TreasuryAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BudgetAccountName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"StatusOfJobsActFundingId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "StatusOfSupplementalFunding"
(
	"SupplementalAuthorityId"
	INTEGER
	NOT
	NULL
	UNIQUE,
	"StatusOfFundsId"
	INTEGER
	NOT
	NULL,
	"BudgetLevel"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"BFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"EFY" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RpioName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AhName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"FundName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"OrgName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"AccountCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"BocName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramProjectName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"ProgramAreaName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"RcName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"LowerName" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Amount" NUMERIC NULL DEFAULT 0.0,
	"Budgeted" NUMERIC NULL DEFAULT 0.0,
	"Posted" NUMERIC NULL DEFAULT 0.0,
	"OpenCommitments" NUMERIC NULL DEFAULT 0.0,
	"ULO" NUMERIC NULL DEFAULT 0.0,
	"Expenditures" NUMERIC NULL DEFAULT 0.0,
	"Obligations" NUMERIC NULL DEFAULT 0.0,
	"Used" NUMERIC NULL DEFAULT 0.0,
	"Available" NUMERIC NULL DEFAULT 0.0,
	"Balance" NUMERIC NULL DEFAULT 0.0,
	"NpmCode" TEXT
(
	80
) NULL DEFAULT 'NS',
	"NpmName" TEXT
(
	80
) NULL DEFAULT 'NS',
	PRIMARY KEY
(
	"SupplementalAuthorityId" AUTOINCREMENT
)
	);

CREATE TABLE IF NOT EXISTS "URL"
(
	"SourceId"
	INTEGER,
	"Name"
	TEXT
(
	80
) NULL DEFAULT 'NS',
	"Location" TEXT
(
	80
) NULL DEFAULT 'NS',
	"Address" TEXT
	);
COMMIT;
