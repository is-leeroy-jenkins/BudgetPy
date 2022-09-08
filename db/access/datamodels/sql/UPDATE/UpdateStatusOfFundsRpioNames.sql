UPDATE StatusOfFunds 
INNER JOIN ResourcePlanningOffices 
ON ResourcePlanningOffices.Code = StatusOfFunds.RpioCode 
SET StatusOfFunds.RpioName = ResourcePlanningOffices.Name
WHERE StatusOfFunds.RpioCode = ResourcePlanningOffices.Code
AND StatusOfFunds.RpioName <> ResourcePlanningOffices.Name;