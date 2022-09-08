UPDATE StateGrantObligations 
INNER JOIN BudgetObjectClasses 
ON BudgetObjectClasses.Code = StateGrantObligations.BocCode 
SET StateGrantObligations.BocName = BudgetObjectClasses.Name
WHERE StateGrantObligations.BocName <> BudgetObjectClasses.Name;