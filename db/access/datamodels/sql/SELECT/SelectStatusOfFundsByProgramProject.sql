SELECT StatusOfFunds.BFY, StatusOfFunds.RpioName, StatusOfFunds.RpioCode, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.ProgramProjectCode, StatusOfFunds.ProgramProjectName, CCur(Sum(StatusOfFunds.Amount)) AS Amount, CCur(Sum(StatusOfFunds.OpenCommitments)) AS OpenCommitments, CCur(Sum(StatusOfFunds.Obligations)) AS Obligations, CCur(Sum(StatusOfFunds.Used)) AS Used, CCur(Sum(StatusOfFunds.Amount)-Sum(StatusOfFunds.Used)) AS Available
FROM StatusOfFunds
WHERE StatusOfFunds.BudgetLevel = '7'
AND StatusOfFunds.Amount <> 0
AND StatusOfFunds.RpioCode NOT LIKE '9%'
GROUP BY StatusOfFunds.BFY, StatusOfFunds.RpioName, StatusOfFunds.RpioCode, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.ProgramProjectCode, StatusOfFunds.ProgramProjectName;