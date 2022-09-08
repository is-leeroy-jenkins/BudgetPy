SELECT OperatingPlans.BFY AS BFY, OperatingPlans.FundCode AS FundCode, OperatingPlans.FundName AS FundName, Sum(CCur(OperatingPlans.Amount)) AS Authority
FROM OperatingPlans
WHERE OperatingPlans.Amount > 0 AND OperatingPlans.FundCode <> 'WR'
GROUP BY OperatingPlans.BFY, OperatingPlans.FundCode, OperatingPlans.FundName
ORDER BY OperatingPlans.FundCode, OperatingPlans.BFY DESC;

