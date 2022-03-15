CREATE TABLE [dbo].[GrowthRates]
(
	[GrowthRatesId] [int] IDENTITY(1,1) NOT NULL,
	[RateId] [nvarchar](50) NULL,
	[DESCRIPTION] [nvarchar](100) NULL,
	[BudgetYearRate] [float] NULL,
	[OutYear1] [float] NULL,
	[OutYear2] [float] NULL,
	[OutYear3] [float] NULL,
	[OutYear4] [float] NULL,
	[OutYear5] [float] NULL,
	[OutYear6] [float] NULL,
	[OutYear7] [float] NULL,
	[OutYear8] [float] NULL,
	[OutYear9] [float] NULL,
	[Sort] [nvarchar](50) NULL
);
