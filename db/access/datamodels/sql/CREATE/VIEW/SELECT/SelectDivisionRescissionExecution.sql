SELECT Purchases.*, Allocations.Amount
FROM Allocations 
LEFT JOIN Purchases 
ON (Allocations.RcCode = Purchases.RcCode) 
AND (Allocations.BocCode = Purchases.BocCode) 
AND (Allocations.AccountCode = Purchases.AccountCode) 
AND (Allocations.FundCode = Purchases.FundCode) 
AND (Allocations.BFY = Purchases.BFY)
WHERE Not IsNull(Purchases.DocumentControlNumbers)
AND Purchases.Used > 0
AND Purchases.RcCode IN ('06N', '06C', '06B', '06G', '06A', '06X', '06H')
ORDER BY Purchases.BFY DESC , Purchases.BocCode, Purchases.DocumentControlNumbers;