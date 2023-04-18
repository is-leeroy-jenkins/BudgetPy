UPDATE Obligations 
INNER JOIN ResourcePlanningOffices 
ON ResourcePlanningOffices.Code = Obligations.RpioCode 
SET Obligations.RpioName = ResourcePlanningOffices.Name;