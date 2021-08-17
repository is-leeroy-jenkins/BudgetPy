UPDATE PayrollAccruals 
INNER JOIN ProgramAreas 
ON ProgramAreas.ProgramAreaCode = PayrollAccruals.ProgramAreaCode 
SET PayrollAccruals.ProgramAreaName = ProgramAreas.ProgramAreaName
WHERE PayrollAccruals.ProgramAreaCode = ProgramAreas.ProgramAreaCode
AND IsNull(PayrollAccruals.ProgramAreaName);