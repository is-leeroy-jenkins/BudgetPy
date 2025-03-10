CREATE TABLE AppropriationAvailableBalances
(
	AppropriationAvailableBalancesId INT           NOT NULL UNIQUE,
	BFY                              NVARCHAR(150) NULL DEFAULT ('NS'),
	EFY                              NVARCHAR(150) NULL DEFAULT ('NS'),
	FundCode                         NVARCHAR(150) NULL DEFAULT ('NS'),
	FundName                         NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode                NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName                NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountCode              NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountName              NVARCHAR(150) NULL DEFAULT ('NS'),
	OriginalAmount                   FLOAT         NULL DEFAULT (0.0),
	Authority                        FLOAT         NULL DEFAULT (0.0),
	Budgeted                         FLOAT         NULL DEFAULT (0.0),
	Posted                           FLOAT         NULL DEFAULT (0.0),
	CarryoverIn                      FLOAT         NULL DEFAULT (0.0),
	CarryoverOut                     FLOAT         NULL DEFAULT (0.0),
	Used                             FLOAT         NULL DEFAULT (0.0),
	Available                        FLOAT         NULL DEFAULT (0.0),
	CONSTRAINT AppropriationAvailableBalancesPrimaryKey PRIMARY KEY
		(
		  AppropriationAvailableBalancesId ASC
			)
);
