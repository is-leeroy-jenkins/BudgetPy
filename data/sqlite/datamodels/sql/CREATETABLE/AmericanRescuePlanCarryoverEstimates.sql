CREATE TABLE IF NOT EXISTS AmericanRescuePlanCarryoverEstimates
(
	AmericanRescuePlanCarryoverEstimatesId INTEGER NOT NULL UNIQUE,
	BFY TEXT(150) NULL DEFAULT NS,
	EFY TEXT(150) NULL DEFAULT NS,
	TreasuryAccountCode TEXT(150) NULL DEFAULT NS,
	FundCode TEXT(150) NULL DEFAULT NS,
	FundName TEXT(150) NULL DEFAULT NS,
	RpioCode TEXT(150) NULL DEFAULT NS,
	RpioName TEXT(150) NULL DEFAULT NS,
	Amount DOUBLE NULL DEFAULT 0.0,
	OpenCommitments DOUBLE NULL DEFAULT 0.0,
	Obligations DOUBLE NULL DEFAULT 0.0,
	Available DOUBLE NULL DEFAULT 0.0,
	Estimate DOUBLE NULL DEFAULT 0.0,
	CONSTRAINT AmericanRescuePlanCarryoverEstimatesPrimaryKey 
		PRIMARY KEY(AmericanRescuePlanCarryoverEstimatesId)
);
