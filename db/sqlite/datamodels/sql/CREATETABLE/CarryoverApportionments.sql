CREATE TABLE IF NOT EXISTS CarryoverApportionments
(
    CarryoverApportionmentsId INTEGER NOT NULL UNIQUE,
    BudgetAccount TEXT(80) NULL DEFAULT NS,
    TreasuryAccount TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    Grouping TEXT(80) NULL DEFAULT NS,
    Description TEXT(80) NULL DEFAULT NS,
    LineName TEXT(80) NULL DEFAULT NS,
    AuthorityType TEXT(80) NULL DEFAULT NS,
    Request DOUBLE NULL DEFAULT 0.0,
    Balance DOUBLE NULL DEFAULT 0.0,
    Deobligations DOUBLE NULL DEFAULT 0.0,
    Amount DOUBLE NULL DEFAULT 0.0,
    LineNumber TEXT(80) NULL DEFAULT NS,
    LineSplit TEXT(80) NULL DEFAULT NS,
    ApportionmentAccountCode TEXT(80) NULL DEFAULT NS,
    TreasuryAccountCode TEXT(80) NULL DEFAULT NS,
    TreasuryAccountName TEXT(80) NULL DEFAULT NS,
    BudgetAccountCode TEXT(80) NULL DEFAULT NS,
    BudgetAccountName TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(CarryoverApportionmentsId AUTOINCREMENT)
);

