UPDATE Allocations 
INNER JOIN ResourcePlanningOffices 
ON ResourcePlanningOffices.Code = Allocations.RpioCode 
SET Allocations.RpioName = ResourcePlanningOffices.Name;