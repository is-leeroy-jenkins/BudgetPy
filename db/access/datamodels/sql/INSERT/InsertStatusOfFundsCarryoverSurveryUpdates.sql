INSERT INTO SystemUpdates
SELECT StatusOfFunds.StatusOfFundsId AS ExtId, StatusOfFunds.BudgetLevel AS BudgetLevel, StatusOfFunds.AhCode AS AhCode, StatusOfFunds.BFY AS BFY, StatusOfFunds.FundCode AS FundCode, StatusOfFunds.FundName AS FundName, StatusOfFunds.OrgCode AS OrgCode, StatusOfFunds.AccountCode AS AccountCode, StatusOfFunds.ProgramProjectCode AS ProgramProjectCode, StatusOfFunds.ProgramProjectName AS ProgramProjectName, StatusOfFunds.BocCode AS BocCode, StatusOfFunds.BocName AS BocName, StatusOfFunds.RcCode AS RcCode, StatusOfFunds.DivisionName AS DivisionName, StatusOfFunds.Amount AS Amount, StatusOfFunds.ProgramAreaCode AS ProgramAreaCode, StatusOfFunds.ProgramAreaName AS ProgramAreaName
FROM StatusOfFunds
WHERE StatusOfFunds.BudgetLevel = 7
ORDER BY StatusOfFunds.BFY DESC , StatusOfFunds.FundCode, StatusOfFunds.AccountCode, StatusOfFunds.BocCode;

