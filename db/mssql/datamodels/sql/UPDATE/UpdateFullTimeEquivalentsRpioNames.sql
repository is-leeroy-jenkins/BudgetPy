UPDATE FullTimeEquivalents
INNER JOIN Allocations
ON FullTimeEquivalents.FundCode = Allocations.FundCode
SET FullTimeEquivalents.FundName = Allocations.FundName
WHERE FullTimeEquivalents.FundName <> Allocations.FundName;