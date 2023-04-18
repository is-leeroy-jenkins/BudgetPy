UPDATE OperatingPlans 
INNER JOIN ResourcePlanningOffices 
ON OperatingPlans.RpioCode = ResourcePlanningOffices.Code 
SET OperatingPlans.RpioName = ResourcePlanningOffices.Name;
