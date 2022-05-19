CREATE TABLE [dbo].[ReimbursableAgreements]
(
	[ReimbursableAgreementId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[AgreementNumber] [nvarchar](255) NULL,
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL,
	[RcCode] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[SiteProjectCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[VendorCode] [nvarchar](255) NULL,
	[VendorName] [nvarchar](255) NULL,
	[Amount] [money] NULL,
	[OpenCommitments] [money] NULL,
	[Obligations] [money] NULL,
	[ULO] [money] NULL,
	[Available] [money] NULL
);

