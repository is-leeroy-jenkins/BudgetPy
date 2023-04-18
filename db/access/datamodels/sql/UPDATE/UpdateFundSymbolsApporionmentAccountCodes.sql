UPDATE FundSymbols 
SET FundSymbols.ApportionmentAccountCode = IIF( FundSymbols.EFY <> 'NS' AND LEN(FundSymbols.BudgetAccountCode) = 11, '68-' & RIGHT(FundSymbols.BudgetAccountCode, 4) & ' ' & FundSymbols.BFY & '/' & FundSymbols.EFY, 
'68-' & RIGHT(FundSymbols.BudgetAccountCode, 4) & ' /X' )
WHERE LEN(FundSymbols.BudgetAccountCode) = 11
AND IsNull(FundSymbols.ApportionmentAccountCode);