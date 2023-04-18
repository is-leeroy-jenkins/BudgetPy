SELECT Allocations.PrcId, Allocations.AhCode, Allocations.BudgetLevel, Allocations.BFY, Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.ActivityCode, Allocations.BocCode, Allocations.DivisionName, Allocations.RcCode, Allocations.BocName, Allocations.ProgramProjectName,
CCur(Allocations.Amount) AS Amount, 
CCur(Round(ExternalUpdates.Amount, 2)) AS Change, 
CCur(0 - Round(Nz(Allocations.Amount, 2) - Round(ExternalUpdates.Amount,2),2)) AS Delta, 
IIf(Delta < -1, "DECREASE", IIF(Delta > 1, "INCREASE", "NET ZERO")) AS NET
FROM Allocations 
LEFT JOIN ExternalUpdates 
ON Allocations.BFY = ExternalUpdates.BFY 
AND Allocations.AhCode = ExternalUpdates.AhCode 
AND Allocations.FundCode = ExternalUpdates.FundCode 
AND Allocations.BudgetLevel = ExternalUpdates.BudgetLevel 
AND Allocations.OrgCode = ExternalUpdates.OrgCode 
AND Allocations.AccountCode = ExternalUpdates.AccountCode 
AND Allocations.RcCode = ExternalUpdates.RcCode
WHERE (ExternalUpdates.BudgetLevel = '8' 
AND Allocations.BocCode IN ('21', '28', '36', '37', '38', '41')
AND Allocations.BFY = ExternalUpdates.BFY 
AND Allocations.BudgetLevel = ExternalUpdates.BudgetLevel 
AND Allocations.AhCode = ExternalUpdates.AhCode 
AND Allocations.FundCode = ExternalUpdates.FundCode 
AND Allocations.OrgCode = ExternalUpdates.OrgCode 
AND Allocations.AccountCode = ExternalUpdates.AccountCode 
AND Allocations.ActivityCode = ExternalUpdates.ActivityCode
AND Allocations.BocCode = ExternalUpdates.BocCode 
AND Allocations.RcCode = ExternalUpdates.RcCode 
AND Allocations.Amount <> ExternalUpdates.Amount);