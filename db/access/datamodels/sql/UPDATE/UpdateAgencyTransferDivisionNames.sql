UPDATE AgencyTransfers 
INNER JOIN Divisions 
ON Divisions.Code = AgencyTransfers.RcCode 
SET AgencyTransfers.DivisionName = Divisions.Title
WHERE AgencyTransfers.RcCode = Divisions.Code
AND (AgencyTransfers.DivisionName <> Divisions.Title
    OR IsNull(AgencyTransfers.DivisionName));