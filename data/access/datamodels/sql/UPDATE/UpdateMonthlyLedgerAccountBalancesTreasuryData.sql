UPDATE MonthlyLedgerAccountBalances 
INNER JOIN Funds 
ON (MonthlyLedgerAccountBalances.BFY = Funds.BFY) 
AND (MonthlyLedgerAccountBalances.EFY = Funds.EFY) 
AND (MonthlyLedgerAccountBalances.FundCode = Funds.Code) 
SET MonthlyLedgerAccountBalances.FundName = Funds.Name, 
MonthlyLedgerAccountBalances.TreasurySymbolName = Funds.TreasuryAccountName, MonthlyLedgerAccountBalances.ApportionmentAccountCode = Funds.TreasuryAccountCode, MonthlyLedgerAccountBalances.BudgetAccountCode = Funds.BudgetAccountCode, MonthlyLedgerAccountBalances.BudgetAccountName = Funds.BudgetAccountName;
