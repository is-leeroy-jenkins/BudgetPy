CREATE TABLE TreasurySymbols
(
	TreasurySymbolsId                AUTOINCREMENT NOT NULL UNIQUE,
	ShortKey                         TEXT( 150 )   NULL DEFAULT NS,
	AllocationTransferAgency         TEXT( 150 )   NULL DEFAULT NS,
	AgencyIdentifier                 TEXT( 150 )   NULL DEFAULT NS,
	BeginningPeriodOfAvailability    TEXT( 150 )   NULL DEFAULT NS,
	EndingPeriodOfAvailability       TEXT( 150 )   NULL DEFAULT NS,
	AvailabilityType                 TEXT( 150 )   NULL DEFAULT NS,
	MainAccount                      TEXT( 150 )   NULL DEFAULT NS,
	SubAccount                       TEXT( 150 )   NULL DEFAULT NS,
	Lapsed                           TEXT( 150 )   NULL DEFAULT NS,
	UseCancelledYearSpendingAccounts TEXT( 150 )   NULL DEFAULT NS,
	AgencyTreasurySymbol             TEXT( 150 )   NULL DEFAULT NS,
	InUse                            TEXT( 150 )   NULL DEFAULT NS,
	PreventNewUse                    TEXT( 150 )   NULL DEFAULT NS,
	Status                           TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	TreasurySymbolsPrimaryKey
)
	PRIMARY KEY
(
	TreasurySymbolsId
)
	);
