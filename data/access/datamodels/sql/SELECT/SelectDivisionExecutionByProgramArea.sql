SELECT DISTINCT DivisionExecution.BFY,
				DivisionExecution.RcCode,
				DivisionExecution.DivisionName,
				DivisionExecution.FundCode,
				DivisionExecution.FundName,
				DivisionExecution.ProgramAreaCode,
				DivisionExecution.ProgramAreaName,
				DivisionExecution.ProgramProjectCode,
				DivisionExecution.ProgramProjectName,
				CCur( Sum( DivisionExecution.Amount ) )          AS Amount,
				CCur( Sum( DivisionExecution.OpenCommitments ) ) AS OpenCommitments,
				CCur( Sum( DivisionExecution.Obligations ) )     AS Obligations,
				CCur( Sum( DivisionExecution.Used ) )            AS Used,
				CCur( Sum( DivisionExecution.Available ) )       AS Available
FROM DivisionExecution
WHERE DivisionExecution.Amount > 0
  AND DivisionExecution.RcCode NOT IN ( '06', '06R' )
GROUP BY DivisionExecution.BFY, DivisionExecution.RcCode,
		 DivisionExecution.DivisionName, DivisionExecution.FundCode,
		 DivisionExecution.FundName, DivisionExecution.ProgramAreaCode,
		 DivisionExecution.ProgramAreaName, DivisionExecution.ProgramProjectCode,
		 DivisionExecution.ProgramAreaName, DivisionExecution.ProgramProjectCode,
		 DivisionExecution.ProgramProjectName
ORDER BY DivisionExecution.BFY DESC,
		 DivisionExecution.RcCode, DivisionExecution.FundCode,
		 DivisionExecution.ProgramAreaCode, DivisionExecution.ProgramProjectCode;