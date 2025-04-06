PARAMETERS BudgetLevelArgs Text ( 255 ), RpioArgs Text ( 255 ), AhCodeArgs Text ( 255 ), FiscalYearArgs Text ( 255 ), FundCodeArgs Text ( 255 ), OrgCodeArgs Text ( 255 ), AccountCodeArgs Text ( 255 ), 
BocCodeArgs Text ( 255 ), RcCodeArgs Text ( 255 ), AmountArgs IEEEDouble;
INSERT INTO Allocations (RPIO, BudgetLevel, AhCode, BFY, FundCode, OrgCode, AccountCode,
						 ActivityCode, BocCode, RcCode, Amount, FundName, BocName, Division,
						 NpmCode, ProgramProjectCode, GoalCode, ObjectiveCode, DivisionName,
						 NpmName, ProgramProjectName, ProgramAreaCode, ProgramAreaName, GoalName,
						 ObjectiveName, AllocationRatio)
SELECT Allocations.RPIO,
	   Allocations.BudgetLevel,
	   Allocations.AhCode,
	   Allocations.BFY,
	   DLookUp( "Code", "Funds", "Funds.Code=[FundCodeArgs]" ) AS FundCode,
	   Allocations.OrgCode,
	   DLookUp( "Code", "Accounts",
				"Accounts.Code=[AccountCodeArgs]" )            AS AccountCode,
	   Nz( IIf( Len( [AccountCodeArgs] ) > 7, Right( [AccountCodeArgs], 2 ),
				"NS" ) )                                       AS ActivityCode,
	   Allocations.BocCode,
	   Allocations.RcCode,
	   Allocations.Amount,
	   Nz( DLookUp( "Name", "Funds", "Funds.Code=[FundCodeArgs]" ),
		   "NS" )                                              AS FundName,
	   Nz( DLookUp( "BocName", "Allocations", "Allocations.BocCode=[BocCodeArgs]" ),
		   "NS" )                                              AS BocName,
	   Nz( DLookUp( "Division", "Allocations", "Allocations.RcCode=[RcCodeArgs]" ),
		   "NS" )                                              AS Division,
	   Nz( Mid( [AccountCodeArgs], 3, 1 ), "NS" )              AS NpmCode,
	   Nz( Mid( [AccountCodeArgs], 4, 2 ), "NS" )              AS ProgramProjectCode,
	   Nz( Left( [AccountCodeArgs], 1 ), "NS" )                AS GoalCode,
	   Nz( DLookUp( "Code", "Objective", "Objective.Code = Mid([AccountCodeArgs],1,2)" ),
		   "NS" )                                              AS ObjectiveCode,
	   Nz( DLookUp( "DivisionName", "Allocations", "Allocations.RcCode=[RcCodeArgs]" ),
		   "NS" )                                              AS DivisionName,
	   Nz( DLookUp( "Name", "NationalPrograms",
					"NationalPrograms.Code=MID([AccountCodeArgs], 3, 1)" ),
		   "NS" )                                              AS NpmName,
	   Nz( DLookUp( "Name", "ProgramProjects", "ProgramProjects.Code=MID([AccountCodeArgs],4,2)" ),
		   "NS" )                                              AS ProgramProjectName,
	   Nz( DLookUp( "ProgramAreaCode", "ProgramProjects",
					"ProgramProjects.Code=MID([AccountCodeArgs],4,2)" ),
		   "NS" )                                              AS ProgramAreaCode,
	   Nz( DLookUp( "ProgramAreaName", "ProgramProjects",
					"ProgramProjects.Code=MID([AccountCodeArgs],4,2)" ),
		   "NS" )                                              AS ProgramAreaName,
	   Nz( DLookUp( "GoalName", "Allocations", "Allocations.GoalCode=[GoalCodeArgs]" ),
		   "NS" )                                              AS GoalName,
	   Nz( DLookUp( "ObjectiveName", "Allocations",
					"Allocations.ObjectiveCode=[ObjectiveCodeArgs]" ),
		   "NS" )                                              AS ObjectiveName,
	   Nz( Switch( [BudgetLevelArgs] = '7', 1, [BudgetLevelArgs] = '8', 0 ),
		   0 )                                                 AS AllocationRatio
FROM (((Allocations
	INNER JOIN (Divisions
		INNER JOIN (ProgramProjects
			INNER JOIN Accounts
					ON ProgramProjects.Code = Accounts.ProgramProjectCode)
				ON Divisions.Code = ProgramProjects.Code)
		ON (Allocations.ProgramAreaCode = ProgramProjects.ProgramAreaCode)
			AND (Allocations.ProgramProjectCode = ProgramProjects.Code)
			AND (Allocations.RcCode = Divisions.Code))
	INNER JOIN Objective
	   ON Accounts.Code = Objective.Code)
	INNER JOIN NationalPrograms
	  ON (Allocations.NpmCode = NationalPrograms.Code)
		  AND (ProgramProjects.Code = NationalPrograms.Code))
		 INNER JOIN Funds
					ON Allocations.FundCode = Funds.Code
WHERE (((Allocations.RpioArgs) = '06')
	AND ((Allocations.BudgetLevel) = [BudgetLevelArgs])
	AND ((Allocations.AhCode) = [AhCodeArgs])
	AND ((Allocations.BFY) = [FiscalYearArgs])
	AND ((DLookUp( "Code", "Funds", "Funds.Code=[FundCodeArgs]" )) = [FundCodeArgs])
	AND ((Allocations.OrgCode) = [OrgCodeArgs])
	AND ((DLookUp( "Code", "Accounts", "Accounts.Code=[AccountCodeArgs]" )) = [AccountCodeArgs])
	AND ((Allocations.BocCode) = [BocCodeArgs])
	AND ((Allocations.RcCode) = [RcCodeArgs])
	AND ((Allocations.Amount) = [AmountArgs]));

