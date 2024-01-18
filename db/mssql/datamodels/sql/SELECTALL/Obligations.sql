SELECT *
FROM Obligations
ORDER BY Obligations.BFY DESC, Obligations.FundCode, Obligations.RpioCode,
		 Obligations.AccountCode, Obligations.BocCode;