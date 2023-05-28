CREATE TABLE ProgramFinancingSchedule 
(
	ProgramFinancingScheduleId	INT NOT NULL IDENTITY(1,1),
	ReportYear	NVARCHAR(80) NULL,
	TreasuryAgencyCode	NVARCHAR(80) NULL,
	TreasuryAccountCode	NVARCHAR(80) NULL,
	LedgerAccountCode	NVARCHAR(80) NULL,
	SectionNumber	NVARCHAR(80) NULL,
	SectionName	NVARCHAR(80) NULL,
	LineNumber	NVARCHAR(80) NULL,
	LineDescription	NVARCHAR(80) NULL,
	OmbAgencyCode	NVARCHAR(80) NULL,
	OmbFundCode	NVARCHAR(80) NULL,
	OmbAccountTitle	NVARCHAR(80) NULL,
	AgencySequence	NVARCHAR(80) NULL,
	AccountSequence	NVARCHAR(80) NULL,
	AgencyName	NVARCHAR(80) NULL,
	FundName	NVARCHAR(80) NULL,
	OriginalAmount	FLOAT NULL,
	BudgetAmount	FLOAT NULL,
	AgencyAmount	FLOAT NULL,
	Amount	FLOAT NULL
);