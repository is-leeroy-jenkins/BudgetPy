SELECT DISTINCT Allocations.BFY, Allocations.AhCode, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.RcCode, 
CCur(Allocations.Amount) AS Initial, 
CCur(OperatingPlans.Amount) AS Change, 
IIf(Allocations.Amount-OperatingPlans.Amount<0,"INCREASE","DECREASE") AS NET, CCUR(Round(Abs(Allocations.Amount-OperatingPlans.Amount),2)) AS Delta
FROM Allocations 
INNER JOIN OperatingPlans 
ON (Allocations.AccountCode = OperatingPlans.AccountCode) 
AND (Allocations.BocCode = OperatingPlans.BocCode) 
AND (Allocations.OrgCode = OperatingPlans.OrgCode) 
AND (Allocations.FundCode = OperatingPlans.FundCode) 
AND (Allocations.AhCode = OperatingPlans.AhCode) 
AND (Allocations.BFY = OperatingPlans.BFY);