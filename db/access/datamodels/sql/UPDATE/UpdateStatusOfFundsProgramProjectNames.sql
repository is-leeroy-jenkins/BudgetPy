UPDATE StatusOfFunds
	INNER JOIN ProgramProjects
ON ProgramProjects.Code = StatusOfFunds.ProgramProjectCode
SET StatusOfFunds.ProgramProjectName = ProgramProjects.Name WHERE IsNull(StatusOfFunds.ProgramProjectName)
OR StatusOfFunds.ProgramProjectName <> ProgramProjects.Name;