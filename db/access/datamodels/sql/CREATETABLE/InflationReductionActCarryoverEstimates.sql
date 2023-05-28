CREATE TABLE InflationReductionActCarryoverEstimates 
(
    InflationReductionActCarryoverEstimatesId AUTOINCREMENT NOT NULL UNIQUE,
    BudgetLevel TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    TreasuryAccountCode TEXT(80) NULL DEFAULT NS,
    RpioCode TEXT(80) NULL DEFAULT NS,
    RpioName TEXT(80) NULL DEFAULT NS,
    OpenCommitments DOUBLE NULL DEFAULT 0.0,
    Obligations DOUBLE NULL DEFAULT 0.0,
    Available DOUBLE NULL DEFAULT 0.0,
    Estimate DOUBLE NULL DEFAULT 0.0,
    CONSTRAINT InflationReductionActCarryoverEstimatesPrimaryKey
        PRIMARY KEY(InflationReductionActCarryoverEstimatesId)
);