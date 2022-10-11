SELECT DISTINCTROW StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, 
IIF(Obligations.DocumentNumber IS NULL, "NS", Obligations.DocumentNumber) AS DocumentNumber, 
IIF(Obligations.ProcessedDate IS NULL, "NS", Obligations.ProcessedDate) AS ProcessedDate, 
IIF(SUM(Obligations.Obligations) > 0, "DECREASE", "ZERO") AS Net, 
SUM(CCur(Nz(Obligations.Obligations, 0))) AS Amount
FROM StatusOfFunds 
LEFT JOIN Obligations 
ON (StatusOfFunds.BocCode = Obligations.BocCode) 
AND (StatusOfFunds.OrgCode = Obligations.OrgCode) 
AND (StatusOfFunds.AccountCode = Obligations.AccountCode) 
AND (StatusOfFunds.AhCode = Obligations.AhCode) 
AND (StatusOfFunds.RpioCode = Obligations.RpioCode) 
AND (StatusOfFunds.FundCode = Obligations.FundCode) 
AND (StatusOfFunds.BFY = Obligations.BFY) 
AND (StatusOfFunds.EFY = Obligations.EFY)
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, 
IIF(Obligations.DocumentNumber IS NULL, "NS", Obligations.DocumentNumber),
IIF(Obligations.ProcessedDate IS NULL, "NS", Obligations.ProcessedDate), 
IIF(Obligations.Obligations > 0, "DECREASE", "ZERO")
HAVING StatusOfFunds.RpioCode NOT IN ("92","94","95")
AND StatusOfFunds.BocCode <> "10"
ORDER BY StatusOfFunds.BFY DESC, 
IIF(Obligations.ProcessedDate IS NULL, "NS", Obligations.ProcessedDate) DESC;