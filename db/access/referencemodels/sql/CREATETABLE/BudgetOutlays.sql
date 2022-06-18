CREATE TABLE BudgetOutlays 
(
	BudgetOutlaysId	INTEGER NOT NULL UNIQUE,
	ReportYear TEXT(80) NULL DEFAULT NS,
	Category TEXT(80) NULL DEFAULT NS,
	AgencyName TEXT(80) NULL DEFAULT NS,
	LineNumber TEXT(80) NULL DEFAULT NS,
	LineSection TEXT(80) NULL DEFAULT NS,
	OmbAccount TEXT(80) NULL DEFAULT NS,
	LineTitle TEXT(80) NULL DEFAULT NS,
	AccountType TEXT(80) NULL DEFAULT NS,
	AuthorityTypeName TEXT(80) NULL DEFAULT NS,
	Line TEXT(80) NULL DEFAULT NS,
	AuthorityType TEXT(80) NULL DEFAULT NS,
	PriorYear DOUBLE DEFAULT 0.0,
	CurrentYear DOUBLE DEFAULT 0.0,
	BudgetYear DOUBLE DEFAULT 0.0,
	BudgetYear1 DOUBLE DEFAULT 0.0,
	BudgetYear2 DOUBLE DEFAULT 0.0,
	BudgetYear3 DOUBLE DEFAULT 0.0,
	BudgetYear4 DOUBLE DEFAULT 0.0,
	BudgetYear5 DOUBLE DEFAULT 0.0,
	BudgetYear6 DOUBLE DEFAULT 0.0,
	BudgetYear7 DOUBLE DEFAULT 0.0,
	BudgetYear8 DOUBLE DEFAULT 0.0,
	BudgetYear9 DOUBLE DEFAULT 0.0,
	PRIMARY KEY(BudgetOutlaysId)
);