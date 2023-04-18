CREATE TABLE IF NOT EXISTS AppropriationAvailableBalances
(
	AppropriationAvailableBalancesId INTEGER NOT NULL UNIQUE,
	BFY TEXT(80) NULL DEFAULT 'NS',
	EFY TEXT(80) NULL DEFAULT 'NS',
	AppropriationFundCode TEXT(80) NULL DEFAULT 'NS',
	AppropriationFundName TEXT(80) NULL DEFAULT 'NS',
	TreasurySymbol TEXT(80) NULL DEFAULT 'NS',
	OmbAccountCode TEXT(80) NULL DEFAULT 'NS',
	Availability TEXT(80) NULL DEFAULT 'NS',
	TotalAuthority  DECIMAL NULL DEFAULT 0.0,
	TotalUsed DECIMAL NULL DEFAULT 0.0,
	Available DECIMAL NULL DEFAULT 0.0,
	PRIMARY KEY(AppropriationAvailableBalancesId AUTOINCREMENT)
);


