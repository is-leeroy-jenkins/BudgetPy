CREATE TABLE PublicLaws
(
	PublicLawsId INT           NOT NULL UNIQUE,
	LawNumber    NVARCHAR(150) NULL DEFAULT ('NS'),
	BillTitle    NVARCHAR(150) NULL DEFAULT ('NS'),
	EnactedDate  DATETIME      NULL,
	Congress     NVARCHAR(150) NULL DEFAULT ('NS'),
	BFY          NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT PublicLawsPrimaryKey PRIMARY KEY
		(
		  PublicLawsId ASC
			)
);
