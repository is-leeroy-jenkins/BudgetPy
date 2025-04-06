INSERT INTO UpperReconcilliation
SELECT SystemUpdates.ExtId                                                        AS ExtId,
	   Allocations.PrcId                                                          AS PrcId,
	   SystemUpdates.BFY                                                          AS BFY,
	   SystemUpdates.BudgetLevel                                                  AS BudgetLevel,
	   LEFT( SystemUpdates.AhCode, 2 )                                            AS AhCode,
	   SystemUpdates.FundName                                                     AS FundName,
	   SystemUpdates.FundCode                                                     AS FundCode,
	   SystemUpdates.OrgCode                                                      AS OrgCode,
	   SystemUpdates.AccountCode                                                  AS AccountCode,
	   SystemUpdates.BocCode                                                      AS BocCode,
	   SystemUpdates.RcCode                                                       AS RcCode,
	   SystemUpdates.BocName                                                      AS BocName,
	   SystemUpdates.DivisionName                                                 AS DivisionName,
	   SystemUpdates.ProgramProjectCode                                           AS ProgramProjectCode,
	   SystemUpdates.ProgramProjectName                                           AS ProgramProjectName,
	   SystemUpdates.ProgramAreaCode                                              AS ProgramAreaCode,
	   SystemUpdates.ProgramAreaName                                              AS ProgramAreaName,
	   CCur( SystemUpdates.Amount )                                               AS System,
	   CCur( Allocations.Amount )                                                 AS Budget,
	   CCur( 0 - Round( Nz( SystemUpdates.Amount, 0 ) - Allocations.Amount, 2 ) ) AS Delta,
	   SWITCH( SystemUpdates.Amount - Allocations.Amount = 0, "ZERO",
			   SystemUpdates.Amount - Allocations.Amount > 1, "INCREASE",
			   SystemUpdates.Amount - Allocations.Amount < 1, "DECREASE" )        AS NET
FROM SystemUpdates
		 LEFT JOIN Allocations ON (SystemUpdates.RcCode = Allocations.RcCode) AND
								  (SystemUpdates.OrgCode = Allocations.OrgCode) AND
								  (SystemUpdates.FundCode = Allocations.FundCode) AND
								  (SystemUpdates.AhCode = Allocations.AhCode) AND
								  (SystemUpdates.BudgetLevel = Allocations.BudgetLevel) AND
								  (SystemUpdates.BFY = Allocations.BFY)
WHERE SystemUpdates.BFY = Allocations.BFY
  AND (SystemUpdates.BudgetLevel = '7'
	AND SystemUpdates.BudgetLevel = Allocations.BudgetLevel
	AND SystemUpdates.AhCode = Allocations.AhCode
	AND SystemUpdates.FundCode = Allocations.FundCode
	AND SystemUpdates.OrgCode = Allocations.OrgCode
	AND SystemUpdates.AccountCode = Allocations.AccountCode
	AND SystemUpdates.BocCode = Allocations.BocCode
	AND SystemUpdates.RcCode = Allocations.RcCode)
ORDER BY SystemUpdates.BFY DESC, SystemUpdates.FundCode, SystemUpdates.AccountCode,
		 SystemUpdates.BocCode;


