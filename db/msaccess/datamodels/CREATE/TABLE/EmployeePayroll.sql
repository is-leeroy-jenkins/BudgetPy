CREATE TABLE IF NOT EXISTS EmployeePayroll
(
	EmployeePayrollId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyEmployeePayroll PRIMARY KEY,
	RcCode TEXT(255) NULL,
	DivisionName TEXT(255) NULL,
	EpaNumber TEXT(255) NULL,
	LastName TEXT(255) NULL,
	FirstName TEXT(255) NULL,
	ReportingCode TEXT(255) NULL,
	ReportingCodeName TEXT(255) NULL,
	Hours DOUBLE NULL,
	Days DOUBLE NULL
);