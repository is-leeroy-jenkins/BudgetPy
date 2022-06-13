CREATE TABLE IF NOT EXISTS AllowanceHolders 
(
	AllowanceHoldersId INTEGER NOT NULL UNIQUE,
	Code TEXT(255) NOT NULL,
	Name TEXT(255),
	CONSTRAINT PrimaryKeyAllowanceHolders PRIMARY KEY(AllowanceHoldersId AUTOINCREMENT)
);