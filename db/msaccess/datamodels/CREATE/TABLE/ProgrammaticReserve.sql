CREATE TABLE ProgrammaticReserve
(
	ProgrammaticReserveId INTEGER NOT NULL UNIQUE CONSTRAINT PK_ProgrammaticReserve PRIMARY KEY,
	PrcId INTEGER NOT NULL,
	BudgetLevel TEXT(255) NULL,
	RPIO TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	BFY TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	ActivityCode TEXT(255) NULL,
	BocCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	CurrentYear DOUBLE NULL,
	Reduction DOUBLE NULL,
	Ratio DOUBLE NULL,
	Budget DOUBLE NULL,
	PriorYear DOUBLE NULL,
	FundName TEXT(255) NULL,
	ProgramProjectCode TEXT(255) NULL,
	ProgramProjectName TEXT(255) NULL,
	BocName TEXT(255) NULL,
	NpmCode TEXT(255) NULL,
	NpmName TEXT(255) NULL,
	Division TEXT(255) NULL,
	DivisionName TEXT(255) NULL,
	Delta DOUBLE NULL,
	CONSTRAINT FK_ProgrammaticReserve
	FOREIGN KEY (PrcId)
	REFERENCES Allocations
);
