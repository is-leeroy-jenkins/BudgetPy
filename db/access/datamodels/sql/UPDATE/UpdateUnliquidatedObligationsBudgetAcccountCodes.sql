UPDATE UnobligatedBalances 
INNER JOIN FundSymbols 
ON (UnobligatedBalances.FundCode = FundSymbols.FundCode) 
AND (RIGHT(UnobligatedBalances.TreasurySymbol, 4) = RIGHT(FundSymbols.TreasuryAccountCode, 4)) 
SET UnobligatedBalances.OmbAccountCode = "020-00-" & RIGHT(FundSymbols.TreasuryAccountCode, 4)
WHERE UnobligatedBalances.OmbAccountCOde IS NULL;
