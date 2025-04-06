INSERT INTO CarryoverEstimates
SELECT DISTINCT StatusOfFunds.BudgetLevel AS BudgetLevel, StatusOfFunds.BFY AS BFY, StatusOfFunds.AhCode AS AhCode, StatusOfFunds.FundCode AS FundCode, StatusOfFunds.FundName AS FundName, StatusOfFunds.OrgCode AS OrgCode, StatusOfFunds.AccountCode AS AccountCode, StatusOfFunds.RcCode AS RcCode, 'REGION 6' AS DivisionName, StatusOfFunds.BocCode AS BocCode, StatusOfFunds.BocName AS BocName, CCur(SUM(StatusOfFunds.Available)) AS Balance, CCur(Sum(StatusOfFunds.OpenCommitments)) AS OpenCommitments, CCur(SUM(StatusOfFunds.Available)) AS Estimate
FROM StatusOfFunds
WHERE (StatusOfFunds.BudgetLevel = '7'
AND StatusOfFunds.FundCode = 'B'
AND StatusOfFunds.BFY = '2021')
GROUP BY StatusOfFunds.BudgetLevel, StatusOfFunds.BFY, StatusOfFunds.AhCode, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.OrgCode, StatusOfFunds.AccountCode, StatusOfFunds.RcCode, StatusOfFunds.DivisionName, StatusOfFunds.BocCode, StatusOfFunds.BocName
ORDER BY StatusOfFunds.BFY, StatusOfFunds.FundCode, StatusOfFunds.AccountCode, StatusOfFunds.BocCode;
