UPDATE StateGrantObligations 
INNER JOIN ResourcePlanningOffices 
ON ResourcePlanningOffices.Code = StateGrantObligations.RpioCode 
SET StateGrantObligations.RpioName = ResourcePlanningOffices.Name
WHERE StateGrantObligations.RpioName <> ResourcePlanningOffices.Code;