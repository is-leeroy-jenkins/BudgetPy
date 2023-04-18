CREATE VIEW "SystemAllocationOperatingPlanAnalysis"
AS SELECT DISTINCT SystemUpdates.BudgetLevel AS BudgetLevel, SystemUpdates.BFY AS BFY, SystemUpdates.AhCode AS AhCode, 
SystemUpdates.FundCode AS FundCode, SystemUpdates.OrgCode AS OrgCode, SystemUpdates.AccountCode AS AccountCode, 
SystemUpdates.BocCode AS BocCode, SystemUpdates.Amount AS System, OperatingPlans.Amount AS OperatingPlan, 
	CASE SystemUpdates.Amount - OperatingPlans.Amount
		WHEN SystemUpdates.Amount - OperatingPlans.Amount > 0 THEN "INCREASE"
		WHEN SystemUpdates.Amount - OperatingPlans.Amount < 0 THEN "DECREASE"
		ELSE "NET ZERO"
	END	NET, 
SystemUpdates.Amount-OperatingPlans.Amount AS Delta
FROM SystemUpdates 
INNER JOIN OperatingPlans 
ON (SystemUpdates.RcCode = OperatingPlans.RcCode) 
AND (SystemUpdates.BocCode = OperatingPlans.BocCode) 
AND (SystemUpdates.AccountCode = OperatingPlans.AccountCode) 
AND (SystemUpdates.OrgCode = OperatingPlans.OrgCode) 
AND (SystemUpdates.FundCode = OperatingPlans.FundCode) 
AND (SystemUpdates.AhCode = OperatingPlans.AhCode) 
AND (SystemUpdates.BFY = OperatingPlans.BFY)
WHERE SystemUpdates.Amount <> OperatingPlans.Amount;