UPDATE AnnualCarryoverSurvey
	INNER JOIN Funds
ON Funds.Code = AnnualCarryoverSurvey.FundCode
SET AnnualCarryoverSurvey.FundName = Funds.Name WHERE AnnualCarryoverSurvey.FundCode = Funds.Code;