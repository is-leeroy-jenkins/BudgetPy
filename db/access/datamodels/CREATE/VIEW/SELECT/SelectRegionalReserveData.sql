SELECT StatusOfFunds.BFY, StatusOfFunds.FundName, StatusOfFunds.FundCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.AccountCode, 
Sum(StatusOfFunds.Amount) AS Authority, 
Sum(StatusOfFunds.OpenCommitments) AS OpenCommitments, 
Sum(StatusOfFunds.Obligations) AS Obligations, 
Sum(StatusOfFunds.Used) AS Used, 
Sum(StatusOfFunds.Available) AS Available
FROM StatusOfFunds
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundName, StatusOfFunds.FundCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.AccountCode, StatusOfFunds.BudgetLevel
HAVING (((StatusOfFunds.BudgetLevel)="7"));
