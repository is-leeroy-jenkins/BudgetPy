CREATE TABLE [dbo].[ReimbursableFunds]
(
	[ReimbursableFundId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[DocumentControlNumber] [nvarchar](255) NULL,
	[AgreeementNumber] [nvarchar](255) NULL,
	[Amount] [money] NULL,
	[OpenCommitments] [money] NULL,
	[Obligations] [money] NULL,
	[ULO] [money] NULL,
	[Available] [money] NULL
);

