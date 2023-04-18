UPDATE OperatingPlans 
INNER JOIN Funds 
ON OperatingPlans.FundCode = Funds.Code 
SET OperatingPlans.FundName = Funds.Name;