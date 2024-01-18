PARAMETERS RcCodeArgs LongText;
SELECT DivisionExecution.BFY,
	   DivisionExecution.RcCode,
	   DivisionExecution.DivisionName,
	   DivisionExecution.ProgramProjectName,
	   DivisionExecution.AccountCode,
	   Sum( DivisionExecution.Amount )          AS Authority,
	   Sum( DivisionExecution.OpenCommitments ) AS [Open Commitments],
	   Sum( DivisionExecution.Obligations )     AS Obligations,
	   Sum( DivisionExecution.Used )            AS Used,
	   DivisionExecution.Available
FROM DivisionExecution
WHERE (((DivisionExecution.Amount) > 0))
  AND DivisionExecution.RcCode = [RcCodeArgs]
GROUP BY DivisionExecution.BFY, DivisionExecution.RcCode, DivisionExecution.DivisionName,
		 DivisionExecution.ProgramProjectName, DivisionExecution.AccountCode,
		 DivisionExecution.Available
ORDER BY DivisionExecution.BFY DESC;