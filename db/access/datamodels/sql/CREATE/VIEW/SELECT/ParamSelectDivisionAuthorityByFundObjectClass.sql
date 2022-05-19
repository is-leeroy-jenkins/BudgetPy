PARAMETERS RcCodeArgs TEXT(255);
SELECT DISTINCTROW DivisionAuthority.RPIO , DivisionAuthority.BFY , DivisionAuthority.AhCode , DivisionAuthority.FundCode, DivisionAuthority.RcCode, DivisionAuthority.DivisionName, DivisionAuthority.FundName, DivisionAuthority.OrgCode, DivisionAuthority.AccountCode, DivisionAuthority.ProgramProjectCode, DivisionAuthority.ProgramProjectName, DivisionAuthority.BocCode, DivisionAuthority.BocName, 
CCur(DivisionAuthority.Amount) AS Amount, 
CCur(Sum(Round([Purchases].[OpenCommitments],2))) AS OpenCommitments, 
CCur(Sum(Round([Purchases].[Obligations],2))) AS Obligations, 
CCur(Sum([Purchases].[OpenCommitments]+[Purchases].[Obligations])) AS Used
FROM DivisionAuthority 
INNER JOIN Purchases 
ON (DivisionAuthority.RcCode = Purchases.RcCode) 
AND (DivisionAuthority.BocCode = Purchases.BocCode) 
AND (DivisionAuthority.AccountCode = Purchases.AccountCode) 
AND (DivisionAuthority.FundCode = Purchases.FundCode) 
AND (DivisionAuthority.BFY = Purchases.BFY)
GROUP BY DivisionAuthority.RPIO, DivisionAuthority.BFY, DivisionAuthority.AhCode, DivisionAuthority.FundCode,   DivisionAuthority.RcCode, DivisionAuthority.DivisionName, DivisionAuthority.FundName, DivisionAuthority.OrgCode, DivisionAuthority.AccountCode, DivisionAuthority.ProgramProjectCode, DivisionAuthority.ProgramProjectName, DivisionAuthority.BocCode, DivisionAuthority.BocName, DivisionAuthority.Amount, DivisionAuthority.Amount
HAVING DivisionAuthority.RcCode = [RcCodeArgs]
ORDER BY DivisionAuthority.BFY DESC , DivisionAuthority.FundCode, DivisionAuthority.AccountCode, DivisionAuthority.BocCode;