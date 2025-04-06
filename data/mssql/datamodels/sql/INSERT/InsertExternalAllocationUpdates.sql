PARAMETERS pBudgetLevel Text ( 255 ), pRPIO Text ( 255 ), pAhCode Text ( 255 ), pBFY Text ( 255 ), pFundCode Text ( 255 ), pOrgCode Text ( 255 ), pAccountCode Text ( 255 ), pBocCode Text ( 255 ), pRcCode Text ( 255 ), pAmount IEEEDouble;
INSERT INTO Allocations (RPIO, BudgetLevel, AhCode, BFY, FundCode, OrgCode, AccountCode,
						 ActivityCode, BocCode, RcCode, Amount, FundName, BocName, Division,
						 NpmCode, ProgramProjectCode, GoalCode, ObjectiveCode, DivisionName,
						 NpmName, ProgramProjectName, ProgramAreaCode, ProgramAreaName, GoalName,
						 ObjectiveName, AllocationRatio)
SELECT Allocations.RPIO,
	   Allocations.BudgetLevel,
	   Allocations.AhCode,
	   Allocations.BFY,
	   DLookUp( "Code", "Funds", "Funds.Code=[pFundCode]" ) AS FundCode,
	   Allocations.OrgCode,
	   DLookUp( "Code", "Accounts",
				"Accounts.Code=[pAccountCode]" )            AS AccountCode,
	   Nz( IIf( Len( [AccountCode] ) > 7, Right( [AccountCode], 2 ),
				"NS" ) )                                    AS ActivityCode,
	   Allocations.BocCode,
	   Allocations.RcCode,
	   Allocations.Amount,
	   Nz( DLookUp( "Name", "Funds", "Funds.Code=[pFundCode]" ),
		   "NS" )                                           AS FundName,
	   Nz( DLookUp( "BocName", "Allocations", "Allocations.BocCode=[pBocCode]" ),
		   "NS" )                                           AS BocName,
	   Nz( DLookUp( "Division", "Allocations", "Allocations.RcCode=[pRcCode]" ),
		   "NS" )                                           AS Division,
	   Nz( Mid( [pAccountCode], 3, 1 ), "NS" )              AS NpmCode,
	   Nz( Mid( [pAccountCode], 4, 2 ), "NS" )              AS ProgramProjectCode,
	   Nz( Left( [pAccountCode], 1 ), "NS" )                AS GoalCode,
	   Nz( DLookUp( "Code", "Objective", "Objective.Code = Mid([pAccountCode],1,2)" ),
		   "NS" )                                           AS ObjectiveCode,
	   Nz( DLookUp( "DivisionName", "Allocations", "Allocations.RcCode=[pRcCode]" ),
		   "NS" )                                           AS DivisionName,
	   Nz( DLookUp( "Name", "NationalPrograms", "NationalPrograms.Code=MID([AccountCode], 3, 1)" ),
		   "NS" )                                           AS NpmName,
	   Nz( DLookUp( "Name", "ProgramProjects", "ProgramProjects.Code=MID([AccountCode],4,2)" ),
		   "NS" )                                           AS ProgramProjectName,
	   Nz( DLookUp( "ProgramAreaCode", "ProgramProjects",
					"ProgramProjects.Code=MID([AccountCode],4,2)" ),
		   "NS" )                                           AS ProgramAreaCode,
	   Nz( DLookUp( "ProgramAreaName", "ProgramProjects",
					"ProgramProjects.Code=MID([AccountCode],4,2)" ),
		   "NS" )                                           AS ProgramAreaName,
	   Nz( DLookUp( "GoalName", "Allocations", "Allocations.GoalCode=[GoalCode]" ),
		   "NS" )                                           AS GoalName,
	   Nz( DLookUp( "ObjectiveName", "Allocations", "Allocations.ObjectiveCode=[ObjectiveCode]" ),
		   "NS" )                                           AS ObjectiveName,
	   Nz( Switch( [BudgetLevel] = '7', 1, [BudgetLevel] = '8', 0 ),
		   0 )                                              AS AllocationRatio
FROM (((Allocations INNER JOIN (Divisions INNER JOIN (ProgramProjects INNER JOIN Accounts
													  ON ProgramProjects.Code = Accounts.ProgramProjectCode)
								ON Divisions.Code = ProgramProjects.Code)
		ON (Allocations.ProgramAreaCode = ProgramProjects.ProgramAreaCode) AND
		   (Allocations.ProgramProjectCode = ProgramProjects.Code) AND
		   (Allocations.RcCode = Divisions.Code)) INNER JOIN Objective
	   ON Accounts.Code = Objective.Code) INNER JOIN NationalPrograms
	  ON (Allocations.NpmCode = NationalPrograms.Code) AND
		 (ProgramProjects.Code = NationalPrograms.Code))
		 INNER JOIN Funds ON Allocations.FundCode = Funds.Code
WHERE (((Allocations.RPIO) = "06")
	AND ((Allocations.BudgetLevel) = [pBudgetLevel])
	AND ((Allocations.AhCode) = [pAhCode])
	AND ((Allocations.BFY) = [pBFY])
	AND ((DLookUp( "Code", "Funds", "Funds.Code=[pFundCode]" )) = [pFundCode])
	AND ((Allocations.OrgCode) = [pOrgCode])
	AND ((DLookUp( "Code", "Accounts", "Accounts.Code=[pAccountCode]" )) = [pAccountCode])
	AND ((Allocations.BocCode) = [pBocCode])
	AND ((Allocations.RcCode) = [pRcCode])
	AND ((Allocations.Amount) = [pAmount]));
