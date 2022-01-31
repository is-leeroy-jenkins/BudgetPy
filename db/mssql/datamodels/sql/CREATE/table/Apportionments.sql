CREATE TABLE [dbo].[Apportionments]
(
	[ApportionmentsId] [int] IDENTITY(1,1) NOT NULL,
	[Year] [nvarchar](50) NULL,
	[ActivityId] [nvarchar](50) NULL,
	[TreasuryFundCode] [nvarchar](50) NULL,
	[TreasuryFundSymbol] [nvarchar](100) NULL,
	[TreasuryAgency] [nvarchar](50) NULL,
	[TreasuryAccountCode] [nvarchar](50) NULL,
	[BFY] [nvarchar](50) NULL,
	[EFY] [nvarchar](50) NULL,
	[AvailabilityType] [nvarchar](50) NULL,
	[TreasuryAccountTitle] [nvarchar](100) NULL,
	[BudgetAgency] [nvarchar](50) NULL,
	[BudgetBureau] [nvarchar](50) NULL,
	[BudgetAccount] [nvarchar](50) NULL,
	[BudgetAgencyTitle] [nvarchar](50) NULL,
	[BudgetBureauTitle] [nvarchar](50) NULL,
	[BudgetAccountTitle] [nvarchar](100) NULL,
	[DateApproved] [date] NULL,
	[LineNumber] [nvarchar](50) NULL,
	[LineSort] [nvarchar](50) NULL,
	[LineDescription] [nvarchar](100) NULL,
	[Amount] [float] NULL
);

