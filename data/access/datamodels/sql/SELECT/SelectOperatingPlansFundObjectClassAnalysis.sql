SELECT OperatingPlans.BFY,
	   OperatingPlans.FundCode,
	   OperatingPlans.FundName,
	   OperatingPlans.BocCode,
	   OperatingPlans.BocName,
	   Sum( CCur( [Amount] ) ) AS Authority
FROM OperatingPlans
GROUP BY OperatingPlans.BFY, OperatingPlans.FundCode, OperatingPlans.FundName,
		 OperatingPlans.BocCode, OperatingPlans.BocName
HAVING (((OperatingPlans.BocCode) <> '17')
	AND ((Sum( CCur( [Amount] ) )) > 0))
ORDER BY OperatingPlans.FundCode, OperatingPlans.BocCode, OperatingPlans.BFY DESC;