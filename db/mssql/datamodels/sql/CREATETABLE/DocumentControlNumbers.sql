CREATE TABLE DocumentControlNumbers 
(
	DocumentControlNumberId	INT NOT NULL IDENTITY(1,1),
	RpioCode	NVARCHAR(80) NULL,
	RpioName	NVARCHAR(80) NULL,
	DocumentType	NVARCHAR(80) NULL,
	DocumentNumber	NVARCHAR(80) NULL,
	DocumentPrefix	NVARCHAR(80) NULL,
	DocumentControlNumber	NVARCHAR(80) NULL
);