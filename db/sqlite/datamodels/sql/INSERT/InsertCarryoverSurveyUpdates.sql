INSERT INTO CongressionalTransfers
SELECT Transfers.BFY AS BFY, Transfers.RpioCode AS RPIO, Transfers.AhCode AS AhCode, Transfers.AhName AS AhName, Transfers.FundCode AS FundCode, Transfers.FundName AS FundName, Transfers.OrgCode AS OrgCode, Transfers.OrganizationName AS OrganizationName, Transfers.AccountCode AS AccountCode, Transfers.ProgramProjectCode AS ProgramProjectCode, Transfers.ProgramProjectName AS ProgramProjectName, Transfers.ProgramAreaCode AS ProgramAreaCode, Transfers.ProgramAreaName AS ProgramAreaName, Nz(Switch(
[BocCode]='38','06G',
[BocCode] <> "10" AND [FundCode] ALike 'E%' OR [BocCode] <> "10" AND [FundCode] = 'B' And [NpmCode]='B','06K',
[BocCode] <> "10" AND [FundCode] ='B' OR [BocCode] <> "10" AND [FundCode] ALike 'F%' OR [BocCode] <> "10" AND [FundCode] ALike 'E%' And [NpmCode] In ('C','D','E'),'06B',
[BocCode] <> "10" AND [AhCode] ALike '6A%' OR [BocCode] <> "10" AND [FundCode] ALike 'T%' AND [NpmCode]<>'F' AND [NpmCode] <> 'Y', '06L', 
[BocCode] <> "10" AND [FundCode] ALike 'E%' OR [BocCode] <> "10" AND [FundCode]='B' And [NpmCode]='A', '06J',
[BocCode] <> "10" AND [FundCode]='B' And [NpmCode]='E','06M',
[BocCode] <> "10" AND [NpmCode]='L', '06F',
[BocCode] <> "10" AND [AccountCode] ALike '%57' Or [BocCode] <> "10" AND [AccountCode] ALike "%M90", '06F',
[BocCode] <> "10" AND [NpmCode]='F' OR [BocCode] <> "10" AND [AccountCode] ALike '%XW2' OR [BocCode] <> "10" AND [AccountCode] ALike "%RL", '06H', 
[BocCode] <> "10" AND [NpmCode]='Y' OR [BocCode] <> "10" AND [AccountCode] ALike '%02' OR [BocCode] <> "10" AND [AccountCode] ALike '%04' OR [BocCode] <> "10" AND [AccountCode] ALike '%03', '06N'),'06') AS RcCode, Transfers.Line AS Line, Transfers.Subline AS Subline, CCur(SUM([Transfers].[Amount])) AS Amount, Transfers.ProcessedDate AS ProcessedDate, IIf([DocPrefix]<>'CRP',Left([ControlNumber],2),'17') AS SPIO, Transfers.ReprogrammingNumber AS ReprogrammingNumber, Transfers.DocType AS DocType, Transfers.DocPrefix AS DocPrefix, Transfers.NpmCode AS NpmCode, Transfers.FromTo AS FromTo, Transfers.BocCode AS BocCode, Transfers.BocName AS BocName, Transfers.Purpose AS Purpose, Transfers.ExtendedPurpose AS ExtendedPurpose, Transfers.ResourceType AS ResourceType
FROM Transfers
GROUP BY Transfers.ReprogrammingNumber, Transfers.ProcessedDate, IIf([DocPrefix]<>'CRP',Left([ControlNumber],2),'17'), Transfers.BFY, Transfers.RpioCode, Transfers.AhCode, Transfers.AhName, Transfers.FundCode, Transfers.FundName, Transfers.OrgCode, Transfers.OrganizationName, Transfers.AccountCode, Transfers.ProgramProjectCode, Transfers.ProgramProjectName, Transfers.ProgramAreaCode, Transfers.ProgramAreaName, Transfers.Line, Transfers.Subline, Transfers.FromTo, Transfers.BocCode, Transfers.BocName, Transfers.DocPrefix, Transfers.BudgetLevel, Transfers.DocPrefix, Transfers.DocType, Transfers.NpmCode, Transfers.Purpose, Transfers.ExtendedPurpose, Transfers.ResourceType
HAVING ((Transfers.DocPrefix)='CRP') AND ((Transfers.FromTo)='To') AND ((Transfers.BudgetLevel)='7')
ORDER BY Transfers.ProcessedDate DESC;
