SELECT * 
FROM UpperReconcilliation
UNION SELECT *
FROM LowerReconcilliation
ORDER BY BFY DESC , FundCode, AccountCode, BocCode;

