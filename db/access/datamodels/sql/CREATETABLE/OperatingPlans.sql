CREATE TABLE OperatingPlans
(
	OperatingPlansId    AUTOINCREMENT NOT NULL UNIQUE,
	BFY                 TEXT( 150 )   NULL DEFAULT NS,
	EFY                 TEXT( 150 )   NULL DEFAULT NS,
	FundCode            TEXT( 150 )   NULL DEFAULT NS,
	FundName            TEXT( 150 )   NULL DEFAULT NS,
	RpioCode            TEXT( 150 )   NULL DEFAULT NS,
	RpioName            TEXT( 150 )   NULL DEFAULT NS,
	AhCode              TEXT( 150 )   NULL DEFAULT NS,
	OrgCode             TEXT( 150 )   NULL DEFAULT NS,
	AccountCode         TEXT( 150 )   NULL DEFAULT NS,
	BocCode             TEXT( 150 )   NULL DEFAULT NS,
	BocName             TEXT( 150 )   NULL DEFAULT NS,
	Amount              DOUBLE        NULL DEFAULT 0.0,
	NpmCode             TEXT( 150 )   NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 150 )   NULL DEFAULT NS,
	ProgramAreaCode     TEXT( 150 )   NULL DEFAULT NS,
	NpmName             TEXT( 150 )   NULL DEFAULT NS,
	AhName              TEXT( 150 )   NULL DEFAULT NS,
	OrgName             TEXT( 150 )   NULL DEFAULT NS,
	ProgramProjectName  TEXT( 150 )   NULL DEFAULT NS,
	ActivityCode        TEXT( 150 )   NULL DEFAULT NS,
	ActivityName        TEXT( 150 )   NULL DEFAULT NS,
	ProgramAreaName     TEXT( 150 )   NULL DEFAULT NS,
	GoalCode            TEXT( 150 )   NULL DEFAULT NS,
	GoalName            TEXT( 150 )   NULL DEFAULT NS,
	ObjectiveCode       TEXT( 150 )   NULL DEFAULT NS,
	ObjectiveName       TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountCode TEXT( 150 )   NULL DEFAULT NS,
	TreasuryAccountName TEXT( MAX )   NULL DEFAULT NS,
	BudgetAccountCode   TEXT( 150 )   NULL DEFAULT NS,
	BudgetAccountName   TEXT( MAX )   NULL DEFAULT NS,
	Version             TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	OperatingPlansPrimaryKey
)
	PRIMARY KEY
(
	OperatingPlansId
)
	);
