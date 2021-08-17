CREATE TABLE Distribution
(
    DistributionId INTEGER NOT NULL UNIQUE CONSTRAINT PK_Distribution PRIMARY KEY,
	PrcId INTEGER NOT NULL UNIQUE,
	BFY TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	FundName TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	ProgramProjectName TEXT(255) NULL,
	BocCode TEXT(255) NULL,
	BocName TEXT(255) NULL,
	BudgetLevel TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	AllocationRatio DOUBLE NULL,
	Amount DOUBLE NULL,
    CONSTRAINT FK_Distribution
    FOREIGN KEY (PrcId)
    REFERENCES Allocations
);