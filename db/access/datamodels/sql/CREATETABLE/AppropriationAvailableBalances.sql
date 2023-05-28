CREATE TABLE AppropriationAvailableBalances
(
	AppropriationAvailableBalancesId AUTOINCREMENT NOT NULL UNIQUE,
	BFY TEXT(80) NULL DEFAULT NS,
	EFY TEXT(80) NULL DEFAULT NS,
	AppropriationFundCode TEXT(80) NULL DEFAULT NS,
	AppropriationFundName TEXT(80) NULL DEFAULT NS,
	TreasurySymbol TEXT(80) NULL DEFAULT NS,
	OmbAccountCode TEXT(80) NULL DEFAULT NS,
	Availability TEXT(80) NULL DEFAULT NS,
	TotalAuthority  NULL,
	TotalUsed DOUBLE NULL DEFAULT 0.0,
	Available DOUBLE NULL DEFAULT 0.0,
	CONSTRAINT AppropriationAvailableBalancesPrimaryKey 
		PRIMARY KEY(AppropriationAvailableBalancesId)
);


