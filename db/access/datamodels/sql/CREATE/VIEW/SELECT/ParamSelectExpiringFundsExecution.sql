PARAMETERS RcCodeArgs Text ( 255 ), FiscalYearArgs Text ( 255 );
SELECT Purchases.RpioCode AS RPIO, Purchases.AhCode, Purchases.BFY, Purchases.FundCode, Purchases.FundName, Purchases.DocumentControlNumbers AS DCN, Purchases.PurchaseRequestNumber AS PurchaseRequest, Purchases.OrgCode, Purchases.AccountCode, Purchases.ActivityCode, Purchases.ProgramProjectName, Purchases.BocCode, Purchases.BocName, Purchases.FocCode, Purchases.FocName, Purchases.OriginalActionDate, Purchases.LastActionDate, 
CCur(Purchases.OpenCommitments) AS OpenCommitments, 
CCur(Purchases.ULO) AS ULO, Allocations.DivisionName, Purchases.RcCode
FROM Allocations 
LEFT JOIN Purchases 
ON (Allocations.RcCode = Purchases.RcCode 
AND Allocations.BocCode = Purchases.BocCode 
AND Allocations.AccountCode = Purchases.AccountCode 
AND Allocations.FundCode = Purchases.FundCode 
AND Allocations.AhCode = LEFTPurchases.AhCode, 2 
AND Allocations.BFY = Purchases.BFY)
GROUP BY Purchases.RpioCode, Purchases.AhCode, Purchases.BFY, Purchases.RcCode, Purchases.FundCode, Purchases.FundName, Purchases.DocumentControlNumbers, Purchases.PurchaseRequestNumber, Purchases.OrgCode, Purchases.AccountCode, Purchases.ActivityCode, Purchases.ProgramProjectName, Purchases.BocCode, Purchases.BocName, Purchases.FocCode, Purchases.FocName, Purchases.OriginalActionDate, Purchases.LastActionDate, Purchases.OpenCommitments, Purchases.ULO, Allocations.Amount, Allocations.DivisionName, Allocations.DivisionName
HAVING Purchases.OpenCommitments + Purchases.ULO > 0
AND NOT IsNull(Purchases.DocumentControlNumbers)
AND Purchases.BFY = FiscalYearArgs
AND Purchases.RcCode = RcCodeArgs
AND Purchases.FundCode = 'B'
ORDER BY Purchases.BFY DESC;
