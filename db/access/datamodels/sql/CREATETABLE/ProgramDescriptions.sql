CREATE TABLE ProgramDescriptions 
(
    ProgramDescriptionsId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    Title TEXT(80) NULL DEFAULT NS,
    Laws TEXT(MAX) NULL DEFAULT NS,
    Narrative TEXT(MAX) NULL DEFAULT NS,
    Definition TEXT(MAX) NULL DEFAULT NS,
    ProgramAreaCode TEXT(80) NULL DEFAULT NS,
    ProgramAreaName TEXT(80) NULL DEFAULT NS,
    CONSTRAINT ProgramDescriptionsPrimaryKey 
        PRIMARY KEY(ProgramDescriptionsId)
);