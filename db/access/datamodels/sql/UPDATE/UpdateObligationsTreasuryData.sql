UPDATE Obligations 
INNER JOIN FundSymbols 
ON (Obligations.BFY = FundSymbols.BFY) 
AND (Obligations.EFY = FundSymbols.EFY) 
AND (Obligations.FundCode = FundSymbols.FundCode) 
SET Obligations.TreasurySymbol = FundSymbols.TreasuryAccountCode, 
Obligations.BudgetAccountCode = FundSymbols.BudgetAccountCode, 
Obligations.BudgetAccountName = FundSymbols.BudgetAccountName, 
Obligations.ApportionmentAccountCode = FundSymbols.ApportionmentAccountCode;
