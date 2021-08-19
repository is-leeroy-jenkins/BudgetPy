INSERT INTO RegionalTransfers
SELECT Transfers.BFY AS BFY, Transfers.RpioCode AS RPIO, Transfers.AhCode AS AhCode, Transfers.AhName AS AhName, Transfers.FundCode AS FundCode, Transfers.FundName AS FundName, Transfers.OrgCode AS OrgCode, Transfers.OrganizationName AS OrganizationName, Transfers.AccountCode AS AccountCode, Transfers.ProgramProjectCode AS ProgramProjectCode, Transfers.ProgramProjectName AS ProgramProjectName, Transfers.ProgramAreaCode AS ProgramAreaCode, Transfers.ProgramAreaName AS ProgramAreaName, Transfers.Line AS Line, Transfers.Subline AS Subline, 
Sum(CCur([Transfers].[Amount])) AS Amount, 
Nz(Switch([FundCode] ALike 'E4%' And [NpmCode]='B','06K',
    [BocCode]='38','06G',
    [FundCode] ALike 'T%' And Len([AccountCode])=6 OR [AccountCode] LIKE '%DC3' And [NpmCode]<>'Y' AND [BocCode] Not In 
        ('10','21','38') Or [AhCode] ALike '6A%' And [BocCode] Not In ('10','21','38'),'06L',
    Len([AccountCode])=6 And [NpmCode]='B' And [BocCode] Not In ('10','21','38'),'06K',
    [NpmCode]='A' Or [FundCode] ALike 'E#%' And [NpmCode]='A','06J',
    [FundCode] ALike 'E1%' And [NpmCode] In ('C','D','E'),'06B',
    [FundCode]='B' And Len([AccountCode])=6 And [NpmCode]='E','06M',
    [FundCode] ALike 'E4%' And [NpmCode]='D','06B',
    [FundCode] ALike 'B%' And [NpmCode]='B','06K',
    [NpmCode]='L' Or [AccountCode] ALike '%57' Or [AccountCode] ALike '%M90' And [BocCode] Not In ('10','21'),'06F',[AccountCode] ALike '%XW2' Or [AccountCode] ALike '%RL' Or [NpmCode]='F' And [BocCode] Not In ('10','21'),'06H',[FundCode] ALike 'F%','06B',[FundCode]='B' And [NpmCode] In ('C','D') And [BocCode]<>'10','06B', [NpmCode]='Y' Or [AccountCode] ALike '%02' Or [AccountCode] ALike '%03','06N'),'06') AS RcCode, 
'06' AS SPIO, 
Transfers.ReprogrammingNumber AS ReprogrammingNumber, Transfers.ProcessedDate AS ProcessedDate, Transfers.DocType AS DocType, Transfers.DocPrefix AS DocPrefix, Transfers.NpmCode AS NpmCode, Transfers.FromTo AS FromTo, Transfers.BocCode AS BocCode, Transfers.BocName AS BocName, Transfers.Purpose AS Purpose, Transfers.ExtendedPurpose AS ExtendedPurpose, Transfers.ResourceType AS ResourceType
FROM Transfers
GROUP BY Transfers.ReprogrammingNumber, Transfers.ProcessedDate, Transfers.BFY, Transfers.RpioCode, Transfers.AhCode, Transfers.AhName, Transfers.FundCode, Transfers.FundName, Transfers.OrgCode, Transfers.OrganizationName, Transfers.AccountCode, Transfers.ProgramProjectCode, Transfers.ProgramProjectName, Transfers.ProgramAreaCode, Transfers.ProgramAreaName, Transfers.Line, Transfers.Subline, Transfers.FromTo, Transfers.BocCode, Transfers.BocName, 
Nz(Switch([FundCode] ALike 'E4%' And [NpmCode]='B','06K',
    [BocCode]='38','06G',
    [FundCode] ALike 'T%' And Len([AccountCode])=6  OR [AccountCode] LIKE '%DC3' And [NpmCode]<>'Y' AND [BocCode] Not IN
        ('10','21','38') Or [AhCode] ALike '6A%' And [BocCode] Not In ('10','21','38'),'06L',
    Len([AccountCode])=6 And [NpmCode]='B' And [BocCode] Not In ('10','21','38'),'06K',[NpmCode]='A' Or [FundCode] 
        ALike 'E#%' And [NpmCode]='A','06J',
    [FundCode] ALike 'E1%' And [NpmCode] In ('C','D','E'),'06B',
    [FundCode]='B' And Len([AccountCode])=6 And [NpmCode]='E','06M',
    [FundCode] ALike 'E4%' And [NpmCode]='D','06B',
    [FundCode] ALike 'B%' And [NpmCode]='B','06K',
    [NpmCode]='L' Or [AccountCode] ALike '%57' Or [AccountCode] ALike '%M90' And [BocCode] Not In ('10','21'),'06F',
    [AccountCode] ALike '%XW2' Or [AccountCode] ALike '%RL' Or [NpmCode]='F' And [BocCode] Not In ('10','21'),'06H',[FundCode] ALike 'F%','06B',
    [FundCode]='B' And [NpmCode] In ('C','D') And [BocCode]<>'10','06B', 
    [NpmCode]='Y' Or [AccountCode] ALike '%02' Or [AccountCode] ALike '%03','06N'),'06'), 
Transfers.DocPrefix, IIf([DocPrefix]<>'CRP',Left([ControlNumber],2),'17'), Transfers.BudgetLevel, Transfers.DocPrefix, Transfers.DocType, Transfers.NpmCode, Transfers.Purpose, Transfers.ExtendedPurpose, Transfers.ResourceType
HAVING ((IIf([DocPrefix]<>'CRP',Left([ControlNumber],2),'17'))='06') AND ((Transfers.DocPrefix)='RP')
ORDER BY Transfers.ProcessedDate DESC;
