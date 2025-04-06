SELECT Allocations.PrcId              AS PrcId,
	   Allocations.BFY                AS BFY,
	   Allocations.AhCode             AS AhCode,
	   Allocations.FundCode           AS FundCode,
	   Allocations.FundName,
	   Allocations.BocCode            AS BocCode,
	   Allocations.BocName            AS BocName,
	   Allocations.OrgCode            AS OrgCode,
	   Allocations.NpmCode,
	   Allocations.AccountCode        AS AccountCode,
	   Allocations.ActivityCode       AS ActivityCode,
	   Allocations.BudgetLevel        AS BudgetLevel,
	   Allocations.RcCode             AS RcCode,
	   Allocations.ProgramProjectCode AS ProgramProjectCode,
	   Allocations.ProgramProjectName AS ProgramProjectName,
	   Allocations.Amount             AS Amount
FROM Allocations
WHERE Allocations.BocCode IN ( '36', '37', '38', '41' )
  AND BudgetLevel = '7'
UNION
SELECT Allocations.PrcId              AS PrcId,
	   Allocations.BFY                AS BFY,
	   Allocations.AhCode             AS AhCode,
	   Allocations.FundCode           AS FundCode,
	   Allocations.FundName,
	   Allocations.BocCode            AS BocCode,
	   Allocations.BocName            AS BocName,
	   Allocations.OrgCode            AS OrgCode,
	   Allocations.NpmCode,
	   Allocations.AccountCode        AS AccountCode,
	   Allocations.ActivityCode       AS ActivityCode,
	   Allocations.BudgetLevel        AS BudgetLevel,
	   Allocations.RcCode             AS RcCode,
	   Allocations.ProgramProjectCode AS ProgramProjectCode,
	   Allocations.ProgramProjectName AS ProgramProjectName,
	   Allocations.Amount             AS Amount
FROM Allocations
WHERE Allocations.BocCode IN ( '36', '37', '38', '41' )
  AND BudgetLevel = '8'
ORDER BY BFY DESC, FundCode, AccountCode, BocCode;
