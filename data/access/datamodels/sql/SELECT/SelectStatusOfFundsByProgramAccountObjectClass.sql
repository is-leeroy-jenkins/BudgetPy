SELECT StatusOfFunds.BFY,
	   StatusOfFunds.RpioCode,
	   StatusOfFunds.RpioName,
	   StatusOfFunds.FundCode,
	   StatusOfFunds.FundName,
	   StatusOfFunds.NpmCode,
	   StatusOfFunds.NpmName,
	   StatusOfFunds.AccountCode,
	   StatusOfFunds.ProgramProjectCode,
	   StatusOfFunds.ProgramProjectName,
	   StatusOfFunds.ProgramAreaCode,
	   StatusOfFunds.ProgramAreaName,
	   StatusOfFunds.BocCode,
	   StatusOfFunds.BocName,
	   CCur( Sum( StatusOfFunds.Amount ) )                             AS Amount,
	   CCur( Sum( StatusOfFunds.OpenCommitments ) )                    AS OpenCommitments,
	   CCur( Sum( StatusOfFunds.Obligations ) )                        AS Obligations,
	   CCur( Sum( StatusOfFunds.Used ) )                               AS Used,
	   CCur( Sum( StatusOfFunds.Amount ) - Sum( StatusOfFunds.Used ) ) AS Available
FROM StatusOfFunds
WHERE StatusOfFunds.BudgetLevel = '7'
  AND StatusOfFunds.RpioCode NOT LIKE '9*'
GROUP BY StatusOfFunds.BFY, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode,
		 StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.NpmCode,
		 StatusOfFunds.NpmName, StatusOfFunds.OrgCode, StatusOfFunds.AccountCode,
		 StatusOfFunds.ProgramProjectCode, StatusOfFunds.ProgramProjectName,
		 StatusOfFunds.ProgramAreaCode, StatusOfFunds.ProgramAreaName, StatusOfFunds.BocCode,
		 StatusOfFunds.BocName;

