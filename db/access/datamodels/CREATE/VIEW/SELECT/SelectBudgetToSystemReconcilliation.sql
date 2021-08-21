SELECT DISTINCT Purchases.RcCode, Purchases.DivisionName, Purchases.DocumentControlNumbers
FROM Purchases
WHERE NOT IsNull(Purchases.DocumentControlNumbers);