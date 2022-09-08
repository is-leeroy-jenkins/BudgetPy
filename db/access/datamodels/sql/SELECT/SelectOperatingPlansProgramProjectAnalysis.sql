SELECT OperatingPlans.BFY, OperatingPlans.ProgramProjectCode, OperatingPlans.ProgramProjectName, Sum(CCur(OperatingPlans.Amount)) AS Authority
FROM OperatingPlans
WHERE OperatingPlans.Amount <>0
GROUP BY OperatingPlans.BFY, OperatingPlans.ProgramProjectCode, OperatingPlans.ProgramProjectName
ORDER BY OperatingPlans.ProgramProjectCode, OperatingPlans.BFY DESC;
