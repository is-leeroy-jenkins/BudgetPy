UPDATE OperatingPlans 
INNER JOIN BudgetObjectClasses 
ON OperatingPlans.BocCode = BudgetObjectClasses.Code 
SET OperatingPlans.BocName = BudgetObjectClasses.Name;