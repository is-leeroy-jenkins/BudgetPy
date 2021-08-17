INSERT INTO CarryoverSurvey
SELECT DISTINCT StatusOfFunds.BFY AS BFY, StatusOfFunds.FundCode AS FundCode, StatusOfFunds.FundName AS FundName, CCur(SUM(StatusOfFunds.Available)) AS Amount
FROM StatusOfFunds
WHERE (StatusOfFunds.BFY = '2021'
AND StatusOfFunds.FundCode = 'B'
AND StatusOfFunds.BudgetLevel = '7')
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundCode, StatusOfFunds.FundName;

