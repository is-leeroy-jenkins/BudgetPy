UPDATE FundSymbols 
SET FundSymbols.ApportionmentAccountCode = IIF( FundSymbols.EFY <> 'NS' AND LEN(FundSymbols.OmbAccountCode) = 11, '68-' & RIGHT(FundSymbols.OmbAccountCode, 4) & ' ' & FundSymbols.BFY & '/' & FundSymbols.EFY, 
'68-' & RIGHT(FundSymbols.OmbAccountCode, 4) & ' /X' )
WHERE LEN(FundSymbols.OmbAccountCode) = 11
AND IsNull(FundSymbols.ApportionmentAccountCode);