SELECT DISTINCTROW StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName,
IIF(Deobligations.DocumentNumber IS NULL, "NS", Deobligations.DocumentNumber) AS DocumentNumber, 
IIF(Deobligations.ProcessedDate IS NULL, "NS", Deobligations.ProcessedDate) As ProcessedDate,
IIF(Deobligations.Amount > 0, "INCREASE", "ZERO") AS Net, 
SUM(CCur(Nz(Deobligations.Amount, 0))) AS Amount
FROM StatusOfFunds 
LEFT JOIN Deobligations 
ON (StatusOfFunds.BocCode = Deobligations.BocCode) 
AND (StatusOfFunds.AccountCode = Deobligations.AccountCode) 
AND (StatusOfFunds.OrgCode = Deobligations.OrgCode) 
AND (StatusOfFunds.AhCode = Deobligations.AhCode) 
AND (StatusOfFunds.RpioCode = Deobligations.RpioCode) 
AND (StatusOfFunds.FundCode = Deobligations.FundCode) 
AND (StatusOfFunds.EFY = Deobligations.EFY) 
AND (StatusOfFunds.BFY = Deobligations.BFY)
GROUP BY StatusOfFunds.BFY, StatusOfFunds.EFY, StatusOfFunds.FundCode, StatusOfFunds.FundName, StatusOfFunds.RpioCode, StatusOfFunds.RpioName, StatusOfFunds.AhCode, StatusOfFunds.AhName, StatusOfFunds.OrgCode, StatusOfFunds.OrgName, StatusOfFunds.AccountCode, StatusOfFunds.ProgramProjectName, StatusOfFunds.BocCode, StatusOfFunds.BocName, 
IIF(Deobligations.DocumentNumber IS NULL, "NS", Deobligations.DocumentNumber), 
IIF(Deobligations.ProcessedDate IS NULL, "NS", Deobligations.ProcessedDate), 
IIF(Deobligations.Amount > 0, "INCREASE", "ZERO")
HAVING StatusOfFunds.BocCode <> "10"
ORDER BY StatusOfFunds.BFY DESC, 
IIF(Deobligations.ProcessedDate IS NULL, "NS", Deobligations.ProcessedDate) DESC;