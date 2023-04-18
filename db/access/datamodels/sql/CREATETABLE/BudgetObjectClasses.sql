CREATE TABLE BudgetObjectClasses 
(
    BudgetObjectClassesId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyBudgetObjectClasses PRIMARY KEY(BudgetObjectClassesId)
);