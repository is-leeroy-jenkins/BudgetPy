CREATE TABLE CarryoverApportionments
(
	CarryoverApportionmentsId AUTOINCREMENT NOT NULL UNIQUE,
	BudgetAccount             TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccount           TEXT( 150 )   NULL DEFAULT NS,
	BFY                       TEXT( 150 )   NULL DEFAULT NS,
	EFY                       TEXT( 150 )   NULL DEFAULT NS,
	Group                     TEXT( 150 )   NULL DEFAULT NS,
	Description               TEXT( 150 )   NULL DEFAULT NS,
	LineName                  TEXT( 150 )   NULL DEFAULT NS,
	AuthorityType             TEXT( 150 )   NULL DEFAULT NS,
	Request                   DOUBLE        NULL DEFAULT 0.0,
	Balance                   DOUBLE        NULL DEFAULT 0.0,
	Deobligations             DOUBLE        NULL DEFAULT 0.0,
	Amount                    DOUBLE        NULL DEFAULT 0.0,
	LineNumber                TEXT( 150 )   NULL DEFAULT NS,
	LineSplit                 TEXT( 150 )   NULL DEFAULT NS,
	ApportionmentAccountCode  TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountCode       TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountName       TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountCode         TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountName         TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	CarryoverApportionmentsPrimaryKey
)
	PRIMARY KEY
(
	CarryoverApportionmentsId
)
	);
