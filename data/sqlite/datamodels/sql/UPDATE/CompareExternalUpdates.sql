CREATE VIEW "CompareExternalUpdates"
AS SELECT Allocations.PrcId, Allocations.AhCode, Allocations.BudgetLevel, Allocations.BFY, Allocations.FundName, 
Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.ActivityCode, Allocations.BocCode, 
Allocations.DivisionName, Allocations.RcCode, 
Allocations.Amount AS Amount, 
ExternalUpdates.Amount AS Change, 
Allocations.Amount-ExternalUpdates.Amount AS Delta,
CASE Allocations.Amount-ExternalUpdates.Amount
    WHEN  Allocations.Amount-ExternalUpdates.Amount < 1 THEN "DECREASE"
    WHEN  Allocations.Amount-ExternalUpdates.Amount > 1 THEN  "INCREASE"
	ELSE "NET ZERO" 
END NET,
Allocations.BocName, Allocations.ProgramProjectName
FROM Allocations 
LEFT JOIN ExternalUpdates 
ON (Allocations.RcCode  =  ExternalUpdates.RcCode) 
AND (Allocations.AccountCode  =  ExternalUpdates.AccountCode) 
AND (Allocations.OrgCode  =  ExternalUpdates.OrgCode) 
AND (Allocations.BudgetLevel  =  ExternalUpdates.BudgetLevel) 
AND (Allocations.FundCode  =  ExternalUpdates.FundCode) 
AND (Allocations.AhCode  =  ExternalUpdates.AhCode) 
AND (Allocations.BFY  =  ExternalUpdates.BFY)
WHERE ExternalUpdates.BudgetLevel  =  '8' 
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
AND Allocations.Amount<>ExternalUpdates.Amount