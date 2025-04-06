UPDATE StatusOfAppropriations 
INNER JOIN Funds 
ON (StatusOfAppropriations.BFY = Funds.BFY) 
AND (StatusOfAppropriations.EFY = Funds.EFY) 
AND (StatusOfAppropriations.FundCode = Funds.Code) 
SET StatusOfAppropriations.TreasuryAccountCode = Funds.TreasuryAccountCode, 
StatusOfAppropriations.TreasuryAccountName = Funds.TreasuryAccountName, 
StatusOfAppropriations.BudgetAccountCode = Funds.BudgetAccountCode, 
StatusOfAppropriations.BudgetAccountName = Funds.BudgetAccountName;