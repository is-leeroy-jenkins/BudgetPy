CREATE TABLE ReimbursableAgreements 
(
    ReimbursableAgreementsId AUTOINCREMENT NOT NULL UNIQUE,
    RPIO TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    AgreementNumber TEXT(80) NULL DEFAULT NS,
    StartDate TEXT(80) NULL DEFAULT NS,
    EndDate TEXT(80) NULL DEFAULT NS,
    RcCode TEXT(80) NULL DEFAULT NS,
    OrgCode TEXT(80) NULL DEFAULT NS,
    RcName TEXT(80) NULL DEFAULT NS,
    SiteProjectCode TEXT(80) NULL DEFAULT NS,
    AccountCode TEXT(80) NULL DEFAULT NS,
    VendorCode TEXT(80) NULL DEFAULT NS,
    VendorName TEXT(80) NULL DEFAULT NS,
    Amount DECIMAL DEFAULT 0.0,
    OpenCommitments DECIMAL DEFAULT 0.0,
    Obligations DECIMAL DEFAULT 0.0,
    ULO DECIMAL DEFAULT 0.0,
    Available DECIMAL DEFAULT 0.0,
    CONSTRAINT ReimbursableAgreementsPrimaryKey
        PRIMARY KEY(ReimbursableAgreementsId)
);