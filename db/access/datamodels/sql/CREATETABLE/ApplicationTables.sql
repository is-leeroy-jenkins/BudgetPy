CREATE TABLE ApplicationTables 
(
    ApplicationTablesId INTEGER NOT NULL UNIQUE,
    TableName TEXT(80) NULL DEFAULT NS,
    Model TEXT(80) NULL DEFAULT NS,
    CONSTRAINT ApplicationTablesPrimaryKey 
    PRIMARY KEY(ApplicationTablesId)
);