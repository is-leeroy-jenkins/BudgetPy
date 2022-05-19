SELECT DISTINCTROW Allocations.PrcId, Allocations.BFY, Allocations.BudgetLevel, Allocations.AhCode, Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.BocName, Allocations.ProgramProjectName, Allocations.RcCode, Allocations.DivisionName, CCur((Round(Allocations.Amount,2))) AS Budget, CCur((Round(SystemUpdates.Amount,2))) AS System, CCur((0-Round(Nz([Allocations].[Amount],2)-Round(SystemUpdates.Amount,2),2))) AS Delta, IIf([Delta]<-1,"DECREASE",IIf([Delta]>1,"INCREASE","NET ZERO")) AS NET
FROM Allocations LEFT JOIN SystemUpdates ON (Allocations.RcCode = SystemUpdates.RcCode) AND (Allocations.AccountCode = SystemUpdates.AccountCode) AND (Allocations.OrgCode = SystemUpdates.OrgCode) AND (Allocations.BudgetLevel = SystemUpdates.BudgetLevel) AND (Allocations.FundCode = SystemUpdates.FundCode) AND (Allocations.AhCode = SystemUpdates.AhCode) AND (Allocations.BFY = SystemUpdates.BFY)
WHERE (((Allocations.BFY)=[SystemUpdates].[BFY]) 
AND ((Allocations.BudgetLevel)=[SystemUpdates].[BudgetLevel]) 
AND ((Allocations.AhCode)=[SystemUpdates].[AhCode]) 
AND ((Allocations.FundCode)=[SystemUpdates].[FundCode]) 
AND ((Allocations.OrgCode)=[SystemUpdates].[OrgCode]) 
AND ((Allocations.AccountCode)=[SystemUpdates].[AccountCode]) 
AND ((Allocations.BocCode)=[SystemUpdates].[BocCode] 
AND (Allocations.BocCode) In ('10', '21','28','36','37','38','41')) 
AND ((Allocations.RcCode)=[SystemUpdates].[RcCode]) 
AND ((SystemUpdates.BudgetLevel)='7'))
GROUP BY Allocations.PrcId, Allocations.BFY, Allocations.BudgetLevel, Allocations.AhCode, Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.BocName, Allocations.ProgramProjectName, Allocations.RcCode, Allocations.DivisionName, CCur((Round(Allocations.Amount,2))), CCur((Round(SystemUpdates.Amount,2))), CCur((0-Round(Nz([Allocations].[Amount],2)-Round(SystemUpdates.Amount,2),2))), IIf((0-Round(Nz([Allocations].[Amount],2)-Round(SystemUpdates.Amount,2),2))<0, "DECREASE", 
IIf((0-Round(Nz([Allocations].[Amount],2)-Round(SystemUpdates.Amount,2),2))>0, "INCREASE",
"NET ZERO"))
ORDER BY Allocations.BFY DESC , Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;
