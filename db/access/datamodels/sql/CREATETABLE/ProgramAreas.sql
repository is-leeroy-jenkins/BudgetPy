CREATE TABLE ProgramAreas 
(
    ProgramAreasId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NOT NULL,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT ProgramAreasPrimaryKey 
        PRIMARY KEY(ProgramAreasId)
);