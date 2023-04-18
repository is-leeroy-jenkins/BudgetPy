CREATE VIEW "BudgetAllocationOperatingPlanAnalysis"
AS SELECT DISTINCT Allocations.BudgetLevel, Allocations.BFY, Allocations.AhCode, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.RcCode, Allocations.Amount AS Initial, OperatingPlans.Amount AS Change, 
    CASE Allocations.Amount-OperatingPlans.Amount
    WHEN Allocations.Amount-OperatingPlans.Amount < 0 THEN "DECREASE"
    WHEN Allocations.Amount-OperatingPlans.Amount > 0 THEN "INCREASE"
    ELSE "NET ZERO"
END NET,
Allocations.Amount-OperatingPlans.Amount AS Delta
FROM Allocations 
INNER JOIN OperatingPlans 
ON Allocations.BFY = OperatingPlans.BFY 
AND Allocations.BudgetLevel = OperatingPlans.BudgetLevel 
AND Allocations.AhCode = OperatingPlans.AhCode 
AND Allocations.FundCode = OperatingPlans.FundCode 
AND Allocations.OrgCode = OperatingPlans.OrgCode 
AND Allocations.BocCode = OperatingPlans.BocCode 
AND Allocations.AccountCode = OperatingPlans.AccountCode 
AND Allocations.RcCode = OperatingPlans.RcCode
WHERE Allocations.Amount <> OperatingPlans.Amount;

