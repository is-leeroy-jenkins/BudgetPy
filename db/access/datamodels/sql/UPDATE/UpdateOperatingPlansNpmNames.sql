UPDATE OperatingPlans 
INNER JOIN NationalPrograms 
ON OperatingPlans.NpmCode = NationalPrograms.Code 
SET OperatingPlans.NpmName = NationalPrograms.Name;