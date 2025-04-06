INSERT INTO PayrollCostCodes
SELECT DISTINCT PayrollObligations.RcCode       AS RcCode,
				PayrollObligations.DivisionName AS DivisionName,
				PayrollObligations.HrOrgCode    AS HrOrgCode,
				PayrollObligations.WorkCode     AS WorkCode,
				PayrollObligations.WorkCodeName AS WorkCodeName
FROM PayrollObligations
WHERE NOT ISNULL( PayrollObligations.WorkCode )
ORDER BY PayrollObligations.RcCode;
