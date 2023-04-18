CREATE TABLE IF NOT EXISTS ObjectClassOutlays 
(
	ObjectClassOutlaysId	INTEGER NOT NULL UNIQUE,
	ReportYear	TEXT(80) NULL DEFAULT 'NS',
	BudgetAgencyCode	TEXT(80) NULL DEFAULT 'NS',
	BudgetAgencyName	TEXT(80) NULL DEFAULT 'NS',
	BudgetBureauCode	TEXT(80) NULL DEFAULT 'NS',
	BudgetBureauName	TEXT(80) NULL DEFAULT 'NS',
	BudgetAccountCode	TEXT(80) NULL DEFAULT 'NS',
	BudgetAccountName	TEXT(80) NULL DEFAULT 'NS',
	ObligationType	TEXT(80) NULL DEFAULT 'NS',
	DirectReimbursableTitle	TEXT(80) NULL DEFAULT 'NS',
	ObjectClassGroupNumber	TEXT(80) NULL DEFAULT 'NS',
	ObjectClassGroupName	TEXT(80) NULL DEFAULT 'NS',
	BocCode	TEXT(80) NULL DEFAULT 'NS',
	BocName	TEXT(80) NULL DEFAULT 'NS',
	FinanceObjectClass	TEXT(80) NULL DEFAULT 'NS',
	PriorYear	NUMERIC NULL DEFAULT 0.0,
	CurrentYear	NUMERIC NULL DEFAULT 0.0,
	BudgetYear	NUMERIC NULL DEFAULT 0.0,
	PRIMARY KEY(ObjectClassOutlaysId AUTOINCREMENT)
);