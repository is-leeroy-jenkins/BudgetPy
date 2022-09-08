CREATE TABLE BudgetObjectClasses 
(
    BudgetObjectClassesId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NOT NULL,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT BudgetObjectClassesPrimaryKey 
        PRIMARY KEY(BudgetObjectClassesId)
)v