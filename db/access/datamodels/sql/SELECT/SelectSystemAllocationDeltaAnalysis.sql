SELECT DISTINCT Purchases.RcCode, Purchases.DivisionName, Purchases.SiteProjectCode
FROM Purchases
GROUP BY Purchases.RcCode, Purchases.DivisionName, Purchases.SiteProjectCode
HAVING NOT IsNull( Purchases.SiteProjectCode );
