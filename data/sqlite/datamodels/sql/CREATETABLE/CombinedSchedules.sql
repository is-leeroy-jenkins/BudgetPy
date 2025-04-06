CREATE TABLE CombinedSchedules 
(
	CombinedSchedulesId AUTOINCREMENT NOT NULL UNIQUE,
	ReportingYear	TEXT(150) DEFAULT NS,
	MainAccount	TEXT(150) DEFAULT NS,
	LineNumber	TEXT(150) DEFAULT NS,
	LineName	TEXT(150) DEFAULT NS,
	SplitNumber	TEXT(150) DEFAULT NS,
	PriorYear	DOUBLE DEFAULT 0.0,
	CurrentYear	DOUBLE DEFAULT 0.0,
	BudgetYear	DOUBLE DEFAULT 0.0,
	BudgetYear1	DOUBLE DEFAULT 0.0,
	BudgetYear2	DOUBLE DEFAULT 0.0,
	BudgetYear3	DOUBLE DEFAULT 0.0,
	BudgetYear4	DOUBLE DEFAULT 0.0,
	BudgetYear5	DOUBLE DEFAULT 0.0,
	BudgetYear6	DOUBLE DEFAULT 0.0,
	BudgetYear7	DOUBLE DEFAULT 0.0,
	BudgetYear8	DOUBLE DEFAULT 0.0,
	BudgetYear9	DOUBLE DEFAULT 0.0,
	AccountName	TEXT(150) DEFAULT NS,
	TreasuryAccount	TEXT(150) DEFAULT NS,
	Subfunction	TEXT(150) DEFAULT NS,
	Classification	TEXT(150) DEFAULT NS,
	BudgetEnforcementCategory	TEXT(150) DEFAULT NS
	CONSTRAINT(CombinedSchedulesPrimaryKey) 
		PRIMARY KEY(CombinedSchedulesId)
);