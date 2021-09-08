CREATE VIEW "BudgetToSystemBalance" AS
SELECT Allocations.PrcId, Allocations.BFY, Allocations.BudgetLevel, Allocations.AhCode, Allocations.FundName, Allocations.FundCode, Allocations.OrgCode, Allocations.AccountCode, Allocations.BocCode, Allocations.DivisionName, Allocations.RcCode, Allocations.BocName, Allocations.ProgramProjectName,
CCur(Allocations.Amount) AS Budget, 
CCur(StatusOfFunds.Amount) AS System, 
CCur(0-Round(Nz([Allocations].[Amount], 0.0)-StatusOfFunds.Amount,1)) AS Delta, 
IIf([Delta]< -1.0,"DECREASE", IIF([Delta] > 1.0, "INCREASE", "NET ZERO")) AS NET 
FROM Allocations 
LEFT JOIN StatusOfFunds 
ON Allocations.RcCode = StatusOfFunds.RcCode 
AND Allocations.AccountCode = StatusOfFunds.AccountCode 
AND Allocations.OrgCode = StatusOfFunds.OrgCode 
AND Allocations.FundCode = StatusOfFunds.FundCode 
AND Allocations.AhCode = StatusOfFunds.AhCode 
AND Allocations.BudgetLevel = StatusOfFunds.BudgetLevel 
AND Allocations.BFY = StatusOfFunds.BFY
WHERE Allocations.BFY = StatusOfFunds.BFY 
AND Allocations.BudgetLevel = StatusOfFunds.BudgetLevel 
AND Allocations.AhCode = StatusOfFunds.AhCode 
AND Allocations.FundCode = StatusOfFunds.FundCode 
AND Allocations.OrgCode = StatusOfFunds.OrgCode 
AND Allocations.AccountCode = StatusOfFunds.AccountCode 
AND Allocations.BocCode = StatusOfFunds.BocCode 
AND Allocations.RcCode = StatusOfFunds.RcCode 
AND Allocations.Amount <> StatusOfFunds.Amount;