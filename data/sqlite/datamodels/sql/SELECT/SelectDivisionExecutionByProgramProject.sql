SELECT DISTINCTROW DivisionAuthority.BudgetLevel, DivisionAuthority.RPIO, DivisionAuthority.BFY, DivisionAuthority.AhCode, DivisionAuthority.FundCode, DivisionAuthority.RcCode, DivisionAuthority.DivisionName, DivisionAuthority.FundName, DivisionAuthority.OrgCode, DivisionAuthority.AccountCode, DivisionAuthority.ActivityCode, DivisionAuthority.ProgramProjectCode, DivisionAuthority.ProgramProjectName, DivisionAuthority.BocCode, DivisionAuthority.BocName, DivisionAuthority.Amount, 
Nz(Sum(Round([Purchases].[OpenCommitments],2)),0) AS OpenCommitments, 
Nz(Sum(Round([Purchases].[Obligations],2)),0) AS Obligations, 
Nz(Sum([Purchases].[OpenCommitments]+[Purchases].[Obligations]),0) AS Used
FROM DivisionAuthority 
LEFT JOIN Purchases 
ON (DivisionAuthority.BFY = Purchases.BFY) 
AND (DivisionAuthority.FundCode = Purchases.FundCode) 
AND (DivisionAuthority.AccountCode = Purchases.AccountCode) 
AND (DivisionAuthority.BocCode = Purchases.BocCode) 
AND (DivisionAuthority.RcCode = Purchases.RcCode)
GROUP BY DivisionAuthority.BudgetLevel, DivisionAuthority.RPIO, DivisionAuthority.BFY, DivisionAuthority.AhCode, DivisionAuthority.FundCode, DivisionAuthority.RcCode, DivisionAuthority.DivisionName, DivisionAuthority.FundName, DivisionAuthority.OrgCode, DivisionAuthority.AccountCode, DivisionAuthority.ActivityCode, DivisionAuthority.ProgramProjectCode, DivisionAuthority.ProgramProjectName, DivisionAuthority.BocCode, DivisionAuthority.BocName, DivisionAuthority.Amount
HAVING DivisionAuthority.Amount <> 0
ORDER BY DivisionAuthority.BFY DESC , DivisionAuthority.FundCode, 
DivisionAuthority.AccountCode, DivisionAuthority.BocCode;