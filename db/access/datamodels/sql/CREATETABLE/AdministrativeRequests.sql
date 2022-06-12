CREATE TABLE AdministrativeRequests 
(
    AdministrativeRequestsId INTEGER NOT NULL UNIQUE,
    RequestId TEXT(80) NULL DEFAULT NS,
    ControlTeamAnalyst TEXT(80) NULL DEFAULT NS,
    RpioCode TEXT(80) NULL DEFAULT NS,
    DocumentTitle TEXT(80) NULL DEFAULT NS,
    Amount TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    Status TEXT(80) NULL DEFAULT NS,
    OriginalRequestDate TEXT(80) NULL DEFAULT NS,
    LastActivityDate TEXT(80) NULL DEFAULT NS,
    Duration INTEGER,
    BFS TEXT(80) NULL DEFAULT NS,
    Comments TEXT(80) NULL DEFAULT NS,
    RequestDocument TEXT(80) NULL DEFAULT NS,
    RequestType TEXT(80) NULL DEFAULT NS,
    TypeCode TEXT(80) NULL DEFAULT NS,
    Decision TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(AdministrativeRequestsId)
);

