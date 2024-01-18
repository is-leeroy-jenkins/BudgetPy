SELECT StatusOfFunds.BFY,
	   StatusOfFunds.FundName,
	   StatusOfFunds.FundCode,
	   StatusOfFunds.ProgramProjectName,
	   StatusOfFunds.AccountCode,
	   StatusOfFunds.BocName,
	   StatusOfFunds.BocCode,
	   Sum( StatusOfFunds.Amount )                AS Authority,
	   Sum( StatusOfFunds.OpenCommitments )       AS OpenCommitments,
	   Sum( StatusOfFunds.Obligations )           AS Obligations,
	   Sum( StatusOfFunds.Used )                  AS Used,
	   ROUND( Sum( StatusOfFunds.Available ), 2 ) AS Available
FROM StatusOfFunds
GROUP BY StatusOfFunds.BudgetLevel, StatusOfFunds.BFY, StatusOfFunds.FundName,
		 StatusOfFunds.FundCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.AccountCode,
		 StatusOfFunds.BocName, StatusOfFunds.BocCode
HAVING StatusOfFunds.BudgetLevel = "7"
ORDER BY StatusOfFunds.BFY DESC, StatusOfFunds.FundCode, StatusOfFunds.AccountCode,
		 StatusOfFunds.BocCode;
