UPDATE PayrollObligations
	INNER JOIN ProgramProjects
ON ProgramProjects.Code = RIGHT (LEFT (PayrollObligations.AccountCode, 6), 2)
SET PayrollObligations.ProgramProjectName = ProgramProjects.Name WHERE RIGHT(LEFT(PayrollObligations.AccountCode, 6), 2) = ProgramProjects.Code
AND PayrollObligations.ProgramProjectName <> ProgramProjects.Name;