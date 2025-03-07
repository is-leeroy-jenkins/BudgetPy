CREATE TABLE DocumentControlNumbers
(
	DocumentControlNumbersId INT           NOT NULL UNIQUE,
	RpioCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	RpioName                 NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentType             NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentNumber           NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentPrefix           NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentControlNumber    NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT DocumentControlNumbersPrimaryKey PRIMARY KEY
		(
		  DocumentControlNumbersId ASC
			)
);
