CREATE TABLE IF NOT EXISTS MonthlyLedgerAccountBalances 
(
	MonthlyLedgerAccountBalancesId	INTEGER NOT NULL UNIQUE,
	FiscalYear	TEXT(80) NULL DEFAULT 'NS',
	BFY	TEXT(80) NULL DEFAULT 'NS',
	EFY	TEXT(80) NULL DEFAULT 'NS',
	FundCode	TEXT(80) NULL DEFAULT 'NS',
	FundName	TEXT(80) NULL DEFAULT 'NS',
	LedgerAccount	TEXT(80) NULL DEFAULT 'NS',
	LedgerName	TEXT(80) NULL DEFAULT 'NS',
	FiscalMonth	TEXT(80) NULL DEFAULT 'NS',
	CreditBalance	DECIMAL DEFAULT 0.0,
	DebitBalance	DECIMAL DEFAULT 0.0,
	YearToDateAmount	DECIMAL DEFAULT 0.0,
	TreasuryAccountCode	TEXT(80) NULL DEFAULT 'NS',
	TreasuryAccountName	TEXT(80) NULL DEFAULT 'NS',
	BudgetAccountCode	TEXT(80) NULL DEFAULT 'NS',
	BudgetAccountName	TEXT(80) NULL DEFAULT 'NS',
	ApportionmentAccountCode	TEXT(80) NULL DEFAULT 'NS',
	PRIMARY KEY(MonthlyLedgerAccountBalancesId AUTOINCREMENT)
);