CREATE TABLE IF NOT EXISTS DeobligationActivity 
(
	DeobligationActivityId	INTEGER NOT NULL UNIQUE,
	BFY	TEXT DEFAULT 'NS',
	EFY	TEXT DEFAULT 'NS',
	TreasuryAccountCode	TEXT DEFAULT 'NS',
	BudgetAccountCode	TEXT DEFAULT 'NS',
	FundCode	TEXT DEFAULT 'NS',
	FundName	TEXT DEFAULT 'NS',
	RpioCode	TEXT DEFAULT 'NS',
	RpioName	TEXT DEFAULT 'NS',
	AhCode	TEXT DEFAULT 'NS',
	AhName	TEXT DEFAULT 'NS',
	OrgCode	TEXT DEFAULT 'NS',
	OrgName	TEXT DEFAULT 'NS',
	AccountCode	TEXT DEFAULT 'NS',
	ProgramProjectName	TEXT DEFAULT 'NS',
	BocCode	TEXT DEFAULT 'NS',
	BocName	TEXT DEFAULT 'NS',
	DocumentNumber	TEXT DEFAULT 'NS',
	ProcessedDate	TEXT DEFAULT 'NS',
	Amount	NUMERIC DEFAULT 0.0,
	PRIMARY KEY(DeobligationActivityId AUTOINCREMENT)
);