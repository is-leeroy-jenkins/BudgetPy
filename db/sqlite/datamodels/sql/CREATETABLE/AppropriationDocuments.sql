CREATE TABLE IF NOT EXISTS "AppropriationDocuments" 
(
	"AppropriationDocumentsId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(80) NULL DEFAULT 'NS'
	"EFY"	TEXT(80) NULL DEFAULT 'NS'
	"FundCode"	TEXT(80) NULL DEFAULT 'NS'
	"Fund"	TEXT(80) NULL DEFAULT 'NS'
	"DocumentType"	TEXT(80) NULL DEFAULT 'NS'
	"DocumentNumber"	TEXT(80) NULL DEFAULT 'NS'
	"DocumentDate"	TEXT(80) NULL DEFAULT 'NS'
	"LastDocumentDate"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetLevel"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetingControls"	TEXT(80) NULL DEFAULT 'NS'
	"PostingControls"	TEXT(80) NULL DEFAULT 'NS'
	"PreCommitmentControls"	TEXT(80) NULL DEFAULT 'NS'
	"CommitmentControls"	TEXT(80) NULL DEFAULT 'NS'
	"ObligationControls"	TEXT(80) NULL DEFAULT 'NS'
	"AccrualControls"	TEXT(80) NULL DEFAULT 'NS'
	"ExpenditureControls"	TEXT(80) NULL DEFAULT 'NS'
	"ExpenseControls"	TEXT(80) NULL DEFAULT 'NS'
	"ReimbursementControls"	TEXT(80) NULL DEFAULT 'NS'
	"ReimbursableAgreementControls"	TEXT(80) NULL DEFAULT 'NS'
	"Budgeted"	DOUBLE NULL DEFAULT 0.0.0,
	"Posted"	DOUBLE NULL DEFAULT 0.0.0,
	"CarryOut"	DOUBLE NULL DEFAULT 0.0.0,
	"CarryIn"	DOUBLE NULL DEFAULT 0.0.0,
	"EstimatedReimbursements"	DOUBLE NULL DEFAULT 0.0,
	"EstimatedRecoveries"	DOUBLE NULL DEFAULT 0.0,
	PRIMARY KEY("AppropriationDocumentsId" AUTOINCREMENT)
);