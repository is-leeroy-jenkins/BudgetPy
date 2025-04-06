UPDATE StateGrantObligations
	INNER JOIN StateOrganizations
ON StateGrantObligations.RpioCode = StateOrganizations.RpioCode
SET StateGrantObligations.StateCode = StateOrganizations.Code WHERE StateGrantObligations.OrgCode = StateOrganizations.Code;