CREATE TABLE ApportionmentData
(
	ApportionmentDataId      AUTOINCREMENT NOT NULL UNIQUE,
	FiscalYear               TEXT( 150 )   NULL DEFAULT NS,
	BFY                      TEXT( 150 )   NULL DEFAULT NS,
	EFY                      TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountCode      TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountName      TEXT( 150 )   NULL DEFAULT NS,
	ApportionmentAccountCode TEXT( 150 )   NULL DEFAULT NS,
	ApportionmentAccountName TEXT( 150 )   NULL DEFAULT NS,
	AvailabilityType         TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountCode        TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountName        TEXT( 150 )   NULL DEFAULT NS,
	ApprovalDate             DATETIME      NULL,
	LineNumber               TEXT( 150 )   NULL DEFAULT NS,
	LineName                 TEXT( 150 )   NULL DEFAULT NS,
	Amount                   DOUBLE        NULL DEFAULT 0.0,
	FundCode                 TEXT( 150 )   NULL DEFAULT NS,
	FundName                 TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	ApportionmentDataPrimaryKey
)
	PRIMARY KEY
(
	ApportionmentDataId
)
	);
