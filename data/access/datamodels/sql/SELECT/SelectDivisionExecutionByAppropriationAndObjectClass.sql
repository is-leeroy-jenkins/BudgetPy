SELECT DivisionExecution.BFY,
	   DivisionExecution.RcCode,
	   DivisionExecution.DivisionName,
	   DivisionExecution.FundCode,
	   DivisionExecution.FundName,
	   DivisionExecution.BocCode,
	   DivisionExecution.BocName,
	   Sum( DivisionExecution.Amount )    AS Authority,
	   SUM( DivisionExecution.Used )      AS Used,
	   SUM( DivisionExecution.Available ) AS Available
FROM DivisionExecution
WHERE DivisionExecution.BFY = '2021'
GROUP BY DivisionExecution.BFY, DivisionExecution.RcCode,
		 DivisionExecution.DivisionName, DivisionExecution.FundCode,
		 DivisionExecution.FundName, DivisionExecution.BocCode, DivisionExecution.BocName;
