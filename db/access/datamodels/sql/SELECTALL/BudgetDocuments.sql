SELECT * 
FROM BudgetDocuments
ORDER BY BudgetDocuments.BFY DESC, BudgetDocuments.FundCode, 
    BudgetDocuments.RpioCode, BudgetDocuments.BudgetLevel;