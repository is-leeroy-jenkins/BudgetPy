CREATE TABLE  AppropriationLevelAuthority  
(
    AppropriationLevelAuthorityId AUTOINCREMENT NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    BudgetAccountCode TEXT(80) NULL DEFAULT NS,
    BudgetAccountName TEXT(255) NULL DEFAULT NS,
    TreasuryAccountCode TEXT(80) NULL DEFAULT NS,
    TreasuryAccountName TEXT(255) NULL DEFAULT NS,
    Budgeted DOUBLE NULL DEFAULT 0.0,
    CarryOver DOUBLE NULL DEFAULT 0.0,
    TotalReimbursements DOUBLE NULL DEFAULT 0.0,
    TotalRecoveries DOUBLE NULL DEFAULT 0.0,
    TotalAuthority DOUBLE NULL DEFAULT 0.0,
	 PRIMARY KEY( AppropriationLevelAuthorityId )
);