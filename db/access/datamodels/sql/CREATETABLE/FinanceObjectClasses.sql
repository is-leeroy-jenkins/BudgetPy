CREATE TABLE FinanceObjectClasses 
(
    FinanceObjectClassesId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyFinanceObjectClasses PRIMARY KEY(FinanceObjectClassesId)
);