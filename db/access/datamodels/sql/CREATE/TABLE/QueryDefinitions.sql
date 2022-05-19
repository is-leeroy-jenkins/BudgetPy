CREATE TABLE QueryDefinitions
(
	QueryDefinitionId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyQueryDefinitions PRIMARY KEY,
	Name TEXT(255) NULL,
	Type TEXT(255) NULL
);

