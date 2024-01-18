UPDATE StateGrantObligations
	INNER JOIN Organizations
ON Organizations.Code = StateGrantObligations.OrgCode
SET StateGrantObligations.OrgName = Organizations.Name WHERE StateGrantObligations.OrgName <> Organizations.Code;