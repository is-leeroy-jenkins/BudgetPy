CREATE TABLE RecoveryFundTransfers
(
	RecoveryFundTransferId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyRecoveryFundTransfers PRIMARY KEY,
	TransferId INTEGER NOT NULL UNIQUE,
	ReprogrammingNumber TEXT(255) NULL,
	ProcessedDate DATETIME NULL,
	RPIO TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	BFY TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	BocCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	Amount DOUBLE NULL,
	FundName TEXT(255) NULL,
	ProgramProjectName TEXT(255) NULL,
	BocName TEXT(255) NULL,
	NpmCode TEXT(255) NULL,
	NpmName TEXT(255) NULL,
	CONSTRAINT FK_RecoveryFundTransfers
	FOREIGN KEY (TransferId)
	REFERENCES Transfers
);
