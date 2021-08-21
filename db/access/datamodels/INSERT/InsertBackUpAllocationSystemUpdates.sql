INSERT INTO Allocations
SELECT *
FROM (SELECT BackUp.RPIO AS RPIO, BackUp.BudgetLevel AS BudgetLevel, BackUp.AhCode AS AhCode, BackUp.BFY AS BFY, BackUp.FundCode AS FundCode, BackUp.OrgCode AS OrgCode, BackUp.AccountCode AS AccountCode,
BackUp.BocCode AS BocCode, BackUp.RcCode AS RcCode, BackUp.Amount AS Amount, 
BackUp.FundName AS FundName, BackUp.BocName AS BocName, BackUp.Division AS Division, BackUp.DivisionName AS DivisionName, BackUp.ActivityCode AS ActivityCode, BackUp.NpmCode AS NpmCode, BackUp.NpmName AS NpmName, BackUp.ProgramProjectCode AS ProgramProjectCode, BackUp.ProgramProjectName AS ProgramProjectName, BackUp.ProgramAreaCode AS ProgramAreaCode, BackUp.ProgramAreaName AS ProgramAreaName, BackUp.GoalCode AS GoalCode, BackUp.GoalName AS GoalName, BackUp.ObjectiveCode AS ObjectiveCode, BackUp.ObjectiveName AS ObjectiveName, 1 AS AllocationRatio
FROM BackUp
WHERE BackUp.BudgetLevel = '8'
OR Backup.BocCode = '17' 
UNION 
SELECT SystemUpdates.RPIO AS RPIO, SystemUpdates.BudgetLevel AS BudgetLevel, SystemUpdates.AhCode AS AhCode, SystemUpdates.BFY AS BFY, SystemUpdates.FundCode AS FundCode, SystemUpdates.OrgCode AS OrgCode, SystemUpdates.AccountCode AS AccountCode, 
SystemUpdates.BocCode AS BocCode, SystemUpdates.RcCode AS RcCode, SystemUpdates.Amount AS Amount,  SystemUpdates.FundName AS FundName, SystemUpdates.BocName AS BocName, SystemUpdates.Division AS Division, SystemUpdates.DivisionName AS DivisionName, SystemUpdates.ActivityCode AS ActivityCode, SystemUpdates.NpmCode AS NpmCode, SystemUpdates.NpmName AS NpmName, 
SystemUpdates.ProgramProjectCode AS ProgramProjectCode, SystemUpdates.ProgramProjectName AS ProgramProjectName, SystemUpdates.ProgramAreaCode AS ProgramAreaCode, 
SystemUpdates.ProgramAreaName AS ProgramAreaName, SystemUpdates.GoalCode AS GoalCode, SystemUpdates.GoalName AS GoalName, SystemUpdates.ObjectiveCode AS ObjectiveCode, SystemUpdates.ObjectiveName AS ObjectiveName, 1 AS AllocationRatio
FROM SystemUpdates
WHERE SystemUpdates.BudgetLevel = '7'
ORDER BY BFY DESC , FundCode, AccountCode, BocCode, BudgetLevel)  AS [%$##@_Alias];