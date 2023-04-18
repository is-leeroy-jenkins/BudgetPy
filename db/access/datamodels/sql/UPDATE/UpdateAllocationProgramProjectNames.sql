UPDATE Allocations 
INNER JOIN ProgramProjects 
ON ProgramProjects.Code = Allocations.ProgramProjectCode
SET Allocations.ProgramProjectName = ProgramProjects.Name;