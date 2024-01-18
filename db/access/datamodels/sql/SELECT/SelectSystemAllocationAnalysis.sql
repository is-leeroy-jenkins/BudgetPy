SELECT Allocations.PrcId,
	   Allocations.BudgetLevel,
	   Allocations.RPIO,
	   Allocations.AhCode,
	   Allocations.BFY,
	   Allocations.FundCode,
	   Allocations.OrgCode,
	   Allocations.AccountCode,
	   Allocations.ActivityCode,
	   Allocations.BocCode,
	   Allocations.RcCode,
	   Allocations.ProgramProjectCode,
	   Allocations.ProgramProjectName,
	   CCur( Round( Sum( [Allocations].[Amount] ), 0 ) )                  AS CurrentYear,
	   CCur( Nz( DLookUp( "Amount", "Allocations",
						  "Allocations.BFY = '2020'" & " AND Allocations.AhCode= '" &
						  [Allocations].[AhCode] & "'" & " AND Allocations.OrgCode = '" &
						  [Allocations].[OrgCode] & "'" & " AND Allocations.FundCode = '" &
						  [Allocations].[FundCode] & "'" & " AND Allocations.AccountCode = '" &
						  [Allocations].[AccountCode] & "'" & " AND Allocations.BocCode = '" &
						  [Allocations].[BocCode] & "'" & " AND Allocations.RcCode = '" &
						  [Allocations].[RcCode] & "'" ),
				 0 ) )                                                    AS PriorYear,
	   CCur( Round( Sum( Allocations.Amount * 0.0102524640567065 ), 0 ) ) AS Reduction,
	   Round( Sum( Allocations.Amount * 0.0102524640567065 ) / Sum( Allocations.Amount ),
			  3 )                                                         AS Ratio,
	   CCur( Round( Sum( Allocations.Amount - (Allocations.Amount * 0.0102524640567065) ),
					0 ) )                                                 AS Budget,
	   Allocations.FundName,
	   Allocations.BocName,
	   Allocations.NpmCode,
	   Allocations.NpmName,
	   Allocations.Division,
	   Allocations.DivisionName
FROM Allocations
WHERE (((Allocations.BudgetLevel) = '8') AND ((Allocations.BocCode) In ( '36', '37' )) AND
	   ((Allocations.RcCode) Not In ( '06G', '06N' )) AND
	   ((Allocations.FundCode) Not ALike "E%" And (Allocations.FundCode) Not ALike "TR%") AND
	   ((Allocations.BFY) = '2021'))
GROUP BY Allocations.PrcId, Allocations.BudgetLevel, Allocations.RPIO, Allocations.AhCode,
		 Allocations.BFY, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode,
		 Allocations.ActivityCode, Allocations.BocCode, Allocations.RcCode,
		 Allocations.ProgramProjectCode, Allocations.ProgramProjectName, Allocations.DivisionName,
		 Allocations.FundName, Allocations.BocName, Allocations.NpmCode, Allocations.NpmName,
		 Allocations.Division, Allocations.Amount
HAVING (((Allocations.Amount) > 0))
   AND Allocations.RcCode = '06L'
ORDER BY Allocations.DivisionName, Allocations.FundCode, Allocations.AccountCode,
		 Allocations.BocCode;