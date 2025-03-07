CREATE TABLE MonthlyOutlays
(
	MonthlyOutlaysId    AUTOINCREMENT NOT NULL UNIQUE,
	FiscalYear          TEXT( 150 )   NULL DEFAULT NS,
	LineNumber          TEXT( 150 )   NULL DEFAULT NS,
	LineTitle           TEXT( 150 )   NULL DEFAULT NS,
	TaxationCode        TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAgencyCode  TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountCode TEXT( 150 )   NULL DEFAULT NS,
	SubAccount          TEXT( 150 )   NULL DEFAULT NS,
	BFY                 TEXT( 150 )   NULL DEFAULT NS,
	EFY                 TEXT( 150 )   NULL DEFAULT NS,
	BudgetAgencyCode    TEXT( 150 )   NULL DEFAULT NS,
	BudgetBureauCode    TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountCode   TEXT( 150 )   NULL DEFAULT NS,
	AgencySequence      TEXT( 150 )   NULL DEFAULT NS,
	BureauSequence      TEXT( 150 )   NULL DEFAULT NS,
	AccountSequence     TEXT( 150 )   NULL DEFAULT NS,
	AgencyTitle         TEXT( 150 )   NULL DEFAULT NS,
	BureauTitle         TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountName   TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountName TEXT( 150 )   NULL DEFAULT NS,
	October             DOUBLE        NULL DEFAULT 0.0,
	November            DOUBLE        NULL DEFAULT 0.0,
	December            DOUBLE        NULL DEFAULT 0.0,
	January             DOUBLE        NULL DEFAULT 0.0,
	Feburary            DOUBLE        NULL DEFAULT 0.0,
	March               DOUBLE        NULL DEFAULT 0.0,
	April               DOUBLE        NULL DEFAULT 0.0,
	May                 DOUBLE        NULL DEFAULT 0.0,
	June                DOUBLE        NULL DEFAULT 0.0,
	July                DOUBLE        NULL DEFAULT 0.0,
	August              DOUBLE        NULL DEFAULT 0.0,
	September           DOUBLE        NULL DEFAULT 0.0, CONSTRAINT
(
	MonthlyOutlaysPrimaryKey
)
	PRIMARY KEY
(
	MonthlyOutlaysId
)
	);
