CREATE VIEW "BudgetLevelReconciliation"
AS SELECT Allocations.PrcId AS PrcId, Allocations.BFY AS BFY, Allocations.AhCode AS AhCode,     
Allocations.FundCode AS FundCode, Allocations.BocCode AS BocCode, 
Allocations.OrgCode AS OrgCode, Allocations.AccountCode AS AccountCode, Allocations.BudgetLevel AS BudgetLevel,  Allocations.RcCode AS RcCode, 
Allocations.Amount AS Amount 
FROM Allocations 
WHERE Allocations.BocCode NOT IN ('10', '17') 
AND BudgetLevel = '7'
UNION SELECT Allocations.PrcId AS PrcId, Allocations.BFY AS BFY, Allocations.AhCode AS AhCode, Allocations.FundCode AS FundCode, Allocations.BocCode AS BocCode, Allocations.OrgCode AS OrgCode,    Allocations.AccountCode AS AccountCode, Allocations.BudgetLevel AS BudgetLevel, Allocations.RcCode AS RcCode, Allocations.Amount AS Amount
FROM Allocations
WHERE Allocations.BocCode NOT IN ('10', '17')
AND BudgetLevel = '8'
ORDER BY BFY DESC , FundCode, AccountCode, BocCode;
