UPDATE Obligations 
INNER JOIN BudgetObjectClasses 
ON Obligations .BocCode = BudgetObjectClasses.Code
SET Obligations .BocName = BudgetObjectClasses.Name;