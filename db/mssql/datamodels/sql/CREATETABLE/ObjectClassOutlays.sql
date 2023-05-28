CREATE TABLE ObjectClassOutlays 
(
	ObjectClassOutlaysId	INT NOT NULL IDENTITY(1,1),
	ReportYear	NVARCHAR(80) NULL,
	BudgetAgencyCode	NVARCHAR(80) NULL,
	BudgetAgencyName	NVARCHAR(80) NULL,
	BudgetBureauCode	NVARCHAR(80) NULL,
	BudgetBureauName	NVARCHAR(80) NULL,
	BudgetAccountCode	NVARCHAR(80) NULL,
	BudgetAccountName NVARCHAR(MAX) NULL,
	ObligationType	NVARCHAR(80) NULL,
	DirectReimbursableTitle	NVARCHAR(80) NULL,
	ObjectClassGroupNumber	NVARCHAR(80) NULL,
	ObjectClassGroupName	NVARCHAR(80) NULL,
	BocCode	NVARCHAR(80) NULL,
	BocName	NVARCHAR(80) NULL,
	FinanceObjectClass	NVARCHAR(80) NULL,
	PriorYear	FLOAT NULL,
	CurrentYear	FLOAT NULL,
	BudgetYear	FLOAT NULL
);