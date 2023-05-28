CREATE TABLE ApportionmentData
(
	ApportionmentDataId AUTOINCREMENT NOT NULL UNIQUE,
	FiscalYear TEXT(80) NULL DEFAULT NS,
	BFY TEXT(80) NULL DEFAULT NS,
	EFY TEXT(80) NULL DEFAULT NS,
	TreasuryAccountCode TEXT(80) NULL DEFAULT NS,
	TreasuryAccountName TEXT(255) NULL DEFAULT NS,
	ApportionmentAccountCode TEXT(80) NULL DEFAULT NS,
	ApportionmentAccountName TEXT(80) NULL DEFAULT NS,
	AvailabilityType TEXT(80) NULL DEFAULT NS,
	BudgetAccountCode TEXT(80) NULL DEFAULT NS,
	BudgetAccountName TEXT(255) NULL DEFAULT NS,
	ApprovalDate DATETIME NULL,
	LineNumber TEXT(80) NULL DEFAULT NS,
	LineName TEXT(80) NULL DEFAULT NS,
	Amount DOUBLE NULL DEFAULT 0.0,
    CONSTRAINT ApportionmentDataPrimaryKey
        PRIMARY KEY(ApportionmentDataId)
);