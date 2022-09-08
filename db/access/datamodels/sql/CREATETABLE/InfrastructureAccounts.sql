CREATE TABLE InfrastructureAccounts 
(
    InfrastructureAccountsId INTEGER,
    StrategicPlan TEXT DEFAULT NS,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    AccountCode TEXT(80) NULL DEFAULT NS,
    GoalCode TEXT(80) NULL DEFAULT NS,
    ObjectiveCode TEXT(80) NULL DEFAULT NS,
    NpmCode TEXT(80) NULL DEFAULT NS,
    NpmName TEXT(80) NULL DEFAULT NS,
    ProgramProjectCode TEXTTEXT(80) NULL DEFAULT NS,
    ProgramProjectName TEXT(80) NULL DEFAULT NS,
    ActivityCode TEXT(80) NULL DEFAULT NS,
    ActivityName TEXT(80) NULL DEFAULT NS,
    ProgramAreaCode TEXT(80) NULL DEFAULT NS,
    ProgramAreaName TEXT(80) NULL DEFAULT NS,
    ProgramName TEXT(80) NULL DEFAULT NS,
    ProgramDescription TEXT(80) DEFAULT NS
);