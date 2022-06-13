SELECT * 
FROM StatusOfFunds
ORDER BY StatusOfFunds.BFY DESC, StatusOfFunds.FundCode, StatusOfFunds.RpioCode, 
    StatusOfFunds.AccountCode, StatusOfFunds.BocCode;