CREATE TABLE IF NOT EXISTS BudgetObjectClasses 
(
	BudgetObjectClassesId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(80) NOT NULL,
	Name	TEXT(80) NOT NULL,
	CONSTRAINT PrimaryKeyBudgetObjectClasses 
		PRIMARY KEY(BudgetObjectClassesId AUTOINCREMENT)
);