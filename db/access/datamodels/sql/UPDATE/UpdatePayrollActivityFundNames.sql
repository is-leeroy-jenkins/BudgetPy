UPDATE PayrollActivity 
INNER JOIN Funds 
ON Funds.Code = PayrollActivity.FundCode 
SET PayrollActivity.FundName = Funds.Name
WHERE PayrollActivity.FundCode = Funds.Code;