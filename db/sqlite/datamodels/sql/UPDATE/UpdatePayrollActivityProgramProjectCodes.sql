UPDATE PayrollActivity 
SET PayrollActivity.ProgramProjectCode = 
Right(Left(PayrollActivity.AccountCode, 6), 2)
WHERE IsNull(PayrollActivity.ProgramProjectCode);
