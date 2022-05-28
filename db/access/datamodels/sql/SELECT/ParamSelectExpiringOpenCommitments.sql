PARAMETERS FiscalYearArgs Text ( 255 ), RcCodeArgs Text ( 255 ), FundCodeArgs Text ( 255 );
SELECT PayrollObligations.BFY, PayrollObligations.AhCode AS [AH Code], PayrollObligations.FundCode AS [Fund Code], PayrollObligations.AccountCode AS AccountCode, PayrollObligations.RcCode AS RcCode, Divisions.Title AS DivisionName, PayrollObligations.PayPeriod AS PayPeriod, PayrollHours.StartDate AS StartDate, PayrollHours.EndDate AS EndDate, PayrollObligations.FocCode AS FocCode, PayrollObligations.FocName AS FocName, PayrollObligations.WorkCode AS WorkCode, PayrollObligations.WorkCodeName AS WorkCodeName, PayrollHours.EmployeeNumber AS EmployeeNumber, PayrollHours.LastName AS LastName, PayrollHours.FirstName AS FirstName, PayrollHours.HumanResourceOrganizationCode AS HrOrgCode, \PayrollHours.HumanResourceOrganizationName AS HrOrgName, 
Sum(PayrollObligations.CumulativeBenefits) AS CumulativeBenefits, 
Sum(PayrollObligations.AnnualOvertimePaid) AS OvertimePaid, 
Sum(PayrollObligations.AnnualOvertimeHours) AS OvertimeHours, 
Sum(PayrollObligations.AnnualBasePaid) AS BasePaid, 
Sum(PayrollObligations.AnnualBaseHours) AS BaseHours, 
Sum(PayrollObligations.AnnualOtherPaid) AS OtherPaid, 
Sum(PayrollObligations.AnnualOtherHours) AS OtherHour], 
Sum(PayrollObligations.Amount) AS Obligations
FROM Divisions 
INNER JOIN (PayrollObligations 
    INNER JOIN PayrollHours 
        ON PayrollObligations.WorkCode = PayrollHours.WorkCode 
            AND PayrollObligations.HumanResourceOrganizationCode = PayrollHours.HumanResourceOrganizationCode 
            AND PayrollObligations.PayPeriod = PayrollHours.PayPeriod 
            AND PayrollObligations.RPIO = PayrollHours.RpioCode) 
                ON Divisions.Code = PayrollObligations.RcCode
GROUP BY PayrollObligations.BFY, PayrollObligations.AhCode, PayrollObligations.FundCode, PayrollObligations.AccountCode, PayrollObligations.RcCode, Divisions.Title, PayrollObligations.PayPeriod, PayrollHours.StartDate, PayrollHours.EndDate, PayrollObligations.FocCode, PayrollObligations.FocName, PayrollObligations.WorkCode, PayrollObligations.WorkCodeName, PayrollHours.EmployeeNumber, PayrollHours.LastName, PayrollHours.FirstName, PayrollHours.HumanResourceOrganizationCode, PayrollHours.HumanResourceOrganizationName, PayrollHours.ReportingCode, PayrollHours.ReportingCodeDescription
HAVING (PayrollObligations.BFY=[FiscalYearArgs] 
AND PayrollObligations.FundCode=[FundCodeArgs] 
AND PayrollObligations.RcCode=[RcCodeArgs]);