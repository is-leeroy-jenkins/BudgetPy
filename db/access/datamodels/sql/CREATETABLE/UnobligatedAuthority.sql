CREATE TABLE UnobligatedAuthority 
(
    UnobligatedAuthorityId AUTOINCREMENT NOT NULL UNIQUE,
    BudgetYear TEXT(80) NULL DEFAULT NS,
    AgencyTitle TEXT(80) NULL DEFAULT NS,
    BureauTitle TEXT(80) NULL DEFAULT NS,
    OmbAccount TEXT(80) NULL DEFAULT NS,
    AgencyCode TEXT(80) NULL DEFAULT NS,
    BureauCode TEXT(80) NULL DEFAULT NS,
    AccountCode TEXT(80) NULL DEFAULT NS,
    Transmit TEXT(80) NULL DEFAULT NS,
    AgencySequence TEXT(80) NULL DEFAULT NS,
    OmbAccountTitle TEXT(80) NULL DEFAULT NS,
    LineName TEXT(80) NULL DEFAULT NS,
    LineNumber TEXT(80) NULL DEFAULT NS,
    PriorYearAmount DECIMAL NULL DEFAULT 0.0,
    CurrentYearAmount DECIMAL NULL DEFAULT 0.0,
    BudgetYearAmount DECIMAL NULL DEFAULT 0.0,
    CONSTRAINT UnobligatedAuthorityPrimaryKey
        PRIMARY KEY(UnobligatedAuthorityId)
);