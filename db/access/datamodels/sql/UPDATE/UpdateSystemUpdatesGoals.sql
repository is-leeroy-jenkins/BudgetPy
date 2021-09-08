UPDATE SystemUpdates 
INNER JOIN Goals 
ON LEFT(SystemUpdates.AccountCode, 1) = Goals.Code 
SET SystemUpdates.GoalCode = Goals.Code, 
    SystemUpdates.GoalName = Goals.Name
WHERE (IsNull(SystemUpdates.GoalCode)
    OR IsNull(SystemUpdates.GoalName));