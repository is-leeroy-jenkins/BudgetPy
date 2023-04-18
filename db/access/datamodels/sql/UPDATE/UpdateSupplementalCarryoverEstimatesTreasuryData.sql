UPDATE SupplementalCarryoverEstimates 
INNER JOIN Funds 
ON (SupplementalCarryoverEstimates.BFY = Funds.BFY) 
AND (SupplementalCarryoverEstimates.EFY = Funds.EFY) 
AND (SupplementalCarryoverEstimates.FundCode = Funds.Code) 
SET SupplementalCarryoverEstimates.TreasuryAccountCode = Funds.TreasuryAccountCode