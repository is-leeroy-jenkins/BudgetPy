CREATE TABLE IF NOT EXISTS AllowanceHolders
(
	AllowanceHoldersId INTEGER NOT NULL UNIQUE,
	Code TEXT(150) NULL DEFAULT NS,
	Name TEXT(150) NULL DEFAULT NS,
	CONSTRAINT AllowanceHoldersPrimaryKey)
		) PRIMARY KEY(AllowanceHoldersId)
);
