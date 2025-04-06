SELECT DISTINCTROW Allocations.BFY, Allocations.AhCode, Allocations.FundCode, Allocations.OrgCode, 
Allocations.AccountCode, Allocations.ActivityCode, Allocations.BocCode, 
CCur(Allocations.Amount) As Budget, 
CCur(OperatingPlanUpdates.Amount) As Opplan, 
CCur(ROUND(Allocations.Amount - OperatingPlanUpdates.Amount, 2)) AS Delta
FROM Allocations 
INNER JOIN 
OperatingPlanUpdates 
ON Allocations.BFY = OperatingPlanUpdates.BFY 
AND Allocations.BudgetLevel = OperatingPlanUpdates.BudgetLevel 
AND Allocations.AhCode = OperatingPlanUpdates.AhCode 
AND Allocations.FundCode = OperatingPlanUpdates.FundCode 
AND Allocations.AccountCode = OperatingPlanUpdates.AccountCode 
AND Allocations.OrgCode = OperatingPlanUpdates.OrgCode 
AND Allocations.BocCode = OperatingPlanUpdates.BocCode 
AND Allocations.RcCode = OperatingPlanUpdates.RcCode
WHERE Allocations.Amount <> OperatingPlanUpdates.Amount
AND Allocations.BocCode <>'17'
ORDER BY Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;