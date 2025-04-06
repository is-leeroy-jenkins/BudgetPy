INSERT INTO PayPeriods
SELECT DISTINCT RIGHT( PayrollActivity.PayPeriod, 2 ) AS Period,
				PayrollActivity.PayPeriod             AS PayPeriod,
				PayrollActivity.StartDate             AS StartDate,
				PayrollActivity.EndDate               AS EndDate
FROM PayrollActivity
WHERE NOT IsNull( PayrollActivity.PayPeriod )
ORDER BY ExternalPayrollHours.PayPeriod;
