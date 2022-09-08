CREATE TABLE ExecutionTables
(
    ExecutionTablesId AUTOINCREMENT NOT NULL UNIQUE,
    TableName TEXT(80) NULL DEFAULT NS,
    TableType TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyExecutionTables 
        PRIMARY KEY(ExecutionTablesId)
);
