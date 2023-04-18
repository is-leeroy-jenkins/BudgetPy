UPDATE AppropriationLevelAuthority 
INNER JOIN Funds 
ON (AppropriationLevelAuthority.FiscalYear = Funds.EFY) 
AND (AppropriationLevelAuthority.FiscalYear = Funds.BFY) 
AND (AppropriationLevelAuthority.FundCode = Funds.Code) 
SET AppropriationLevelAuthority.FundName = Funds.Name, 
AppropriationLevelAuthority.BudgetAccountCode = Funds.BudgetAccountCode, 
.BudgetAccountName = Funds.BudgetAccountName;