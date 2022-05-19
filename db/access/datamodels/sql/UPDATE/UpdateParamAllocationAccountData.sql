UPDATE Allocations 
INNER JOIN StatusOfFunds 
ON (Allocations.RcCode = StatusOfFunds.RcCode) 
AND (Allocations.AccountCode = StatusOfFunds.AccountCode) 
AND (Allocations.BocCode = StatusOfFunds.BocCode) 
AND (Allocations.OrgCode = StatusOfFunds.OrgCode) 
AND (Allocations.FundCode = StatusOfFunds.FundCode) 
AND (Allocations.AhCode = StatusOfFunds.AhCode) 
AND (Allocations.BudgetLevel = StatusOfFunds.BudgetLevel) 
AND (Allocations.BFY = StatusOfFunds.BFY) SET Allocations.Amount = StatusOfFunds.Amount
WHERE ABS(((Allocations.Amount)-[StatusOfFunds].[Amount])) > 1
AND ((Allocations.Amount)<>[StatusOfFunds].[Amount])
AND ((StatusOfFunds.BudgetLevel)='7') 
AND Allocations.BocCode <> '17';
