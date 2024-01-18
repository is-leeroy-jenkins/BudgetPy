SELECT *
FROM UnliquidatedObligations
ORDER BY UnliquidatedObligations.BFY DESC, UnliquidatedObligations.FundCode,
		 UnliquidatedObligations.RpioCode,
		 UnliquidatedObligations.AccountCode, UnliquidatedObligations.BocCode;