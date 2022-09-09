CREATE TABLE LedgerAccounts 
(
    LedgerAccountsId INTEGER NOT NULL UNIQUE,
    BFY TEXT(80) DEFAULT NS,
    EFY TEXT(80) DEFAULT NS,
    FundCode TEXT(80) DEFAULT NS,
    FundName TEXT(80) DEFAULT NS,
    TreasurySymbol TEXTTEXT(80) DEFAULT NS,
    AccountNumber TEXT(80) DEFAULT NS,
    AccountName TEXT(80) DEFAULT NS,
    BeginningBalance DOUBLE DEFAULT 0.0,
    CreditBalance DOUBLE DEFAULT 0.0,
    DebitBalance DOUBLE DEFAULT 0.0,
    ClosingAmount DOUBLE DEFAULT 0.0,
    PRIMARY KEY(LedgerAccountsId)
);