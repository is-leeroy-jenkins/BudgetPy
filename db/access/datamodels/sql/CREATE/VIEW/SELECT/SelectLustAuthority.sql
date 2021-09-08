SELECT OperatingPlan.BFY, OperatingPlan.BocName, OperatingPlan.BocCode, Sum(CCur([Amount])) AS Authority
FROM OperatingPlan
GROUP BY OperatingPlan.BFY, OperatingPlan.BocName, OperatingPlan.BocCode
HAVING (((OperatingPlan.BocCode)<>'17') AND ((Sum(CCur([Amount])))>0))
ORDER BY OperatingPlan.BocCode, OperatingPlan.BocName, OperatingPlan.BFY DESC;