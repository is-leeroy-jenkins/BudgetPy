UPDATE Obligations 
INNER JOIN Funds 
ON Obligations.EFY = Funds.EFY
AND Obligations.BFY = Funds.BFY
AND Obligations.FundCode = Funds.Code
SET Obligations.FundName = Funds.Name;