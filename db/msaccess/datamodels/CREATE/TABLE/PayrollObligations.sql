CREATE TABLE PayrollObligations
(
	PayrollObligationId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyPayrollObligations PRIMARY KEY,
	RPIO TEXT(255) NULL,
	BFY TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	OrgCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	AccountCode TEXT(255) NULL,
	ProgramProjectCode TEXT(255) NULL,
	Amount DOUBLE NULL,
	Hours DOUBLE NULL,
	CumulativeBenefits DOUBLE NULL,
	AnnualBasePaid DOUBLE NULL,
	AnnualBaseHours DOUBLE NULL,
	AnnualOvertimePaid DOUBLE NULL,
	AnnualOvertimeHours DOUBLE NULL,
	AnnualOtherHours DOUBLE NULL,
	AnnualOtherPaid DOUBLE NULL,
	AllocationPercentage TEXT(255) NULL,
	PayPeriod TEXT(255) NULL,
	FocCode TEXT(255) NULL,
	FocName TEXT(255) NULL,
	WorkCode TEXT(255) NULL,
	WorkCodeName TEXT(255) NULL,
	HumanResourceOrganizationCode TEXT(255) NULL
);

