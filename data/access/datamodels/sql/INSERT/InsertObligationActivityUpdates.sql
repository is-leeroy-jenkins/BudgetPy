INSERT INTO ObligationActivity
SELECT DISTINCT Obligations.BFY                                          AS BFY,
				Obligations.EFY                                          AS EFY,
				Obligations.FundCode                                     AS FundCode,
				Obligations.FundName                                     AS FundName,
				Obligations.TreasurySymbol                               AS TreasuryAccountCode,
				Obligations.BudgetAccountCode                            AS BudgetAccountCode,
				Obligations.RpioCode                                     AS RpioCode,
				Obligations.RpioName                                     AS RpioName,
				Obligations.AhCode                                       AS AhCode,
				Obligations.AhName                                       AS AhName,
				Obligations.OrgCode                                      AS OrgCode,
				Obligations.OrgName                                      AS OrgName,
				Obligations.AccountCode                                  AS AccountCode,
				Obligations.ProgramProjectName                           AS ProgramProjectName,
				Obligations.BocCode                                      AS BocCode,
				Obligations.BocName                                      AS BocName,
				Obligations.FocCode                                      AS FocCode,
				Obligations.FocName                                      AS FocName,
				Obligations.DocumentType                                 AS DocumentType,
				Obligations.DocumentNumber                               AS DocumentNumber,
				Obligations.ProcessedDate                                AS ProcessedDate,
				Sum( CCur( Nz( Obligations.OpenCommitments ) ) )         AS OpenCommitments,
				Sum( CCur( Nz( Obligations.Obligations ) ) )             AS Obligations,
				Sum( CCur( Nz( Obligations.OpenCommitments ) ) ) +
				Sum( CCur( Nz( Obligations.Obligations ) ) )             AS Used,
				Sum( CCur( Nz( Obligations.UnliquidatedObligations ) ) ) AS UnliquidatedObligations,
				Sum( CCur( Nz( Obligations.Expenditures ) ) )            AS Outlays
FROM Obligations
GROUP BY Obligations.BFY, Obligations.EFY, Obligations.FundCode, Obligations.FundName,
		 Obligations.TreasurySymbol, Obligations.BudgetAccountCode, Obligations.RpioCode,
		 Obligations.RpioName, Obligations.AhCode, Obligations.AhName, Obligations.OrgCode,
		 Obligations.OrgName, Obligations.AccountCode, Obligations.ProgramProjectName,
		 Obligations.BocCode, Obligations.BocName, Obligations.FocCode, Obligations.FocName,
		 Obligations.DocumentType, Obligations.DocumentNumber, Obligations.ProcessedDate
HAVING Obligations.RpioCode NOT IN ( "92", "94", "95" )
   AND Sum( CCur( Nz( Obligations.OpenCommitments ) ) ) +
	   Sum( CCur( Nz( Obligations.Obligations ) ) ) > 0
ORDER BY Obligations.ProcessedDate DESC;
