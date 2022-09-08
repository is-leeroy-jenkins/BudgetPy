UPDATE EarMarks 
INNER JOIN Funds 
ON EarMarks.FundCode = Funds.Code SET EarMarks.FundName = Funds.Name
WHERE EarMarks.FundCode = Funds.Code;