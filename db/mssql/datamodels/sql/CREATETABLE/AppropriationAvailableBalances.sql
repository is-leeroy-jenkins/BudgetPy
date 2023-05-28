CREATE TABLE AppropriationAvailableBalances
(
	AppropriationAvailableBalancesId INT NOT NULL IDENTITY(1,1),
	BFY NVARCHAR(80) NULL,
	EFY NVARCHAR(80) NULL,
	AppropriationFundCode NVARCHAR(80) NULL,
	AppropriationFundName NVARCHAR(80) NULL,
	TreasurySymbol NVARCHAR(80) NULL,
	OmbAccountCode NVARCHAR(80) NULL,
	Availability NVARCHAR(80) NULL,
	TotalAuthority  FLOAT NULL,
	TotalUsed FLOAT NULL,
	Available FLOAT NULL
);


