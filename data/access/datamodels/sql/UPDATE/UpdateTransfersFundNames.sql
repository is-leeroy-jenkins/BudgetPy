UPDATE Transfers
	INNER JOIN ProgramAreas
ON Transfers.ProgramAreaCode = ProgramAreas.Code
SET Transfers.ProgramAreaName = ProgramAreas.Name WHERE Transfers.ProgramAreaCode = ProgramAreas.Code 
AND Transfers.ProgramAreaName <> ProgramAreas.Name;