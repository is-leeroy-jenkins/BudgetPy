CREATE TABLE UnobligatedAuthority 
(
	UnobligatedAuthorityId	INT NOT NULL IDENTITY(1,1),
	BudgetYear	NVARCHAR(80) NULL,
	AgencyTitle	NVARCHAR(80) NULL,
	BureauTitle	NVARCHAR(80) NULL,
	OmbAccount	NVARCHAR(80) NULL,
	AgencyCode	NVARCHAR(80) NULL,
	BureauCode	NVARCHAR(80) NULL,
	AccountCode	NVARCHAR(80) NULL,
	Transmit	NVARCHAR(80) NULL,
	AgencySequence	NVARCHAR(80) NULL,
	OmbAccountTitle	NVARCHAR(80) NULL,
	LineName	NVARCHAR(80) NULL,
	LineNumber	NVARCHAR(80) NULL,
	PriorYearAmount	FLOAT NULL,
	CurrentYearAmount	FLOAT NULL,
	BudgetYearAmount	FLOAT NULL
);