UPDATE Transfers 
INNER JOIN ResourcePlanningOffices 
ON ResourcePlanningOffices.Code = Transfers.RpioCode 
SET Transfers.RpioName = ResourcePlanningOffices.Name
WHERE Transfers.RpioCode = ResourcePlanningOffices.Code
AND Transfers.RpioName <> ResourcePlanningOffices.Name;