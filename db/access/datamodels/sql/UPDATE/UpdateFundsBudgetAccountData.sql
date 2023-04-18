UPDATE Funds 
SET Funds.BudgetAccountCode = "020-00-" & Funds.MainAccount, 
Funds.BudgetAccountName = "020-00-" & Funds.MainAccount & " " & Funds.Name;