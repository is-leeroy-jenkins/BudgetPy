CREATE TABLE IF NOT EXISTS Reprogrammings
(
	ReprogrammingsId INTEGER NOT NULL UNIQUE,
	TransfersId INTEGER NOT NULL UNIQUE,
	ReprogrammingNumber TEXT(80) DEFAULT 'NS',
	ProcessedDate DATETIME NULL,
	RPIO TEXT(80) DEFAULT 'NS',
	AhCode TEXT(80) DEFAULT 'NS',
	BFY TEXT(80) DEFAULT 'NS',
	FundCode TEXT(80) DEFAULT 'NS',
	OrgCode TEXT(80) DEFAULT 'NS',
	AccountCode TEXT(80) DEFAULT 'NS',
	FromTo TEXT(80) DEFAULT 'NS',
	BocCode TEXT(80) DEFAULT 'NS',
	RcCode TEXT(80) DEFAULT 'NS',
	Amount REAL DEFAULT 0.0,
	FundName TEXT(80) DEFAULT 'NS',
	ProgramProjectCode TEXT(80) DEFAULT 'NS',
	ProgramProjectName TEXT(80) DEFAULT 'NS',
	ProgramAreaCode TEXT(80) DEFAULT 'NS',
	ProgramAreaName TEXT(80) DEFAULT 'NS',
	BocName TEXT(80) DEFAULT 'NS',
	DocPrefix TEXT(80) DEFAULT 'NS', 
	CONSTRAINT PrimaryKeyReprogrammings 
	PRIMARY KEY(ReprogrammingsId AUTOINCREMENT),
	CONSTRAINT ReprogrammingsForeignKey 
	FOREIGN KEY("TransfersId") 
	REFERENCES "Transfers"("TransfersId")
);