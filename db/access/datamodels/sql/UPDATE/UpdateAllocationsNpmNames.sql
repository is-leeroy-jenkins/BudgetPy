UPDATE Allocations 
INNER JOIN NationalPrograms 
ON NationalPrograms.Code = Allocations.NpmCode 
SET Allocations.NpmName = NationalPrograms.Name
WHERE Allocations.NpmCode = NationalPrograms.Code;
