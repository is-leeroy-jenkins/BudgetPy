CREATE TABLE DivisionExecution
(
	DivisionExecutionId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyDivisionExecution PRIMARY KEY,
	BudgetLevel TEXT(255) NULL,
	RPIO TEXT(255) NULL,
	BFY TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	DivisionName TEXT(255) NULL,
	FundName TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	ActivityCode TEXT(255) NULL,
	ProgramProjectCode TEXT(255) NULL,
	ProgramProjectName TEXT(255) NULL,
	BocCode TEXT(255) NULL,
	BocName TEXT(255) NULL,
	SiteProjectCode TEXT(255) NULL,
	Amount DOUBLE NULL,
	OpenCommitments DOUBLE NULL,
	CommitmentRatio DOUBLE NULL,
	Obligations DOUBLE NULL,
	ObligationRatio DOUBLE NULL,
	Used DOUBLE NULL,
	Utilization DOUBLE NULL,
	Available DOUBLE NULL,
	Availability DOUBLE NULL
);


