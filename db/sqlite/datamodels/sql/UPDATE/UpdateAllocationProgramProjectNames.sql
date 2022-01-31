UPDATE Allocations 
INNER JOIN ProgramProjects 
ON ProgramProjects.Code = Allocations.ProgramProjectCode
SET Allocations.ProgramProjectName = ProgramProjects.Name
WHERE Allocations.ProgramProjectCode = ProgramProjects.Code
AND Allocations.ProgramProjectName <> ProgramProjects.Name;