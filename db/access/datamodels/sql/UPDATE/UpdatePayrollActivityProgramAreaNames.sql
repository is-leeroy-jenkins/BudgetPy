UPDATE PayrollActivity
	INNER JOIN ProgramAreas
ON ProgramAreas.Code = PayrollActivity.ProgramAreaCode
SET PayrollActivity.ProgramAreaName = ProgramAreas.Name WHERE PayrollActivity.ProgramAreaCode = ProgramAreas.Code;