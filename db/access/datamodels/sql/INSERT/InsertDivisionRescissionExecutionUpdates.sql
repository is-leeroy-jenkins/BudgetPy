INSERT INTO DivisionTraining
SELECT *
FROM Allocations
WHERE Allocations.AccountCode LIKE "%YF2"
  AND BudgetLevel = '8'
  AND Allocations.BocCode = '37'
  AND Allocations.RcCode NOT IN ( '06N', '06R' )
ORDER BY Allocations.BFY DESC;
