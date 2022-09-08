CREATE TABLE UnobligatedBalances 
(
    UnobligatedBalancesId AUTOINCREMENT NOT NULL UNIQUE,
    BudgetYear TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    TreasurySymbol TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    AccountNumber TEXT(80) NULL DEFAULT NS,
    AccountName TEXT(80) NULL DEFAULT NS,
    Amount DECIMAL NULL DEFAULT 0.0,
    CONSTRAINT UnobligatedBalancePrimaryKey
        PRIMARY KEY(UnobligatedBalancesId)
);