CREATE TABLE AppropriationLevelAuthority  
(
	 AppropriationLevelAuthorityId INT NOT NULL IDENTITY(1,1),
	 BFY NVARCHAR(80) NULL, 
	 EFY NVARCHAR(80) NULL, 
	 FundCode NVARCHAR(80) NULL,
	 FundName NVARCHAR(80) NULL, 
	 BudgetAccountCode NVARCHAR(80) NULL, 
	 BudgetAccountName NVARCHAR(80) NULL, 
	 TreasuryAccountCode NVARCHAR(80) NULL, 
	 TreasuryAccountName NVARCHAR(80) NULL, 
	 Budgeted FLOAT NULL,
	 CarryOver FLOAT NULL,
	 TotalReimbursements FLOAT NULL,
	 TotalRecoveries FLOAT NULL,
	 TotalAuthority FLOAT NULL
);