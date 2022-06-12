CREATE TABLE FinanceObjectClasses 
(
    FinanceObjectClassesId INTEGER NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyFinanceObjectClasses PRIMARY KEY(FinanceObjectClassesId)
);