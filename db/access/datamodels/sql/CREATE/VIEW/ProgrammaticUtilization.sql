
CREATE VIEW "ProgrammaticUtilization" 
AS SELECT DivisionExecution.BFY, DivisionExecution.AhCode, DivisionExecution.RcCode, DivisionExecution.DivisionName, DivisionExecution.FundCode, DivisionExecution.FundName, DivisionExecution.OrgCode, DivisionExecution.AccountCode, DivisionExecution.ProgramProjectName, 
Sum(DivisionExecution.Amount) AS Amount, 
Sum(DivisionExecution.OpenCommitments) AS OpenCommitments, 
Sum(DivisionExecution.Obligations) AS Obligations, 
Sum(DivisionExecution.Used) AS Used, 
Sum(DivisionExecution.Available) AS Available
FROM DivisionExecution
WHERE DivisionExecution.Available > 0
AND DivisionExecution.BocCode IN ('21', '28', '36', '37','38', '41')
GROUP BY DivisionExecution.BFY, DivisionExecution.AhCode, DivisionExecution.RcCode, DivisionExecution.DivisionName, DivisionExecution.FundCode, DivisionExecution.FundName, DivisionExecution.OrgCode, DivisionExecution.AccountCode, DivisionExecution.ProgramProjectName;
