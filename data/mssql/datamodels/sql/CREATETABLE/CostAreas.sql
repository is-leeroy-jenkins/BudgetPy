CREATE TABLE CostAreas
(
	CostAreasId INT           NOT NULL UNIQUE,
	Code        NVARCHAR(150) NULL DEFAULT ('NS'),
	Name        NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT CostAreasPrimaryKey PRIMARY KEY
		(
		  CostAreasId ASC
			)
);
