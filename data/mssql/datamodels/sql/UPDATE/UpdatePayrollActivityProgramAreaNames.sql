UPDATE PayrollActivity
	INNER JOIN ProgramAreas
ON ProgramAreas.ProgramAreaCode = PayrollActivity.ProgramAreaCode
SET PayrollActivity.ProgramAreaName = ProgramAreas.ProgramAreaName WHERE PayrollActivity.ProgramAreaCode = ProgramAreas.ProgramAreaCode
AND IsNull(PayrollActivity.ProgramAreaName);
