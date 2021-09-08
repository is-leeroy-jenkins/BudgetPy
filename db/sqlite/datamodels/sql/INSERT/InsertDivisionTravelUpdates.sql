INSERT INTO DocumentControlNumbers
SELECT DISTINCT ExternalPurchases.RcCode AS RcCode, ExternalPurchases.DocumentControlNumbers AS DocumentControlNumber
FROM ExternalPurchases
WHERE NOT IsNull(ExternalPurchases.RcCode)
AND ExternalPurchases.DocumentControlNumbers <> 'NS';
