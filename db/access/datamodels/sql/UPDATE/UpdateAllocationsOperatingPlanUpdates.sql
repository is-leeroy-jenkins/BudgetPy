UPDATE Allocations 
INNER JOIN OperatingPlanUpdates 
ON (Allocations.BFY = OperatingPlanUpdates.BFY 
AND Allocations.BudgetLevel = OperatingPlanUpdates.BudgetLevel 
AND Allocations.AhCode = OperatingPlanUpdates.AhCode 
AND Allocations.FundCode = OperatingPlanUpdates.FundCode 
AND Allocations.AccountCode = OperatingPlanUpdates.AccountCode 
AND Allocations.OrgCode = OperatingPlanUpdates.OrgCode 
AND Allocations.BocCode = OperatingPlanUpdates.BocCode 
AND Allocations.RcCode = OperatingPlanUpdates.RcCode) 
SET Allocations.Amount = OperatingPlanUpdates.Amount
WHERE Allocations.Amount <> OperatingPlanUpdates.Amount;