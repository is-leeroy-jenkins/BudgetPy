UPDATE Allocations
	INNER JOIN Funds
ON Funds.Code = Allocations.FundCode
SET Allocations.FundName = Funds.Name WHERE Allocations.FundCode = Funds.Code
AND Allocations.FundName <> Funds.Name;
