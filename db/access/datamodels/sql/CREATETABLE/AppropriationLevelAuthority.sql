CREATE TABLE AppropriationLevelAuthority
(
	AppropriationLevelAuthorityId AUTOINCREMENT NOT NULL UNIQUE,
	BudgetAccountCode TEXT(80) NULL DEFAULT NS,
	BudgetAccountName TEXT(80) NULL DEFAULT NS,
	FiscalYear TEXT(80) NULL DEFAULT NS,
	FundCode TEXT(80) NULL DEFAULT NS,
	FundName TEXT(80) NULL DEFAULT NS,
	Budgeted DECIMAL NULL DEFAULT 0.0,
	Posted DECIMAL NULL DEFAULT 0.0,
	CarryOut DECIMAL NULL DEFAULT 0.0,
	CarryIn DECIMAL NULL DEFAULT 0.0,
	EstimatedReimbursements DECIMAL NULL DEFAULT 0.0,
	EstimatedRecoveries DECIMAL NULL DEFAULT 0.0,
	CONSTRAINT AppropriationLevelAuthorityPrimaryKey 
		PRIMARY KEY(AppropriationLevelAuthorityId)
);


