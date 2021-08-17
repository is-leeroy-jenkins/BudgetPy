CREATE TABLE IF NOT EXISTS ReferenceTables
(
   ReferenceTableId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyReferenceTables PRIMARY KEY,
   TableName TEXT(255),
   Type TEXT(255)
);
