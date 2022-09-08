SELECT StatusOfFunds.BFY, StatusOfFunds.FundName, StatusOfFunds.FundCode,
Sum(StatusOfFunds.Amount) AS Authority, 
Sum(StatusOfFunds.OpenCommitments) AS OpenCommitments, 
Sum(StatusOfFunds.Obligations) AS Obligations, 
Sum(StatusOfFunds.Used) AS Used, 
CCur(Sum(StatusOfFunds.Amount)- SUM(StatusOfFunds.Used)) AS Available 
FROM StatusOfFunds
WHERE StatusOfFunds.BudgetLevel = '7'
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundName, StatusOfFunds.FundCode
ORDER BY StatusOfFunds.FundCode, StatusOfFunds.BFY DESC;


