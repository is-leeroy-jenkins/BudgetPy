SELECT DISTINCTROW Allocations.BudgetLevel, Allocations.BFY,
	   Allocations.AhCode,
	   Allocations.FundCode,
	   Allocations.OrgCode,
	   Allocations.AccountCode,
	   Allocations.BocCode,
	   Allocations.RcCode,
	   CCur( Round( Allocations.Amount, 2 ) )                              AS Initial,
	   CCur( Round( StatusOfFunds.Amount, 2 ) )                            AS Change,
	   Switch( (Allocations.Amount - StatusOfFunds.Amount) > 1, "INCREASE",
			   (Allocations.Amount - StatusOfFunds.Amount) < -1, "DECREASE",
			   (Allocations.Amount - StatusOfFunds.Amount) <= 1 AND
			   (Allocations.Amount - StatusOfFunds.Amount) >= -1, "ZERO" ) AS NET,
	   Round( Abs( Allocations.Amount - StatusOfFunds.Amount ), 2 )        AS Delta
FROM Allocations
		 INNER JOIN StatusOfFunds
					ON (Allocations.BFY = StatusOfFunds.BFY)
						AND (Allocations.BudgetLevel = StatusOfFunds.BudgetLevel)
						AND (Allocations.AhCode = StatusOfFunds.AhCode)
						AND (Allocations.FundCode = StatusOfFunds.FundCode)
						AND (Allocations.OrgCode = StatusOfFunds.OrgCode)
						AND (Allocations.BocCode = StatusOfFunds.BocCode)
						AND (Allocations.AccountCode = StatusOfFunds.AccountCode)
						AND (Allocations.RcCode = StatusOfFunds.RcCode)
WHERE (((Allocations.Amount) <> [StatusOfFunds].[Amount]))
ORDER BY Allocations.BFY DESC, Allocations.FundName,
		 Allocations.AccountCode, Allocations.BocCode;
