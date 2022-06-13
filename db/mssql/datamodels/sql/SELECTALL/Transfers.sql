SELECT *
FROM Transfers
ORDER BY Transfers.ProcessedDate DESC, Transfers.FundCode, 
    Transfers.RpioCode, Transfers.AccountCode, Transfers.FromTo;