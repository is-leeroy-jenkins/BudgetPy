INSERT INTO SystemUpdates
SELECT DISTINCT StatusOfFunds.StatusOfFundsId AS ExtId, '06' AS RPIO, StatusOfFunds.BudgetLevel AS BudgetLevel, StatusOfFunds.AhCode AS AhCode, StatusOfFunds.BFY AS BFY, StatusOfFunds.FundCode AS FundCode, StatusOfFunds.FundName AS FundName, StatusOfFunds.OrgCode AS OrgCode, StatusOfFunds.AccountCode AS AccountCode, StatusOfFunds.ProgramProjectCode AS ProgramProjectCode, StatusOfFunds.ProgramProjectName AS ProgramProjectName, StatusOfFunds.ProgramAreaCode AS ProgramAreaCode, StatusOfFunds.ProgramAreaName AS ProgramAreaName, StatusOfFunds.BocCode AS BocCode, StatusOfFunds.BocName AS BocName, StatusOfFunds.RcCode AS RcCode, StatusOfFunds.Amount AS Amount, StatusOfFunds.NpmCode AS NpmCode, StatusOfFunds.NpmTitle AS NpmName, 
    SWITCH(LEN(StatusOfFunds.AccountCode) < 7, 'NS', 
        LEN(StatusOfFunds.AccountCode) > 7, 
        RIGHT(StatusOfFunds.AccountCode, 2)) AS ActivityCode
FROM StatusOfFunds
WHERE StatusOfFunds.BudgetLevel = '7'
ORDER BY StatusOfFunds.BFY DESC , StatusOfFunds.FundCode, StatusOfFunds.AccountCode, StatusOfFunds.BocCode;