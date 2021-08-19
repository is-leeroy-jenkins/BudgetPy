CREATE TABLE EmployeeData
(
	EmployeeDataId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyEmployeeData PRIMARY KEY,
	RpioCode TEXT(255) NULL,
	RpioName TEXT(255) NULL,
	ActionDate DATETIME NULL,
	HiringAuthority TEXT(255) NULL,
	SupervisorId TEXT(255) NULL,
	JobTitle TEXT(255) NULL,
	HrOrgCode TEXT(255) NULL,
	HrOrgName TEXT(255) NULL,
	EmployeeId TEXT(255) NULL,
	FirstName TEXT(255) NULL,
	LastName TEXT(255) NULL,
	RetirementPlan TEXT(255) NULL,
	ScheduledRetirementDate DATETIME NULL,
	HireDate DATETIME NULL,
	Grade TEXT(255) NULL,
	Step TEXT(255) NULL,
	GradeEntry DATETIME NULL,
	LastIncrease DATETIME NULL,
	StepEntry DATETIME NULL,
	WigiDueDate DATETIME NULL,
	EmployeeStatus TEXT(255) NULL,
	HoursEarnedYearToDate DOUBLE NULL,
	CarryoverHours DOUBLE NULL,
	HoursAdjustedYearToDate DOUBLE NULL,
	HoursBalance DOUBLE NULL,
	ProjectedAnnualHours DOUBLE NULL,
	ProjectedNextPeriodHours DOUBLE NULL,
	HoursTakenYearToDate DOUBLE NULL
);


