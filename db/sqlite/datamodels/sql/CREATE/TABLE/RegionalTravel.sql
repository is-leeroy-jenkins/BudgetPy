CREATE TABLE RegionalTravel
(
	RegionalTravelId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyRegionalTravel PRIMARY KEY,
	PrcId INTEGER NOT NULL UNIQUE,
	BudgetLevel TEXT(255) NOT NULL,
	RPIO TEXT(255) NOT NULL,
	BFY TEXT(255) NOT NULL,
	FundCode TEXT(255) NOT NULL,
	AhCode TEXT(255) NOT NULL,
	OrgCode TEXT(255) NOT NULL,
	RcCode TEXT(255) NOT NULL,
	AccountCode TEXT(255) NULL,
	BocCode TEXT(255) NOT NULL,
	Amount DOUBLE NULL,
	FundName TEXT(255) NULL,
	BocName TEXT(255) NULL,
	Division TEXT(255) NULL,
	DivisionName TEXT(255) NULL,
	ActivityCode TEXT(255) NULL,
	NpmCode TEXT(255) NULL,
	NpmName TEXT(255) NULL,
	ProgramProjectCode TEXT(255) NOT NULL,
	ProgramProjectName TEXT(255) NULL,
	ProgramAreaCode TEXT(255) NULL,
	ProgramAreaName TEXT(255) NULL,
	GoalCode TEXT(255) NULL,
	GoalName TEXT(255) NULL,
	ObjectiveCode TEXT(255) NULL,
	ObjectiveName TEXT(255) NULL,
	AllocationRatio DOUBLE NULL,
	ChangeDate DATETIME NULL,
	CONSTRAINT ForeignKeyRegionalTravel
	FOREIGN KEY (PrcId)
	REFERENCES Allocations
);

