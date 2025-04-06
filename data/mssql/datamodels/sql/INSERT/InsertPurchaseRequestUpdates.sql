INSERT INTO PurchaseRequestNumbers
SELECT DISTINCT ExternalPurchases.RcCode                AS RcCode,
				ExternalPurchases.PurchaseRequestNumber AS PurchaseRequest
FROM ExternalPurchases
WHERE ExternalPurchases.PurchaseRequestNumber <> 'NS'
  AND NOT IsNull( ExternalPurchases.RcCode );
