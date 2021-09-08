CREATE TABLE FinanceObjectClasses 
(
	FinanceObjectClassId INTEGER NOT NULL UNIQUE,
	Code TEXT(255) NOT NULL,
	Name TEXT(255),
	CONSTRAINT PrimaryKeyFinanceObjectClasses PRIMARY KEY(FinanceObjectClassId AUTOINCREMENT)
)