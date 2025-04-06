INSERT INTO BudgetParameters
SELECT DISTINCT Allocations.AhCode AS AhCode, Allocations.BFY AS BFY, Allocations.RcCode AS RcCode, Allocations.DivisionName AS DivisionName, Allocations.FundCode AS FundCode, Allocations.FundName AS FundName
FROM Allocations
WHERE Allocations.RcCode <> '06'
AND NOT IsNull(Allocations.RcCode)
ORDER BY Allocations.BFY DESC;

