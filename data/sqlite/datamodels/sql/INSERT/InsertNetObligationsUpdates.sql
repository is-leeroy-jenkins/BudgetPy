INSERT INTO NetObligations
SELECT DISTINCTROW StatusOfFunds.BFY AS BFY, StatusOfFunds.EFY AS EFY,
	   StatusOfFunds.FundCode                                                    AS FundCode,
	   StatusOfFunds.FundName                                                    AS FundName,
	   StatusOfFunds.RpioCode                                                    AS RpioCode,
	   StatusOfFunds.RpioName                                                    AS RpioName,
	   StatusOfFunds.AhCode                                                      AS AhCode,
	   StatusOfFunds.AhName                                                      AS AhName,
	   StatusOfFunds.OrgCode                                                     AS OrgCode,
	   StatusOfFunds.OrgName                                                     AS OrgName,
	   StatusOfFunds.AccountCode                                                 AS AccountCode,
	   StatusOfFunds.ProgramProjectName                                          AS ProgramProjectName,
	   StatusOfFunds.BocCode                                                     AS BocCode,
	   StatusOfFunds.BocName                                                     AS BocName,
	   Sum( CCur( Nz( StatusOfFunds.Budgeted ) ) )                               AS Budgeted,
	   Sum( CCur( Nz( StatusOfFunds.OpenCommitments ) ) )                        AS OpenCommitments,
	   Sum( CCur( Nz( StatusOfFunds.Obligations ) ) )                            AS Obligations,
	   Sum( CCur( Nz( StatusOfFunds.ULO ) ) )                                    AS UnliquidatedObligations,
	   Sum( CCur( Nz( StatusOfFunds.Used ) ) )                                   AS Used,
	   Sum( CCur( Nz( StatusOfFunds.Available ) ) )                              AS Available,
	   IIF( Obligations.DocumentNumber IS NULL, "NS",
			Obligations.DocumentNumber )                                         AS DocumentNumber,
	   IIF( Obligations.ProcessedDate IS NULL, "NS", Obligations.ProcessedDate ) AS ProcessedDate,
	   IIF( SUM( Obligations.Obligations ) > 0, "DECREASE", "ZERO" )             AS Net,
	   SUM( CCur( Nz( Obligations.Obligations ) ) )                              AS Amount
FROM StatusOfFunds
		 LEFT JOIN Obligations
				   ON (StatusOfFunds.BocCode = Obligations.BocCode)
					   AND (StatusOfFunds.OrgCode = Obligations.OrgCode)
					   AND (StatusOfFunds.AccountCode = Obligations.AccountCode)
					   AND (StatusOfFunds.AhCode = Obligations.AhCode)
					   AND (StatusOfFunds.RpioCode = Obligations.RpioCode)
					   AND (StatusOfFunds.FundCode = Obligations.FundCode)
					   AND (StatusOfFunds.BFY = Obligations.BFY)
					   AND (StatusOfFunds.EFY = Obligations.EFY)
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName,
		 StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName,
		 StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode,
		 StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName,
		 IIF( Obligations.DocumentNumber IS NULL, "NS", Obligations.DocumentNumber ),
		 IIF( Obligations.ProcessedDate IS NULL, "NS", Obligations.ProcessedDate ),
		 IIF( Obligations.Obligations > 0, "DECREASE", "ZERO" )
HAVING StatusOfFunds.RpioCode NOT IN ( "92", "94", "95" )
   AND StatusOfFunds.BocCode <> "10"
ORDER BY StatusOfFunds.BFY DESC,
		 IIF( Obligations.ProcessedDate IS NULL, "NS", Obligations.ProcessedDate ) DESC;