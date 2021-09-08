UPDATE Allocations 
INNER JOIN FullTimeEquivalents 
ON (Allocations.AccountCode = FullTimeEquivalents.AccountCode) 
AND (Allocations.OrgCode = FullTimeEquivalents.OrgCode) 
AND (Allocations.AhCode = FullTimeEquivalents.AhCode) 
AND (Allocations.RcCode = FullTimeEquivalents.RcCode) 
AND (Allocations.BocCode = FullTimeEquivalents.BocCode) 
AND (Allocations.FundCode = FullTimeEquivalents.FundCode) 
AND (Allocations.BFY = FullTimeEquivalents.BFY) 
AND (Allocations.BudgetLevel = FullTimeEquivalents.BudgetLevel) 
SET Allocations.Amount = FullTimeEquivalents.Amount
WHERE (((Allocations.Amount)<> FullTimeEquivalents.Amount))
AND FullTimeEquivalents.BocCode = '17';