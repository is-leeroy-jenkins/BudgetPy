UPDATE SystemUpdates 
INNER JOIN Divisions 
ON SystemUpdates.RcCode = Divisions.Code 
SET SystemUpdates.Division = Divisions.Caption, 
    SystemUpdates.DivisionName = Divisions.Title;