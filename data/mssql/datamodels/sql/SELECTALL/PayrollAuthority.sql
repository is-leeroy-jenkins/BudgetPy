SELECT *
FROM PayrollAuthority
ORDER BY PayrollAuthority.BFY DESC, PayrollAuthority.FundCode, PayrollAuthority.RpioCode,
		 PayrollAuthority.AccountCode, PayrollAuthority.BocCode;