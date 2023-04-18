UPDATE AnnualCarryoverEstimates
INNER JOIN Funds 
ON (AnnualCarryoverEstimates.FundCode = Funds.Code) 
AND (AnnualReimbursableEstimates.EFY = Funds.EFY) 
AND (AnnualReimbursableEstimates.BFY = Funds.BFY) 
SET AnnualCarryoverEstimates.TreasuryAccountCode = Funds.TreasuryAccountCode;
