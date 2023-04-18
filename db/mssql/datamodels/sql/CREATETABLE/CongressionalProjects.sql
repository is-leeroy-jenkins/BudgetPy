CREATE TABLE [dbo].[CongressionalProjects]
(
	[CongressionalProjectsId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](255) NULL,
	[EFY] [nvarchar](255) NULL,
	[RpioCode] [nvarchar](255) NULL,
	[RpioName] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[NpmCode] [nvarchar](255) NULL,
	[NpmName] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[StateCode] [nvarchar](255) NULL,
	[StateName] [nvarchar](255) NULL,
	[Project] [nvarchar](255) NULL,
	[Amount] [float] NULL,
	[TreasuryAccountCode] [nvarchar](255) NULL,
	[TreasuryAccountName] [nvarchar](255) NULL,
	[BudgetAccountCode] [nvarchar](255) NULL,
	[BudgetAccountName] [nvarchar](255) NULL
);

