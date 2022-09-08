INSERT INTO OplanAllocations
SELECT OperatingPlan.BudgetLevel AS BudgetLevel, OperatingPlan.BFY AS BFY, OperatingPlan.AhCode AS AhCode, OperatingPlan.FundCode AS FundCode, 
IIF(OperatingPlan.BocCode = 10, Left(OperatingPlan.OrgCode, 2), OperatingPlan.OrgCode) AS OrgCode, 
OperatingPlan.BocCode AS BocCode, 
REPLACE(OperatingPlan.AccountCode, LEFT(OperatingPlan.AccountCode, 3), 000) AS AccountCode, 
IIF(OperatingPlan.BocCode = 10, Left(OperatingPlan.RcCode, 2), OperatingPlan.RcCode) AS RcCode, 
SUM(OperatingPlan.Amount) AS Amount
FROM OperatingPlan
WHERE OperatingPlan.BudgetLevel = 7
GROUP BY OperatingPlan.BudgetLevel, OperatingPlan.BFY, OperatingPlan.AhCode, OperatingPlan.FundCode, IIF(OperatingPlan.BocCode = 10, Left(OperatingPlan.OrgCode, 2), OperatingPlan.OrgCode), 
REPLACE(OperatingPlan.AccountCode, LEFT(OperatingPlan.AccountCode, 3), 000), 
IIF(OperatingPlan.BocCode = 10, Left(OperatingPlan.RcCode, 2), OperatingPlan.RcCode), OperatingPlan.BocCode
ORDER BY OperatingPlan.BFY DESC , OperatingPlan.FundCode, OperatingPlan.BocCode;
