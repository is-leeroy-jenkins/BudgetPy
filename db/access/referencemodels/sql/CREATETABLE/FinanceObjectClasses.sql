CREATE TABLE IF NOT EXISTS FinanceObjectClasses 
(
	FinanceObjectClassesId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255) NOT NULL,
	Name	TEXT(255),
	CONSTRAINT PrimaryKeyFinanceObjectClasses PRIMARY KEY(FinanceObjectClassesId AUTOINCREMENT)
);