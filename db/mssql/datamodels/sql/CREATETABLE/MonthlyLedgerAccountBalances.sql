CREATE TABLE MonthlyLedgerAccountBalances 
(
	MonthlyLedgerAccountBalancesId	INT NOT NULL IDENTITY(1,1),
	FiscalYear	NVARCHAR(80) NULL,
	BFY	NVARCHAR(80) NULL,
	EFY	NVARCHAR(80) NULL,
	FundCode	NVARCHAR(80) NULL,
	FundName	NVARCHAR(80) NULL,
	LedgerAccount	NVARCHAR(80) NULL,
	LedgerName	NVARCHAR(80) NULL,
	FiscalMonth	NVARCHAR(80) NULL,
	CreditBalance	FLOAT NULL,
	DebitBalance	FLOAT NULL,
	YearToDateAmount	FLOAT NULL,
	TreasuryAccountCode	NVARCHAR(80) NULL,
	TreasuryAccountName NVARCHAR(MAX) NULL,
	BudgetAccountCode	NVARCHAR(80) NULL,
	BudgetAccountName NVARCHAR(MAX) NULL,
	ApportionmentAccountCode	NVARCHAR(80) NULL
);