CREATE TABLE IF NOT EXISTS BudgetObjectClasses 
(
	BudgetObjectClassesId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255) NOT NULL,
	Name	TEXT(255),
	CONSTRAINT PrimaryKeyBudgetObjectClasses PRIMARY KEY(BudgetObjectClassesId AUTOINCREMENT)
)v