CREATE TABLE [dbo].[UnobligatedBalances]
(
	[UnobligatedBalancesId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetYear] [nvarchar](50) NULL,
	[AgencyTitle] [nvarchar](50) NULL,
	[BureauTitle] [nvarchar](50) NULL,
	[OmbAccount] [nvarchar](100) NULL,
	[AgencyCode] [nvarchar](50) NULL,
	[BureauCode] [nvarchar](50) NULL,
	[AccountCode] [nvarchar](50) NULL,
	[Transmit] [nvarchar](50) NULL,
	[Agency_Sequence] [nvarchar](50) NULL,
	[OmbAccountTitle] [nvarchar](100) NULL,
	[LineName] [nvarchar](50) NULL,
	[LineNumber] [nvarchar](50) NULL,
	[PriorYearAmount] [float] NULL,
	[CurrentYearAmount] [float] NULL,
	[BudgetYearAmount] [float] NULL
);

