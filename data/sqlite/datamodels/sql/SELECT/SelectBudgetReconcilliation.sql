SELECT StatusOfFunds.BFY AS BFY, StatusOfFunds.FundCode AS FundCode, StatusOfFunds.FundName AS FundName, 
CCur(Sum(StatusOfFunds.Available)) AS Amount, 
CCur(Sum(StatusOfFunds.OpenCommitments)) AS OpenCommitments, 
CCur(SUM(StatusOfFunds.Available + StatusOfFunds.OpenCommitments)) AS Estimate
FROM StatusOfFunds
WHERE StatusOfFunds.FundCode IN (SELECT DISTINCT FundCode FROM CarryoverSurvey) 
AND StatusOfFunds.BudgetLevel = '7'
AND NOT IsNull(StatusOfFunds.BFY)
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundCode, StatusOfFunds.FundName
HAVING SUM(StatusOfFunds.Available + StatusOfFunds.OpenCommitments) > 0;