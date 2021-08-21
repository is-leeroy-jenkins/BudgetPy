INSERT INTO CarryoverSurvey ( BFY, FundCode, FundName, Amount )
SELECT DISTINCT CarryoverEstimates.BFY, CarryoverEstimates.FundCode, CarryoverEstimates.FundName, 
CCur(Sum(CarryoverEstimates.Estimate)) AS Amount
FROM CarryoverEstimates
GROUP BY CarryoverEstimates.BFY, 
CarryoverEstimates.FundCode, CarryoverEstimates.FundName;
