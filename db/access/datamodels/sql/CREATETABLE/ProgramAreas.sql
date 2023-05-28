CREATE TABLE ProgramAreas 
(
    ProgramAreasId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyProgramAreas 
        PRIMARY KEY(ProgramAreasId)
);