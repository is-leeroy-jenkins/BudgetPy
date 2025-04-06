SELECT OperatingPlans.BFY,
	   OperatingPlans.NpmCode,
	   OperatingPlans.NpmName,
	   OperatingPlans.BocCode,
	   OperatingPlans.BocName,
	   Sum( CCur( [Amount] ) ) AS Amount,
	   OperatingPlans.FundCode,
	   Funds.Title             As FundName,
	   NationalPrograms.Name   As NpmName
FROM Funds
		 INNER JOIN (NationalPrograms
	INNER JOIN OperatingPlans
					 ON NationalPrograms.Code = OperatingPlans.NpmCode)
					ON Funds.Code = OperatingPlans.FundCode
GROUP BY OperatingPlans.BFY, OperatingPlans.NpmCode, OperatingPlans.NpmName, OperatingPlans.BocCode,
		 OperatingPlans.BocName, OperatingPlans.FundCode, Funds.Title, NationalPrograms.Name
HAVING (((OperatingPlans.BocCode) <> '17')
	AND ((Sum( CCur( [Amount] ) )) > 0));