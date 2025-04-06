PARAMETERS RcCodeArgs LongText;
SELECT DISTINCTROW Purchases.RpioCode, Purchases.AhCode,
	   Purchases.BFY,
	   Purchases.FundCode,
	   Purchases.AccountCode,
	   Purchases.BocCode,
	   Purchases.RcCode,
	   Sum( Purchases.OpenCommitments )                  AS OpenCommitments,
	   Sum( Purchases.ULO )                              AS ULO,
	   Sum( Purchases.Deobligations )                    AS Deobligations,
	   Sum( Purchases.Obligations )                      AS Obligations,
	   Purchases.OpenCommitments + Purchases.Obligations AS Used,
	   Purchases.ProgramProjectName,
	   Purchases.BocName,
	   Purchases.AhName,
	   Purchases.OrgCode,
	   DivisionAuthority.Amount,
	   Purchases.OriginalActionDate,
	   Purchases.FundName,
	   Purchases.DocumentControlNumbers                  AS DCN
FROM DivisionAuthority
		 INNER JOIN Purchases
					ON (DivisionAuthority.BFY = Purchases.BFY)
						AND (DivisionAuthority.FundCode = Purchases.FundCode)
						AND (DivisionAuthority.AhCode = Purchases.AhCode)
						AND (DivisionAuthority.AccountCode = Purchases.AccountCode)
						AND (DivisionAuthority.BocCode = Purchases.BocCode)
						AND (DivisionAuthority.RcCode = Purchases.RcCode)
GROUP BY Purchases.RpioCode, Purchases.AhCode, Purchases.BFY, Purchases.FundCode,
		 Purchases.AccountCode, Purchases.BocCode, Purchases.RcCode,
		 Purchases.OpenCommitments + Purchases.Obligations, Purchases.ProgramProjectName,
		 Purchases.BocName, Purchases.AhName, Purchases.OrgCode, DivisionAuthority.Amount,
		 Purchases.OriginalActionDate, Purchases.FundName, Purchases.DocumentControlNumbers,
		 DivisionAuthority.BFY
HAVING (((Purchases.RcCode) = [RcCodeArgs])
	AND ((DivisionAuthority.BFY) = [Purchases].[BFY]));
