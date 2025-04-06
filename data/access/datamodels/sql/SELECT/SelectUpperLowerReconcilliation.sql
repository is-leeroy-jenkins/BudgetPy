SELECT StatusOfFunds.BFY,
	   StatusOfFunds.FundCode,
	   StatusOfFunds.FundName,
	   StatusOfFunds.ProgramProjectCode,
	   StatusOfFunds.ProgramProjectName,
	   CCur( Sum( StatusOfFunds.Amount ) )          AS Amount,
	   CCur( Sum( StatusOfFunds.OpenCommitments ) ) AS OpenCommitments,
	   CCur( Sum( StatusOfFunds.Obligations ) )     AS Obligations,
	   CCur( Sum( StatusOfFunds.Used ) )            AS Used,
	   CCur( Sum( StatusOfFunds.Available ) )       AS Available
FROM StatusOfFunds
WHERE StatusOfFunds.Amount > 0
  AND StatusOfFunds.BudgetLevel = '7'
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundCode, StatusOfFunds.FundName,
		 StatusOfFunds.ProgramProjectCode, StatusOfFunds.ProgramProjectName
ORDER BY StatusOfFunds.BFY DESC, StatusOfFunds.FundCode, StatusOfFunds.ProgramProjectName;

