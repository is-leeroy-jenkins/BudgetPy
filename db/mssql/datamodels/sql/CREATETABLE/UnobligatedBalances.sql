CREATE TABLE UnobligatedBalances
(
	UnobligatedBalancesId INT           NOT NULL UNIQUE,
	BudgetYear            NVARCHAR(150) NULL DEFAULT ('NS'),
	BFY                   NVARCHAR(150) NULL DEFAULT ('NS'),
	EFY                   NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccount         NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountCode   NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountName   NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode     NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName     NVARCHAR(150) NULL DEFAULT ('NS'),
	FundCode              NVARCHAR(150) NULL DEFAULT ('NS'),
	FundName              NVARCHAR(150) NULL DEFAULT ('NS'),
	AccountNumber         NVARCHAR(150) NULL DEFAULT ('NS'),
	AccountName           NVARCHAR(150) NULL DEFAULT ('NS'),
	Amount                FLOAT         NULL DEFAULT (0.0),
	CONSTRAINT UnobligatedBalancesPrimaryKey PRIMARY KEY
		(
		  UnobligatedBalancesId ASC
			)
);
