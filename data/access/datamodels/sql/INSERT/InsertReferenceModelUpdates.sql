INSERT INTO CarryoverEstimates
SELECT StatusOfFunds.BudgetLevel                                AS BudgetLevel,
	   StatusOfFunds.BFY                                        AS BFY,
	   StatusOfFunds.AhCode                                     AS AhCode,
	   StatusOfFunds.FundCode                                   AS FundCode,
	   StatusOfFunds.FundName                                   AS FundName,
	   StatusOfFunds.OrgCode                                    AS OrgCode,
	   StatusOfFunds.AccountCode                                AS AccountCode,
	   StatusOfFunds.RcCode                                     AS RcCode,
	   StatusOfFunds.DivisionName                               AS DivisionName,
	   StatusOfFunds.BocCode                                    AS BocCode,
	   StatusOfFunds.BocName                                    AS BocName,
	   CCur( Sum( StatusOfFunds.Amount - StatusOfFunds.Used ) ) AS Balance,
	   CCur( Sum( StatusOfFunds.OpenCommitments ) )             AS OpenCommitments,
	   CCur( SUM( StatusOfFunds.Amount - StatusOfFunds.Used +
				  StatusOfFunds.OpenCommitments ) )             AS Estimate
FROM StatusOfFunds
WHERE (StatusOfFunds.FundCode <> 'B'
	AND StatusOfFunds.BudgetLevel = '7'
	AND StatusOfFunds.BFY IN ( '2020', '2021' )
	AND StatusOfFunds.BocCode <> '10'
	AND (StatusOfFunds.Amount - StatusOfFunds.Used > 0 OR StatusOfFunds.OpenCommitments > 0))
GROUP BY StatusOfFunds.BudgetLevel, StatusOfFunds.BFY, StatusOfFunds.AhCode, StatusOfFunds.FundCode,
		 StatusOfFunds.FundName, StatusOfFunds.OrgCode, StatusOfFunds.AccountCode,
		 StatusOfFunds.RcCode, StatusOfFunds.DivisionName, StatusOfFunds.BocCode,
		 StatusOfFunds.BocName;