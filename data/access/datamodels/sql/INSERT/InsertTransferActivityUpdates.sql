INSERT INTO TransferActivity
SELECT DISTINCT Transfers.BFY                                            AS BFY,
				Transfers.EFY                                            AS EFY,
				Transfers.FundCode                                       AS FundCode,
				Transfers.FundName                                       AS FundName,
				Transfers.RpioCode                                       AS RpioCode,
				Transfers.RpioName                                       AS RpioName,
				Transfers.AhCode                                         AS AhCode,
				Transfers.AhName                                         AS AhName,
				Transfers.OrgCode                                        AS OrgCode,
				Transfers.OrgName                                        AS OrgName,
				Transfers.AccountCode                                    AS AccountCode,
				Transfers.ProgramProjectName                             AS ProgramProjectName,
				Transfers.FromTo                                         AS FromTo,
				Transfers.BocCode                                        AS BocCode,
				Transfers.BocName                                        AS BocName,
				IIf( Transfers.ProcessedDate Is Null, "NS",
					 Transfers.ProcessedDate )                           AS ProcessedDate,
				IIf( Transfers.ReprogrammingNumber Is Null, "NS",
					 Transfers.ReprogrammingNumber )                     AS DocumentNumber,
				IIf( Transfers.FromTo = "FROM", "DECREASE", "INCREASE" ) AS Net,
				Sum( CCur( Nz( Transfers.Amount ) ) )                    AS Amount
FROM Transfers
GROUP BY Transfers.BFY, Transfers.EFY, Transfers.FundCode, Transfers.FundName, Transfers.RpioCode,
		 Transfers.RpioName, Transfers.AhCode, Transfers.AhName, Transfers.OrgCode,
		 Transfers.OrgName, Transfers.AccountCode, Transfers.ProgramProjectName, Transfers.FromTo,
		 Transfers.BocCode, Transfers.BocName,
		 IIf( Transfers.ReprogrammingNumber Is Null, "NS", Transfers.ReprogrammingNumber ),
		 IIf( Transfers.ProcessedDate Is Null, "NS", Transfers.ProcessedDate ),
		 IIf( Transfers.FromTo = "FROM", "DECREASE", "INCREASE" )
HAVING Transfers.RpioCode Not In ( "92", "94", "95" )
   AND ((Sum( CCur( Nz( [Transfers].[Amount] ) ) )) > 0)
ORDER BY IIf( Transfers.ProcessedDate Is Null, "NS", Transfers.ProcessedDate ) DESC;