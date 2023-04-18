UPDATE AnnualReimbursableEstimates INNER JOIN Funds 
ON (AnnualReimbursableEstimates.FundCode = Funds.Code) 
AND (AnnualReimbursableEstimates.EFY = Funds.EFY) 
AND (AnnualReimbursableEstimates.BFY = Funds.BFY) 
SET AnnualReimbursableEstimates.TreasuryAccountCode = Funds.TreasuryAccountCode;
