BEGIN TRANSACTION;
CREATE TABLE Allocations
(
	AllocationsId      AUTOINCREMENT NOT NULL UNIQUE,
	StatusOfFundsId    INTEGER       NOT NULL,
	BudgetLevel        TEXT( 80 )    NULL DEFAULT NS,
	RpioCode           TEXT( 80 )    NULL DEFAULT NS,
	BFY                TEXT( 80 )    NULL DEFAULT NS,
	EFY                TEXT( 80 )    NULL DEFAULT NS,
	AhCode             TEXT( 80 )    NULL DEFAULT NS,
	FundCode           TEXT( 80 )    NULL DEFAULT NS,
	OrgCode            TEXT( 80 )    NULL DEFAULT NS,
	AccountCode        TEXT( 80 )    NULL DEFAULT NS,
	BocCode            TEXT( 80 )    NULL DEFAULT NS,
	RcCode             TEXT( 80 )    NULL DEFAULT NS,
	Amount             DECIMAL       NULL DEFAULT 0.0,
	RpioName           TEXT( 80 )    NULL DEFAULT NS,
	FundName           TEXT( 80 )    NULL DEFAULT NS,
	AhName             TEXT( 80 )    NULL DEFAULT NS,
	BocName            TEXT( 80 )    NULL DEFAULT NS,
	RcName             TEXT( 80 )    NULL DEFAULT NS,
	OrgName            TEXT( 80 )    NULL DEFAULT NS,
	NpmName            TEXT( 80 )    NULL DEFAULT NS,
	NpmCode            TEXT( 80 )    NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 )    NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 )    NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 )    NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 )    NULL DEFAULT NS,
	CONSTRAINT AllocationsPrimaryKey
		PRIMARY KEY ( AllocationsId ),
	CONSTRAINT StatusOfFundsForeignKey
		FOREIGN KEY ( StatusOfFundsId ) REFERENCES StatusOfFunds( StatusOfFundsId )
);

CREATE TABLE ApplicationTables
(
	ApplicationTablesId AUTOINCREMENT NOT NULL UNIQUE,
	TableName           TEXT( 80 )    NULL DEFAULT NS,
	Model               TEXT( 80 )    NULL DEFAULT NS,
	CONSTRAINT ApplicationTablesPrimaryKey
		PRIMARY KEY ( ApplicationTablesId )
);

CREATE TABLE Deobligations
(
	DeobligationsId    INTEGER    NOT NULL UNIQUE,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	DocumentNumber     TEXT( 80 ) NULL DEFAULT NS,
	CalendarYear       TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate      DATETIME   NULL,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyDeobligations PRIMARY KEY ( DeobligationId )
);

CREATE TABLE RegionalTransfers
(
	RegionalTransfersId INTEGER    NOT NULL UNIQUE,
	TransfersId         INTEGER    NOT NULL UNIQUE,
	ReprogrammingNumber TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate       DATETIME,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	FromTo              TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	DocPrefix           TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT RegionalTransfersForeignKey FOREIGN KEY ( TransferId ) REFERENCES Transfers,
	CONSTRAINT RegionalTransfersPrimaryKey PRIMARY KEY ( RegionalTransferId )
);

CREATE TABLE Changes
(
	ChangesId  INTEGER    NOT NULL UNIQUE,
	TableName  TEXT( 80 ) NULL DEFAULT NS,
	FieldName  TEXT( 80 ) NULL DEFAULT NS,
	ActionType TEXT( 80 ) NULL DEFAULT NS,
	OldValue   TEXT( 80 ) NULL DEFAULT NS,
	NewValue   TEXT( 80 ) NULL DEFAULT NS,
	ChangeDate DATETIME,
	Message    TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyChanges PRIMARY KEY ( ChangeId )
);

CREATE TABLE BackUpAllocations
(
	BackupAllocationId INTEGER    NOT NULL UNIQUE,
	PrcId              INTEGER    NOT NULL UNIQUE,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	AllocationRatio    INTEGER,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	Division           TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode       TEXT( 80 ) NULL DEFAULT NS,
	NpmName            TEXT( 80 ) NULL DEFAULT NS,
	NpmCode            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 ) NULL DEFAULT NS,
	GoalCode           TEXT( 80 ) NULL DEFAULT NS,
	GoalName           TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode      TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName      TEXT( 80 ) NULL DEFAULT NS,
	ChangeDate         DATETIME,
	CONSTRAINT ForeignKeyBackUpAllocations FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyBackUpAllocations PRIMARY KEY ( BackupAllocationId )
);

CREATE TABLE Distribution
(
	DistributionId     INTEGER    NOT NULL UNIQUE,
	PrcId              INTEGER    NOT NULL UNIQUE,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio    DECIMAL    NULL DEFAULT 0.0,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT ForeignKeyDistribution FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyDistribution PRIMARY KEY ( DistributionId )
);

CREATE TABLE DivisionAuthority
(
	DivisionAuthorityId INTEGER    NOT NULL UNIQUE,
	PrcId               INTEGER    NOT NULL UNIQUE,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	Reduction           DECIMAL    NULL DEFAULT 0.0,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	Division            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	NpmCode             TEXT( 80 ) NULL DEFAULT NS,
	NpmName             TEXT( 80 ) NULL DEFAULT NS,
	GoalCode            TEXT( 80 ) NULL DEFAULT NS,
	GoalName            TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode       TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName       TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio     DECIMAL    NULL DEFAULT 0.0,
	ChangeDate          DATETIME,
	CONSTRAINT ForeignKeyDivisionAuthority FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyDivisionAuthority PRIMARY KEY ( DivisionAuthorityId )
);

CREATE TABLE DivisionExecution
(
	DivisionExecutionId INTEGER    NOT NULL UNIQUE,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	SiteProjectCode     TEXT( 80 ) NULL DEFAULT NS,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	OpenCommitments     DECIMAL    NULL DEFAULT 0.0,
	CommitmentRatio     DECIMAL    NULL DEFAULT 0.0,
	Obligations         DECIMAL    NULL DEFAULT 0.0,
	ObligationRatio     DECIMAL    NULL DEFAULT 0.0,
	Used                DECIMAL    NULL DEFAULT 0.0,
	Utilization         DECIMAL    NULL DEFAULT 0.0,
	Available           DECIMAL    NULL DEFAULT 0.0,
	Availability        DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyDivisionExecution PRIMARY KEY ( DivisionExecutionId )
);

CREATE TABLE DivisionRescissionAuthority
(
	DivisionAuthorityId INTEGER    NOT NULL UNIQUE,
	RescissionId        INTEGER    NOT NULL UNIQUE,
	PrcId               INTEGER    NOT NULL UNIQUE,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	Reduction           DECIMAL    NULL DEFAULT 0.0,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	Division            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	NpmCode             TEXT( 80 ) NULL DEFAULT NS,
	NpmName             TEXT( 80 ) NULL DEFAULT NS,
	GoalCode            TEXT( 80 ) NULL DEFAULT NS,
	GoalName            TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode       TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName       TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio     DECIMAL    NULL DEFAULT 0.0,
	ChangeDate          DATETIME,
	CONSTRAINT ForeignKeyDivisionRescission FOREIGN KEY ( RescissionId ) REFERENCES Rescission,
	CONSTRAINT ForeignKeyDivisionAllocations FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyDivisionRescissionAuthority PRIMARY KEY ( DivisionAuthorityId )
);

CREATE TABLE ExecutionTables
(
	ExecutionTableId INTEGER    NOT NULL UNIQUE,
	TableName        TEXT( 80 ) NULL DEFAULT NS,
	TableType        TEXT( 50 ),
	CONSTRAINT PrimaryKeyExecutionTables PRIMARY KEY ( ExecutionTableId )
);

CREATE TABLE QueryDefinitions
(
	QueryDefinitionId INTEGER    NOT NULL UNIQUE,
	Name              TEXT( 80 ) NULL DEFAULT NS,
	Type              TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyQueryDefinitions PRIMARY KEY ( QueryDefinitionId )
);

CREATE TABLE RecoveryFundTransfers
(
	RecoveryFundTransferId INTEGER    NOT NULL UNIQUE,
	TransferId             INTEGER    NOT NULL UNIQUE,
	ReprogrammingNumber    TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate          DATETIME,
	RPIO                   TEXT( 80 ) NULL DEFAULT NS,
	AhCode                 TEXT( 80 ) NULL DEFAULT NS,
	BFY                    TEXT( 80 ) NULL DEFAULT NS,
	FundCode               TEXT( 80 ) NULL DEFAULT NS,
	AccountCode            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode                TEXT( 80 ) NULL DEFAULT NS,
	BocCode                TEXT( 80 ) NULL DEFAULT NS,
	RcCode                 TEXT( 80 ) NULL DEFAULT NS,
	Amount                 DECIMAL    NULL DEFAULT 0.0,
	FundName               TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName     TEXT( 80 ) NULL DEFAULT NS,
	BocName                TEXT( 80 ) NULL DEFAULT NS,
	NpmCode                TEXT( 80 ) NULL DEFAULT NS,
	NpmName                TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT ForeignKeyRecoveryFundTransfers FOREIGN KEY ( TransferId ) REFERENCES Transfers,
	CONSTRAINT PrimaryKeyRecoveryFundTransfers PRIMARY KEY ( RecoveryFundTransferId )
);

CREATE TABLE RegionalAuthority
(
	RegionalAuthorityId INTEGER    NOT NULL UNIQUE,
	RescissionId        INTEGER    NOT NULL UNIQUE,
	PrcId               INTEGER    NOT NULL UNIQUE,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	Reduction           DECIMAL    NULL DEFAULT 0.0,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	Division            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	NpmCode             TEXT( 80 ) NULL DEFAULT NS,
	NpmName             TEXT( 80 ) NULL DEFAULT NS,
	GoalCode            TEXT( 80 ) NULL DEFAULT NS,
	GoalName            TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode       TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName       TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio     DECIMAL    NULL DEFAULT 0.0,
	ChangeDate          DATETIME,
	CONSTRAINT ForeignKeyRegionalAuthorityAllocations FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT ForeignKeyRegionalAuthorityRescissions FOREIGN KEY ( RescissionId ) REFERENCES Rescission,
	CONSTRAINT PrimaryKeyRegionalAuthority PRIMARY KEY ( RegionalAuthorityId )
);

CREATE TABLE Rescission
(
	RescissionId       INTEGER    NOT NULL UNIQUE,
	PrcId              INTEGER,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode       TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	Allocation         DECIMAL    NULL DEFAULT 0.0,
	Reduction          DECIMAL    NULL DEFAULT 0.0,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	Division           TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	NpmCode            TEXT( 80 ) NULL DEFAULT NS,
	NpmName            TEXT( 80 ) NULL DEFAULT NS,
	GoalCode           TEXT( 80 ) NULL DEFAULT NS,
	GoalName           TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode      TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName      TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT ForeignKeyRescission FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyRescission PRIMARY KEY ( RescissionId )
);

CREATE TABLE StatusOfFunds
(
	StatusOfFundsId      INTEGER    NOT NULL UNIQUE,
	BudgetLevel          TEXT( 80 ) NULL DEFAULT NS,
	BFY                  TEXT( 80 ) NULL DEFAULT NS,
	AhCode               TEXT( 80 ) NULL DEFAULT NS,
	AhName               TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName      TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode   TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName   TEXT( 80 ) NULL DEFAULT NS,
	AccountCode          TEXT( 80 ) NULL DEFAULT NS,
	LowerName            TEXT( 80 ) NULL DEFAULT NS,
	RcCode               TEXT( 80 ) NULL DEFAULT NS,
	RcName               TEXT( 80 ) NULL DEFAULT NS,
	DivisionName         TEXT( 80 ) NULL DEFAULT NS,
	OrgCode              TEXT( 80 ) NULL DEFAULT NS,
	OrgName              TEXT( 80 ) NULL DEFAULT NS,
	BocCode              TEXT( 80 ) NULL DEFAULT NS,
	BocName              TEXT( 80 ) NULL DEFAULT NS,
	FundCode             TEXT( 80 ) NULL DEFAULT NS,
	FundName             TEXT( 80 ) NULL DEFAULT NS,
	Amount               DECIMAL    NULL DEFAULT 0.0,
	OpenCommitments      DECIMAL    NULL DEFAULT 0.0,
	ULO                  DECIMAL    NULL DEFAULT 0.0,
	TotalExpenseAccruals DECIMAL    NULL DEFAULT 0.0,
	Expenditures         DECIMAL    NULL DEFAULT 0.0,
	Obligations          DECIMAL    NULL DEFAULT 0.0,
	Used                 DECIMAL    NULL DEFAULT 0.0,
	Available            DECIMAL    NULL DEFAULT 0.0,
	NpmCode              TEXT( 80 ) NULL DEFAULT NS,
	NpmName              TEXT( 80 ) NULL DEFAULT NS,
	NpmTitle             TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode      TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyStatusOfFunds PRIMARY KEY ( StatusOfFundsId )
);

CREATE TABLE Supplemental
(
	SupplementalId INTEGER    NOT NULL UNIQUE,
	Type           TEXT( 80 ) NULL DEFAULT NS,
	RcCode         TEXT( 80 ) NULL DEFAULT NS,
	FundCode       TEXT( 80 ) NULL DEFAULT NS,
	BFY            TEXT( 80 ) NULL DEFAULT NS,
	BocCode        TEXT( 80 ) NULL DEFAULT NS,
	BocName        TEXT( 80 ) NULL DEFAULT NS,
	Amount         DECIMAL    NULL DEFAULT 0.0,
	TimeOff        DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeySupplemental PRIMARY KEY ( SupplementalId )
);

CREATE TABLE TravelObligations
(
	TravelObligationId INTEGER    NOT NULL UNIQUE,
	RpioCode           TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	AhName             TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	OrgName            TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	RcName             TEXT( 80 ) NULL DEFAULT NS,
	FocCode            TEXT( 80 ) NULL DEFAULT NS,
	FocName            TEXT( 80 ) NULL DEFAULT NS,
	FirstName          TEXT( 80 ) NULL DEFAULT NS,
	LastName           TEXT( 80 ) NULL DEFAULT NS,
	DepartureDate      DATETIME,
	ReturnDate         DATETIME,
	DocumentType       TEXT( 80 ) NULL DEFAULT NS,
	DCN                TEXT( 80 ) NULL DEFAULT NS,
	Obligations        DECIMAL    NULL DEFAULT 0.0,
	ULO                DECIMAL    NULL DEFAULT 0.0,
	Expenditures       DECIMAL    NULL DEFAULT 0.0,
	NpmCode            TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyTravelObligations PRIMARY KEY ( TravelObligationId )
);

CREATE TABLE ProgrammaticReservePriorYearUtilization
(
	ProgrammaticReservePriorYearUtilizationId INTEGER,
	OrgCode                                   INTEGER,
	BFY                                       INTEGER,
	RcCode                                    TEXT( 80 ) NULL DEFAULT NS,
	DivisionName                              TEXT( 80 ) NULL DEFAULT NS,
	FundCode                                  TEXT( 80 ) NULL DEFAULT NS,
	FundName                                  TEXT( 80 ) NULL DEFAULT NS,
	AccountCode                               TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName                        TEXT( 80 ) NULL DEFAULT NS,
	BocCode                                   INTEGER,
	BocName                                   TEXT( 80 ) NULL DEFAULT NS,
	CurrentYear                               INTEGER,
	Reduction                                 INTEGER,
	Budget                                    INTEGER,
	PriorYear                                 INTEGER,
	OpenCommitments                           INTEGER,
	ULO                                       INTEGER
);

CREATE TABLE ReimbursableFunds
(
	ReimbursableFundId    INTEGER,
	RPIO                  INTEGER,
	BFY                   INTEGER,
	FundCode              TEXT( 80 ) NULL DEFAULT NS,
	AccountCode           TEXT( 80 ) NULL DEFAULT NS,
	RcCode                TEXT( 80 ) NULL DEFAULT NS,
	DivisionName          TEXT( 80 ) NULL DEFAULT NS,
	BocCode               INTEGER,
	DocumentControlNumber TEXT( 80 ) NULL DEFAULT NS,
	AgreeementNumber      TEXT( 80 ) NULL DEFAULT NS,
	Amount                FLOAT      NULL DEFAULT 0,
	OpenCommitments       INTEGER,
	Obligations           FLOAT      NULL DEFAULT 0,
	ULO                   INTEGER,
	Available             REAL
);

CREATE TABLE DocumentControlNumbers
(
	DocumentControlNumberId INTEGER    NOT NULL UNIQUE,
	RcCode                  TEXT( 80 ) NULL DEFAULT NS,
	DocumentControlNumber   TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( DocumentControlNumberId AUTOINCREMENT )
);

CREATE TABLE DivisionTravel
(
	PrcId               INTEGER    NOT NULL UNIQUE,
	DivisionAuthorityId INTEGER    NOT NULL UNIQUE,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	Division            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode        TEXT( 80 ) NULL DEFAULT NS,
	NpmName             TEXT( 80 ) NULL DEFAULT NS,
	NpmCode             TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode     TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName     TEXT( 80 ) NULL DEFAULT NS,
	GoalCode            TEXT( 80 ) NULL DEFAULT NS,
	GoalName            TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode       TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName       TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio     DECIMAL    NULL DEFAULT 0.0,
	ChangeDate          DATETIME,
	PRIMARY KEY ( PrcId AUTOINCREMENT )
);

CREATE TABLE ExternalUpdates
(
	ExternalUpdateId   INTEGER    NOT NULL UNIQUE,
	ExtId              INTEGER    NOT NULL UNIQUE,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode       TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	Amount             FLOAT,
	PRIMARY KEY ( ExternalUpdateId AUTOINCREMENT )
);

CREATE TABLE ProgrammaticReserve
(
	ProgrammaticReserveId INTEGER    NOT NULL UNIQUE,
	PrcId                 INTEGER    NOT NULL UNIQUE,
	BudgetLevel           TEXT( 80 ) NULL DEFAULT NS,
	RPIO                  TEXT( 80 ) NULL DEFAULT NS,
	AhCode                TEXT( 80 ) NULL DEFAULT NS,
	BFY                   TEXT( 80 ) NULL DEFAULT NS,
	FundCode              TEXT( 80 ) NULL DEFAULT NS,
	OrgCode               TEXT( 80 ) NULL DEFAULT NS,
	AccountCode           TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode          TEXT( 80 ) NULL DEFAULT NS,
	BocCode               TEXT( 80 ) NULL DEFAULT NS,
	RcCode                TEXT( 80 ) NULL DEFAULT NS,
	CurrentYear           DECIMAL    NULL DEFAULT 0.0,
	Reduction             DECIMAL    NULL DEFAULT 0.0,
	Ratio                 DECIMAL    NULL DEFAULT 0.0,
	Budget                DECIMAL    NULL DEFAULT 0.0,
	PriorYear             DECIMAL    NULL DEFAULT 0.0,
	FundName              TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode    TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName    TEXT( 80 ) NULL DEFAULT NS,
	BocName               TEXT( 80 ) NULL DEFAULT NS,
	NpmCode               TEXT( 80 ) NULL DEFAULT NS,
	NpmName               TEXT( 80 ) NULL DEFAULT NS,
	Division              TEXT( 80 ) NULL DEFAULT NS,
	DivisionName          TEXT( 80 ) NULL DEFAULT NS,
	Delta                 DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT ForeignKeyProgrammaticReserve FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyProgrammaticReserve PRIMARY KEY ( ProgrammaticReserveId AUTOINCREMENT )
);

CREATE TABLE PurchaseRequestNumbers
(
	PurchaseRequestId INTEGER    NOT NULL UNIQUE,
	RcCode            TEXT( 80 ) NULL DEFAULT NS,
	PurchaseRequest   TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( PurchaseRequestId AUTOINCREMENT )
);

CREATE TABLE Purchases
(
	PurchaseId                  INTEGER    NOT NULL UNIQUE,
	RpioCode                    TEXT( 80 ) NULL DEFAULT NS,
	BFY                         TEXT( 80 ) NULL DEFAULT NS,
	FundCode                    TEXT( 80 ) NULL DEFAULT NS,
	FundName                    TEXT( 80 ) NULL DEFAULT NS,
	AhCode                      TEXT( 80 ) NULL DEFAULT NS,
	AhName                      TEXT( 80 ) NULL DEFAULT NS,
	RcCode                      TEXT( 80 ) NULL DEFAULT NS,
	DivisionName                TEXT( 80 ) NULL DEFAULT NS,
	AccountCode                 TEXT( 80 ) NULL DEFAULT NS,
	BocCode                     TEXT( 80 ) NULL DEFAULT NS,
	BocName                     TEXT( 80 ) NULL DEFAULT NS,
	DocumentControlNumbers      TEXT( 80 ) NULL DEFAULT NS,
	ObligationDocumentNumber    TEXT( 80 ) NULL DEFAULT NS,
	DocType                     TEXT( 80 ) NULL DEFAULT NS,
	DcnPrefix                   TEXT( 80 ) NULL DEFAULT NS,
	System                      TEXT( 80 ) NULL DEFAULT NS,
	LineNumber                  TEXT( 80 ) NULL DEFAULT NS,
	FocCode                     TEXT( 80 ) NULL DEFAULT NS,
	FocName                     TEXT( 80 ) NULL DEFAULT NS,
	OriginalActionDate          DATETIME,
	LastActionDate              DATETIME,
	TransactionNumber           TEXT( 80 ) NULL DEFAULT NS,
	NpmCode                     TEXT( 80 ) NULL DEFAULT NS,
	NpmName                     TEXT( 80 ) NULL DEFAULT NS,
	OrgCode                     TEXT( 80 ) NULL DEFAULT NS,
	OrgName                     TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode          TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName          TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode             TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName             TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode                TEXT( 80 ) NULL DEFAULT NS,
	PurchaseRequestNumber       TEXT( 80 ) NULL DEFAULT NS,
	ReimbursableAgreementNumber TEXT( 80 ) NULL DEFAULT NS,
	SiteProjectCode             TEXT( 80 ) NULL DEFAULT NS,
	VendorCode                  TEXT( 80 ) NULL DEFAULT NS,
	VendorName                  TEXT( 80 ) NULL DEFAULT NS,
	Commitments                 DECIMAL    NULL DEFAULT 0.0,
	OpenCommitments             DECIMAL    NULL DEFAULT 0.0,
	Obligations                 DECIMAL    NULL DEFAULT 0.0,
	Deobligations               DECIMAL    NULL DEFAULT 0.0,
	Used                        DECIMAL    NULL DEFAULT 0.0,
	ULO                         DECIMAL    NULL DEFAULT 0.0,
	Expenditures                DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyPurchases PRIMARY KEY ( PurchaseId AUTOINCREMENT )
);

CREATE TABLE RegionalTravel
(
	RegionalTravelId   INTEGER         NOT NULL UNIQUE,
	PrcId              INTEGER         NOT NULL UNIQUE,
	BudgetLevel        TEXT( 255 ) NOT NULL,
	RPIO               TEXT( 255 ) NOT NULL,
	BFY                TEXT( 255 ) NOT NULL,
	FundCode           TEXT( 255 ) NOT NULL,
	AhCode             TEXT( 255 ) NOT NULL,
	OrgCode            TEXT( 255 ) NOT NULL,
	RcCode             TEXT( 255 ) NOT NULL,
	AccountCode        TEXT( 80 )      NULL DEFAULT NS,
	BocCode            TEXT( 255 ) NOT NULL,
	Amount             DECIMAL         NULL DEFAULT 0.0,
	FundName           TEXT( 80 )      NULL DEFAULT NS,
	BocName            TEXT( 80 )      NULL DEFAULT NS,
	Division           TEXT( 80 )      NULL DEFAULT NS,
	DivisionName       TEXT( 80 )      NULL DEFAULT NS,
	ActivityCode       TEXT( 80 )      NULL DEFAULT NS,
	NpmCode            TEXT( 80 )      NULL DEFAULT NS,
	NpmName            TEXT( 80 )      NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 )      NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 )      NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 )      NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 )      NULL DEFAULT NS,
	GoalCode           TEXT( 80 )      NULL DEFAULT NS,
	GoalName           TEXT( 80 )      NULL DEFAULT NS,
	ObjectiveCode      TEXT( 80 )      NULL DEFAULT NS,
	ObjectiveName      TEXT( 80 )      NULL DEFAULT NS,
	AllocationRatio    DECIMAL         NULL DEFAULT 0.0,
	ChangeDate         DATETIME,
	CONSTRAINT ForeignKeyRegionalTravel FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyRegionalTravel PRIMARY KEY ( RegionalTravelId AUTOINCREMENT )
);

CREATE TABLE ReimbursableAgreements
(
	ReimbursableAgreementId INTEGER    NOT NULL UNIQUE,
	RPIO                    TEXT( 80 ) NULL DEFAULT NS,
	BFY                     TEXT( 80 ) NULL DEFAULT NS,
	FundCode                TEXT( 80 ) NULL DEFAULT NS,
	AgreementNumber         TEXT( 80 ) NULL DEFAULT NS,
	StartDate               TEXT( 80 ) NULL DEFAULT NS,
	EndDate                 INTEGER,
	RcCode                  TEXT( 80 ) NULL DEFAULT NS,
	OrgCode                 TEXT( 80 ) NULL DEFAULT NS,
	DivisionName            TEXT( 80 ) NULL DEFAULT NS,
	SiteProjectCode         TEXT( 80 ) NULL DEFAULT NS,
	AccountCode             TEXT( 80 ) NULL DEFAULT NS,
	VendorCode              TEXT( 80 ) NULL DEFAULT NS,
	VendorName              TEXT( 80 ) NULL DEFAULT NS,
	Amount                  FLOAT,
	OpenCommitments         FLOAT,
	Obligations             FLOAT,
	ULO                     FLOAT,
	Available               FLOAT,
	PRIMARY KEY ( ReimbursableAgreementId AUTOINCREMENT )
);

CREATE TABLE ReimbursableSurvey
(
	ReimbursableSurveyId INTEGER    NOT NULL UNIQUE,
	BFY                  TEXT( 80 ) NULL DEFAULT NS,
	FundCode             TEXT( 80 ) NULL DEFAULT NS,
	FundName             TEXT( 80 ) NULL DEFAULT NS,
	Amount               FLOAT,
	PRIMARY KEY ( ReimbursableSurveyId AUTOINCREMENT )
);

CREATE TABLE Reprogrammings
(
	ReprogrammingId     INTEGER    NOT NULL UNIQUE,
	ReprogrammingNumber TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate       TEXT( 80 ) NULL DEFAULT NS,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode     TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName     TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	Amount              FLOAT,
	SPIO                TEXT( 80 ) NULL DEFAULT NS,
	Purpose             TEXT( 80 ) NULL DEFAULT NS,
	ExtendedPurpose     TEXT( 80 ) NULL DEFAULT NS,
	FromTo              TEXT( 80 ) NULL DEFAULT NS,
	DocType             TEXT( 80 ) NULL DEFAULT NS,
	DocPrefix           TEXT( 80 ) NULL DEFAULT NS,
	NpmCode             TEXT( 80 ) NULL DEFAULT NS,
	Line                TEXT( 80 ) NULL DEFAULT NS,
	Subline             TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( ReprogrammingId AUTOINCREMENT )
);

CREATE TABLE SystemUpdates
(
	SystemUpdateId     INTEGER    NOT NULL UNIQUE,
	ExtId              INTEGER    NOT NULL UNIQUE,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	Amount             FLOAT,
	PRIMARY KEY ( SystemUpdateId AUTOINCREMENT )
);

CREATE TABLE Transfers
(
	TransferId          INTEGER    NOT NULL UNIQUE,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	DocPrefix           TEXT( 80 ) NULL DEFAULT NS,
	DocType             TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	RpioCode            TEXT( 80 ) NULL DEFAULT NS,
	RpioName            TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	ReprogrammingNumber TEXT( 80 ) NULL DEFAULT NS,
	ControlNumber       TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate       datetime,
	Quarter             TEXT( 80 ) NULL DEFAULT NS,
	Line                TEXT( 80 ) NULL DEFAULT NS,
	Subline             TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	AhName              TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	OrganizationName    TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode     TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName     TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	FromTo              TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	NpmCode             TEXT( 80 ) NULL DEFAULT NS,
	NpmName             TEXT( 80 ) NULL DEFAULT NS,
	Amount              DECIMAL    NULL DEFAULT 0.0,
	Purpose             TEXT( 80 ) NULL DEFAULT NS,
	PurposeExtended     TEXT( 80 ) NULL DEFAULT NS,
	ResourceType        TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyTransfers PRIMARY KEY ( TransferId AUTOINCREMENT )
);

CREATE TABLE UpperReconcilliation
(
	ReconcilliationId  INTEGER    NOT NULL UNIQUE,
	ExtId              INTEGER    NOT NULL,
	PrcId              INTEGER    NOT NULL UNIQUE,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	System             FLOAT,
	Budget             FLOAT,
	Delta              FLOAT,
	NET                TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( ReconcilliationId AUTOINCREMENT )
);

CREATE TABLE LowerReconcilliation
(
	ReconcilliationId  INTEGER    NOT NULL UNIQUE,
	ExtId              INTEGER    NOT NULL,
	PrcId              INTEGER    NOT NULL UNIQUE,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	System             FLOAT,
	Budget             FLOAT,
	Delta              FLOAT,
	NET                TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( ReconcilliationId AUTOINCREMENT )
);

CREATE TABLE AgencyTransfers
(
	AgencyTransferId    INTEGER    NOT NULL UNIQUE,
	TransferId          INTEGER    NOT NULL UNIQUE,
	ReprogrammingNumber TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate       datetime,
	RPIO                TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	Amount              money,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName  TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	FromTo              TEXT( 80 ) NULL DEFAULT NS,
	SPIO                TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT ForeignKeyAgencyTransfers FOREIGN KEY ( TransferId ) REFERENCES Transfers,
	CONSTRAINT PrimaryKeyAgencyTransfers PRIMARY KEY ( AgencyTransferId )
);

CREATE TABLE CarryoverSurvey
(
	CarryoverSurveyId INTEGER    NOT NULL UNIQUE,
	BFY               TEXT( 80 ) NULL DEFAULT NS,
	FundCode          TEXT( 80 ) NULL DEFAULT NS,
	FundName          TEXT( 80 ) NULL DEFAULT NS,
	Amount            FLOAT      NULL DEFAULT 0,
	PRIMARY KEY ( CarryoverSurveyId AUTOINCREMENT )
);

CREATE TABLE ControlNumbers
(
	ControlNumberId INTEGER    NOT NULL UNIQUE,
	RPIO            TEXT( 80 ) NULL DEFAULT NS,
	RegionNumber    DECIMAL    NULL DEFAULT 0.0,
	BFY             TEXT( 80 ) NULL DEFAULT NS,
	CalendarYear    TEXT( 80 ) NULL DEFAULT NS,
	FundCode        TEXT( 80 ) NULL DEFAULT NS,
	FundNumber      TEXT( 80 ) NULL DEFAULT NS,
	AhCode          TEXT( 80 ) NULL DEFAULT NS,
	RcCode          TEXT( 80 ) NULL DEFAULT NS,
	DivisionName    TEXT( 80 ) NULL DEFAULT NS,
	DivisionNumber  DECIMAL    NULL DEFAULT 0.0,
	DateIssued      DATETIME,
	Purpose         TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( ControlNumberId AUTOINCREMENT )
);

CREATE TABLE CongressionalTransfers
(
	CongressionalTransferId INTEGER    NOT NULL UNIQUE,
	ReprogrammingNumber     TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate           DATETIME,
	RPIO                    TEXT( 80 ) NULL DEFAULT NS,
	AhCode                  TEXT( 80 ) NULL DEFAULT NS,
	BFY                     TEXT( 80 ) NULL DEFAULT NS,
	FundCode                TEXT( 80 ) NULL DEFAULT NS,
	AccountCode             TEXT( 80 ) NULL DEFAULT NS,
	OrgCode                 TEXT( 80 ) NULL DEFAULT NS,
	BocCode                 TEXT( 80 ) NULL DEFAULT NS,
	RcCode                  TEXT( 80 ) NULL DEFAULT NS,
	Amount                  NUMBER,
	FundName                TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode      TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName      TEXT( 80 ) NULL DEFAULT NS,
	BocName                 TEXT( 80 ) NULL DEFAULT NS,
	SPIO                    TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyCongressionalTransfers PRIMARY KEY ( CongressionalTransferId )
);

CREATE TABLE OperatingPlans
(
	OppId              INTEGER    NOT NULL UNIQUE,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            INTEGER,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	NpmCode            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 ) NULL DEFAULT NS,
	NpmName            TEXT( 80 ) NULL DEFAULT NS,
	AhName             TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	OrgName            TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode       TEXT( 80 ) NULL DEFAULT NS,
	ActivityName       TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 ) NULL DEFAULT NS,
	GoalCode           TEXT( 80 ) NULL DEFAULT NS,
	GoalName           TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode      TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName      TEXT( 80 ) NULL DEFAULT NS,
	PRIMARY KEY ( OppId AUTOINCREMENT )
);

CREATE TABLE RegionalRescissionAuthority
(
	RegionalRescissionAuthorityId INTEGER    NOT NULL UNIQUE,
	RescissionId                  INTEGER    NOT NULL UNIQUE,
	PrcId                         INTEGER    NOT NULL UNIQUE,
	RPIO                          TEXT( 80 ) NULL DEFAULT NS,
	BudgetLevel                   TEXT( 80 ) NULL DEFAULT NS,
	AhCode                        TEXT( 80 ) NULL DEFAULT NS,
	BFY                           TEXT( 80 ) NULL DEFAULT NS,
	FundCode                      TEXT( 80 ) NULL DEFAULT NS,
	OrgCode                       TEXT( 80 ) NULL DEFAULT NS,
	AccountCode                   TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode                  TEXT( 80 ) NULL DEFAULT NS,
	BocCode                       TEXT( 80 ) NULL DEFAULT NS,
	RcCode                        TEXT( 80 ) NULL DEFAULT NS,
	Reduction                     DECIMAL    NULL DEFAULT 0.0,
	Amount                        DECIMAL    NULL DEFAULT 0.0,
	FundName                      TEXT( 80 ) NULL DEFAULT NS,
	BocName                       TEXT( 80 ) NULL DEFAULT NS,
	Division                      TEXT( 80 ) NULL DEFAULT NS,
	DivisionName                  TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName            TEXT( 80 ) NULL DEFAULT NS,
	NpmCode                       TEXT( 80 ) NULL DEFAULT NS,
	NpmName                       TEXT( 80 ) NULL DEFAULT NS,
	GoalCode                      TEXT( 80 ) NULL DEFAULT NS,
	GoalName                      TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode                 TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName                 TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio               DECIMAL    NULL DEFAULT 0.0,
	ChangeDate                    DATETIME,
	CONSTRAINT ForeignKeyRegionalAuthorityAllocations FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT ForeignKeyRegionalAuthorityRescissions FOREIGN KEY ( RescissionId ) REFERENCES Rescission,
	CONSTRAINT PrimaryKeyRegionalRescissionAuthority PRIMARY KEY ( RegionalRescissionAuthorityId )
);

CREATE TABLE EmployeeData
(
	EmployeeDataId           INTEGER    NOT NULL UNIQUE,
	RpioCode                 TEXT( 80 ) NULL DEFAULT NS,
	RpioName                 TEXT( 80 ) NULL DEFAULT NS,
	ActionDate               DATETIME,
	HiringAuthority          TEXT( 80 ) NULL DEFAULT NS,
	SupervisorId             TEXT( 80 ) NULL DEFAULT NS,
	JobTitle                 TEXT( 80 ) NULL DEFAULT NS,
	HrOrgCode                TEXT( 80 ) NULL DEFAULT NS,
	HrOrgName                TEXT( 80 ) NULL DEFAULT NS,
	EmployeeId               TEXT( 80 ) NULL DEFAULT NS,
	FirstName                TEXT( 80 ) NULL DEFAULT NS,
	LastName                 TEXT( 80 ) NULL DEFAULT NS,
	RetirementPlan           TEXT( 80 ) NULL DEFAULT NS,
	ScheduledRetirementDate  DATETIME,
	HireDate                 DATETIME,
	Grade                    TEXT( 80 ) NULL DEFAULT NS,
	Step                     TEXT( 80 ) NULL DEFAULT NS,
	GradeEntry               DATETIME,
	LastIncrease             DATETIME,
	StepEntry                DATETIME,
	WigiDueDate              DATETIME,
	EmployeeStatus           TEXT( 80 ) NULL DEFAULT NS,
	HoursEarnedYearToDate    DECIMAL    NULL DEFAULT 0.0,
	CarryoverHours           DECIMAL    NULL DEFAULT 0.0,
	HoursAdjustedYearToDate  DECIMAL    NULL DEFAULT 0.0,
	HoursBalance             DECIMAL    NULL DEFAULT 0.0,
	ProjectedAnnualHours     DECIMAL    NULL DEFAULT 0.0,
	ProjectedNextPeriodHours DECIMAL    NULL DEFAULT 0.0,
	HoursTakenYearToDate     DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyEmployeeData PRIMARY KEY ( EmployeeDataId )
);

CREATE TABLE Employees
(
	PersonnelId INTEGER    NOT NULL UNIQUE,
	RcCode      TEXT( 80 ) NULL DEFAULT NS,
	EpaNumber   TEXT( 80 ) NULL DEFAULT NS,
	LastName    TEXT( 80 ) NULL DEFAULT NS,
	FirstName   TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyEmployees PRIMARY KEY ( PersonnelId )
);

CREATE TABLE EmployeePayroll
(
	EmployeePayrollId INTEGER    NOT NULL UNIQUE,
	RcCode            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName      TEXT( 80 ) NULL DEFAULT NS,
	EpaNumber         TEXT( 80 ) NULL DEFAULT NS,
	LastName          TEXT( 80 ) NULL DEFAULT NS,
	FirstName         TEXT( 80 ) NULL DEFAULT NS,
	ReportingCode     TEXT( 80 ) NULL DEFAULT NS,
	ReportingCodeName TEXT( 80 ) NULL DEFAULT NS,
	Hours             DECIMAL    NULL DEFAULT 0.0,
	Days              DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyEmployeePayroll PRIMARY KEY ( EmployeePayrollId )
);

CREATE TABLE FullTimeEquivalents
(
	FullTimeEquivalentId INTEGER    NOT NULL UNIQUE,
	PrcId                INTEGER    NOT NULL UNIQUE,
	BudgetLevel          TEXT( 80 ) NULL DEFAULT NS,
	RPIO                 TEXT( 80 ) NULL DEFAULT NS,
	BFY                  TEXT( 80 ) NULL DEFAULT NS,
	FundCode             TEXT( 80 ) NULL DEFAULT NS,
	AhCode               TEXT( 80 ) NULL DEFAULT NS,
	OrgCode              TEXT( 80 ) NULL DEFAULT NS,
	RcCode               TEXT( 80 ) NULL DEFAULT NS,
	AccountCode          TEXT( 80 ) NULL DEFAULT NS,
	BocCode              TEXT( 80 ) NULL DEFAULT NS,
	Amount               DECIMAL    NULL DEFAULT 0.0,
	FundName             TEXT( 80 ) NULL DEFAULT NS,
	BocName              TEXT( 80 ) NULL DEFAULT NS,
	Division             TEXT( 80 ) NULL DEFAULT NS,
	DivisionName         TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode         TEXT( 80 ) NULL DEFAULT NS,
	NpmCode              TEXT( 80 ) NULL DEFAULT NS,
	NpmName              TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode   TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName   TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode      TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName      TEXT( 80 ) NULL DEFAULT NS,
	GoalCode             TEXT( 80 ) NULL DEFAULT NS,
	GoalName             TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode        TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName        TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio      DECIMAL    NULL DEFAULT 0.0,
	ChangeDate           DATETIME,
	CONSTRAINT ForeignKeyFullTimeEquivalents FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyFullTimeEquivalents PRIMARY KEY ( FullTimeEquivalentId )
);

CREATE TABLE HumanResourceOrganizations
(
	HumanResourceOrganizationId INTEGER,
	RcCode                      NVARCHAR(255),
	DivisionName                NVARCHAR(255),
	HrOrgCode                   NVARCHAR(255),
	HrOrgName                   NVARCHAR(255)
);

CREATE TABLE PayPeriods
(
	PayPeriodId INTEGER NOT NULL UNIQUE,
	Period TEXT(255
) NOT NULL,
	PayPeriod TEXT(80) NULL DEFAULT NS,
	StartDate DATETIME,
	EndDate DATETIME,
	CONSTRAINT PrimaryKeyPayPeriods PRIMARY KEY(PayPeriodId)
);

CREATE TABLE Payroll
(
	PayrollId          INTEGER    NOT NULL UNIQUE,
	PrcId              INTEGER    NOT NULL UNIQUE,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	Division           TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode       TEXT( 80 ) NULL DEFAULT NS,
	NpmCode            TEXT( 80 ) NULL DEFAULT NS,
	NpmName            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 ) NULL DEFAULT NS,
	GoalCode           TEXT( 80 ) NULL DEFAULT NS,
	GoalName           TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode      TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName      TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio    DECIMAL    NULL DEFAULT 0.0,
	ChangeDate         DATETIME,
	CONSTRAINT ForiegnKeyPayroll FOREIGN KEY ( PrcId ) REFERENCES Allocations,
	CONSTRAINT PrimaryKeyPayroll PRIMARY KEY ( PayrollId )
);

CREATE TABLE PayrollHours
(
	PayrollHoursId    INTEGER    NOT NULL UNIQUE,
	RpioCode          TEXT( 80 ) NULL DEFAULT NS,
	PayPeriod         TEXT( 80 ) NULL DEFAULT NS,
	StartDate         DATETIME,
	EndDate           DATETIME,
	EpaNumber         TEXT( 80 ) NULL DEFAULT NS,
	FirstName         TEXT( 80 ) NULL DEFAULT NS,
	LastName          TEXT( 80 ) NULL DEFAULT NS,
	ProcessedDate     DATETIME,
	HrOrgCode         TEXT( 80 ) NULL DEFAULT NS,
	HrOrgCodeName     TEXT( 80 ) NULL DEFAULT NS,
	ReportingCode     TEXT( 80 ) NULL DEFAULT NS,
	ReportingCodeName TEXT( 80 ) NULL DEFAULT NS,
	ApprovalDate      DATETIME,
	WorkCode          TEXT( 80 ) NULL DEFAULT NS,
	Hours             DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyPayrollHours PRIMARY KEY ( PayrollHoursId )
);

CREATE TABLE PayrollObligations
(
	PayrollObligationId           INTEGER    NOT NULL UNIQUE,
	RPIO                          TEXT( 80 ) NULL DEFAULT NS,
	BFY                           TEXT( 80 ) NULL DEFAULT NS,
	FundCode                      TEXT( 80 ) NULL DEFAULT NS,
	AhCode                        TEXT( 80 ) NULL DEFAULT NS,
	OrgCode                       TEXT( 80 ) NULL DEFAULT NS,
	RcCode                        TEXT( 80 ) NULL DEFAULT NS,
	AccountCode                   TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode            TEXT( 80 ) NULL DEFAULT NS,
	Amount                        DECIMAL    NULL DEFAULT 0.0,
	Hours                         DECIMAL    NULL DEFAULT 0.0,
	CumulativeBenefits            DECIMAL    NULL DEFAULT 0.0,
	AnnualBasePaid                DECIMAL    NULL DEFAULT 0.0,
	AnnualBaseHours               DECIMAL    NULL DEFAULT 0.0,
	AnnualOvertimePaid            DECIMAL    NULL DEFAULT 0.0,
	AnnualOvertimeHours           DECIMAL    NULL DEFAULT 0.0,
	AnnualOtherHours              DECIMAL    NULL DEFAULT 0.0,
	AnnualOtherPaid               DECIMAL    NULL DEFAULT 0.0,
	AllocationPercentage          TEXT( 80 ) NULL DEFAULT NS,
	PayPeriod                     TEXT( 80 ) NULL DEFAULT NS,
	FocCode                       TEXT( 80 ) NULL DEFAULT NS,
	FocName                       TEXT( 80 ) NULL DEFAULT NS,
	WorkCode                      TEXT( 80 ) NULL DEFAULT NS,
	WorkCodeName                  TEXT( 80 ) NULL DEFAULT NS,
	HumanResourceOrganizationCode TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyPayrollObligations PRIMARY KEY ( PayrollObligationId )
);

CREATE TABLE WorkCodes
(
	WorkCodeId       INTEGER NOT NULL UNIQUE,
	RpioCode         TEXT( 255 )      DEFAULT (NS),
	WorkCode         TEXT( 255 )      DEFAULT (NS),
	WorkCodeName     TEXT( 255 )      DEFAULT (NS),
	ChargeType       TEXT( 255 )      DEFAULT (NS),
	Notifications    TEXT( 255 )      DEFAULT (NS),
	PayPeriod        TEXT( 255 )      DEFAULT (NS),
	BFY              TEXT( 255 )      DEFAULT (NS),
	ApproverUserName TEXT( 255 )      DEFAULT (NS),
	ApprovedDate     TEXT( 255 )      DEFAULT (NS),
	ModifierUserName TEXT( 255 )      DEFAULT (NS),
	ModifiedDate     TEXT( 255 )      DEFAULT (NS),
	FundCode         TEXT( 255 )      DEFAULT (NS),
	FocCode          TEXT( 255 )      DEFAULT (NS),
	CostOrgCode      TEXT( 255 )      DEFAULT (NS),
	CostOrgName      TEXT( 255 )      DEFAULT (NS),
	RcCode           TEXT( 255 )      DEFAULT (NS),
	AccountCode      TEXT( 255 )      DEFAULT (NS),
	WorkProjectCode  TEXT( 255 )      DEFAULT (NS),
	WorkProjectName  TEXT( 255 )      DEFAULT (NS),
	Percentage       FLOAT   NOT NULL DEFAULT (0.0),
	CONSTRAINT PrimaryKeyWorkCodes PRIMARY KEY ( WorkCodeId )
);

CREATE TABLE BudgetParameters
(
	BudgetParameterId INTEGER    NOT NULL UNIQUE,
	AhCode            TEXT( 80 ) NULL DEFAULT NS,
	BFY               TEXT( 80 ) NULL DEFAULT NS,
	RcCode            TEXT( 80 ) NULL DEFAULT NS,
	FundCode          TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyBudgetParameters PRIMARY KEY ( BudgetParameterId )
);

CREATE TABLE ReferenceTables
(
	ReferenceTableId INTEGER    NOT NULL UNIQUE,
	TableName        TEXT( 80 ) NULL DEFAULT NS,
	Type             TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyReferenceTables PRIMARY KEY ( ReferenceTableId )
);

CREATE TABLE PeoplePlus
(
	PeoplePlusId      INTEGER    NOT NULL UNIQUE,
	RcCode            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName      TEXT( 80 ) NULL DEFAULT NS,
	EpaNumber         TEXT( 80 ) NULL DEFAULT NS,
	LastName          TEXT( 80 ) NULL DEFAULT NS,
	FirstName         TEXT( 80 ) NULL DEFAULT NS,
	ReportingCode     TEXT( 80 ) NULL DEFAULT NS,
	ReportingCodeName TEXT( 80 ) NULL DEFAULT NS,
	WorkCode          TEXT( 80 ) NULL DEFAULT NS,
	Hours             FLOAT,
	CONSTRAINT PrimaryKeyPeoplePlus PRIMARY KEY ( PeoplePlusId )
);

CREATE TABLE EmployeeLeave
(
	EmployeeLeaveId          INTEGER    NOT NULL UNIQUE,
	LastName                 TEXT( 80 ) NULL DEFAULT NS,
	FirstName                TEXT( 80 ) NULL DEFAULT NS,
	EmployeeId               TEXT( 80 ) NULL DEFAULT NS,
	HoursEarnedYearToDate    FLOAT,
	CarryoverHours           FLOAT,
	HoursAdjustedYearToDate  FLOAT,
	HoursBalance             FLOAT,
	ProjectedAnnualHours     FLOAT,
	ProjectedNextPeriodHours FLOAT,
	HoursTakenYearToDate     FLOAT,
	CONSTRAINT PrimaryKeyEmployeeLeave PRIMARY KEY ( EmployeeLeaveId )
);

CREATE TABLE DivisionTraining
(
	DivisionTrainingId INTEGER    NOT NULL UNIQUE,
	PrcId              FLOAT,
	BudgetLevel        TEXT( 80 ) NULL DEFAULT NS,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	BocCode            TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	Amount             DECIMAL(18, 0),
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	BocName            TEXT( 80 ) NULL DEFAULT NS,
	Division           TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	ActivityCode       TEXT( 80 ) NULL DEFAULT NS,
	NpmName            TEXT( 80 ) NULL DEFAULT NS,
	NpmCode            TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 ) NULL DEFAULT NS,
	GoalCode           TEXT( 80 ) NULL DEFAULT NS,
	GoalName           TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveCode      TEXT( 80 ) NULL DEFAULT NS,
	ObjectiveName      TEXT( 80 ) NULL DEFAULT NS,
	AllocationRatio    FLOAT,
	ChangeDate         DATETIME,
	CONSTRAINT PrimaryKeyDivisionTraining PRIMARY KEY ( DivisionTrainingId )
);

CREATE TABLE LocatorData
(
	LocatorId   INTEGER    NOT NULL UNIQUE,
	LastName    TEXT( 80 ) NULL DEFAULT NS,
	FirstName   TEXT( 80 ) NULL DEFAULT NS,
	Email       TEXT( 80 ) NULL DEFAULT NS,
	PhoneNumber TEXT( 80 ) NULL DEFAULT NS,
	MailCode    TEXT( 80 ) NULL DEFAULT NS,
	Office      TEXT( 80 ) NULL DEFAULT NS,
	CellNumber  TEXT( 80 ) NULL DEFAULT NS,
	Status      TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyLocatorData PRIMARY KEY ( LocatorId )
);

CREATE TABLE DivisionPersonnel
(
	PersonnelId INTEGER    NOT NULL UNIQUE,
	RcCode      TEXT( 80 ) NULL DEFAULT NS,
	EmployeeId  TEXT( 80 ) NULL DEFAULT NS,
	LastName    TEXT( 80 ) NULL DEFAULT NS,
	FirstName   TEXT( 80 ) NULL DEFAULT NS,
	JobTitle    TEXT( 80 ) NULL DEFAULT NS,
	Grade       TEXT( 80 ) NULL DEFAULT NS,
	Step        TEXT( 80 ) NULL DEFAULT NS,
	HireDate    DATETIME,
	Tenure      FLOAT,
	HrOrgName   TEXT( 80 ) NULL DEFAULT NS,
	Email       TEXT( 80 ) NULL DEFAULT NS,
	PhoneNumber TEXT( 80 ) NULL DEFAULT NS,
	Office      TEXT( 80 ) NULL DEFAULT NS,
	MailCode    TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyDivisionPersonnel PRIMARY KEY ( PersonnelId )
);

CREATE TABLE CarryoverEstimates
(
	CarryoverEstimateId INTEGER    NOT NULL UNIQUE,
	BudgetLevel         TEXT( 80 ) NULL DEFAULT NS,
	BFY                 TEXT( 80 ) NULL DEFAULT NS,
	AhCode              TEXT( 80 ) NULL DEFAULT NS,
	FundCode            TEXT( 80 ) NULL DEFAULT NS,
	FundName            TEXT( 80 ) NULL DEFAULT NS,
	OrgCode             TEXT( 80 ) NULL DEFAULT NS,
	AccountCode         TEXT( 80 ) NULL DEFAULT NS,
	RcCode              TEXT( 80 ) NULL DEFAULT NS,
	DivisionName        TEXT( 80 ) NULL DEFAULT NS,
	BocCode             TEXT( 80 ) NULL DEFAULT NS,
	BocName             TEXT( 80 ) NULL DEFAULT NS,
	Balance             FLOAT      NULL DEFAULT 0,
	OpenCommitment      RREA,
	Estimate            FLOAT      NULL DEFAULT 0,
	PRIMARY KEY ( CarryoverEstimateId AUTOINCREMENT )
);

CREATE TABLE PayrollAccruals
(
	PayrollAccrualId   INTEGER    NOT NULL UNIQUE,
	RPIO               TEXT( 80 ) NULL DEFAULT NS,
	AhCode             TEXT( 80 ) NULL DEFAULT NS,
	BFY                TEXT( 80 ) NULL DEFAULT NS,
	RcCode             TEXT( 80 ) NULL DEFAULT NS,
	DivisionName       TEXT( 80 ) NULL DEFAULT NS,
	EpaNumber          TEXT( 80 ) NULL DEFAULT NS,
	LastName           TEXT( 80 ) NULL DEFAULT NS,
	FirstName          TEXT( 80 ) NULL DEFAULT NS,
	FundCode           TEXT( 80 ) NULL DEFAULT NS,
	FundName           TEXT( 80 ) NULL DEFAULT NS,
	OrgCode            TEXT( 80 ) NULL DEFAULT NS,
	AccountCode        TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectCode TEXT( 80 ) NULL DEFAULT NS,
	ProgramProjectName TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaCode    TEXT( 80 ) NULL DEFAULT NS,
	ProgramAreaName    TEXT( 80 ) NULL DEFAULT NS,
	WorkCode           TEXT( 80 ) NULL DEFAULT NS,
	HrOrgCode          TEXT( 80 ) NULL DEFAULT NS,
	PayPeriod          TEXT( 80 ) NULL DEFAULT NS,
	StartDate          DATETIME,
	EndDate            DATETIME,
	Amount             DECIMAL    NULL DEFAULT 0.0,
	Hours              DECIMAL    NULL DEFAULT 0.0,
	Benfits            DECIMAL    NULL DEFAULT 0.0,
	OvertimePaid       DECIMAL    NULL DEFAULT 0.0,
	OvertimeHours      DECIMAL    NULL DEFAULT 0.0,
	CONSTRAINT PrimaryKeyPayrollAccruals PRIMARY KEY ( PayrollAccrualId AUTOINCREMENT )
);

CREATE TABLE PayrollCostCodes
(
	PayrollCostCodeId INTEGER    NOT NULL UNIQUE,
	RPIO              TEXT( 80 ) NULL DEFAULT NS,
	AhCode            TEXT( 80 ) NULL DEFAULT NS,
	BFY               TEXT( 80 ) NULL DEFAULT NS,
	RcCode            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName      TEXT( 80 ) NULL DEFAULT NS,
	WorkCode          TEXT( 80 ) NULL DEFAULT NS,
	WorkCodeName      TEXT( 80 ) NULL DEFAULT NS,
	HrOrgCode         TEXT( 80 ) NULL DEFAULT NS,
	HrOrgName         TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyPayrollCostCodes PRIMARY KEY ( PayrollCostCodeId AUTOINCREMENT )
);

CREATE TABLE ReportingCodes
(
	ReportingCodesId  INTEGER    NOT NULL UNIQUE,
	ReportingCode     TEXT( 80 ) NULL DEFAULT NS,
	ReportingCodeName TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyReportingCodes PRIMARY KEY ( ReportingCodesId AUTOINCREMENT )
);

CREATE TABLE SiteProjectCodes
(
	SiteProjectCodeId INTEGER    NOT NULL UNIQUE,
	RcCode            TEXT( 80 ) NULL DEFAULT NS,
	DivisionName      TEXT( 80 ) NULL DEFAULT NS,
	SiteProjectCode   TEXT( 80 ) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeySiteProjectCodes PRIMARY KEY ( SiteProjectCodeId AUTOINCREMENT )
);

COMMIT;
