CREATE TABLE [dbo].[MonthlyActuals]
(
	[MonthlyActualsId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](255) NULL,
	[EFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[RpioCode] [nvarchar](255) NULL,
	[RpioName] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[AhName] [nvarchar](255) NULL,
	[AppropriationCode] [nvarchar](255) NULL,
	[AppropriationName] [nvarchar](255) NULL,
	[SubAppropriationCode] [nvarchar](255) NULL,
	[SubAppropriationName] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[OrgName] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[NetOutlays] [float] NULL,
	[GrossOutlays] [float] NULL,
	[Obligations] [float] NULL,
	[TreasuryAccountCode] [nvarchar](255) NULL,
	[TreasuryAccountName] [nvarchar](255) NULL,
	[BudgetAccountCode] [nvarchar](255) NULL,
	[BudgetAccountName] [nvarchar](255) NULL
);


