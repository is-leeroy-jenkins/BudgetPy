UPDATE StatusOfFunds 
INNER JOIN Funds 
ON (StatusOfFunds.FundCode = Funds.Code) 
AND (StatusOfFunds.EFY = Funds.EFY) 
AND (StatusOfFunds.BFY = Funds.BFY) 
SET StatusOfFunds.TreasuryAccountCode = Funds.TreasuryAccountCode, 
StatusOfFunds.TreasuryAccountName = Funds.TreasuryAccountName, 
StatusOfFunds.BudgetAccountCode = Funds.BudgetAccountCode, 
StatusOfFunds.BudgetAccountName = Funds.BudgetAccountName;