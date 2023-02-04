CREATE TABLE  AppropriationLevelAuthority  
(
	 AppropriationLevelAuthorityId INTEGER NOT NULL UNIQUE,
	 BFY TEXT NULL DEFAULT NS,
	 EFY TEXT NULL DEFAULT NS,
	 FundCode TEXT NULL DEFAULT NS,
	 FundName TEXT NULL DEFAULT NS,
	 BudgetAccountCode TEXT NULL DEFAULT NS,
	 BudgetAccountName TEXT NULL DEFAULT NS,
	 TreasuryAccountCode TEXT NULL DEFAULT NS,
	 TreasuryAccountName TEXT NULL DEFAULT NS,
	 Budgeted NUMERIC NULL DEFAULT 0.0,
	 CarryOver NUMERIC NULL DEFAULT 0.0,
	 TotalReimbursements NUMERIC NULL DEFAULT 0.0,
	 TotalRecoveries NUMERIC NULL DEFAULT 0.0,
	 TotalAuthority NUMERIC NULL DEFAULT 0.0,
	PRIMARY KEY( AppropriationLevelAuthorityId  AUTOINCREMENT)
);