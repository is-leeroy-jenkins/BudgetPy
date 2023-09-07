CREATE TABLE IF NOT EXISTS AnnualReimbursableEstimates 
(
    AnnualReimbursableEstimates Id INTEGER NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    Amount DOUBLE NULL DEFAULT 0.0
    PRIMARY KEY(AnnualReimbursableEstimatesId AUTOINCREMENT)
);