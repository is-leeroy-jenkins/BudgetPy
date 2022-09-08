UPDATE PayrollActivity 
INNER JOIN ProgramProjects 
ON PayrollActivity.ProgramProjectCode = ProgramProjects.Code 
SET PayrollActivity.ProgramProjectName = ProgramProjects.Name
WHERE PayrollActivity.ProgramProjectCode = ProgramProjects.Code;