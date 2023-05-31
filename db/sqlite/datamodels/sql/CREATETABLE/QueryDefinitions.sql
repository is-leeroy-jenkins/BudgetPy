CREATE TABLE QueryDefinitions
(
	QueryDefinitionsId INTEGER NOT NULL UNIQUE,
	Name TEXT(80) NULL DEFAULT NS,
	Type TEXT(80) NULL DEFAULT NS,
	CONSTRAINT QueryDefinitionsPrimaryKey 
	PRIMARY KEY (QueryDefinitionsId AUTOINCREMENT)
);

