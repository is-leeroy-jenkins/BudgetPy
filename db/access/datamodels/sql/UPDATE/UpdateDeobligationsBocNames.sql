UPDATE Deobligations 
INNER JOIN Funds 
ON Funds.Code = Deobligations.FundCode 
SET Deobligations.FundName = Funds.Name
WHERE Deobligations.FundCode = Funds.Code;