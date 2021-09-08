CREATE TABLE PayrollHours
(
	PayrollHoursId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyPayrollHours PRIMARY KEY,
	RpioCode TEXT(255) NULL,
	PayPeriod TEXT(255) NULL,
	StartDate DATETIME NULL,
	EndDate DATETIME NULL,
	EpaNumber TEXT(255) NULL,
	FirstName TEXT(255) NULL,
	LastName TEXT(255) NULL,
	ProcessedDate DATETIME NULL,
	HrOrgCode TEXT(255) NULL,
	HrOrgCodeName TEXT(255) NULL,
	ReportingCode TEXT(255) NULL,
	ReportingCodeName TEXT(255) NULL,
	ApprovalDate DATETIME NULL,
	WorkCode TEXT(255) NULL,
	Hours DOUBLE NULL
);