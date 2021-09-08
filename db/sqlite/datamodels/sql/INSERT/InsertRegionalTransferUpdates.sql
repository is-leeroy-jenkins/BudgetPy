INSERT INTO RegionTravel
SELECT *
FROM Allocations
WHERE Allocations.BocCode IN ('21', '28')
AND Allocations.BudgetLevel = '7';
