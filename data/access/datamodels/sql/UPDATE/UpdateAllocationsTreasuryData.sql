UPDATE Allocations 
INNER JOIN Funds 
ON (Allocations.BFY = Funds.BFY) 
AND (Allocations.EFY = Funds.EFY) 
AND (Allocations.FundCode = Funds.Code) 
SET Allocations.TreasuryAccountCode = Funds.TreasuryAccountCode,
Allocations.TreasuryAccountName = Funds.TreasuryAccountName, 
Allocations.BudgetAccountCode = Funds.BudgetAccountCode, 
Allocations.BudgetAccountName = Funds.BudgetAccountName;