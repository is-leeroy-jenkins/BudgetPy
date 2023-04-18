UPDATE Deobligations 
INNER JOIN BudgetObjectClasses 
ON Deobligations.BocCode = BudgetObjectClasses.Code
SET Deobligations.BocName = BudgetObjectClasses.Name;