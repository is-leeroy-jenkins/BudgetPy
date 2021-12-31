CREATE TABLE [dbo].[ObjectClassOutlays]
(
	[ObjectClassOutlaysId] [int] IDENTITY(1,1) NOT NULL,
	[ReportYear] [nvarchar](50) NULL,
	[OmbAgencyCode] [nvarchar](50) NULL,
	[OmbAgencyName] [nvarchar](100) NULL,
	[OmbBureauCode] [nvarchar](100) NULL,
	[OmbBureauName] [nvarchar](100) NULL,
	[OmbAccountCode] [nvarchar](100) NULL,
	[OmbAccountName] [nvarchar](100) NULL,
	[Direct_Reimbursable] [nvarchar](50) NULL,
	[DirectReimbursableTitle] [nvarchar](50) NULL,
	[ObjectClassGroupNumber] [nvarchar](50) NULL,
	[ObjectClassGroupName] [nvarchar](50) NULL,
	[FinanceObjectClass] [nvarchar](100) NULL,
	[PriorYear] [float] NULL,
	[CurrentYear] [float] NULL,
	[BudgetYear] [nvarchar](50) NULL
 );

