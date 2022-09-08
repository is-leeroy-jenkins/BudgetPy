SELECT OperatingPlans.BFY AS BFY, OperatingPlans.ProgramAreaCode AS ProgramAreaCode, OperatingPlans.ProgramAreaName AS ProgramAreaName, OperatingPlans.AccountCode AS AccountCode, OperatingPlans.ProgramProjectName AS ProgramProjectName, OperatingPlans.BocName AS BocName, OperatingPlans.BocCode AS BocCode, Sum(CCur([Amount])) AS Authority
FROM OperatingPlans
WHERE ((([OperatingPlans].[BocCode])<>'17'))
AND OperatingPlans.ProgramAreaCode <> 'NS'
GROUP BY OperatingPlans.BFY, OperatingPlans.ProgramAreaName, OperatingPlans.ProgramAreaCode, OperatingPlans.AccountCode, OperatingPlans.ProgramProjectName, OperatingPlans.BocName, OperatingPlans.BocCode
HAVING Sum(CCur( Amount ) )>0
ORDER BY OperatingPlans.AccountCode, OperatingPlans.BocCode, OperatingPlans.BFY DESC;
