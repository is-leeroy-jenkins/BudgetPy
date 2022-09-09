CREATE TABLE CongressionalControls 
(
    CongressionalControlsId INTEGER NOT NULL UNIQUE,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    ProgramAreaCode TEXT(80) NULL DEFAULT NS,
    ProgramAreaName TEXT(80) NULL DEFAULT NS,
    ProgramProjectCode TEXT(80) NULL DEFAULT NS,
    ProgramProjectName TEXT(80) NULL DEFAULT NS,
    SubProjectCode TEXT(80) NULL DEFAULT NS,
    SubProjectName TEXT(80) NULL DEFAULT NS,
    ReprogrammingRestriction TEXT(80) NULL DEFAULT NS,
    IncreaseRestriction TEXT(80) NULL DEFAULT NS,
    DecreaseRestriction TEXT(80) NULL DEFAULT NS,
    MemoRequirement TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(CongressionalControlsId)
);