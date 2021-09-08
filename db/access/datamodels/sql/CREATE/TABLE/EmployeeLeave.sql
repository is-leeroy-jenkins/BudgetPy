CREATE TABLE DivisionRescissionAuthority
(
	DivisionAuthorityId INTEGER NOT NULL UNIQUE CONSTRAINT PK_DivisionRescissionAuthority PRIMARY KEY,
    RescissionId INTEGER NOT NULL UNIQUE,
	PrcId INTEGER NOT NULL UNIQUE,
	RPIO TEXT(255) NULL,
	BudgetLevel TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	BFY TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	ActivityCode TEXT(255) NULL,
	BocCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	Reduction DOUBLE NULL,
	Amount DOUBLE NULL,
	FundName TEXT(255) NULL,
	BocName TEXT(255) NULL,
	Division TEXT(255) NULL,
	DivisionName TEXT(255) NULL,
	ProgramProjectCode TEXT(255) NULL,
	ProgramProjectName TEXT(255) NULL,
	NpmCode TEXT(255) NULL,
	NpmName TEXT(255) NULL,
	GoalCode TEXT(255) NULL,
	GoalName TEXT(255) NULL,
	ObjectiveCode TEXT(255) NULL,
	ObjectiveName TEXT(255) NULL,
	AllocationRatio DOUBLE NULL,
	ChangeDate DATETIME NULL,
    CONSTRAINT FK_DivisionRescission
    FOREIGN KEY (RescissionId)
    REFERENCES Rescission,
    CONSTRAINT FK_DivisionAllocations
    FOREIGN KEY (PrcId)
    REFERENCES Allocations
);
