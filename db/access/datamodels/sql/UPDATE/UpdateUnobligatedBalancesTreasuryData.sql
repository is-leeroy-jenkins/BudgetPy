UPDATE UnobligatedBalances 
INNER JOIN Funds 
ON (UnobligatedBalances.FundCode = Funds.Code) 
AND (UnobligatedBalances.EFY = Funds.EFY) 
AND (UnobligatedBalances.BFY = Funds.BFY) 
SET UnobligatedBalances.TreasuryAccountName = Funds.TreasuryAccountName, 
UnobligatedBalances.BudgetAccountCode = Funds.BudgetAccountCode, 
UnobligatedBalances.BudgetAccountName = Funds.BudgetAccountName;