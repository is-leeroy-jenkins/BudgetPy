CREATE TABLE TreasurySymbols 
(
	TreasurySymbolsId	INT NOT NULL IDENTITY(1,1),
	ShortKey	NVARCHAR(80) NULL,
	AllocationTransferAgency	NVARCHAR(80) NULL,
	AgencyIdentifier	NVARCHAR(80) NULL,
	BeginningPeriodOfAvailability	NVARCHAR(80) NULL,
	EndingPeriodOfAvailability	NVARCHAR(80) NULL,
	AvailabilityType	NVARCHAR(80) NULL,
	MainAccount	NVARCHAR(80) NULL,
	SubAccount	NVARCHAR(80) NULL,
	Lapsed	NVARCHAR(80) NULL,
	UseCancelledYearSpendingAccounts	NVARCHAR(80) NULL,
	AgencyTreasurySymbol	NVARCHAR(80) NULL,
	InUse	NVARCHAR(80) NULL,
	PreventNewUse	NVARCHAR(80) NULL,
	Status	NVARCHAR(80) NULL
);