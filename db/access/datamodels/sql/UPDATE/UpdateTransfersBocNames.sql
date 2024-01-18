UPDATE AnnualCarryoverEstimates
	INNER JOIN FundSymbols
ON (AnnualCarryoverEstimates.BFY = FundSymbols.BFY)
	AND (AnnualCarryoverEstimates.EFY = FundSymbols.EFY)
	AND (AnnualCarryoverEstimates.FundCode = FundSymbols.FundCode)
SET AnnualCarryoverEstimates.TreasuryAccountCode = FundSymbols.TreasuryAccountCode WHERE AnnualCarryoverEstimates.BFY = FundSymbols.BFY
AND AnnualCarryoverEstimates.EFY = FundSymbols.EFY
AND AnnualCarryoverEstimates.FundCode = FundSymbols.FundCode
AND AnnualCarryoverEstimates.TreasuryAccountCode IS NULL;