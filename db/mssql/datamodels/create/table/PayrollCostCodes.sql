CREATE TABLE [dbo].[PayrollCostCodes]
(
	[PayrollCostCodeId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[WorkCode] [nvarchar](255) NULL,
	[WorkCodeName] [nvarchar](255) NULL,
	[HrOrgCode] [nvarchar](255) NULL,
	[HrOrgName] [nvarchar](255) NULL
);
