SELECT Allocations.PrcId, Allocations.BFY, Allocations.RPIO, Allocations.AhCode, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.RcCode, CCur(Round(Allocations.Amount,2)) AS Budget, CCur(Round(StatusOfFunds.Amount,2)) AS System, CCur(Round(StatusOfFunds.Amount-Allocations.Amount,2)) AS DELTA
FROM Allocations INNER JOIN StatusOfFunds ON Allocations.RcCode = StatusOfFunds.RcCode 
AND Allocations.AccountCode = StatusOfFunds.AccountCode 
AND Allocations.BocCode = StatusOfFunds.BocCode 
AND Allocations.OrgCode = StatusOfFunds.OrgCode 
AND Allocations.FundCode = StatusOfFunds.FundCode 
AND Allocations.AhCode = StatusOfFunds.AhCode 
AND Allocations.BudgetLevel = StatusOfFunds.BudgetLevel 
AND Allocations.BFY = StatusOfFunds.BFY
AND Allocations.BudgetLevel='7'
ORDER BY Allocations.BFY DESC , Allocations.FundCode, Allocations.AccountCode, Allocations.BocCode;