UPDATE AnnualCarryoverSurvey 
INNER JOIN Funds 
ON AnnualCarryoverSurvey.FundCode = Funds.Code
SET AnnualCarryoverSurvey.FundName = Funds.Name;