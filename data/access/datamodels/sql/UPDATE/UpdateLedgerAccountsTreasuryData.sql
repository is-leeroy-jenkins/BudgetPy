UPDATE LedgerAccounts
	INNER JOIN Funds
ON Funds.Code = LedgerAccounts.FundCode
SET LedgerAccounts.FundName = Funds.Name, LedgerAccounts.TreasurySymbol = Funds.TreasuryAccountCode
WHERE LedgerAccounts.FundCode = Funds.Code;