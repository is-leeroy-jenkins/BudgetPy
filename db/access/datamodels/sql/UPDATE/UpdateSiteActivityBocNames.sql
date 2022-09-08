UPDATE SiteActivity INNER JOIN BudgetObjectClasses 
ON BudgetObjectClasses.Code = SiteActivity.BocCode 
SET SiteActivity.BocName = BudgetObjectClasses.Name
WHERE SiteActivity.BocCode = BudgetObjectClasses.Code;
