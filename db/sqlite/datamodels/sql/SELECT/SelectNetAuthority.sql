
SELECT DISTINCT StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, 
SUM(CCur(Nz(StatusOfFunds.Amount,0))) AS Authority, 
Sum(CCur(Nz(StatusOfFunds.OpenCommitments,0))) AS OpenCommitments, 
SUM(IIF(StatusOfFunds.OpenCommitments > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.OpenCommitments/StatusOfFunds.Budgeted, 2), 0)) AS Committed, SUM(CCur(Nz(StatusOfFunds.Obligations,0))) AS Obligations, 
SUM(IIF(StatusOfFunds.Obligations > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Obligations/StatusOfFunds.Budgeted, 2), 0)) AS Obligated, 
SUM(CCur(Nz(StatusOfFunds.ULO,0))) AS UnliquidatedObligations, 
SUM(IIF(StatusOfFunds.ULO > 0 AND StatusOfFunds.Obligations > 0, 
    ROUND(StatusOfFunds.ULO/StatusOfFunds.Obligations, 2), 0)) AS Unliquidated,
SUM(CCur(Nz(StatusOfFunds.Used,0))) AS Used, 
SUM(IIF(StatusOfFunds.Used > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Used/StatusOfFunds.Budgeted, 2), 0)) AS Utilization, 
SUM(CCur(Nz(StatusOfFunds.Available,0))) AS Available, 
SUM(IIF(StatusOfFunds.Available > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Available/StatusOfFunds.Budgeted, 2), 0)) AS Availability, 
SUM(CCur(Nz(StatusOfFunds.Expenditures,0))) AS Outlays, 
SUM(IIF(StatusOfFunds.Expenditures > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Expenditures/StatusOfFunds.Budgeted, 2), 0)) AS Outlaid
FROM StatusOfFunds
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, CStr("NS"), CStr("NS"), CCur(0)
HAVING (((StatusOfFunds.RpioCode) Not In ("92","94","95")) 
AND ((StatusOfFunds.BocCode)<>"10"))
ORDER BY StatusOfFunds.BFY DESC;SELECT DISTINCT StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, 
SUM(CCur(Nz(StatusOfFunds.Amount,0))) AS Authority, 
Sum(CCur(Nz(StatusOfFunds.OpenCommitments,0))) AS OpenCommitments, 
SUM(IIF(StatusOfFunds.OpenCommitments > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.OpenCommitments/StatusOfFunds.Budgeted, 2), 0)) AS Committed, SUM(CCur(Nz(StatusOfFunds.Obligations,0))) AS Obligations, 
SUM(IIF(StatusOfFunds.Obligations > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Obligations/StatusOfFunds.Budgeted, 2), 0)) AS Obligated, 
SUM(CCur(Nz(StatusOfFunds.ULO,0))) AS UnliquidatedObligations, 
SUM(IIF(StatusOfFunds.ULO > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.ULO/StatusOfFunds.Budgeted, 2), 0)) AS Unliquidated, 
SUM(CCur(Nz(StatusOfFunds.Used,0))) AS Used, SUM(IIF(StatusOfFunds.Used > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Used/StatusOfFunds.Budgeted, 2), 0)) AS Utilization, 
SUM(CCur(Nz(StatusOfFunds.Available,0))) AS Available, 
SUM(IIF(StatusOfFunds.Available > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Available/StatusOfFunds.Budgeted, 2), 0)) AS Availability, SUM(CCur(Nz(StatusOfFunds.Expenditures,0))) AS Outlays, 
SUM(IIF(StatusOfFunds.Expenditures > 0 AND StatusOfFunds.Budgeted > 0, 
    ROUND(StatusOfFunds.Expenditures/StatusOfFunds.Budgeted, 2), 0)) AS Outlaid
FROM StatusOfFunds
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, CStr("NS"), CStr("NS"), CCur(0)
HAVING (((StatusOfFunds.RpioCode) Not In ("92","94","95")) 
AND ((StatusOfFunds.BocCode)<>"10"))
ORDER BY StatusOfFunds.BFY DESC;