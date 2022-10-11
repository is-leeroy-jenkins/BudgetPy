SELECT DISTINCTROW StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName,
IIF(Transfers.ControlNumber IS NULL, "NS", Transfers.ControlNumber) AS DocumentNumber, 
IIF(Transfers.ProcessedDate IS NULL, "NS", Transfers.ProcessedDate) AS ProcessedDate, 
IIF(Transfers.FromTo = "FROM", "DECREASE", IIF(Transfers.FromTo = "TO", "INCREASE", "ZERO")) AS Net, 
SUM(CCur(Nz(Transfers.Amount))) AS Amount
FROM StatusOfFunds 
LEFT JOIN Transfers 
ON (StatusOfFunds.BocCode = Transfers.BocCode) 
AND (StatusOfFunds.AccountCode = Transfers.AccountCode) 
AND (StatusOfFunds.OrgCode = Transfers.OrgCode) 
AND (StatusOfFunds.AhCode = Transfers.AhCode) 
AND (StatusOfFunds.RpioCode = Transfers.RpioCode) 
AND (StatusOfFunds.FundCode = Transfers.FundCode) 
AND (StatusOfFunds.EFY = Transfers.EFY) 
AND (StatusOfFunds.BFY = Transfers.BFY)
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, 
IIF(Transfers.ControlNumber IS NULL, "NS", Transfers.ControlNumber), 
IIF(Transfers.ProcessedDate IS NULL, "NS", Transfers.ProcessedDate), 
IIF(Transfers.FromTo = "FROM", "DECREASE", IIF(Transfers.FromTo = "TO", "INCREASE", "ZERO"))
HAVING StatusOfFunds.RpioCode Not In ("92", "94", "95")
ORDER BY StatusOfFunds.BFY DESC, 
IIF(Transfers.ProcessedDate IS NULL, "NS", Transfers.ProcessedDate) DESC;