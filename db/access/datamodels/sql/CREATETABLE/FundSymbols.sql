CREATE TABLE FundSymbols 
(
    FundSymbolsId AUTOINCREMENT NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    TreasuryAccountCode TEXT(80) NULL DEFAULT NS,
    TreasuryAccountName TEXT(80) NULL DEFAULT NS,
    BudgetAccountCode TEXT(80) NULL DEFAULT NS,
    BudgetAccountName TEXT(80) NULL DEFAULT NS,
    ApportionmentAccountCode TEXT(80) NULL DEFAULT NS,
    CONSTRAIN FundSymbolsPrimaryKey
        PRIMARY KEY(FundSymbolsId)
);