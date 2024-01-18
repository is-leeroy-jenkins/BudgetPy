CREATE TABLE QueryDefinitions
(
	QueryDefinitionsId INT           NOT NULL UNIQUE,
	Name               NVARCHAR(150) NULL DEFAULT ('NS'),
	Type               NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT QueryDefinitionsPrimaryKey PRIMARY KEY
		(
		  QueryDefinitionsId ASC
			)
);
