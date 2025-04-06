PARAMETERS RcCodeArgs TEXT(255);
SELECT DivisionExecution.BFY,
	   DivisionExecution.AhCode,
	   DivisionExecution.FundCode,
	   DivisionExecution.AccountCode,
	   DivisionExecution.ProgramProjectCode,
	   DivisionExecution.OrgCode,
	   DivisionExecution.BocCode,
	   DivisionExecution.RcCode,
	   DivisionExecution.Amount AS Authority,
	   DivisionExecution.OpenCommitments,
	   DivisionExecution.Obligations,
	   DivisionExecution.Used,
	   DivisionExecution.Available,
	   DivisionExecution.FundName,
	   DivisionExecution.ProgramProjectName,
	   DivisionExecution.BocName,
	   DivisionExecution.DivisionName
FROM DivisionExecution
WHERE DivisionExecution.BocCode <> '10'
  AND DivisionExecution.RcCode = [RcCodeArgs]
ORDER BY DivisionExecution.BFY DESC, DivisionExecution.FundCode,
		 DivisionExecution.AccountCode, DivisionExecution.BocCode;