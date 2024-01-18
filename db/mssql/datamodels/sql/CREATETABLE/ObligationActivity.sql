CREATE TABLE ObligationActivity
(
	ObligationActivityId    INT           NOT NULL UNIQUE,
	BFY                     NVARCHAR(150) NULL DEFAULT ('NS'),
	EFY                     NVARCHAR(150) NULL DEFAULT ('NS'),
	FundCode                NVARCHAR(150) NULL DEFAULT ('NS'),
	FundName                NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountCode     NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode       NVARCHAR(150) NULL DEFAULT ('NS'),
	RpioCode                NVARCHAR(150) NULL DEFAULT ('NS'),
	RpioName                NVARCHAR(150) NULL DEFAULT ('NS'),
	AhCode                  NVARCHAR(150) NULL DEFAULT ('NS'),
	AhName                  NVARCHAR(150) NULL DEFAULT ('NS'),
	OrgCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	OrgName                 NVARCHAR(150) NULL DEFAULT ('NS'),
	AccountCode             NVARCHAR(150) NULL DEFAULT ('NS'),
	ProgramProjectName      NVARCHAR(150) NULL DEFAULT ('NS'),
	BocCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	BocName                 NVARCHAR(150) NULL DEFAULT ('NS'),
	FocCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	FocName                 NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentType            NVARCHAR(150) NULL DEFAULT ('NS'),
	DocumentNumber          NVARCHAR(150) NULL DEFAULT ('NS'),
	ProcessedDate           NVARCHAR(150) NULL DEFAULT ('NS'),
	OpenCommitments         FLOAT         NULL DEFAULT (0.0),
	Obligations             FLOAT         NULL DEFAULT (0.0),
	Used                    FLOAT         NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT         NULL DEFAULT (0.0),
	Outlays                 FLOAT         NULL DEFAULT (0.0),
	CONSTRAINT ObligationActivityPrimaryKey PRIMARY KEY
		(
		  ObligationActivityId ASC
			)
);