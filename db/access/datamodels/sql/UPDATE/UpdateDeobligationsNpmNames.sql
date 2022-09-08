UPDATE Deobligations 
INNER JOIN NationalPrograms 
ON Deobligations.NpmCode = NationalPrograms.Code 
SET Deobligations.NpmName = NationalPrograms.Name
WHERE Deobligations.NpmCode = NationalPrograms.Code
AND (Deobligations.NpmName IS NULL OR
    Deobligations.NpmName <> NationalPrograms.Name);