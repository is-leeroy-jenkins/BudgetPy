PARAMETERS RpioCodeArgs LongText;
SELECT StatusOfFunds.BFY, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.ProgramProjectName, StatusOfFunds.AccountCode, Sum(StatusOfFunds.Amount) AS Authority, Sum(StatusOfFunds.OpenCommitments) AS [Open Commitments], Sum(StatusOfFunds.Obligations) AS Obligations, Sum(StatusOfFunds.Used) AS Used, Sum(StatusOfFunds.Amount) - Sum(StatusOfFunds.Used) As Available
FROM StatusOfFunds
WHERE (((StatusOfFunds.Amount)>0)) 
AND StatusOfFunds.RpioCode = [RpioCodeArgs]
GROUP BY StatusOfFunds.BFY, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.ProgramProjectName, StatusOfFunds.AccountCode, Sum(StatusOfFunds.Amount) - Sum(StatusOfFunds.Used)
ORDER BY StatusOfFunds.BFY DESC;
