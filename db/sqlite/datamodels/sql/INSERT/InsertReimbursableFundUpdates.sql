INSERT INTO ReportingCodes
SELECT DISTINCT PayrollHours.ReportingCode AS ReportingCode, PayrollHours.ReportingCodeName AS ReportingCodeName
FROM PayrollHours
WHERE NOT IsNull(PayrollHours.ReportingCode);
