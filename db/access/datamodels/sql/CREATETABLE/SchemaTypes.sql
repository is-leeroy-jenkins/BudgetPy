CREATE TABLE SchemaTypes 
(
    SchemaTypesId AUTOINCREMENT NOT NULL UNIQUE,
    TypeName TEXT(80) NULL DEFAULT NS,
    Database TEXT(80) NULL DEFAULT NS,
    CONSTRAINT SchemaTypePrimaryKey
        PRIMARY KEY(SchemaTypesId)
);