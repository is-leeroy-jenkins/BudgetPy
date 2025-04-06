INSERT INTO HumanResourceOrganizations (RcCode, DivisionName, HrOrgCode, HrOrgName)
SELECT DISTINCT PayrollObligations.RcCode,
				PayrollObligations.DivisionName,
				PayrollHours.HrOrgCode,
				PayrollHours.HrOrgName
FROM PayrollHours
		 INNER JOIN PayrollObligations
					ON (PayrollHours.RpioCode = PayrollObligations.RPIO)
						AND (PayrollHours.PayPeriod = PayrollObligations.PayPeriod)
						AND (PayrollHours.HrOrgCode = PayrollObligations.HrOrgCode)
WHERE (((IsNull( [PayrollHours].[HrOrgCode] )) = False));
