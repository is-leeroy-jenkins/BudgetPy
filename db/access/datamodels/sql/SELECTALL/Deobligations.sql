SELECT *
FROM Deobligations
ORDER BY Deobligations.BFY DESC, Deobligations.FundCode, Deobligations.RpioCode, 
    Deobligations.AccountCode, Deobligations.BocCode;