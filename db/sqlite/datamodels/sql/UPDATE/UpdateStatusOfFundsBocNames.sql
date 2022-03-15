UPDATE StatusOfFunds 
INNER JOIN Funds 
ON StatusOfFunds.FundCode = Funds.Code SET StatusOfFunds.FundName = Funds.Name
WHERE StatusOfFunds.FundCode = Funds.Code
AND StatusOfFunds.FundName <> Funds.Name;
