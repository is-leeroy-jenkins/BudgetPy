CREATE TABLE Accounts
(
    AccountsId INTEGER NOT NULL UNIQUE,
    Code TEXT(80),
    ProgramAreaCode TEXT(80),
    GoalCode TEXT(80),
    ObjectiveCode TEXT(80),
    NpmCode TEXT(80),
    NpmName TEXT(80),
    ProgramProjectCode TEXT(80),
    ProgramProjectName TEXT(80),
    ActivityCode TEXT(80),
    ActivityName TEXT(80),
    AgencyActivity TEXT(80),
    PRIMARY KEY(AccountsId)
);