CREATE TABLE LedgerAccounts
(
	LedgerAccountsId        INT           NOT NULL UNIQUE,
	BFY                     NVARCHAR(150) NULL DEFAULT ('NS'),
	Number                  NVARCHAR(150) NULL DEFAULT ('NS'),
	Name                    NVARCHAR(150) NULL DEFAULT ('NS'),
	ShortName               NVARCHAR(150) NULL DEFAULT ('NS'),
	AccountClassification   NVARCHAR(150) NULL DEFAULT ('NS'),
	NormalBalance           NVARCHAR(150) NULL DEFAULT ('NS'),
	RealOrClosingAccount    NVARCHAR(150) NULL DEFAULT ('NS'),
	CashAccount             NVARCHAR(150) NULL DEFAULT ('NS'),
	SummaryAccount          NVARCHAR(150) NULL DEFAULT ('NS'),
	ReportableAccount       NVARCHAR(150) NULL DEFAULT ('NS'),
	CostAllocationIndicator NVARCHAR(150) NULL DEFAULT ('NS'),
	FederalNonFederal       NVARCHAR(150) NULL DEFAULT ('NS'),
	AttributeValue          NVARCHAR(150) NULL DEFAULT ('NS'),
	Usage                   NVARCHAR(150) NULL DEFAULT ('NS'),
	Deposit                 NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT LedgerAccountsPrimaryKey PRIMARY KEY
		(
		  LedgerAccountsId ASC
			)
);