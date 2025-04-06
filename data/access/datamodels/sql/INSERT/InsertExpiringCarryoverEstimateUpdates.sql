INSERT INTO ExternalUpdates
SELECT ExternalAllocations.PrcId              AS ExtId,
	   ExternalAllocations.BudgetLevel        AS BudgetLevel,
	   ExternalAllocations.AhCode             AS AhCode,
	   ExternalAllocations.BFY                AS BFY,
	   ExternalAllocations.FundCode           AS FundCode,
	   ExternalAllocations.FundName           AS FundName,
	   ExternalAllocations.OrgCode            AS OrgCode,
	   ExternalAllocations.AccountCode        AS AccountCode,
	   ExternalAllocations.ActivityCode       AS ActivityCode,
	   ExternalAllocations.ProgramProjectCode AS ProgramProjectCode,
	   ExternalAllocations.ProgramProjectName AS ProgramProjectName,
	   ExternalAllocations.ProgramAreaCode    AS ProgramAreaCode,
	   ExternalAllocations.ProgramAreaName    AS ProgramAreaName,
	   ExternalAllocations.RcCode             AS RcCode,
	   ExternalAllocations.DivisionName       AS DivisionName,
	   ExternalAllocations.BocCode            AS BocCode,
	   ExternalAllocations.BocName            AS BocName,
	   ExternalAllocations.Amount             AS Amount
FROM ExternalAllocations
WHERE ExternalAllocations.BudgetLevel = 8
ORDER BY ExternalAllocations.BFY DESC, ExternalAllocations.FundCode, ExternalAllocations.RcCode,
		 ExternalAllocations.AccountCode, ExternalAllocations.BocCode;