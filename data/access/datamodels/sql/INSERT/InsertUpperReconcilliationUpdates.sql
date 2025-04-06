INSERT INTO WorkCodes
SELECT DISTINCT PayrollObligations.RcCode       AS RcCode,
				PayrollObligations.DivisionName AS DivisionName,
				PayrollObligations.WorkCode     AS WorkCode,
				PayrollObligations.WorkCodeName AS WorkCodeName
FROM PayrollObligations
WHERE NOT IsNull( PayrollObligations.WorkCode );



