CREATE TABLE QueryDefinitions
(
	QueryDefinitionsId AUTOINCREMENT NOT NULL UNIQUE,
	Name               TEXT( 150 )   NULL DEFAULT NS,
	Type               TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	QueryDefinitionsPrimaryKey
)
	PRIMARY KEY
(
	QueryDefinitionsId
)
	);
