SELECT StatusOfFunds.BudgetLevel,
	   StatusOfFunds.BFY,
	   StatusOfFunds.AhCode,
	   StatusOfFunds.FundCode,
	   StatusOfFunds.OrgCode,
	   StatusOfFunds.AccountCode,
	   StatusOfFunds.ProgramProjectCode,
	   StatusOfFunds.ProgramProjectName,
	   StatusOfFunds.ProgramAreaCode,
	   StatusOfFunds.ProgramAreaName,
	   StatusOfFunds.BocCode,
	   StatusOfFunds.LowerName
FROM StatusOfFunds
WHERE (((StatusOfFunds.BudgetLevel) = '7')
	AND ((StatusOfFunds.BocCode) <> '17'))
ORDER BY StatusOfFunds.BFY DESC, StatusOfFunds.FundCode, StatusOfFunds.AccountCode,
		 StatusOfFunds.BocCode;