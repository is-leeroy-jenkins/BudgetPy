CREATE TABLE GeneralLedgerAccounts 
(
	GeneralLedgerAccountsId	INT NOT NULL IDENTITY(1,1),
	BFY	NVARCHAR(80) NULL,
	Number	NVARCHAR(80) NULL,
	Name	NVARCHAR(80) NULL,
	ShortName	NVARCHAR(80) NULL,
	AccountClassification	NVARCHAR(80) NULL,
	NormalBalance	NVARCHAR(80) NULL,
	FLOATOrClosingAccount	NVARCHAR(80) NULL,
	CashAccount	NVARCHAR(80) NULL,
	SummaryAccount	NVARCHAR(80) NULL,
	ReportableAccount	NVARCHAR(80) NULL,
	CostAllocationIndicator	NVARCHAR(80) NULL,
	FederalNonFederal	NVARCHAR(80) NULL,
	AttributeValue	NVARCHAR(80) NULL,
	Usage	NVARCHAR(80) NULL,
	Deposit	NVARCHAR(80) NULL
);