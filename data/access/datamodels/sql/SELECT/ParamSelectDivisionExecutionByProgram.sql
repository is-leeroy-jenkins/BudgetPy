PARAMETERS RcCodeArgs TEXT(255);
SELECT AvailableBalances.BFY,
	   AvailableBalances.RcCode,
	   AvailableBalances.DivisionName,
	   AvailableBalances.ProgramProjectName,
	   AvailableBalances.AccountCode,
	   Sum( AvailableBalances.Amount )          AS Authority,
	   Sum( AvailableBalances.OpenCommitments ) AS [Open Commitments],
	   Sum( AvailableBalances.Obligations )     AS Obligations,
	   Sum( AvailableBalances.Used )            AS Used,
	   AvailableBalances.Available
FROM AvailableBalances
WHERE (((AvailableBalances.Amount) > 0))
  AND AvailableBalances.RcCode = [RcCodeArgs]
GROUP BY AvailableBalances.BFY, AvailableBalances.RcCode, AvailableBalances.DivisionName,
		 AvailableBalances.ProgramProjectName, AvailableBalances.AccountCode,
		 AvailableBalances.Available
ORDER BY AvailableBalances.BFY DESC;
