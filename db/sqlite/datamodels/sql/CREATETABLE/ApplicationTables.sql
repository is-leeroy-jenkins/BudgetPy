CREATE TABLE IF NOT EXISTS ApplicationTables
(
	ApplicationTablesId INTEGER NOT NULL UNIQUE,
	TableName TEXT(150) NULL DEFAULT NS,
	Model TEXT(150) NULL DEFAULT NS,
	Title TEXT(150) NULL DEFAULT NS,
	CONSTRAINT ApplicationTablesPrimaryKey 
		PRIMARY KEY(ApplicationTablesId)
);
