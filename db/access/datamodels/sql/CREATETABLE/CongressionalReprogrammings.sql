CREATE TABLE CongressionalReprogrammings 
(
    CongressionalReprogrammingsId AUTOINCREMENT NOT NULL UNIQUE,
    ReprogrammingNumber TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    RpioCode TEXT(80) NULL DEFAULT NS,
    AhCode TEXT(80) NULL DEFAULT NS,
    AhName TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    AccountCode TEXT(80) NULL DEFAULT NS,
    ProgramProjectCode TEXT(80) NULL DEFAULT NS,
    ProgramProjectName TEXT(80) NULL DEFAULT NS,
    ProgramAreaCode TEXT(80) NULL DEFAULT NS,
    ProgramAreaName TEXT(80) NULL DEFAULT NS,
    OrgCode TEXT(80) NULL DEFAULT NS,
    OrgName TEXT(80) NULL DEFAULT NS,
    BocCode TEXT(80) NULL DEFAULT NS,
    BocName TEXT(80) NULL DEFAULT NS,
    FromTo TEXT(80) NULL DEFAULT NS,
    ActivityCode TEXT(80) NULL DEFAULT NS,
    Amount DOUBLE NULL DEFAULT 0.0,
    Description TEXT(MAX) NULL DEFAULT NS,
    ExtendedDescription TEXT(MAX) NULL DEFAULT NS,
    Cycle TEXT(80) NULL DEFAULT NS,
    CONSTAINT CongressionalReprogrammingsPrimaryKey
         PRIMARY KEY(CongressionalReprogrammingsId)
);