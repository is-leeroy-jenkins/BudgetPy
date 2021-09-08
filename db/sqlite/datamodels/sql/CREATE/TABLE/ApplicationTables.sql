CREATE TABLE ApplicationTables
(
	ApplicationTableId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyApplicationTables PRIMARY KEY,
	TableName TEXT NULL,
	Model TEXT NULL
);

