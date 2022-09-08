CREATE TABLE Objectives
(
    ObjectivesId AUTOINCREMENT NOT NULL UNIQUE, 
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    Title TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyObjectives
        PRIMARY KEY(ObjectivesId)
);

