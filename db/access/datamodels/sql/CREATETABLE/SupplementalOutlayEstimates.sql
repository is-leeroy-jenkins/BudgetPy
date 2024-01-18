CREATE TABLE SupplementalOutlayEstimates
(
	SupplementalOutlayEstimatesId INT           NOT NULL UNIQUE,
	BFY                           NVARCHAR(150) NULL DEFAULT ('NS'),
	EFY                           NVARCHAR(150) NULL DEFAULT ('NS'),
	MainAccount                   NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode             NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName             NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountCode           NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountName           NVARCHAR(150) NULL DEFAULT ('NS'),
	Program                       NVARCHAR(150) NULL DEFAULT ('NS'),
	Authority                     FLOAT         NULL DEFAULT (0.0),
	FY22                          FLOAT         NULL DEFAULT (0.0),
	FY23                          FLOAT         NULL DEFAULT (0.0),
	FY24                          FLOAT         NULL DEFAULT (0.0),
	FY25                          FLOAT         NULL DEFAULT (0.0),
	FY26                          FLOAT         NULL DEFAULT (0.0),
	FY2731                        FLOAT         NULL DEFAULT (0.0),
	Supplemental                  NVARCHAR(150) NULL DEFAULT ('NS'),
	FundCode                      NVARCHAR(150) NULL DEFAULT ('NS'),
	FundName                      NVARCHAR(150) NULL DEFAULT ('NS'), CONSTRAINT
(
	SupplementalOutlayEstimatesPrimaryKey
)
	PRIMARY KEY
(
	SupplementalOutlayEstimatesId
)
	);