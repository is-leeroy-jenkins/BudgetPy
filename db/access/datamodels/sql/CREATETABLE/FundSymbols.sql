CREATE TABLE FundSymbols 
(
    FundSymbolsId AUTOINCREMENT NOT NULL UNIQUE,
    TreasuryAccount TEXT(80) NULL DEFAULT NS,
    OmbAccount TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(FundSymbolsId)
);