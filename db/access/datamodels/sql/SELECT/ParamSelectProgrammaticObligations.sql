SELECT DISTINCTROW Allocations.PrcId, Allocations.BFY,
	   Allocations.BudgetLevel,
	   Allocations.AhCode,
	   Allocations.FundName,
	   Allocations.FundCode,
	   Allocations.OrgCode,
	   Allocations.AccountCode,
	   Allocations.BocCode,
	   Allocations.BocName,
	   Allocations.DivisionName,
	   Allocations.RcCode,
	   Allocations.ProgramProjectName,
	   CCur( Allocations.Amount )                                          AS Budget,
	   CCur( StatusOfFunds.Amount )                                        AS System,
	   CCur( StatusOfFunds.Amount - Allocations.Amount )                   AS DELTA,
	   SWITCH( StatusOfFunds.Amount - Allocations.Amount = 0, "ZERO",
			   StatusOfFunds.Amount - Allocations.Amount > 1, "INCREASE",
			   StatusOfFunds.Amount - Allocations.Amount < 1, "DECREASE" ) AS NET
FROM Allocations
		 INNER JOIN StatusOfFunds
					ON (Allocations.BocCode = StatusOfFunds.BocCode)
						AND (Allocations.AccountCode = StatusOfFunds.AccountCode)
						AND (Allocations.OrgCode = StatusOfFunds.OrgCode)
						AND (Allocations.FundCode = StatusOfFunds.FundCode)
						AND (Allocations.BudgetLevel = StatusOfFunds.BudgetLevel)
						AND (Allocations.AhCode = StatusOfFunds.AhCode)
						AND (Allocations.BFY = StatusOfFunds.BFY)
WHERE StatusOfFunds.BudgetLevel = '8'
  AND Allocations.BocCode IN ( '10', '21', '28', '36', '37', '38', '41' )
ORDER BY Allocations.BFY DESC, Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;