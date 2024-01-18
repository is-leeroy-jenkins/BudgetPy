UPDATE Funds
SET Funds.BudgetAccountCode = "020-00-" & Funds.MAIN,
	Funds.BudgetAccountName = "020-00-" & Funds.MAIN & " " & Funds.Name;