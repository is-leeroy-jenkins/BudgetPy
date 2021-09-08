INSERT INTO ProgrammaticReserve ( PrcId, BudgetLevel, RPIO, AhCode, BFY, FundCode, OrgCode, AccountCode, ActivityCode, BocCode, RcCode, ProgramProjectCode, ProgramProjectName, CurrentYear, PriorYear, Reduction, Ratio, Budget, FundName, BocName, NpmCode, NpmName, Division, DivisionName )
SELECT Allocations.PrcId, Allocations.BudgetLevel, Allocations.RPIO, Allocations.AhCode, Allocations.BFY, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.ActivityCode, Allocations.BocCode, Allocations.RcCode, Allocations.ProgramProjectCode, Allocations.ProgramProjectName, 
Round(Sum([Allocations].[Amount]),0) AS CurrentYear, Nz(DLookUp("Amount","Allocations","Allocations.BFY = '2020'" & " AND Allocations.AhCode= '" & [Allocations].[AhCode] & "'" & " AND Allocations.OrgCode = '" & [Allocations].[OrgCode] & "'" & " AND Allocations.FundCode = '" & [Allocations].[FundCode] & "'" & " AND Allocations.AccountCode = '" & [Allocations].[AccountCode] & "'" & " AND Allocations.BocCode = '" & [Allocations].[BocCode] & "'" & " AND Allocations.RcCode = '" & [Allocations].[RcCode] & "'"),0) AS PriorYear, 
Round(Sum(Allocations.Amount*0.00772028905587925),3) AS Reduction, 
IIf(Allocations.Amount>0, Round(Sum(Allocations.Amount*0.00772028905587925)/Sum(Allocations.Amount),3),0) AS Ratio, Round(Sum(Allocations.Amount-(Allocations.Amount*0.00772028905587925)),0) AS Budget, 
Allocations.FundName, Allocations.BocName, Allocations.NpmCode, Allocations.NpmName, Allocations.Division, Allocations.DivisionName
FROM Allocations
WHERE (((Allocations.BudgetLevel)='8')  
AND ((Allocations.BocCode) In ('36','37'))  
AND ((Allocations.RcCode) Not In ('06G','06N','06R'))  
AND ((Allocations.FundCode) Not ALike "E%"  
AND (Allocations.FundCode) Not ALike "%R%")  
AND Allocations.ProgramProjectCode NOT IN ('89', '68')
 AND ((Allocations.BFY)='2021'))
GROUP BY Allocations.PrcId, Allocations.BudgetLevel, Allocations.RPIO, Allocations.AhCode, Allocations.BFY, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.ActivityCode, Allocations.BocCode, Allocations.RcCode, Allocations.ProgramProjectCode, Allocations.ProgramProjectName, Allocations.DivisionName, Allocations.FundName, Allocations.BocName, Allocations.NpmCode, Allocations.NpmName, Allocations.Division, Allocations.Amount
ORDER BY Allocations.BFY DESC , Allocations.DivisionName, 
Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;
