PARAMETERS RcCodeArgs LongText;
SELECT DISTINCTROW PayrollHours.EpaNumber, PayrollHours.LastName,
	   PayrollHours.FirstName,
	   DivisionPersonnel.RcCode,
	   DivisionPersonnel.DivisionName,
	   PayrollHours.PayPeriod,
	   Right( PayrollHours.PayPeriod, 2 ) AS Period,
	   PayrollHours.StartDate,
	   PayrollHours.EndDate,
	   PayrollHours.ReportingCodeName,
	   Sum( PayrollHours.Hours )          AS Hours,
	   Round( Hours / 8, 2 )              AS WorkDays,
	   DivisionPersonnel.JobTitle,
	   DivisionPersonnel.Grade,
	   DivisionPersonnel.Step
FROM DivisionPersonnel
		 INNER JOIN PayrollHours ON (DivisionPersonnel.EmployeeId = PayrollHours.EpaNumber) AND
									(DivisionPersonnel.EmployeeId = PayrollHours.EpaNumber)
GROUP BY PayrollHours.EpaNumber, PayrollHours.LastName, PayrollHours.FirstName,
		 DivisionPersonnel.RcCode, DivisionPersonnel.DivisionName, PayrollHours.PayPeriod,
		 Right( PayrollHours.PayPeriod, 2 ), PayrollHours.StartDate, PayrollHours.EndDate,
		 PayrollHours.ReportingCodeName, Round( Hours / 8, 2 ), DivisionPersonnel.JobTitle,
		 DivisionPersonnel.Grade, DivisionPersonnel.Step, DivisionPersonnel.EmployeeId
HAVING (((DivisionPersonnel.RcCode) = RcCodeArgs) And
		((DivisionPersonnel.EmployeeId) = PayrollHours.EpaNumber));
