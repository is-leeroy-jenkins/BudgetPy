UPDATE StateGrantObligations 
INNER JOIN Funds 
ON Funds.Code = StateGrantObligations.FundCode 
SET StateGrantObligations.FundName = Funds.Name
WHERE StateGrantObligations.FundCode = Funds.Code;