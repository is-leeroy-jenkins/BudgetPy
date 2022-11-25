UPDATE AppropriationLevelAuthority 
INNER JOIN FundSymbols 
ON (AppropriationLevelAuthority.FundCode = FundSymbols.FundCode) 
AND (AppropriationLevelAuthority.EFY = FundSymbols.EFY) 
AND (AppropriationLevelAuthority.BFY = FundSymbols.BFY) 
SET AppropriationLevelAuthority.TreasuryAccountCode = FundSymbols.TreasuryAccountCode, 
AppropriationLevelAuthority.TreasuryAccountName = FundSymbols.TreasuryAccountName, 
AppropriationLevelAuthority.BudgetAccountCode = FundSymbols.BudgetAccountCode, 
AppropriationLevelAuthority.BudgetAccountName = FundSymbols.BudgetAccountName;