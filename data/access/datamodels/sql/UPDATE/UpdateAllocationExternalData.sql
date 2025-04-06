UPDATE Allocations
	LEFT JOIN ExternalUpdates
ON (Allocations.RcCode = ExternalUpdates.RcCode)
	AND (Allocations.AccountCode = ExternalUpdates.AccountCode)
	AND (Allocations.OrgCode = ExternalUpdates.OrgCode)
	AND (Allocations.BudgetLevel = ExternalUpdates.BudgetLevel)
	AND (Allocations.FundCode = ExternalUpdates.FundCode)
	AND (Allocations.AhCode = ExternalUpdates.AhCode)
	AND (Allocations.BFY = ExternalUpdates.BFY)
SET Allocations.Amount = ExternalUpdates.Amount WHERE (((Allocations.AhCode)= ExternalUpdates.AhCode) 
AND ((Allocations.BudgetLevel)= ExternalUpdates.BudgetLevel) 
AND ((Allocations.BFY)= ExternalUpdates.BFY) 
AND ((Allocations.FundCode)= ExternalUpdates.FundCode) 
AND ((Allocations.OrgCode)= ExternalUpdates.OrgCode) 
AND ((Allocations.AccountCode)= ExternalUpdates.AccountCode) 
AND ((Allocations.BocCode) In ('21','28','36','37','38','41') 
AND (Allocations.BocCode)= ExternalUpdates.BocCode) 
AND ((Allocations.RcCode)= ExternalUpdates.RcCode) 
AND ((Allocations.Amount) <> ExternalUpdates.Amount) 
AND Allocations.BudgetLevel = '8' 
AND ((Allocations.Amount <> ExternalUpdates.Amount)));
