UPDATE Deobligations 
SET Deobligations.NpmCode = Mid(Deobligations.AccountCode, 4, 1)
WHERE Deobligations.NpmCode IS NULL;