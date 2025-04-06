PARAMETERS AhCodeArgs Text ( 255 ), FiscalYearArgs Text ( 255 ), RcCodeArgs Text ( 255 );
SELECT DISTINCT DivisionExecution.AhCode,
				DivisionExecution.RcCode,
				DivisionExecution.DivisionName,
				DivisionExecution.BFY,
				DivisionExecution.FundCode,
				DivisionExecution.FundName,
				DivisionExecution.AccountCode,
				DivisionExecution.ProgramProjectName,
				DivisionExecution.BocCode,
				DivisionExecution.BocName,
				CCur( Sum( DivisionExecution.Amount ) )          AS Authority,
				CCur( Sum( DivisionExecution.OpenCommitments ) ) AS OpenCommitments,
				CCur( Sum( DivisionExecution.Obligations ) )     AS Obligations,
				CCur( Sum( DivisionExecution.Used ) )            AS Used,
				CCur( DivisionExecution.Amount - DivisionExecution.OpenCommitments -
					  DivisionExecution.Obligations )            AS Available
FROM DivisionExecution
WHERE (DivisionExecution.Amount > 0
	AND DivisionExecution.FundCode = 'B')
GROUP BY DivisionExecution.AhCode, DivisionExecution.RcCode, DivisionExecution.DivisionName,
		 DivisionExecution.BFY, DivisionExecution.FundCode, DivisionExecution.FundName,
		 DivisionExecution.AccountCode, DivisionExecution.ProgramProjectName,
		 DivisionExecution.BocCode, DivisionExecution.BocName,
		 (DivisionExecution.Amount - DivisionExecution.OpenCommitments -
		  DivisionExecution.Obligations), DivisionExecution.DivisionName, DivisionExecution.FundCode
HAVING DivisionExecution.AhCode = [AhCodeArgs]
   AND DivisionExecution.BFY = [FiscalYearArgs]
   AND DivisionExecution.RcCode = [RcCodeArgs]
ORDER BY DivisionExecution.BFY DESC;
