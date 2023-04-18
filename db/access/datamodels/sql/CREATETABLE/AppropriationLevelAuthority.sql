CREATE TABLE  AppropriationLevelAuthority  
(
	 AppropriationLevelAuthorityId AUTOINCREMENT NOT NULL UNIQUE,
	 BFY TEXT NULL DEFAULT NS,
	 EFY TEXT NULL DEFAULT NS,
	 FundCode TEXT NULL DEFAULT NS,
	 FundName TEXT NULL DEFAULT NS,
	 BudgetAccountCode TEXT NULL DEFAULT NS,
	 BudgetAccountName TEXT NULL DEFAULT NS,
	 TreasuryAccountCode TEXT NULL DEFAULT NS,
	 TreasuryAccountName TEXT NULL DEFAULT NS,
	 Budgeted DOUBLE NULL DEFAULT 0.0,
	 CarryOver DOUBLE NULL DEFAULT 0.0,
	 TotalReimbursements DOUBLE NULL DEFAULT 0.0,
	 TotalRecoveries DOUBLE NULL DEFAULT 0.0,
	 TotalAuthority DOUBLE NULL DEFAULT 0.0,
	PRIMARY KEY( AppropriationLevelAuthorityId )
);