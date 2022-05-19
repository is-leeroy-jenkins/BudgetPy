INSERT INTO PeoplePlus ( RcCode, DivisionName, EpaNumber, LastName, FirstName, ReportingCode, ReportingCodeName, HrOrgCode, WorkCode, PayPeriod, StartDate, EndDate, Hours )
SELECT DivisionPersonnel.RcCode, DivisionPersonnel.DivisionName, PayrollHours.EpaNumber, PayrollHours.LastName, PayrollHours.FirstName, PayrollHours.ReportingCode, PayrollHours.ReportingCodeName, PayrollHours.WorkCode, PayrollHours.HrOrgCode, PayrollHours.PayPeriod, PayrollHours.StartDate, PayrollHours.EndDate, 
Sum(PayrollHours.Hours) AS Hours
FROM Divisions 
INNER JOIN (PayrollHours 
    INNER JOIN DivisionPersonnel
     ON (PayrollHours.EpaNumber = DivisionPersonnel.EmployeeId) 
     AND (PayrollHours.LastName = DivisionPersonnel.LastName) 
     AND (PayrollHours.FirstName = DivisionPersonnel.FirstName)) 
     ON Divisions.Code = DivisionPersonnel.RcCode
GROUP BY DivisionPersonnel.RcCode, DivisionPersonnel.DivisionName, PayrollHours.EpaNumber, PayrollHours.LastName, PayrollHours.FirstName, PayrollHours.ReportingCode, PayrollHours.ReportingCodeName, PayrollHours.WorkCode, PayrollHours.HrOrgCode, PayrollHours.PayPeriod, PayrollHours.StartDate, PayrollHours.EndDate, PayrollHours.Hours;
