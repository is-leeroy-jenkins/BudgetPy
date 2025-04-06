SELECT Allocations.PrcId                  AS PrcId,
	   Allocations.BFY                    AS BFY,
	   Allocations.AhCode                 AS AhCode,
	   Allocations.FundCode               AS FundCode,
	   Allocations.FundName,
	   Allocations.BocCode                AS BocCode,
	   Allocations.BocName                AS BocName,
	   Allocations.OrgCode                AS OrgCode,
	   Allocations.AccountCode            AS AccountCode,
	   Allocations.ActivityCode           AS ActivityCode,
	   Allocations.BudgetLevel            AS BudgetLevel,
	   Allocations.RcCode                 AS RcCode,
	   Allocations.ProgramProjectName     AS ProgramProjectName,
	   SWITCH( Allocations.BudgetLevel = '7', Allocations.Amount, Allocations.BudgetLevel = '8',
			   (0 - Allocations.Amount) ) AS Amount
FROM Allocations
WHERE Allocations.BudgetLevel = '7'
  AND Allocations.BocCode NOT IN ( '10', '17' )
UNION
SELECT Allocations.PrcId              AS PrcId,
	   Allocations.BFY                AS BFY,
	   Allocations.AhCode             AS AhCode,
	   Allocations.FundCode           AS FundCode,
	   Allocations.FundName,
	   Allocations.BocCode            AS BocCode,
	   Allocations.BocName            AS BocName,
	   Allocations.OrgCode            AS OrgCode,
	   Allocations.AccountCode        AS AccountCode,
	   Allocations.ActivityCode       AS ActivityCode,
	   Allocations.BudgetLevel        AS BudgetLevel,
	   Allocations.RcCode             AS RcCode,
	   Allocations.ProgramProjectName AS ProgramProjectName,
	   Allocations.Amount             AS Amount
FROM Allocations
WHERE Allocations.BudgetLevel = '8'
  AND Allocations.BocCode NOT IN ( '10', '17' )
ORDER BY BFY DESC, FundCode, AccountCode, BocCode;