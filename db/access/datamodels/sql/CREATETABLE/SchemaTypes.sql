CREATE TABLE SchemaTypes
(
	SchemaTypesId AUTOINCREMENT NOT NULL UNIQUE,
	TypeName      TEXT( 150 )   NULL DEFAULT NS,
	Database      TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	SchemaTypesPrimaryKey
)
	PRIMARY KEY
(
	SchemaTypesId
)
	);
