SELECT *
FROM Actuals
ORDER BY Actuals.BFY DESC, Actuals.FundCode, Actuals.RpioCode,
		 Actuals.AccountCode, Actuals.BocCode;