UPDATE Allocations 
INNER JOIN OperatingPlans 
ON (Allocations.RcCode = OperatingPlans.RcCode) 
AND (Allocations.BocCode = OperatingPlans.BocCode) 
AND (Allocations.OrgCode = OperatingPlans.OrgCode) 
AND (Allocations.AccountCode = OperatingPlans.AccountCode) 
AND (Allocations.FundCode = OperatingPlans.FundCode) 
AND (Allocations.AhCode = OperatingPlans.AhCode) 
AND (Allocations.BudgetLevel = OperatingPlans.BudgetLevel) 
AND (Allocations.BFY = OperatingPlans.BFY) 
SET Allocations.Amount = OperatingPlans.Amount
WHERE (((Allocations.Amount) <> OperatingPlans.Amount));
