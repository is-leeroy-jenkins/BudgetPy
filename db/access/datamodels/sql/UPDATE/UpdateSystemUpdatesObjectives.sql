UPDATE SystemUpdates 
INNER JOIN Objectives 
ON RIGHT(LEFT(SystemUpdates.AccountCode, 3), 2) = Objectives.Code 
SET SystemUpdates.ObjectiveCode = Objectives.Code, 
    SystemUpdates.ObjectiveName = Objectives.Name
WHERE (IsNull(SystemUpdates.ObjectiveCode)
    OR IsNull(SystemUpdates.ObjectiveName));