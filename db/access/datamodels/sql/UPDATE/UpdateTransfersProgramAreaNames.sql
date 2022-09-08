UPDATE Transfers 
INNER JOIN ProgramProjects 
ON Transfers.ProgramProjectCode = ProgramProjects.Code 
SET Transfers.ProgramAreaName = ProgramProjects.Name
WHERE Transfers.ProgramProjectCode = ProgramProjects.Code 
AND Transfers.ProgramProjectName <> ProgramProjects.Name;