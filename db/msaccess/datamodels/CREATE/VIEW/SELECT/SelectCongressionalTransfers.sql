SELECT Transfers.ReprogrammingNumber AS ReprogrammingNumber, Transfers.BFY AS BFY, Transfers.RpioCode AS RPIO, Transfers.AhCode AS AhCode, Transfers.FundCode AS FundCode, Transfers.FundName AS FundName, Transfers.OrgCode AS OrgCode, Transfers.AccountCode AS AccountCode, Transfers.ProgramProjectName AS ProgramProjectName, Transfers.BocCode AS BocCode, Transfers.BocName AS BocName, Nz(Switch(
[BocCode]='38','06G',
[BocCode] <> "10" AND [FundCode] ALike 'E%' OR [BocCode] <> "10" AND [FundCode] = 'B' And [NpmCode]='B','06K',
[BocCode] <> "10" AND [FundCode] ='B' OR [BocCode] <> "10" AND [FundCode] ALike 'F%' OR [BocCode] <> "10" AND [FundCode] ALike 'E%' And [NpmCode] In ('C','D','E'),'06B',
[BocCode] <> "10" AND [AhCode] ALike '6A%' OR [BocCode] <> "10" AND [FundCode] ALike 'T%' AND [NpmCode]<>'F' AND [NpmCode] <> 'Y', '06L', 
[BocCode] <> "10" AND [FundCode] ALike 'E%' OR [BocCode] <> "10" AND [FundCode]='B' And [NpmCode]='A', '06J',
[BocCode] <> "10" AND [FundCode]='B' And [NpmCode]='E','06M',
[BocCode] <> "10" AND [NpmCode]='L', '06F',
[BocCode] <> "10" AND [AccountCode] ALike '%57' Or [BocCode] <> "10" AND [AccountCode] ALike "%M90", '06F',
[BocCode] <> "10" AND [NpmCode]='F' OR [BocCode] <> "10" AND [AccountCode] ALike '%XW2' OR [BocCode] <> "10" AND [AccountCode] ALike "%RL", '06H', 
[BocCode] <> "10" AND [NpmCode]='Y' OR [BocCode] <> "10" AND [AccountCode] ALike '%02' OR [BocCode] <> "10" AND [AccountCode] ALike '%04' OR [BocCode] <> "10" AND [AccountCode] ALike '%03', '06N'),'06') AS RcCode, CCur([Transfers].[Amount]) AS Amount, Transfers.ProcessedDate AS ProcessedDate, IIf([DocPrefix]<>'CRP',Left([ControlNumber],2),'17') AS SPIO
FROM Transfers
WHERE (((Transfers.ProcessedDate)>#10/1/2019#) AND ((Transfers.DocPrefix)='CRP') AND ((Transfers.FromTo)='To') AND ((Transfers.BudgetLevel)='7'))
ORDER BY Transfers.ProcessedDate DESC;