UPDATE Transfers
	INNER JOIN BudgetObjectClasses
ON Transfers.BocCode = BudgetObjectClasses.Code
SET Transfers.BocName = BudgetObjectClasses.Name WHERE Transfers.BocCode = BudgetObjectClasses.Code
AND Transfers.BocName <> BudgetObjectClasses.Name;