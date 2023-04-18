CREATE TABLE ApplicationTables 
(
	ApplicationTablesId	INTEGER NOT NULL UNIQUE,
	TableName	TEXT(80) NULL DEFAULT 'NS',
	Title	TEXT(80) NULL DEFAULT 'NS',
	Model	TEXT(80) NULL DEFAULT 'NS',
	CONSTRAINT PrimaryKeyApplicationTables PRIMARY KEY(ApplicationTablesId)
);