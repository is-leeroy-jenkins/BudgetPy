UPDATE Obligations 
INNER JOIN Funds 
ON Obligations.FundCode = Funds.Code 
SET Obligations.FundName = Funds.Name
WHERE Obligations.FundCode = Funds.Code
AND Obligations.FundName <> Funds.Name;