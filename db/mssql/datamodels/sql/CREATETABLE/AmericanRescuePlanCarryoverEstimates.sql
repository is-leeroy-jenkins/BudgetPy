CREATE TABLE AmericanRescuePlanCarryoverEstimates 
(
	AmericanRescuePlanCarryoverEstimatesId INT NOT NULL IDENTITY(1,1),
	BFY	NVARCHAR(80) NULL,
	EFY	NVARCHAR(80) NULL,
	TreasuryAccountCode	NVARCHAR(80) NULL,
	FundCode	NVARCHAR(80) NULL,
	FundName	NVARCHAR(80) NULL,
	RpioCode	NVARCHAR(80) NULL,
	RpioName	NVARCHAR(80) NULL,
	Amount	FLOAT NULL,
	OpenCommitments	FLOAT NULL,
	Obligations	FLOAT NULL,
	Available	FLOAT NULL,
	Estimate	FLOAT NULL
);