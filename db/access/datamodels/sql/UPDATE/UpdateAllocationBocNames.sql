UPDATE Allocations 
INNER JOIN BudgetObjectClass 
ON BudgetObjectClass.Code = Allocations.BocCode 
SET Allocations.BocName = BudgetObjectClass.Name
WHERE Allocations.BocCode = BudgetObjectClass.Code
AND Allocations.BocName <> BudgetObjectClass.Name;