CREATE TABLE IF NOT EXISTS "BudgetDocuments" 
(
	"BudgetDocumentsId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(80) NULL DEFAULT 'NS'
	"EFY"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetLevel"	TEXT(80) NULL DEFAULT 'NS'
	"DocumentDate"	TEXT(80) NULL DEFAULT 'NS'
	"LastDocumentDate"	TEXT(80) NULL DEFAULT 'NS'
	"DocumentType"	TEXT(80) NULL DEFAULT 'NS'
	"DocumentNumber"	TEXT(80) NULL DEFAULT 'NS'
	"FundCode"	TEXT(80) NULL DEFAULT 'NS'
	"FundName"	TEXT(80) NULL DEFAULT 'NS'
	"RpioCode"	TEXT(80) NULL DEFAULT 'NS'
	"RpioName"	TEXT(80) NULL DEFAULT 'NS'
	"AhCode"	TEXT(80) NULL DEFAULT 'NS'
	"AhName"	TEXT(80) NULL DEFAULT 'NS'
	"OrgCode"	TEXT(80) NULL DEFAULT 'NS'
	"OrgName"	TEXT(80) NULL DEFAULT 'NS'
	"AccountCode"	TEXT(80) NULL DEFAULT 'NS'
	"ProgramProjectName"	TEXT(80) NULL DEFAULT 'NS'
	"ProgramAreaCode"	TEXT(80) NULL DEFAULT 'NS'
	"ProgramAreaName"	TEXT(80) NULL DEFAULT 'NS'
	"BocCode"	TEXT(80) NULL DEFAULT 'NS'
	"BocName"	TEXT(80) NULL DEFAULT 'NS'
	"ReimbursableAgreementControls"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetingControls"	TEXT(80) NULL DEFAULT 'NS'
	"PostingControls"	TEXT(80) NULL DEFAULT 'NS'
	"PreCommitmentControls"	TEXT(80) NULL DEFAULT 'NS'
	"CommitmentControls"	TEXT(80) NULL DEFAULT 'NS'
	"ObligationControls"	TEXT(80) NULL DEFAULT 'NS'
	"ExpenditureControls"	TEXT(80) NULL DEFAULT 'NS'
	"ExpenseControls"	TEXT(80) NULL DEFAULT 'NS'
	"AccrualControls"	TEXT(80) NULL DEFAULT 'NS'
	"ReimbursementControls"	TEXT(80) NULL DEFAULT 'NS'
	"Budgeted"	NUMERIC NULL DEFAULT 0,
	"Posted"	NUMERIC NULL DEFAULT 0,
	"CarryOut"	NUMERIC NULL DEFAULT 0,
	"CarryIn"	NUMERIC NULL DEFAULT 0,
	"EstimatedRecoveries"	NUMERIC NULL DEFAULT 0,
	"EstimatedReimbursements"	NUMERIC NULL DEFAULT 0,
	PRIMARY KEY("BudgetDocumentsId" AUTOINCREMENT)
);