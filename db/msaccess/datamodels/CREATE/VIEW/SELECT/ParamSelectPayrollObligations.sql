PARAMETERS FiscalYearArgs Text ( 255 ), RcCodeArgs Text ( 255 ), FundCodeArgs Text ( 255 );
SELECT DISTINCTROW Purchases.RpioCode AS RPIO, Purchases.BFY, Purchases.AhCode AS [AH Code], Purchases.AhName AS [AH Name], Purchases.FundCode AS FundCode, Purchases.FundName AS FundName, Purchases.AccountCode AS AccountCode, Purchases.ProgramProjectName AS ProgramProjectName, Purchases.BocCode AS BocCode, Purchases.BocName AS BocName, 
Purchases.OriginalActionDate AS OriginalAction, Purchases.LastActionDate AS LastActivity, 
Sum(Purchases.Commitments) AS Commitments, 
Sum(Purchases.OpenCommitments) AS OpenCommitments, 
Sum(Purchases.ULO) AS ULO, 
Sum(Purchases.Deobligations) AS Deobligations, 
Sum(Purchases.Obligations) AS Obligations, 
Purchases.OpenCommitments+Purchases.Obligations AS Used, 
Divisions.Title AS DivisionName, Purchases.OrgCode, Purchases.RcCode
FROM Divisions 
INNER JOIN Purchases 
ON Divisions.Code = Purchases.RcCode
GROUP BY Purchases.RpioCode, Purchases.BFY, Purchases.AhCode, Purchases.AhName, Purchases.FundCode, Purchases.FundName, Purchases.AccountCode, Purchases.ProgramProjectName, Purchases.BocCode, Purchases.BocName, Purchases.OriginalActionDate, Purchases.LastActionDate, Purchases.OpenCommitments+Purchases.Obligations, Divisions.Title, Purchases.OrgCode, Purchases.RcCode, Divisions.Code
HAVING Purchases.BFY = [FiscalYearArgs] 
And Purchases.FundCode = [FundCodeArgs] 
And Divisions.Code = Purchases.RcCode 
Or Purchases.RcCode = [RcCodeArgs]
ORDER BY Purchases.BFY DESC , Purchases.FundCode,
Purchases.AccountCode, Purchases.BocCode;