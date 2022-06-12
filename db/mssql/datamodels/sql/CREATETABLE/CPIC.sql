CREATE TABLE [dbo].[CPIC]
(
	[CpicId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](255) NOT NULL,
	[CostAreaCode] [nvarchar](255) NULL,
	[CostAreaName] [nvarchar](255) NULL,
	[ProjectCode] [nvarchar](255) NULL,
	[ProjectName] [nvarchar](255) NULL
);

