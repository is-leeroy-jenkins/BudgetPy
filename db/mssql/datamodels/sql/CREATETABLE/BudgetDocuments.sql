CREATE TABLE BudgetDocuments 
(
	BudgetDocumentsId	INT NOT NULL IDENTITY(1,1),
	BFY	NVARCHAR(80) NULL,
	EFY	NVARCHAR(80) NULL,
	BudgetLevel	NVARCHAR(80) NULL,
	DocumentDate	NVARCHAR(80) NULL,
	DocumentType	NVARCHAR(80) NULL,
	DocumentNumber	NVARCHAR(80) NULL,
	FundCode	NVARCHAR(80) NULL,
	FundName	NVARCHAR(80) NULL,
	Budgeted	FLOAT NULL,
	Posted	FLOAT NULL,
	CarryoverOut	FLOAT NULL,
	CarryoverIn	FLOAT NULL,
	Recoveries	FLOAT NULL,
	Reimbursements	FLOAT NULL,
	TreasuryAccountCode	NVARCHAR(80) NULL,
	TreasuryAccountName NVARCHAR(MAX) NULL,
	BudgetAccountCode	NVARCHAR(80) NULL,
	BudgetAccountName NVARCHAR(MAX) NULL
);