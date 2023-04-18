UPDATE Deobligations 
INNER JOIN Funds
ON Deobligations.FundCode = Funds.Code
SET Deobligations.FundName = Funds.Name;