SELECT * 
FROM Allocations
ORDER BY Allocations.BFY DESC, Allocations.FundCode, Allocations.RpioCode, 
    Allocations.AccountCode, Allocations.BocCode;