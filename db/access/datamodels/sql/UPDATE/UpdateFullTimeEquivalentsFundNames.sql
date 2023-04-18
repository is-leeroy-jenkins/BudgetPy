UPDATE FullTimeEquivalents
INNER JOIN Funds
ON FullTimeEquivalents.EFY = Funds.EFY
AND FullTimeEquivalents.BFY = Funds.BFY
AND FullTimeEquivalents.FundCode = Funds.Code
SET FullTimeEquivalents.FundName = Funds.Name;