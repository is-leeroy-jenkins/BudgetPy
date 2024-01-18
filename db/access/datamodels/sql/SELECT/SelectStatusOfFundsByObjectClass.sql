SELECT StatusOfFunds.BFY                                               AS BFY,
	   StatusOfFunds.FundCode                                          AS FundCode,
	   StatusOfFunds.FundName                                          AS FundName,
	   StatusOfFunds.BocCode                                           AS BocCode,
	   StatusOfFunds.BocName                                           AS BocName,
	   CCur( Sum( StatusOfFunds.Amount ) )                             AS Amount,
	   CCur( Sum( StatusOfFunds.OpenCommitments ) )                    AS OpenCommitments,
	   CCur( Sum( StatusOfFunds.Obligations ) )                        AS Obligations,
	   CCur( Sum( StatusOfFunds.Used ) )                               AS Used,
	   CCur( Sum( StatusOfFunds.Amount ) - Sum( StatusOfFunds.Used ) ) AS Available
FROM StatusOfFunds
WHERE (((StatusOfFunds.BudgetLevel) = '7'))
GROUP BY StatusOfFunds.BFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.BocCode,
		 StatusOfFunds.BocName
ORDER BY StatusOfFunds.BFY DESC, StatusOfFunds.BocCode;