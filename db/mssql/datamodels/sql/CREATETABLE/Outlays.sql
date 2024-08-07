CREATE TABLE Outlays
(
	CompassOutlaysId        INT           NOT NULL UNIQUE,
	BFY                     NVARCHAR(150) NULL DEFAULT ('NS'),
	EFY                     NVARCHAR(150) NULL DEFAULT ('NS'),
	FundCode                NVARCHAR(150) NULL DEFAULT ('NS'),
	FundName                NVARCHAR(150) NULL DEFAULT ('NS'),
	AppropriationCode       NVARCHAR(150) NULL DEFAULT ('NS'),
	AppropriationName       NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasurySymbol          NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountCode     NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountName     NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode       NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName       NVARCHAR(150) NULL DEFAULT ('NS'),
	ProgramAreaCode         NVARCHAR(150) NULL DEFAULT ('NS'),
	ProgramAreaName         NVARCHAR(150) NULL DEFAULT ('NS'),
	ProgramProjectCode      NVARCHAR(150) NULL DEFAULT ('NS'),
	ProgramProjectName      NVARCHAR(150) NULL DEFAULT ('NS'),
	BocCode                 NVARCHAR(150) NULL DEFAULT ('NS'),
	BocName                 NVARCHAR(150) NULL DEFAULT ('NS'),
	ProcessedDate           NVARCHAR(150) NULL DEFAULT ('NS'),
	LastActivityDate        NVARCHAR(150) NULL DEFAULT ('NS'),
	TotalObligations        FLOAT         NULL DEFAULT (0.0),
	UnliquidatedObligations FLOAT         NULL DEFAULT (0.0),
	ObligationsPaid         FLOAT         NULL DEFAULT (0.0),
	CONSTRAINT CompassOutlaysPrimaryKey PRIMARY KEY
		(
		  CompassOutlaysId ASC
			)
);
