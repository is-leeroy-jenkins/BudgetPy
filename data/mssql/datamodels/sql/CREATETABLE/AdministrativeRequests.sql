CREATE TABLE AdministrativeRequests
(
	AdministrativeRequestsId INT           NOT NULL UNIQUE,
	RequestId                FLOAT         NULL DEFAULT (0.0),
	Analyst                  NVARCHAR(150) NULL DEFAULT ('NS'),
	RpioCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentTitle            NVARCHAR(150) NULL DEFAULT ('NS'),
	Amount                   FLOAT         NULL DEFAULT (0.0),
	FundCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	BFY                      NVARCHAR(150) NULL DEFAULT ('NS'),
	Status                   NVARCHAR(150) NULL DEFAULT ('NS'),
	OriginalRequestDate      DATETIME      NULL,
	LastActivityDate         DATETIME      NULL,
	Duration                 FLOAT         NULL DEFAULT (0.0),
	BudgetFormulationSystem  NVARCHAR(150) NULL DEFAULT ('NS'),
	Comments                 NVARCHAR(MAX) NULL,
	RequestDocument          NVARCHAR(MAX) NULL,
	RequestType              NVARCHAR(150) NULL DEFAULT ('NS'),
	TypeCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	Decision                 NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT AdministrativeRequestsPrimaryKey PRIMARY KEY
		(
		  AdministrativeRequestsId ASC
			)
);
