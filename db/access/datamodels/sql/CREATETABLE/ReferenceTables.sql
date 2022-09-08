CREATE TABLE ReferenceTables
(
   ReferenceTablesId AUTOINCREMENT NOT NULL UNIQUE,
   TableName TEXT(80) NULL DEFAULT NS
   Type TEXT(80) NULL DEFAULT NS 
   CONSTRAINT ReferenceTablesPrimaryKey
      PRIMARY KEY (ReferenceTablesId)
);
