CREATE TABLE Rescission
(
	RescissionId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyRescission PRIMARY KEY,
	PrcId INTEGER NULL,
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
	Allocation DOUBLE NULL,
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
	CONSTRAINT ForeignKeyRescission
	FOREIGN KEY (PrcId)
	REFERENCES Allocations
);

