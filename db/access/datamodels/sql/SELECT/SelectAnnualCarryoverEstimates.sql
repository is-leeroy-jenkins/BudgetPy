SELECT StatusOfFunds.BFY AS BFY, StatusOfFunds.EFY AS EFY, StatusOfFunds.FundCode AS FundCode, StatusOfFunds.FundName AS FundName, StatusOfFunds.RpioCode AS RpioCode, StatusOfFunds.RpioName AS RpioName, CCur(SUM(StatusOfFunds.Amount)) AS Amount, CCur(SUM(StatusOfFunds.OpenCommitments)) AS OpenCommitments, CCur(SUM(StatusOfFunds.Obligations)) AS Obligations, CCur(SUM(StatusOfFunds.Amount) - SUM(StatusOfFunds.Obligations) - SUM(StatusOfFunds.OpenCommitments)) AS Available, CCur(SUM(StatusOfFunds.Amount) - SUM(StatusOfFunds.Obligations)) AS Estimate
FROM StatusOfFunds
WHERE (StatusOfFunds.BudgetLevel = '7'
AND StatusOfFunds.BFY IN ('2021', '2022')
AND StatusOfFunds.FundCode NOT LIKE '%S%')
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName
HAVING SUM(StatusOfFunds.Amount) - SUM(StatusOfFunds.Obligations) - SUM(StatusOfFunds.OpenCommitments) > 0 
AND StatusOfFunds.FundCode NOT LIKE '%R%'
ORDER BY StatusOfFunds.RpioCode, StatusOfFunds.FundCode, StatusOfFunds.BFY DESC;