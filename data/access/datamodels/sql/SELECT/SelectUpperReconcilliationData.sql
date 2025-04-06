SELECT DISTINCTROW Allocation.PrcId, Allocations.BFY,
	   Allocations.BudgetLevel,
	   Allocations.AhCode,
	   Allocations.FundName,
	   Allocations.FundCode,
	   Allocations.OrgCode,
	   Allocations.AccountCode,
	   Allocations.BocCode,
	   Allocations.BocName,
	   Allocations.ProgramProjectName,
	   Allocations.RcCode,
	   Allocations.DivisionName,
	   CCur( (Round( Allocations.Amount, 2 )) )          AS Budget,
	   CCur( (Round( ExternalUpdates.Amount, 2 )) )      AS System,
	   CCur( (0 - Round( Nz( [Allocations].[Amount], 2 ) - Round( ExternalUpdates.Amount, 2 ),
						 2 )) )                          AS Delta,
	   IIf( [Delta] < -1, "DECREASE",
			IIf( [Delta] > 1, "INCREASE", "NET ZERO" ) ) AS NET
FROM Allocations
		 LEFT JOIN ExternalUpdates
				   ON (Allocations.RcCode = ExternalUpdates.RcCode)
					   AND (Allocations.AccountCode = ExternalUpdates.AccountCode)
					   AND (Allocations.OrgCode = ExternalUpdates.OrgCode)
					   AND (Allocations.BudgetLevel = ExternalUpdates.BudgetLevel)
					   AND (Allocations.FundCode = ExternalUpdates.FundCode)
					   AND (Allocations.AhCode = ExternalUpdates.AhCode)
					   AND (Allocations.BFY = ExternalUpdates.BFY)
WHERE (((Allocations.BFY) = [ExternalUpdates].[BFY])
	AND ((Allocations.BudgetLevel) = [ExternalUpdates].[BudgetLevel])
	AND ((Allocations.AhCode) = [ExternalUpdates].[AhCode])
	AND ((Allocations.FundCode) = [ExternalUpdates].[FundCode])
	AND ((Allocations.OrgCode) = [ExternalUpdates].[OrgCode])
	AND ((Allocations.AccountCode) = [ExternalUpdates].[AccountCode])
	AND ((Allocations.BocCode) = [ExternalUpdates].[BocCode]
		AND (Allocations.BocCode) In ( '10', '21', '28', '36', '37', '38', '41' ))
	AND ((Allocations.RcCode) = [ExternalUpdates].[RcCode])
	AND ((ExternalUpdates.BudgetLevel) = '7')
	AND ((Allocations.Amount) <> [ExternalUpdates].[Amount]))
GROUP BY Allocations.PrcId, Allocations.BFY, Allocations.BudgetLevel, Allocations.AhCode,
		 Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode,
		 Allocations.BocCode, Allocations.BocName, Allocations.ProgramProjectName,
		 Allocations.RcCode, Allocations.DivisionName, CCur( (Round( Allocations.Amount, 2 )) ),
		 CCur( (Round( ExternalUpdates.Amount, 2 )) ),
		 CCur( (0 - Round(
					 Nz( [Allocations].[Amount], 2 ) - Round( ExternalUpdates.Amount, 2 ), 2 )) ),
		 IIf( (0 -
			   Round( Nz( [Allocations].[Amount], 2 ) - Round( ExternalUpdates.Amount, 2 ), 2 )) <
			  0, "DECREASE",
			  IIf( (0 - Round( Nz( [Allocations].[Amount], 2 ) - Round( ExternalUpdates.Amount, 2 ),
							   2 )) > 0, "INCREASE",
				   "NET ZERO" ) )
ORDER BY Allocations.BFY DESC, Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;
