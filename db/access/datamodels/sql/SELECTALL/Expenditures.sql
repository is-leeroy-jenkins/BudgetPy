SELECT *
FROM Expenditures
ORDER BY Expenditures.BFY DESC, Expenditures.FundCode, Expenditures.RpioCode, 
    Expenditures.AccountCode, Expenditures.BocCode;