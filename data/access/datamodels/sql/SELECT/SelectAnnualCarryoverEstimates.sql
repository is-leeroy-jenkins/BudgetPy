SELECT AnnualCarryoverEstimates.TreasuryAccountCode,
	   (AnnualCarryoverEstimates.BFY & "/" & AnnualCarryoverEstimates.EFY) AS FiscalYear,
	   AnnualCarryoverEstimates.FundCode,
	   AnnualCarryoverEstimates.FundName,
	   SUM( AnnualCarryoverEstimates.Estimate )                            AS Estimate
FROM AnnualCarryoverEstimates
GROUP BY AnnualCarryoverEstimates.TreasuryAccountCode,
		 (AnnualCarryoverEstimates.BFY & "/" & AnnualCarryoverEstimates.EFY),
		 AnnualCarryoverEstimates.FundCode, AnnualCarryoverEstimates.FundName;