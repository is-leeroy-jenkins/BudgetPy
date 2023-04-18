UPDATE Deobligations 
INNER JOIN Funds 
ON (Funds.BFY = Deobligations.BFY) 
AND (Funds.Code = Deobligations.FundCode) 
SET Deobligations.TreasurySymbol = Funds.TreasuryAccountCode, 
Deobligations.BudgetAccountCode = Funds.BudgetAccountCode, 
Deobligations.BudgetAccountName = Funds.BudgetAccountName;