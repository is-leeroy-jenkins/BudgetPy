CREATE TABLE [dbo].[PayPeriods]
(
	[PayPeriodId] [int] IDENTITY(1,1) NOT NULL,
	[Period] [nvarchar](255) NOT NULL,
	[PayPeriod] [nvarchar](255) NULL,
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL
);

