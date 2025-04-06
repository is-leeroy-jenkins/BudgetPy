INSERT INTO DivisionExecution (BudgetLevel, RPIO, BFY, AhCode, FundCode, RcCode, DivisionName,
							   FundName, OrgCode, AccountCode, ActivityCode, ProgramProjectCode,
							   ProgramProjectName, ProgramAreaCode, ProgramAreaName, BocCode,
							   BocName, Amount, OpenCommitments, Obligations, Used)
SELECT DISTINCTROW Allocations.BudgetLevel, Allocations.RPIO,
	   Allocations.BFY,
	   Allocations.AhCode,
	   Allocations.FundCode,
	   Allocations.RcCode,
	   Allocations.DivisionName,
	   Allocations.FundName,
	   Allocations.OrgCode,
	   Allocations.AccountCode,
	   Allocations.ActivityCode,
	   Allocations.ProgramProjectCode,
	   Allocations.ProgramProjectName,
	   Allocations.ProgramAreaCode,
	   Allocations.ProgramAreaName,
	   Allocations.BocCode,
	   Allocations.BocName,
	   Allocations.Amount,
	   Nz( Sum( Round( [Purchases].[OpenCommitments], 2 ) ), 0 )                 AS OpenCommitments,
	   Nz( Sum( Round( [Purchases].[Obligations], 2 ) ), 0 )                     AS Obligations,
	   Nz( Sum( [Purchases].[OpenCommitments] + [Purchases].[Obligations] ), 0 ) AS Used
FROM Allocations
		 LEFT JOIN Purchases ON (Allocations.BFY = Purchases.BFY) AND
								(Allocations.FundCode = Purchases.FundCode) AND
								(Allocations.AccountCode = Purchases.AccountCode) AND
								(Allocations.BocCode = Purchases.BocCode) AND
								(Allocations.RcCode = Purchases.RcCode)
GROUP BY Allocations.BudgetLevel, Allocations.RPIO, Allocations.BFY, Allocations.AhCode,
		 Allocations.FundCode, Allocations.RcCode, Allocations.DivisionName, Allocations.FundName,
		 Allocations.OrgCode, Allocations.AccountCode, Allocations.ActivityCode,
		 Allocations.ProgramProjectCode, Allocations.ProgramProjectName,
		 Allocations.ProgramAreaCode, Allocations.ProgramAreaName, Allocations.BocCode,
		 Allocations.BocName, Allocations.Amount
HAVING (((Allocations.BudgetLevel) = '8'))
   AND Allocations.Amount <> 0
ORDER BY Allocations.BFY DESC, Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;

