SELECT DISTINCTROW Allocations.PrcId, Allocations.BFY, Allocations.BudgetLevel, Allocations.AhCode, Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.BocName, Allocations.DivisionName, Allocations.RcCode, Allocations.ProgramProjectName, 
CCur(Allocations.Amount) AS Budget, 
CCur(SystemUpdates.Amount) AS System, 
CCur(SystemUpdates.Amount - Allocations.Amount) AS DELTA, 
    SWITCH(SystemUpdates.Amount - Allocations.Amount = 0, "ZERO", 
        SystemUpdates.Amount - Allocations.Amount > 0, "INCREASE", 
        SystemUpdates.Amount - Allocations.Amount < 0, "DECREASE") AS NET
FROM Allocations 
INNER JOIN SystemUpdates 
ON (Allocations.BocCode = SystemUpdates.BocCode) 
AND (Allocations.AccountCode = SystemUpdates.AccountCode) 
AND (Allocations.OrgCode = SystemUpdates.OrgCode) 
AND (Allocations.FundCode = SystemUpdates.FundCode) 
AND (Allocations.BudgetLevel = SystemUpdates.BudgetLevel) 
AND (Allocations.AhCode = SystemUpdates.AhCode) 
AND (Allocations.BFY = SystemUpdates.BFY)
WHERE SystemUpdates.BudgetLevel = '7'
AND Allocations.BocCode IN ('10', '21', '28', '36', '37', '38', '41')
ORDER BY Allocations.BFY DESC , Allocations.FundCode, 
    Allocations.AccountCode, Allocations.BocCode;