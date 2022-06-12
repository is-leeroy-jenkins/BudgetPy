CREATE TABLE Appropriations 
(
    AppropriationsId INTEGER NOT NULL UNIQUE,
    BFY TEXT(80) NOT NULL,
    Title TEXT(80) NULL DEFAULT NS,
    PublicLaw TEXT(80) NULL DEFAULT NS,
    EnactedDate DATETIME,
    CONSTRAINT PrimaryKeyAppropriations PRIMARY KEY(AppropriationsId)
);