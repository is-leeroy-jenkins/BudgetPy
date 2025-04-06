UPDATE AppropriationLevelAuthority
	INNER JOIN FundSymbols
ON (AppropriationLevelAuthority.FiscalYear = FundSymbols.BFY)
	AND (AppropriationLevelAuthority.FundCode = FundSymbols.FundCode)
SET AppropriationLevelAuthority.FundName = FundSymbols.FundName, AppropriationLevelAuthority.BudgetAccountCode = FundSymbols.OmbAccountCode, AppropriationLevelAuthority.BudgetAccountName = FundSymbols.OmbAccountName
WHERE AppropriationLevelAuthority.FundName IS NULL;