SELECT Allocations.PrcId AS PrcId, Allocations.BFY AS BFY, Allocations.AhCode AS AhCode,  
    Allocations.FundCode AS FundCode, Allocations.FundName AS FundName,
    Allocations.BocCode AS BocCode, Allocations.BocName as BocName, 
    Allocations.OrgCode AS OrgCode, Allocations.AccountCode AS AccountCode,     
    Allocations.ProgramProjectCode AS ProgramProjectCode,      
    Allocations.ProgramProjectName AS ProgramProjectName, 
    Allocations.BudgetLevel AS BudgetLevel,  
    Allocations.RcCode AS RcCode, 
    Allocations.AllocationRatio as AllocationRatio,
    CCur(nz(Allocations.Amount, 0)) AS Amount
FROM Allocations 
WHERE Allocations.BocCode NOT IN ('10', '17') AND 
    Allocations.Amount > 0 AND
    Allocations.BudgetLevel = '7'
UNION SELECT Allocations.PrcId AS PrcId, Allocations.BFY AS BFY, Allocations.AhCode AS AhCode, 
    Allocations.FundCode AS FundCode, Allocations.FundName AS FundName, 
    Allocations.BocCode AS BocCode, Allocations.BocName AS BocName, 
    Allocations.OrgCode AS OrgCode,    
    Allocations.AccountCode AS AccountCode,      
    Allocations.ProgramProjectCode AS ProgramProjectCode,
    Allocations.ProgramProjectName AS ProgramProjectName, 
    Allocations.BudgetLevel AS BudgetLevel, 
    Allocations.RcCode AS RcCode, 
    Allocations.AllocationRatio as AllocationRatio,
    CCur(nz(Allocations.Amount, 0)) AS Amount
FROM Allocations
WHERE Allocations.BocCode NOT IN ('10', '17') AND
    Allocations.Amount > 0 AND
    Allocations.BudgetLevel = '8'
ORDER BY BFY DESC , FundCode, AccountCode, BocCode;
