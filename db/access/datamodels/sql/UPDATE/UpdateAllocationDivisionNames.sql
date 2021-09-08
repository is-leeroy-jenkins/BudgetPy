UPDATE Allocations 
INNER JOIN Divisions 
ON Divisions.Code = Allocations.RcCode 
SET Allocations.DivisionName = Divisions.Title
WHERE Allocations.RcCode = Divisions.Code;
