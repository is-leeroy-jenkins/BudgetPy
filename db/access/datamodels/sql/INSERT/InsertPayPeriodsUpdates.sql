UPDATE Transfers
	INNER JOIN Funds
ON Funds.Code = Transfers.FundCode
SET Transfers.FundName = Funds.Name WHERE Transfers.FundCode = Funds.Code
AND Transfers.FundName <> Funds.Name;