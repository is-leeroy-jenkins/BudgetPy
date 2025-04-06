UPDATE Allocations
	INNER JOIN BudgetObjectClasses
ON BudgetObjectClasses.Code = Allocations.BocCode
SET Allocations.BocName = BudgetObjectClasses.Name WHERE Allocations.BocCode = BudgetObjectClasses.Code
AND Allocations.BocName <> BudgetObjectClasses.Name;