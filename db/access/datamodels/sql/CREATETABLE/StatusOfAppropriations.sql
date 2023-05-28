CREATE TABLE StatusOfAppropriations 
(
    StatusOfAppropriationsId AUTOINCREMENT NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    FundCode TEXT(80) NULL DEFAULT NS,
    FundName TEXT(80) NULL DEFAULT NS,
    Availability TEXT(80) NULL DEFAULT NS,
    TransType TEXT(80) NULL DEFAULT NS,
    TreasurySymbol TEXT(80) NULL DEFAULT NS,
    OriginalAmount DOUBLE NULL DEFAULT 0.0,
    Authority DOUBLE NULL DEFAULT 0.0,
    Budgeted DOUBLE NULL DEFAULT 0.0,
    Posted DDOUBLE NULL DEFAULT 0.0,
    CarryoverOut DOUBLE NULL DEFAULT 0.0,
    CarryoverIn DOUBLE NULL DEFAULT 0.0,
    TransferIn DOUBLE NULL DEFAULT 0.0,
    TransferOut DOUBLE NULL DEFAULT 0.0,
    OpenCommitments DOUBLE NULL DEFAULT 0.0,
    Obligations DOUBLE NULL DEFAULT 0.0,
    UnliquidatedObligations DOUBLE NULL DEFAULT 0.0,
    Available DOUBLE NULL DEFAULT 0.0,
	TreasuryAccountCode TEXT(80) NULL DEFAULT NS,
	TreasuryAccountName TEXT(255) NULL DEFAULT NS,
	BudgetAccountCode TEXT(80) NULL DEFAULT NS,
	BudgetAccountName TEXT(255) NULL DEFAULT NS,
    CONSTRAINT StatusOfAppropriationsPrimaryKey
        PRIMARY KEY(StatusOfAppropriationsId)
);