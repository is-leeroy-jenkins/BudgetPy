SELECT Allocations.PrcId,
	   Allocations.BudgetLevel,
	   Allocations.RPIO,
	   Allocations.AhCode,
	   Allocations.BFY,
	   Allocations.FundCode,
	   Allocations.OrgCode,
	   Allocations.AccountCode,
	   Allocations.BocCode,
	   Allocations.RcCode,
	   Allocations.ProgramProjectName,
	   Allocations.DivisionName,
	   Allocations.FundName,
	   Allocations.BocName,
	   Allocations.NpmCode,
	   Allocations.NpmName,
	   CCur( Round( Sum( [Allocations].[Amount] ), 0 ) ) AS Allocation,
	   CCur( Nz( DLookUp( "Amount", "Allocations",
						  "Allocations.BFY = '2020'" & " AND Allocations.AhCode= '" &
						  [Allocations].[AhCode] & "'" & " AND Allocations.OrgCode = '" &
						  [Allocations].[OrgCode] & "'" & " AND Allocations.FundCode = '" &
						  [Allocations].[FundCode] & "'" & " AND Allocations.AccountCode = '" &
						  [Allocations].[AccountCode] & "'" & " AND Allocations.BocCode = '" &
						  [Allocations].[BocCode] & "'" & " AND Allocations.RcCode = '" &
						  [Allocations].[RcCode] & "'", 0 ) ) AS PriorYear,
			 CCur( Sum( [Allocations].[Amount] * 0.007989 ) ) AS Reduction,
			 CCur( Sum( [Allocations].[Amount] * 0.007989 ) /
				   Sum( [Allocations].[Amount] ) ) AS Ratio,
			 CCur( Sum( [Allocations].[Amount] - ([Allocations].[Amount] * 0.007989) ) ) AS Budget
FROM Allocations
WHERE (Allocations.BudgetLevel = '8' 
AND Allocations.BocCode In ('36','37')
AND Allocations.RcCode Not In ('06G','06N')
AND Allocations.FundCode Not Like "E%" 
AND Allocations.FundCode Not Like "TR%"
AND Allocations.BFY = '2021')
GROUP BY Allocations.PrcId, Allocations.BudgetLevel, Allocations.RPIO, Allocations.AhCode,
			 Allocations.BFY, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode,
			 Allocations.BocCode, Allocations.RcCode, Allocations.ProgramProjectName,
			 Allocations.DivisionName, Allocations.FundName, Allocations.BocName,
			 Allocations.NpmCode, Allocations.NpmName, Allocations.Division, Allocations.Amount HAVING Allocations.Amount > 0 
ORDER BY Allocations.DivisionName, Allocations.FundCode, Allocations.AccountCode,
			 Allocations.BocCode;