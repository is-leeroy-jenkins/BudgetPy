CREATE TABLE AgencyTransfers
(
	AgencyTransferId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyAgencyTransfers PRIMARY KEY,
	TransferId INTEGER NOT NULL UNIQUE,
	ReprogrammingNumber TEXT(255) NULL,
	ProcessedDate datetime NULL,
	RPIO TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	BFY TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	BocCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	Amount money NULL,
	FundName TEXT(255) NULL,
	ProgramProjectCode TEXT(255) NULL,
	ProgramProjectName TEXT(255) NULL,
	BocName TEXT(255) NULL,
	FromTo TEXT(255) NULL,
	SPIO TEXT(255) NULL,
	CONSTRAINT ForeignKeyAgencyTransfers
	FOREIGN KEY (TransferId) 
    REFERENCES Transfers
);
