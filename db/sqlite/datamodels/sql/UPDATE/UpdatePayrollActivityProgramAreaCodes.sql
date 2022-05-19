UPDATE PayrollActivity 
INNER JOIN ProgramDescriptions 
ON ProgramDescriptions.ProgramProjectCode = PayrollActivity.ProgramProjectCode 
SET PayrollActivity.ProgramAreaCode = ProgramDescriptions.ProgramAreaCode
WHERE PayrollActivity.ProgramProjectCode = ProgramDescriptions.ProgramProjectCode
AND IsNull(PayrollActivity.ProgramAreaCode);
