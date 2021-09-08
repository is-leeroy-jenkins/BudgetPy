SELECT Allocations.PrcId, Allocations.BFY, allocations.RPIO, Allocations.AhCode, Allocations.FundCode, Allocations.FundName, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.BocName, 
Allocations.ActivityCode , Allocations.BudgetLevel, Allocations.RcCode, Allocations.ProgramProjectName,      
CCur(Allocations.Amount) AS Amount
FROM Allocations 
WHERE Allocations.BocCode NOT IN ('10', '17')
    AND Allocations.BudgetLevel = '7'
UNION SELECT Allocations.PrcId, Allocations.BFY, allocations.RPIO, Allocations.AhCode, Allocations.FundCode, Allocations.FundName, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.BocName, 
Allocations.ActivityCode , Allocations.BudgetLevel, Allocations.RcCode, Allocations.ProgramProjectName,      
CCur(Allocations.Amount) AS Amount
FROM Allocations
WHERE Allocations.BocCode NOT IN ('10', '17')
AND Allocations.BudgetLevel = '8'
ORDER BY Allocations.BFY DESC , Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;
