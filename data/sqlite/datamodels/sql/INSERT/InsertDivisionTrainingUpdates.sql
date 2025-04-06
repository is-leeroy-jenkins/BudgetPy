INSERT INTO DivisionTravel
SELECT *
FROM Allocations
WHERE Allocations.BudgetLevel = "8" AND
     Allocations.BocCode IN ("21", "28");
