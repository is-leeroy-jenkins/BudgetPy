INSERT INTO Employees
SELECT DISTINCT PayrollCostCodes.RcCode       AS RcCode,
				PayrollCostCodes.DivisionName AS DivisionName,
				PayrollHours.LastName         AS LastName,
				PayrollHours.FirstName        AS FirstName,
				PayrollHours.EpaNumber        AS EpaNumber
FROM PayrollCostCodes
		 INNER JOIN PayrollHours ON (PayrollCostCodes.HrOrgCode = PayrollHours.HrOrgCode) AND
									(PayrollCostCodes.WorkCode = PayrollHours.WorkCode)
WHERE PayrollHours.WorkCode = PayrollHours.HrOrgCode;