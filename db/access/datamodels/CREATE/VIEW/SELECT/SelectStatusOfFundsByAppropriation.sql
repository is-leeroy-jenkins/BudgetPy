SELECT StatusOfFunds.BFY, StatusOfFunds.FundName, StatusOfFunds.FundCode, 
Sum(StatusOfFunds.Amount) AS Authority, 
Sum(StatusOfFunds.OpenCommitments) AS OpenCommitments, 
Sum(StatusOfFunds.Obligations) AS Obligations, 
Sum(StatusOfFunds.Used) AS Used, 
ROUND(Sum(StatusOfFunds.Available), 2) AS Available, 
StatusOfFunds.BocCode, StatusOfFunds.BocName
FROM StatusOfFunds
WHERE StatusOfFunds.BocCode <> '10'
AND StatusOfFunds.BFY = '2020'
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundName, 
StatusOfFunds.FundCode, StatusOfFunds.BudgetLevel, 
StatusOfFunds.BocCode, StatusOfFunds.BocName
HAVING (((StatusOfFunds.BudgetLevel)="7"))
ORDER BY StatusOfFunds.BFY DESC , StatusOfFunds.FundCode;

