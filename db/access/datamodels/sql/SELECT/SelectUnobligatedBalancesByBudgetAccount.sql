SELECT UnobligatedBalances.FundCode, UnobligatedBalances.FundName, "020-00-" & RIGHT(UnobligatedBalances.TreasurySymbol, 4) AS [OMB Account Code], UnobligatedBalances.AccountNumber AS [Ledger Account Number], UnobligatedBalances.AccountName AS [Ledger Account Name], IIF(SUM(UnobligatedBalances.Amount) < 0, ABS(SUM(UnobligatedBalances.Amount)), SUM(UnobligatedBalances.Amount)) AS Amount
FROM UnobligatedBalances
WHERE UnobligatedBalances.AccountName NOT LIKE "%UNAPPORTIONED%"
GROUP BY "020-00-" & RIGHT(UnobligatedBalances.TreasurySymbol, 4), UnobligatedBalances.FundCode, UnobligatedBalances.FundName, UnobligatedBalances.AccountNumber, UnobligatedBalances.AccountName
ORDER BY UnobligatedBalances.FundName, UnobligatedBalances.AccountNumber;