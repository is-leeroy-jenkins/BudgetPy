CREATE TABLE Changes
(
     ChangesId AUTOINCREMENT NOT NULL UNIQUE,
     TableName TEXT(80) NULL DEFAULT NS,
     FieldName TEXT(80) NULL DEFAULT NS,
     ActionType TEXT(80) NULL DEFAULT NS,
     OldValue TEXT(80) NULL DEFAULT NS,
     NewValue TEXT(80) NULL DEFAULT NS,
     ChangeDate DATETIME NULL,
     Message TEXT(80) NULL DEFAULT NS
     CONSTRAINT ChangesPrimaryKey 
          PRIMARY KEY(ChangesId)
);