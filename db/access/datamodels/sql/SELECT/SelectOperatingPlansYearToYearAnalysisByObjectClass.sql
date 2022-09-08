SELECT OperatingPlans.BFY, OperatingPlans.BocName, OperatingPlans.BocCode, Sum(CCur([Amount])) AS Authority
FROM OperatingPlans
GROUP BY OperatingPlans.BFY, OperatingPlans.BocName, OperatingPlans.BocCode
HAVING (((OperatingPlans.BocCode)<>'17') 
AND ((Sum(CCur([Amount])))>0))
ORDER BY OperatingPlans.BocCode, OperatingPlans.BocName, OperatingPlans.BFY DESC;