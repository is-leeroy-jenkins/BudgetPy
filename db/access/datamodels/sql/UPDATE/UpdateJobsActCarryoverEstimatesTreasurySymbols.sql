UPDATE JobsActCarryoverEstimates 
INNER JOIN FundSymbols 
ON (JobsActCarryoverEstimates.FundCode = FundSymbols.FundCode) 
AND (JobsActCarryoverEstimates.EFY = FundSymbols.EFY) 
AND (JobsActCarryoverEstimates.BFY = FundSymbols.BFY) 
SET JobsActCarryoverEstimates.TreasuryAccountCode = FundSymbols.TreasuryAccountCode
WHERE JobsActCarryoverEstimates.BFY = FundSymbols.BFY
AND JobsActCarryoverEstimates.EFY = FundSymbols.EFY
AND JobsActCarryoverEstimates.FundCode = FundSymbols.FundCode
AND JobsActCarryoverEstimates.TreasuryAccountCode IS NULL;