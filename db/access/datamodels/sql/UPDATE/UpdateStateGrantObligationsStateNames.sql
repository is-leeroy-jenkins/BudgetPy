UPDATE StateGrantObligations 
INNER JOIN StateOrganizations 
ON StateGrantObligations.RpioCode = StateOrganizations.RpioCode 
SET StateGrantObligations.StateName = StateOrganizations.Name
WHERE StateGrantObligations.OrgCode = StateOrganizations.Code;