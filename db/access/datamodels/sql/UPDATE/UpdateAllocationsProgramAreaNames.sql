UPDATE Allocations
	INNER JOIN ProgramAreas
ON ProgramAreas.ProgramAreaCode = Allocations.ProgramAreaCode
SET Allocations.ProgramAreaName = ProgramAreas.ProgramAreaName;