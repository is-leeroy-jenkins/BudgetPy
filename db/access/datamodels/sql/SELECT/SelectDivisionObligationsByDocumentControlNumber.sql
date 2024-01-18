SELECT ExternalUpdates.PrcId,
	   ExternalUpdates.BFY,
	   ExternalUpdates.BudgetLevel,
	   ExternalUpdates.AhCode,
	   ExternalUpdates.FundName,
	   ExternalUpdates.FundCode,
	   ExternalUpdates.OrgCode,
	   ExternalUpdates.AccountCode,
	   ExternalUpdates.BocCode,
	   ExternalUpdates.RcCode,
	   ExternalUpdates.BocName,
	   ExternalUpdates.DivisionName,
	   ExternalUpdates.ProgramProjectName,
	   CCur( [ExternalUpdates].[Amount] )                                               AS R6,
	   CCur( [Allocations].[Amount] )                                                   AS BudEx,
	   CCur( 0 - Round( Nz( ExternalUpdates.Amount, 0 ) - [Allocations].[Amount], 2 ) ) AS Delta,
	   IIf( (([ExternalUpdates].[Amount] - [Allocations].[Amount] > -1)
		   AND ([ExternalUpdates].[Amount] - [Allocations].[Amount] < 1)), "ZERO",
			IIf( [ExternalUpdates].[Amount] - [Allocations].[Amount] > 1, "DECREASE",
				 "INCREASE" ) )                                                         AS NET
FROM ExternalUpdates
		 LEFT JOIN Allocations ON (ExternalUpdates.RcCode = Allocations.RcCode) AND
								  (ExternalUpdates.OrgCode = Allocations.OrgCode) AND
								  (ExternalUpdates.FundCode = Allocations.FundCode) AND
								  (ExternalUpdates.AhCode = Allocations.AhCode) AND
								  (ExternalUpdates.BudgetLevel = Allocations.BudgetLevel) AND
								  (ExternalUpdates.BFY = Allocations.BFY)
WHERE (((ExternalUpdates.BFY) = [Allocations].[BFY])
	AND ((ExternalUpdates.BudgetLevel) = [Allocations].[BudgetLevel])
	AND ((ExternalUpdates.AhCode) = [Allocations].[AhCode])
	AND ((ExternalUpdates.FundCode) = [Allocations].[FundCode])
	AND ((ExternalUpdates.OrgCode) = [Allocations].[OrgCode])
	AND ((ExternalUpdates.AccountCode) = [Allocations].[AccountCode])
	AND ((ExternalUpdates.BocCode) = [Allocations].[BocCode])
	AND ((ExternalUpdates.RcCode) = [Allocations].[RcCode])
	AND ((ExternalUpdates.Amount) <> [Allocations].[Amount]));