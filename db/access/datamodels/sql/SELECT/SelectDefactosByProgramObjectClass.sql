SELECT StatusOfFunds.BFY,
	   StatusOfFunds.RpioName,
	   StatusOfFunds.RpioCode,
	   StatusOfFunds.FundName,
	   StatusOfFunds.FundCode,
	   StatusOfFunds.ProgramProjectName,
	   StatusOfFunds.BocName,
	   StatusOfFunds.BocCode,
	   CCur( Sum( StatusOfFunds.Amount ) )                             AS Amount,
	   CCur( Sum( StatusOfFunds.OpenCommitments ) )                    AS OpenCommitments,
	   CCur( Sum( StatusOfFunds.Obligations ) )                        AS Obligations,
	   CCur( Sum( StatusOfFunds.Used ) )                               AS Used,
	   CCur( Sum( StatusOfFunds.Amount ) - Sum( StatusOfFunds.Used ) ) AS Available
FROM StatusOfFunds
WHERE StatusOfFunds.BudgetLevel = '7'
  AND (StatusOfFunds.Amount - StatusOfFunds.Used) < 0
GROUP BY StatusOfFunds.BFY, StatusOfFunds.RpioName, StatusOfFunds.RpioCode, StatusOfFunds.FundName,
		 StatusOfFunds.FundCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocName,
		 StatusOfFunds.BocCode, StatusOfFunds.BocCode, StatusOfFunds.Amount,
		 StatusOfFunds.OpenCommitments, StatusOfFunds.Obligations,
		 (StatusOfFunds.Amount - StatusOfFunds.Used)
ORDER BY StatusOfFunds.BFY DESC, StatusOfFunds.RpioName, StatusOfFunds.FundName,
		 StatusOfFunds.ProgramProjectName;
