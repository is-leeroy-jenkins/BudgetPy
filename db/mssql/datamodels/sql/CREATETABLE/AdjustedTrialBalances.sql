CREATE TABLE AdjustedTrialBalances
(
	AdjustedTrialBalancesId INT IDENTITY(1,1) NOT NULL,
	AgencyIdentifier NVARCHAR(255) NULL DEFAULT ('NS'),
	AllocationTransferAgency NVARCHAR(255) NULL DEFAULT ('NS'),
	AvailabilityType NVARCHAR(255) NULL DEFAULT ('NS'),
	MainAccount NVARCHAR(255) NULL DEFAULT ('NS'),
	SubAccount NVARCHAR(255) NULL DEFAULT ('NS'),
	TreasurySymbol NVARCHAR(255) NULL DEFAULT ('NS'),
	BFY NVARCHAR(255) NULL DEFAULT ('NS'),
	EFY NVARCHAR(255) NULL DEFAULT ('NS'),
	FundCode NVARCHAR(255) NULL DEFAULT ('NS'),
	FundName NVARCHAR(255) NULL DEFAULT ('NS'),
	LedgerAccount NVARCHAR(255) NULL DEFAULT ('NS'),
	AccountName NVARCHAR(255) NULL DEFAULT ('NS'),
	BeginningBalance FLOAT NULL DEFAULT (0.0),
	CreditBalance FLOAT NULL DEFAULT (0.0),
	DebitBalance FLOAT NULL DEFAULT (0.0),
	EndingBalance FLOAT NULL DEFAULT (0.0),
	TreasuryAccountCode NVARCHAR(255) NULL DEFAULT ('NS'),
	TreasuryAccountName NVARCHAR(255) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(255) NULL DEFAULT ('NS'),
	BudgetAccountName nvarchar(255) NULL,
	CONSTRAINT AdjustedTrialBalancesPrimaryKey PRIMARY KEY
	(
		AdjustedTrialBalancesId ASC
	)
);
