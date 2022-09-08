CREATE TABLE LedgerAccounts 
(
    LedgerAccountsId AUTOINCREMENT NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    TreasurySymbol TEXTTEXT(80) NULL DEFAULT NS,
    AccountNumber TEXT(80) NULL DEFAULT NS,
    AccountName TEXT(80) NULL DEFAULT NS,
    BeginningBalance DECIMAL NULL DEFAULT 0.0,
    CreditBalance DECIMAL NULL DEFAULT 0.0,
    DebitBalance DECIMAL NULL DEFAULT 0.0,
    ClosingAmount DECIMAL NULL DEFAULT 0.0,
    CONSTRAINT LedgerAccountsPrimaryKey
        PRIMARY KEY(LedgerAccountsId)
);