INSERT INTO DivisionAuthority
SELECT *
FROM Allocations
WHERE Allocations.BudgetLevel = '8'
  AND Allocations.RcCode <> '06'
  AND Allocations.BocCode <> '10';
