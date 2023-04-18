UPDATE FullTimeEquivalents
INNER JOIN AllowanceHolders
ON FullTimeEquivalents.AhCode = AllowanceHolders.Code
SET FullTimeEquivalents.AhName = AllowanceHolders.Name;