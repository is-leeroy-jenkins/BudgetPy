CREATE TABLE "TreasurySymbols" 
(
	"TreasurySymbolsId"	INTEGER UNIQUE,
	"ShortKey"	TEXT(80) NULL DEFAULT NS,
	"AllocationTransferAgency"	TEXT(80) NULL DEFAULT NS,
	"AgencyIdentifier"	TEXT(80) NULL DEFAULT NS,
	"BeginningPeriodOfAvailability"	TEXT(80) NULL DEFAULT NS,
	"EndingPeriodOfAvailability"	TEXT(80) NULL DEFAULT NS,
	"AvailabilityType"	TEXT(80) NULL DEFAULT NS,
	"MainAccount"	TEXT(80) NULL DEFAULT NS,
	"SubAccount"	TEXT(80) NULL DEFAULT NS,
	"Lapsed"	TEXT(80) NULL DEFAULT NS,
	"UseCancelledYearSpendingAccounts"	TEXT(80) NULL DEFAULT NS,
	"AgencyTreasurySymbol"	TEXT(80) NULL DEFAULT NS,
	"InUse"	TEXT(80) NULL DEFAULT NS,
	"PreventNewUse"	TEXT(80) NULL DEFAULT NS,
	"Status"	TEXT(80) NULL DEFAULT NS,
	PRIMARY KEY("TreasurySymbolsId")
);