INSERT INTO DeobligationActivity
SELECT DISTINCT Deobligations.BFY                            AS BFY,
				Deobligations.EFY                            AS EFY,
				Deobligations.TreasuryAccountCode            AS TreasuryAccountCode,
				Deobligations.BudgetAccountCode              AS BudgetAccountCode,
				Deobligations.FundCode                       AS FundCode,
				Deobligations.FundName                       AS FundName,
				Deobligations.RpioCode                       AS RpioCode,
				Deobligations.RpioName                       AS RpioName,
				Deobligations.AhCode                         AS AhCode,
				Deobligations.AhName                         AS AhName,
				Deobligations.OrgCode                        AS OrgCode,
				Deobligations.OrgName                        AS OrgName,
				Deobligations.AccountCode                    AS AccountCode,
				Deobligations.ProgramProjectName             AS ProgramProjectName,
				Deobligations.BocCode                        AS BocCode,
				Deobligations.BocName                        AS BocName,
				Deobligations.DocumentNumber                 AS DocumentNumber,
				Deobligations.ProcessedDate                  AS ProcessedDate,
				Sum( CCur( Nz( Deobligations.Amount, 0 ) ) ) AS Amount
FROM Deobligations
GROUP BY Deobligations.BFY, Deobligations.EFY, Deobligations.TreasuryAccountCode,
		 Deobligations.BudgetAccountCode, Deobligations.FundCode, Deobligations.FundName,
		 Deobligations.RpioCode, Deobligations.RpioName, Deobligations.AhCode, Deobligations.AhName,
		 Deobligations.OrgCode, Deobligations.OrgName, Deobligations.AccountCode,
		 Deobligations.ProgramProjectName, Deobligations.BocCode, Deobligations.BocName,
		 Deobligations.DocumentNumber, Deobligations.ProcessedDate
HAVING Deobligations.BocCode <> "10"
   AND Deobligations.RpioCode NOT IN ( "92", "94", "95" )
   AND Sum( CCur( Nz( Deobligations.Amount, 0 ) ) ) > 0
ORDER BY Deobligations.ProcessedDate DESC;