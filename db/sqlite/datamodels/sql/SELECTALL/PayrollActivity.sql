SELECT *
FROM PayrollActivity
ORDER BY PayrollActivity.StartDate DESC, PayrollActivity.BFY, PayrollActivity.FundCode,
    PayrollActivity.RpioCode, PayrollActivity.AccountCode, PayrollActivity.FocCode;