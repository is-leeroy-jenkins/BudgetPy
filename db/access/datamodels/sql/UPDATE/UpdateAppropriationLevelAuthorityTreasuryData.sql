UPDATE Deobligations 
INNER JOIN Funds 
ON (Funds.BFY = Deobligations.BFY) 
AND (Funds.Code = Deobligations.FundCode) 
SET Deobligations.TreasurySymbol = Funds.TreasuryAccountCode, Deobligations.OmbAccountCode = Funds.OmbAccountCode, Deobligations.OmbAccountName = Funds.OmbAccountName
WHERE Funds.Code = Deobligations.FundCode 
AND Funds.BFY = Deobligations.BFY;