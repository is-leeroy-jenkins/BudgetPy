SELECT DISTINCT StatusOfFunds.BFY AS BFY, StatusOfFunds.RpioCode AS RpioCode, StatusOfFunds.RpioName AS RpioName, StatusOfFunds.FundCode AS FundCode, UCase(StatusOfFunds.FundName) AS FundName, StatusOfFunds.AccountCode AS AccountCode, UCase(StatusOfFunds.ProgramProjectName) AS ProgramProjectName, StatusOfFunds.ProgramProjectCode, StatusOfFunds.ProgramAreaCode, StatusOfFunds.BocCode AS BocCode, UCase(StatusOfFunds.BocName) AS BocName, 
SUM(CCur(StatusOfFunds.Amount)) AS [Current Allocation], 
SUM(CCur(OperatingPlans.Amount)) AS [Operating Plan], 
IIf(SUM(StatusOfFunds.Amount)-SUM(OperatingPlans.Amount)<0,"DECREASE","INCREASE") AS NET, 
CCur(Round(Abs(StatusOfFunds.Amount-OperatingPlans.Amount),2)) AS Delta
FROM StatusOfFunds 
INNER JOIN OperatingPlans 
ON (StatusOfFunds.RpioCode = OperatingPlans.RpioCode) 
AND (StatusOfFunds.BocCode = OperatingPlans.BocCode) 
AND (StatusOfFunds.AccountCode = OperatingPlans.AccountCode) 
AND (StatusOfFunds.FundCode = OperatingPlans.FundCode) 
AND (StatusOfFunds.BFY = OperatingPlans.BFY)
GROUP BY StatusOfFunds.BFY, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.ProgramAreaCode, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, CCur(Round(Abs(StatusOfFunds.Amount-OperatingPlans.Amount),2))
ORDER BY StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.FundCode,  StatusOfFunds.AccountCode,  StatusOfFunds.BocCode, StatusOfFunds.BFY DESC;