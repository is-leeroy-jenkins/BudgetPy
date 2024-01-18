INSERT INTO PayrollAccruals
SELECT DISTINCTROW PayrollObligations.RPIO AS RPIO, PayrollObligations.AhCode AS AhCode,
	   PayrollObligations.BFY                             AS BFY,
	   PayrollObligations.RcCode                          AS RcCode,
	   PayrollObligations.DivisionName                    AS DivisionName,
	   PayrollHours.EpaNumber                             AS EpaNumber,
	   PayrollHours.LastName                              AS LastName,
	   PayrollHours.FirstName                             AS FirstName,
	   PayrollObligations.FundCode                        AS FundCode,
	   PayrollObligations.FundName                        AS FundName,
	   PayrollObligations.OrgCOde                         AS OrgCOde,
	   PayrollObligations.AccountCode                     AS AccountCode,
	   PayrollObligations.ProgramProjectCode              AS ProgramProjectCode,
	   PayrollObligations.ProgramProjectName              AS ProgramProjectName,
	   PayrollObligations.WorkCode                        AS WorkCode,
	   PayrollObligations.HrOrgCode                       AS HrOrgCode,
	   PayrollObligations.PayPeriod                       AS PayPeriod,
	   PayrollHours.StartDate                             AS StartDate,
	   PayrollHours.EndDate                               AS EndDate,
	   ROUND( PayrollObligations.Amount, 2 )              AS Amount,
	   ROUND( PayrollObligations.Hours, 2 )               AS Hours,
	   ROUND( PayrollObligations.CumulativeBenefits, 2 )  AS Benefits,
	   ROUND( PayrollObligations.AnnualOvertimePaid, 2 )  AS OvertimePaid,
	   ROUND( PayrollObligations.AnnualOvertimeHours, 2 ) AS OvertimeHours
FROM PayrollObligations
		 INNER JOIN PayrollHours
					ON (PayrollObligations.HrOrgCode = PayrollHours.HrOrgCode)
						AND (PayrollObligations.WorkCode = PayrollHours.WorkCode)
						AND (PayrollObligations.PayPeriod = PayrollHours.PayPeriod)
GROUP BY PayrollObligations.RPIO, PayrollObligations.AhCode, PayrollObligations.BFY,
		 PayrollObligations.RcCode, PayrollObligations.DivisionName, PayrollHours.EpaNumber,
		 PayrollHours.LastName, PayrollHours.FirstName, PayrollObligations.FundCode,
		 PayrollObligations.FundName, PayrollObligations.OrgCOde, PayrollObligations.AccountCode,
		 PayrollObligations.ProgramProjectCode, PayrollObligations.ProgramProjectName,
		 PayrollObligations.WorkCode, PayrollObligations.HrOrgCode, PayrollObligations.PayPeriod,
		 PayrollHours.StartDate, PayrollHours.EndDate, PayrollObligations.Amount,
		 PayrollObligations.Hours, PayrollObligations.CumulativeBenefits,
		 PayrollObligations.AnnualOvertimePaid, PayrollObligations.AnnualOvertimeHours
HAVING PayrollObligations.BFY = 2021;

