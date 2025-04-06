UPDATE PayrollObligations
	INNER JOIN Divisions
ON Divisions.Code = PayrollObligations.RcCode
SET PayrollObligations.DivisionName = Divisions.Title WHERE PayrollObligations.RcCode = Divisions.Code
AND (IsNull(PayrollObligations.DivisionName)
OR PayrollObligations.DivisionName <> Divisions.Title);