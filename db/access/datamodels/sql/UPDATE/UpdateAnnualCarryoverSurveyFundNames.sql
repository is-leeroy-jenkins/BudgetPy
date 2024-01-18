UPDATE AnnualReimbursableEstimates
	INNER JOIN FundSymbols
ON (AnnualReimbursableEstimates.FundCode = FundSymbols.FundCode)
	AND (AnnualReimbursableEstimates.EFY = FundSymbols.EFY)
	AND (AnnualReimbursableEstimates.BFY = FundSymbols.BFY)
SET AnnualReimbursableEstimates.TreasuryAccountCode = FundSymbols.TreasuryAccountCode WHERE AnnualReimbursableEstimates.BFY = FundSymbols.BFY
AND AnnualReimbursableEstimates.EFY = FundSymbols.EFY
AND AnnualReimbursableEstimates.FundCode = FundSymbols.FundCode
AND AnnualReimbursableEstimates.TreasuryAccountCode IS NULL;