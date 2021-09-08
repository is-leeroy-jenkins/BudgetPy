SELECT DISTINCT Allocations.PrcId, Allocations.BFY, Allocations.BudgetLevel, Allocations.AhCode, Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.BocName, Allocations.ProgramProjectName, Allocations.RcCode, Allocations.DivisionName, CCur((Round(Allocations.Amount,2))) AS Budget, 
CCur((Round(StatusOfFunds.Amount,2))) AS System, 
CCur((0-Round(Nz([Allocations].[Amount],2)-Round(StatusOfFunds.Amount,2),2))) AS Delta, 
IIf([Delta]<-1,"DECREASE",IIf([Delta]>1, "INCREASE","NET ZERO")) AS NET
FROM Allocations 
LEFT JOIN StatusOfFunds 
ON (Allocations.RcCode  =  StatusOfFunds.RcCode 
AND Allocations.AccountCode  =  StatusOfFunds.AccountCode 
AND Allocations.OrgCode  =  StatusOfFunds.OrgCode 
AND Allocations.BudgetLevel  =  StatusOfFunds.BudgetLevel 
AND Allocations.FundCode  =  StatusOfFunds.FundCode 
AND Allocations.AhCode  =  StatusOfFunds.AhCode 
AND Allocations.BFY  =  StatusOfFunds.BFY)
WHERE (Allocations.BFY = StatusOfFunds.BFY 
AND Allocations.BudgetLevel = StatusOfFunds.BudgetLevel 
AND Allocations.AhCode = StatusOfFunds.AhCode 
AND Allocations.FundCode = StatusOfFunds.FundCode 
AND Allocations.OrgCode = StatusOfFunds.OrgCode 
AND Allocations.AccountCode = StatusOfFunds.AccountCode 
AND Allocations.BocCode = StatusOfFunds.BocCode 
AND Allocations.BocCode IN ('10', '21','28','36','37','38','41')
AND Allocations.RcCode = StatusOfFunds.RcCode 
AND StatusOfFunds.BudgetLevel = '7' 
AND Allocations.Amount <> StatusOfFunds.Amount 
AND Abs(Allocations.Amount-StatusOfFunds.Amount) > 0)
ORDER BY Allocations.BFY DESC, Allocations.FundCode, 
Allocations.AccountCode, Allocations.BocCode;