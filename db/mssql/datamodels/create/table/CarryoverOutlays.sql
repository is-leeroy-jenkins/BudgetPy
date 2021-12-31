CREATE TABLE [dbo].[CarryoverOutlays]
(
	[CarryoverOutlaysId] [int] IDENTITY(1,1) NOT NULL,
	[ReportYear] [nvarchar](50) NULL,
	[AgencyName] [nvarchar](50) NULL,
	[OmbAccountName] [nvarchar](100) NULL,
	[LINE] [nvarchar](50) NULL,
	[Carryover] [float] NULL,
	[CarryoverOutlays] [float] NULL,
	[Delta] [float] NULL,
	[AvailableBalance] [float] NULL,
	[ULO] [float] NULL,
	[CurrentYearAdjustment] [float] NULL,
	[BudgetYearAdjustment] [float] NULL,
	[CurrentYear] [float] NULL,
	[BudgetYear] [float] NULL,
	[OutYear1] [float] NULL,
	[OutYear2] [float] NULL,
	[OutYear3] [float] NULL,
	[OutYear4] [float] NULL,
	[OutYear5] [float] NULL,
	[OutYear6] [float] NULL,
	[OutYear7] [float] NULL,
	[OutYear8] [float] NULL,
	[OutYear9] [time](7) NULL
);

