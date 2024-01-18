INSERT INTO HumanResourceOrganizations
SELECT DISTINCT PayrollHours.HrOrgCode AS Code, PayrollHours.HrOrgName AS Name
FROM PayrollHours
WHERE NOT IsNull( PayrollHours.HrOrgCode );
