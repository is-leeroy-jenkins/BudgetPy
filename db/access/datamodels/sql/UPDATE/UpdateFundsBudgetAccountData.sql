UPDATE Obligations 
INNER JOIN Funds 
ON (Funds.Code = Obligations.FundCode) 
AND (Funds.BFY = Obligations.BFY) 
AND (Funds.EFY = Obligations.EFY) 
SET Obligations.TreasurySymbol = Funds.TreasuryAccountCode, 
Obligations.BudgetAccountCode = Funds.BudgetAccountCode, 
Obligations.BudgetAccountName = Funds.BudgetAccountName
WHERE Funds.Code = Obligations.FundCode 
AND Funds.BFY = Obligations.BFY
AND Funds.EFY = Obligations.EFY;