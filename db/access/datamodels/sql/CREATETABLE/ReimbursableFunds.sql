CREATE TABLE ReimbursableFunds 
(
    ReimbursableFundsId AUTOINCREMENT NOT NULL UNIQUE,
    RpioCode TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    AccountCode TEXT(80) NULL DEFAULT NS,
    RcCode TEXT(80) NULL DEFAULT NS,
    RcName TEXT(80) NULL DEFAULT NS,
    BocCode TEXT(80) NULL DEFAULT NS,
    DocumentControlNumber TEXT(80) NULL DEFAULT NS,
    AgreeementNumber TEXT(80) NULL DEFAULT NS,
    Amount DECIMAL NULL DEFAULT 0.0,
    OpenCommitments DECIMAL NULL DEFAULT 0.0,
    Obligations DECIMAL NULL DEFAULT 0.0,
    ULO DECIMAL NULL DEFAULT 0.0,
    Available DECIMAL NULL DEFAULT 0.0,
    CONSTRAINT ReimbursableFundsPrimaryKey
        PRIMARY KEY(ReimbursableFundsId)
);