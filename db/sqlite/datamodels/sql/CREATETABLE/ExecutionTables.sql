CREATE TABLE ExecutionTables
(
	ExecutionTableId INTEGER NOT NULL UNIQUE CONSTRAINT PK_ExecutionTables PRIMARY KEY,
	TableName TEXT(255) NULL,
	TableType TEXT(50) NULL
);
