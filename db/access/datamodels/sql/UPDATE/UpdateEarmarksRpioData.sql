UPDATE EarMarks
	INNER JOIN StateOrganizations
ON EarMarks.StateCode = StateOrganizations.Code
SET EarMarks.RpioCode = StateOrganizations.RpioCode, EarMarks.RpioName = StateOrganizations.RpioName
WHERE EarMarks.StateCode = StateOrganizations.Code;
