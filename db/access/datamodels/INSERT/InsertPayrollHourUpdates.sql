INSERT INTO PayPeriods
SELECT DISTINCT RIGHT(PayPeriod, 2) AS Period, PayPeriod AS PayPeriod, StartDate AS StartDate, EndDate AS EndDate
FROM ExternalPayrollHours
WHERE NOT IsNull(PayPeriod)
ORDER BY ExternalPayrollHours.PayPeriod;

