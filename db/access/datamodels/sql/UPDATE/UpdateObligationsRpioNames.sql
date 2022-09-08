UPDATE Obligations 
INNER JOIN ResourcePlanningOffices 
ON ResourcePlanningOffices.Code = Obligations.RpioCode 
SET Obligations.RpioName = ResourcePlanningOffices.Name
WHERE Obligations.RpioCode = ResourcePlanningOffices.Code
AND Obligations.RpioName <> ResourcePlanningOffices.Name;