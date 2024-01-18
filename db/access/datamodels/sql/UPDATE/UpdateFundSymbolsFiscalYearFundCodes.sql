UPDATE FundSymbols
	INNER JOIN Funds
ON FundSymbols.TreasuryAccountCode = Funds.TreasuryAccountCode
SET FundSymbols.BFY = Funds.BFY, FundSymbols.EFY = Funds.EFY, FundSymbols.FundCode = Funds.Code, FundSymbols.OmbAccountName = Funds.OmbAccountName
WHERE FundSymbols.TreasuryAccountCode = Funds.TreasuryAccountCode;