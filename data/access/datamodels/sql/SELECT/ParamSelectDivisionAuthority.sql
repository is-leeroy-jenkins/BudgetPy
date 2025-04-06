PARAMETERS RcCodeArgs TEXT(255);
SELECT DISTINCT DivisionAuthority.PrcId                 AS ID,
				DivisionAuthority.BFY,
				DivisionAuthority.DivisionName,
				DivisionAuthority.RcCode,
				DivisionAuthority.FundCode,
				DivisionAuthority.FundName,
				DivisionAuthority.AccountCode,
				DivisionAuthority.ProgramProjectName,
				DivisionAuthority.BocName,
				CCUR( Sum( DivisionAuthority.Amount ) ) AS Amount
FROM DivisionAuthority
WHERE (((DivisionAuthority.Amount) > 0))
GROUP BY DivisionAuthority.PrcId, DivisionAuthority.BFY, DivisionAuthority.DivisionName,
		 DivisionAuthority.RcCode, DivisionAuthority.FundCode, DivisionAuthority.FundName,
		 DivisionAuthority.AccountCode, DivisionAuthority.ProgramProjectName,
		 DivisionAuthority.BocName
HAVING (((Sum( DivisionAuthority.Amount )) > 0))
   AND DivisionAuthority.RcCode = [RcCodeArgs]
ORDER BY DivisionAuthority.BFY DESC;