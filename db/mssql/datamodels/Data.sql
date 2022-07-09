USE [Data]
GO
/****** Object:  Table [dbo].[Allocations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Allocations](
	[PrcId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetLevel] [nvarchar](50) NOT NULL,
	[RPIO] [nvarchar](50) NOT NULL,
	[BFY] [nvarchar](50) NOT NULL,
	[FundCode] [nvarchar](50) NOT NULL,
	[AhCode] [nvarchar](50) NOT NULL,
	[OrgCode] [nvarchar](50) NOT NULL,
	[RcCode] [nvarchar](50) NOT NULL,
	[AccountCode] [nvarchar](50) NOT NULL,
	[BocCode] [nvarchar](50) NOT NULL,
	[Amount] [float] NOT NULL,
	[ActivityCode] [nvarchar](50) NOT NULL,
	[ActivityName] [nvarchar](50) NOT NULL,
	[FundName] [nvarchar](50) NOT NULL,
	[BocName] [nvarchar](50) NOT NULL,
	[NpmName] [nvarchar](50) NOT NULL,
	[Division] [nvarchar](50) NOT NULL,
	[DivisionName] [nvarchar](50) NOT NULL,
	[ProgramProjectCode] [nvarchar](50) NOT NULL,
	[ProgramProjectName] [nvarchar](100) NOT NULL,
	[ProgramAreaName] [nvarchar](50) NOT NULL,
	[AhName] [nvarchar](50) NOT NULL,
	[OrgName] [nvarchar](50) NOT NULL,
	[GoalName] [nvarchar](50) NOT NULL,
	[ObjectiveName] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ApplicationTables]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ApplicationTables](
	[ApplicationTableId] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](255) NULL,
	[Model] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AppropriationDocuments]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AppropriationDocuments](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](50) NOT NULL,
	[EFY] [nvarchar](50) NOT NULL,
	[Fund] [nvarchar](50) NOT NULL,
	[FundCode] [nvarchar](50) NOT NULL,
	[DocumentType] [nvarchar](50) NOT NULL,
	[DocumentNumber] [nvarchar](50) NOT NULL,
	[DocumentDate] [today] NOT NULL,
	[LastDocumentDate] [today] NOT NULL,
	[BudgetLevel] [nvarchar](50) NOT NULL,
	[BudgetingControls] [nvarchar](50) NOT NULL,
	[PostingControls] [nvarchar](50) NOT NULL,
	[PreCommitmentControls] [nvarchar](50) NOT NULL,
	[CommitmentControls] [nvarchar](50) NOT NULL,
	[ObligationControls] [nvarchar](50) NOT NULL,
	[AccrualControls] [nvarchar](50) NOT NULL,
	[ExpenditureControls] [nvarchar](50) NOT NULL,
	[ExpenseControls] [nvarchar](50) NOT NULL,
	[ReimbursementControls] [nvarchar](50) NOT NULL,
	[ReimbursableAgreementControls] [nvarchar](50) NOT NULL,
	[Budgeted] [float] NOT NULL,
	[Posted] [float] NOT NULL,
	[CarryOut] [float] NOT NULL,
	[CarryIn] [float] NOT NULL,
	[EstimatedReimbursements] [float] NOT NULL,
	[EstimatedRecoveries] [float] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BackUp]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BackUp](
	[BackupAllocationId] [int] IDENTITY(1,1) NOT NULL,
	[PrcId] [float] NULL,
	[BudgetLevel] [nvarchar](255) NULL,
	[RPIO] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[Amount] [float] NULL,
	[AllocationRatio] [float] NULL,
	[FundName] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[Division] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[ActivityCode] [nvarchar](255) NULL,
	[NpmName] [nvarchar](255) NULL,
	[NpmCode] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[GoalCode] [nvarchar](255) NULL,
	[GoalName] [nvarchar](255) NULL,
	[ObjectiveCode] [nvarchar](255) NULL,
	[ObjectiveName] [nvarchar](255) NULL,
	[ChangeDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BudgetControlValues]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BudgetControlValues](
	[ControlValueId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](50) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[SecOrg] [nvarchar](50) NOT NULL,
	[BdgtTransType] [nvarchar](50) NOT NULL,
	[PstdTransType] [nvarchar](50) NOT NULL,
	[EstReimTransType] [nvarchar](50) NOT NULL,
	[SpngAdjTransType] [nvarchar](50) NULL,
	[EstRecTransType] [nvarchar](50) NOT NULL,
	[ActlRecTransType] [nvarchar](50) NULL,
	[StatRsrvTransType] [nvarchar](50) NOT NULL,
	[ProfLossTransType] [nvarchar](50) NOT NULL,
	[EstReimSpngOpt] [nvarchar](50) NOT NULL,
	[EstReimBdgtOpt] [nvarchar](50) NOT NULL,
	[TrckAgreLowerLevel] [nvarchar](50) NOT NULL,
	[BdgtEstLowerLevel] [nvarchar](50) NOT NULL,
	[EstRecSpngOpt] [nvarchar](50) NOT NULL,
	[EstRecBdgtOpt] [nvarchar](50) NOT NULL,
	[RecNextLevel] [nvarchar](50) NOT NULL,
	[RecBdgtMismatch] [nvarchar](50) NOT NULL,
	[ProfitLossSpngOpt] [nvarchar](50) NOT NULL,
	[ProfitLossBdgtOpt] [nvarchar](50) NOT NULL,
	[RecCrryInLowerLevel] [nvarchar](50) NOT NULL,
	[RecCrryInLowerLevelCtrl] [nvarchar](50) NOT NULL,
	[RecCrryInAMCtrl] [nvarchar](50) NOT NULL,
	[BdgtCtrl] [nvarchar](50) NOT NULL,
	[PstdCtrl] [nvarchar](50) NOT NULL,
	[PreCommSpngCtrl] [nvarchar](50) NOT NULL,
	[CommSpngCtrl] [nvarchar](50) NOT NULL,
	[ObligSpngCtrl] [nvarchar](50) NOT NULL,
	[AccrSpngCtrl] [nvarchar](50) NOT NULL,
	[ExpndSpngCtrl] [nvarchar](50) NOT NULL,
	[ExpnsSpngCtrl] [nvarchar](50) NOT NULL,
	[ReimSpngCtrl] [nvarchar](50) NOT NULL,
	[ReimAgreSpngCtrl] [nvarchar](50) NOT NULL,
	[FteBdgtCtrl] [nvarchar](50) NOT NULL,
	[FteSpngCtrl] [nvarchar](50) NOT NULL,
	[TransactionTypeCtrl] [nvarchar](50) NOT NULL,
	[AuthorityDistributionCtrl] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BudgetDocuments]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BudgetDocuments](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [ntext] NULL,
	[EFY] [ntext] NULL,
	[BudgetLevel] [ntext] NULL,
	[DocumentDate] [datetime] NULL,
	[LastDocumentDate] [datetime] NULL,
	[DocumentType] [ntext] NULL,
	[DocumentNumber] [ntext] NULL,
	[FundCode] [ntext] NULL,
	[FundName] [ntext] NULL,
	[RpioCode] [ntext] NULL,
	[RpioName] [ntext] NULL,
	[AhCode] [ntext] NULL,
	[AhName] [ntext] NULL,
	[OrgCode] [ntext] NULL,
	[OrgName] [ntext] NULL,
	[AccountCode] [ntext] NULL,
	[ProgramProjectName] [ntext] NULL,
	[ProgramAreaCode] [ntext] NULL,
	[ProgramAreaName] [ntext] NULL,
	[BocCode] [ntext] NULL,
	[BocName] [ntext] NULL,
	[ReimbursableAgreementControls] [ntext] NULL,
	[BudgetingControls] [ntext] NULL,
	[PostingControls] [ntext] NULL,
	[PreCommitmentControls] [ntext] NULL,
	[CommitmentControls] [ntext] NULL,
	[ObligationControls] [ntext] NULL,
	[ExpenditureControls] [ntext] NULL,
	[ExpenseControls] [ntext] NULL,
	[AccrualControls] [ntext] NULL,
	[ReimbursementControls] [ntext] NULL,
	[Budgeted] [float] NOT NULL,
	[Posted] [float] NOT NULL,
	[CarryOut] [float] NOT NULL,
	[CarryIn] [float] NOT NULL,
	[EstimatedRecoveries] [float] NOT NULL,
	[EstimatedReimbursements] [float] NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CarryoverEstimates]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CarryoverEstimates](
	[CarryoverEstimateId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetLevel] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[Balance] [real] NULL,
	[OpenCommitment] [real] NULL,
	[Estimate] [real] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Changes]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Changes](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](255) NULL,
	[FieldName] [nvarchar](255) NULL,
	[Action] [nvarchar](255) NULL,
	[OldValue] [nvarchar](255) NULL,
	[NewValue] [nvarchar](255) NULL,
	[TimeStamp] [datetime] NULL,
	[Message] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CPIC]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CPIC](
	[CpicId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](255) NOT NULL,
	[CostAreaCode] [nvarchar](255) NULL,
	[CostAreaName] [nvarchar](255) NULL,
	[ProjectCode] [nvarchar](255) NULL,
	[ProjectName] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Defactos]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Defactos](
	[DefactoId] [int] IDENTITY(1,1) NOT NULL,
	[StatusOfFundsId] [int] NULL,
	[BudgetLevel] [nvarchar](100) NULL,
	[BFY] [nvarchar](100) NULL,
	[EFY] [nvarchar](100) NULL,
	[RpioCode] [nvarchar](100) NULL,
	[RpioName] [nvarchar](100) NULL,
	[AhCode] [nvarchar](100) NULL,
	[AhName] [nvarchar](100) NULL,
	[FundCode] [nvarchar](100) NULL,
	[FundName] [nvarchar](100) NULL,
	[OrgCode] [nvarchar](100) NULL,
	[OrgName] [nvarchar](100) NULL,
	[AccountCode] [nvarchar](50) NULL,
	[RcCode] [nvarchar](100) NULL,
	[BocCode] [nvarchar](100) NULL,
	[BocName] [nvarchar](100) NULL,
	[ProgramProjectCode] [nvarchar](100) NULL,
	[ProgramProjectName] [nvarchar](100) NULL,
	[ProgramAreaCode] [nvarchar](100) NULL,
	[ProgramAreaName] [nvarchar](100) NULL,
	[RcName] [nvarchar](100) NULL,
	[LowerName] [nvarchar](100) NULL,
	[Amount] [float] NULL,
	[Budgeted] [float] NULL,
	[Posted] [float] NULL,
	[OpenCommitments] [float] NULL,
	[ULO] [float] NULL,
	[Expenditures] [float] NULL,
	[Obligations] [float] NULL,
	[Used] [float] NULL,
	[Available] [float] NULL,
	[NpmCode] [nvarchar](100) NULL,
	[NpmName] [nvarchar](100) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Deobligations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Deobligations](
	[DeobligationId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[DocumentNumber] [nvarchar](255) NULL,
	[CalendarYear] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[Date] [datetime] NULL,
	[Amount] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExecutionTables]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExecutionTables](
	[ExecutionTableId] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](255) NULL,
	[Type] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[FullTimeEquivalents]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FullTimeEquivalents](
	[FullTimeEquivalentId] [int] IDENTITY(1,1) NOT NULL,
	[PrcId] [int] NOT NULL,
	[BudgetLevel] [nvarchar](255) NULL,
	[RPIO] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[Amount] [float] NULL,
	[FundName] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[Division] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[ActivityCode] [nvarchar](255) NULL,
	[NpmCode] [nvarchar](255) NULL,
	[NpmName] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[GoalCode] [nvarchar](255) NULL,
	[GoalName] [nvarchar](255) NULL,
	[ObjectiveCode] [nvarchar](255) NULL,
	[ObjectiveName] [nvarchar](255) NULL,
	[AllocationRatio] [float] NULL,
	[ChangeDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Obligations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Obligations](
	[ObligationId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[AhCode] [text] NULL,
	[AhName] [text] NULL,
	[FundCode] [text] NULL,
	[FundName] [text] NULL,
	[OrgCode] [text] NULL,
	[OrgName] [text] NULL,
	[AccountCode] [text] NULL,
	[ProgramProjectCode] [text] NULL,
	[ProgramProjectName] [text] NULL,
	[RcCode] [text] NULL,
	[RcName] [text] NULL,
	[DocumentType] [text] NULL,
	[DocumentNumber] [text] NULL,
	[DocumentControlNumber] [text] NULL,
	[ReferenceDocumentNumber] [text] NULL,
	[ProcessedDate] [today] NULL,
	[LastActivityDate] [today] NULL,
	[Age] [text] NULL,
	[BocCode] [text] NULL,
	[BocName] [text] NULL,
	[FocCode] [text] NULL,
	[FocName] [text] NULL,
	[NpmCode] [text] NULL,
	[NpmName] [text] NULL,
	[VendorCode] [text] NULL,
	[VendorName] [text] NULL,
	[OpenCommitments] [float] NULL,
	[Obligations] [float] NULL,
	[ULO] [float] NULL,
	[Expenditures] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OperatingPlans]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OperatingPlans](
	[OperatingPlanId] [int] IDENTITY(1,1) NOT NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[AhCode] [text] NULL,
	[FundCode] [text] NULL,
	[OrgCode] [text] NULL,
	[AccountCode] [text] NULL,
	[RcCode] [text] NULL,
	[BocCode] [text] NULL,
	[BocName] [text] NULL,
	[Amount] [float] NULL,
	[ITProjectCode] [text] NULL,
	[ProjectCode] [text] NULL,
	[ProjectName] [text] NULL,
	[NpmCode] [text] NULL,
	[ProjectTypeName] [text] NULL,
	[ProjectTypeCode] [text] NULL,
	[ProgramProjectCode] [text] NULL,
	[ProgramAreaCode] [text] NULL,
	[NpmName] [text] NULL,
	[AhName] [text] NULL,
	[FundName] [text] NULL,
	[OrgName] [text] NULL,
	[RcName] [text] NULL,
	[ProgramProjectName] [text] NULL,
	[ActivityCode] [text] NULL,
	[ActivityName] [text] NULL,
	[LocalCode] [text] NULL,
	[LocalCodeName] [text] NULL,
	[ProgramAreaName] [text] NULL,
	[CostAreaCode] [text] NULL,
	[CostAreaName] [text] NULL,
	[GoalCode] [text] NULL,
	[GoalName] [text] NULL,
	[ObjectiveCode] [text] NULL,
	[ObjectiveName] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayPeriods]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayPeriods](
	[PayPeriodId] [int] IDENTITY(1,1) NOT NULL,
	[Period] [nvarchar](255) NOT NULL,
	[PayPeriod] [nvarchar](255) NULL,
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayrollActivity]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollActivity](
	[PayrollActivityId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[FundCode] [text] NULL,
	[FundName] [text] NULL,
	[AhCode] [text] NULL,
	[AhName] [text] NULL,
	[RcCode] [text] NULL,
	[RcName] [text] NULL,
	[SubRcCode] [text] NULL,
	[SubRcName] [text] NULL,
	[AccountCode] [text] NULL,
	[ProgramProjectCode] [text] NULL,
	[ProgramProjectName] [text] NULL,
	[ProgramAreaCode] [text] NULL,
	[ProgramAreaName] [text] NULL,
	[NpmCode] [text] NULL,
	[NpmName] [text] NOT NULL,
	[FocCode] [text] NULL,
	[FocName] [text] NULL,
	[HrOrgCode] [text] NULL,
	[HrOrgName] [text] NULL,
	[WorkCode] [text] NULL,
	[WorkCodeName] [text] NULL,
	[PayPeriod] [text] NULL,
	[StartDate] [today] NULL,
	[EndDate] [today] NULL,
	[CheckDate] [today] NULL,
	[Amount] [float] NULL,
	[Hours] [float] NULL,
	[BasePaid] [float] NULL,
	[BaseHours] [float] NULL,
	[Benefits] [float] NULL,
	[OvertimePaid] [float] NULL,
	[OvertimeHours] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayrollAuthority]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollAuthority](
	[PayrollId] [int] IDENTITY(1,1) NOT NULL,
	[AllocationsId] [int] NOT NULL,
	[StatusOfFundsId] [int] NOT NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[BudgetLevel] [text] NULL,
	[AhCode] [text] NULL,
	[AhName] [text] NULL,
	[FundCode] [text] NULL,
	[FundName] [text] NULL,
	[OrgCode] [text] NULL,
	[OrgName] [text] NULL,
	[AccountCode] [text] NULL,
	[RcCode] [text] NULL,
	[RcName] [text] NULL,
	[BocCode] [tinyint] NULL,
	[BocName] [text] NULL,
	[Amount] [float] NULL,
	[ProgramProjectCode] [text] NULL,
	[ProgramProjectName] [text] NULL,
	[ProgramAreaCode] [text] NULL,
	[ProgramAreaName] [text] NULL,
	[NpmCode] [text] NULL,
	[NpmName] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayrollCostCodes]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollCostCodes](
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
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProgramFinancingSchedule]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProgramFinancingSchedule](
	[ID] [int] NOT NULL,
	[ReportFiscalYear] [text] NULL,
	[ReportFiscalMonth] [text] NULL,
	[ReportFiscalQuarter] [text] NULL,
	[FY1] [text] NULL,
	[FY2] [text] NULL,
	[TRACCT] [text] NULL,
	[SGL_ACCT] [text] NULL,
	[LINENO] [text] NULL,
	[AMT] [float] NULL,
	[AMT_ORIG] [float] NULL,
	[BUD_AMT] [float] NULL,
	[AGY_AMT] [float] NULL,
	[SECTION_NO] [text] NULL,
	[SECTION_NAME] [text] NULL,
	[LINE_DESC_SHORT] [text] NULL,
	[BUDGET_ACCT_ID] [text] NULL,
	[ACCT] [text] NULL,
	[AGESEQ] [text] NULL,
	[ACCTSEQ] [text] NULL,
	[AGETL] [text] NULL,
	[BURTL] [text] NULL,
	[ACCTTL] [text] NULL,
	[TRACCTTL] [text] NULL,
	[TRAG_ALLO_TRAC] [text] NULL,
	[Year2Year1] [text] NULL,
	[FLTR_AGETL] [text] NULL,
	[FLTR_BUDGET_ACCT_ID] [text] NULL,
 CONSTRAINT [PK_ProgramFinancingSchedule] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RegionalAuthority]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RegionalAuthority](
	[RescissionId] [int] IDENTITY(1,1) NOT NULL,
	[PrcId] [int] NULL,
	[RPIO] [nvarchar](255) NULL,
	[BudgetLevel] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[ActivityCode] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[Allocation] [money] NULL,
	[Reduction] [money] NULL,
	[Amount] [money] NULL,
	[FundName] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[Division] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[NpmCode] [nvarchar](255) NULL,
	[NpmName] [nvarchar](255) NULL,
	[GoalCode] [nvarchar](255) NULL,
	[GoalName] [nvarchar](255) NULL,
	[ObjectiveCode] [nvarchar](255) NULL,
	[ObjectiveName] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ReimbursableAgreements]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ReimbursableAgreements](
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
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ReimbursableFunds]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ReimbursableFunds](
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
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Reprogrammings]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Reprogrammings](
	[ReprogrammingId] [int] IDENTITY(1,1) NOT NULL,
	[ReprogrammingNumber] [nvarchar](255) NULL,
	[ProcessedDate] [nvarchar](255) NULL,
	[RPIO] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[Amount] [numeric](18, 0) NULL,
	[SPIO] [nvarchar](255) NULL,
	[Purpose] [nvarchar](255) NULL,
	[ExtendedPurpose] [nvarchar](255) NULL,
	[FromTo] [nvarchar](255) NULL,
	[DocType] [nvarchar](255) NULL,
	[DocPrefix] [nvarchar](255) NULL,
	[NpmCode] [nvarchar](255) NULL,
	[Line] [nvarchar](255) NULL,
	[Subline] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SF132]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SF132](
	[ID] [int] IDENTITY(713,1) NOT NULL,
	[FiscalYear] [text] NULL,
	[ActivityID] [text] NULL,
	[TAFS] [text] NULL,
	[FilteronTAFS] [text] NULL,
	[TAFS10] [text] NULL,
	[FilteronTAFS10] [text] NULL,
	[TreasuryAgency] [text] NULL,
	[AllocationAgency] [text] NULL,
	[AllocationSubaccount] [text] NULL,
	[TreasuryAccount] [text] NULL,
	[BeginPeriodOfAvailability] [text] NULL,
	[EndPeriodOfAvailability] [text] NULL,
	[AvailabilityType] [text] NULL,
	[TreasuryAccountTitle] [text] NULL,
	[AllocationAgencyTitle] [text] NULL,
	[BudgetAgency] [text] NULL,
	[BudgetBureau] [text] NULL,
	[BudgetAccount] [text] NULL,
	[BudgetAgencyTitle] [text] NULL,
	[BudgetBureauTitle] [text] NULL,
	[BudgetAccountTitle] [text] NULL,
	[TreasuryAgencyTAFS10] [text] NULL,
	[AllocationAccount10] [text] NULL,
	[TreasuryAccount10] [text] NULL,
	[FY1TAFS10] [text] NULL,
	[FY2TAFS10] [text] NULL,
	[BudgetAgencySeq] [text] NULL,
	[BudgetBureauSeq] [text] NULL,
	[BudgetAccountSeq] [text] NULL,
	[ApprovalDate] [text] NULL,
	[ApprovedFootnoteId] [text] NULL,
	[ApportionmentLineNumber] [text] NULL,
	[LineSplit] [text] NULL,
	[LineStub] [text] NULL,
	[ApprovedAmount] [float] NULL,
	[LineSort] [text] NULL,
	[FootnoteNumber] [text] NULL,
	[FootnoteText] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SF133]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SF133](
	[ID] [int] IDENTITY(713,1) NOT NULL,
	[ReportYear] [text] NULL,
	[AGENCY] [text] NULL,
	[BUREAU] [text] NULL,
	[OmbAccount] [text] NULL,
	[TreasuryAccountGroup] [text] NULL,
	[AllocationAccount] [text] NULL,
	[TreasuryAccount] [text] NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[STAT] [text] NULL,
	[CreditIndicator] [text] NULL,
	[COHORT] [text] NULL,
	[LineNumber] [text] NULL,
	[LineDescription] [text] NULL,
	[Category] [text] NULL,
	[TAFS] [text] NULL,
	[AgencyTitle] [text] NULL,
	[LastUpdated] [today] NULL,
	[SECTION] [text] NULL,
	[SectionNumber] [text] NULL,
	[LineType] [text] NULL,
	[TafsAccount] [text] NULL,
	[BureauTitle] [text] NULL,
	[OmbAccountTitle] [text] NULL,
	[FinancingAccounts] [text] NULL,
	[AMT_NOV] [float] NULL,
	[AMT_JAN] [float] NULL,
	[AMT_FEB] [float] NULL,
	[AMT_APR] [float] NULL,
	[AMT_MAY] [float] NULL,
	[AMT_JUL] [float] NULL,
	[AMT_AUG] [float] NULL,
	[AGEUP] [text] NULL,
	[AMT_OCT] [float] NULL,
	[AMT1] [float] NULL,
	[AMT2] [float] NULL,
	[AMT3] [float] NULL,
	[AMT4] [float] NULL,
	[LineShortDescription] [text] NULL,
	[ProgramCategory] [text] NULL,
	[ProgramCategoryStub] [text] NULL,
	[CategoryStub] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SiteProjectCodes]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SiteProjectCodes](
	[SiteProjectCodeId] [int] IDENTITY(713,1) NOT NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[State] [text] NULL,
	[CongressionalDistrict] [text] NULL,
	[EpaSiteId] [text] NULL,
	[SiteProjectName] [text] NULL,
	[SiteProjectCode] [text] NULL,
	[SSID] [text] NULL,
	[ActionCode] [text] NULL,
	[OperableUnit] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[StateGrantObligations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StateGrantObligations](
	[StateGrantObligationId] [int] IDENTITY(713,1) NOT NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[FundCode] [text] NULL,
	[FundName] [text] NULL,
	[AhCode] [text] NULL,
	[AhName] [text] NULL,
	[OrgCode] [text] NULL,
	[OrgName] [text] NULL,
	[StateCode] [text] NULL,
	[StateName] [text] NULL,
	[AccountCode] [text] NULL,
	[ProgramProjectCode] [text] NULL,
	[ProgramProjectName] [text] NULL,
	[RcCode] [text] NULL,
	[RcName] [text] NULL,
	[BocCode] [text] NULL,
	[BocName] [text] NULL,
	[Amount] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[StatusOfFunds]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StatusOfFunds](
	[StatusOfFundsId] [int] IDENTITY(713,1) NOT NULL,
	[BudgetLevel] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[AhName] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[LowerName] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[RcName] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[OrgName] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[Amount] [float] NULL,
	[OpenCommitments] [float] NULL,
	[ULO] [float] NULL,
	[Total Expense Accruals] [float] NULL,
	[Expenditures] [float] NULL,
	[Obligations] [float] NULL,
	[Used] [float] NULL,
	[Available] [float] NULL,
	[NpmCode] [nvarchar](255) NULL,
	[NpmName] [nvarchar](255) NULL,
	[NpmTitle] [nvarchar](255) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SuperfundSites]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SuperfundSites](
	[SiteId] [int] NOT NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[City] [text] NULL,
	[State] [text] NULL,
	[SSID] [text] NULL,
	[SiteProjectName] [text] NULL,
	[EpaSiteId] [text] NULL,
 CONSTRAINT [PK_SuperfundSites] PRIMARY KEY CLUSTERED 
(
	[SiteId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TAFS]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TAFS](
	[TafsId] [int] IDENTITY(713,1) NOT NULL,
	[FiscalYear] [text] NULL,
	[ActivityID] [text] NULL,
	[TAFS] [text] NULL,
	[FilteronTAFS] [text] NULL,
	[TAFS_10] [text] NULL,
	[FilteronTAFS_10] [text] NULL,
	[TreasuryAgency] [text] NULL,
	[AllocationAgency] [text] NULL,
	[AllocationSubaccount] [text] NULL,
	[TreasuryAccountNumber] [text] NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[AvailabilityType] [text] NULL,
	[TreasuryAccountTitle] [text] NULL,
	[AllocationAgencyTitle] [text] NULL,
	[BudgetAgency] [text] NULL,
	[BudgetBureau] [text] NULL,
	[BudgetAccount] [text] NULL,
	[BudgetAgencyTitle] [text] NULL,
	[BudgetBureauTitle] [text] NULL,
	[BudgetAccountTitle] [text] NULL,
	[TreasuryAgencyTAF] [text] NULL,
	[AllocationAccount] [text] NULL,
	[TreasuryAccount] [text] NULL,
	[FY1TAFS] [text] NULL,
	[FY2TAFS] [text] NULL,
	[BudgetAgencySeq] [text] NULL,
	[BudgetBureauSeq] [text] NULL,
	[BudgetAccountSeq] [text] NULL,
	[ApprovedDate] [today] NULL,
	[RequestDate] [today] NULL,
	[LastDate] [text] NULL,
	[Transfers] [text] NULL,
	[Warrants] [text] NULL,
	[Exempt] [text] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Transfers]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Transfers](
	[TransferId] [int] IDENTITY(713,1) NOT NULL,
	[BudgetLevel] [nvarchar](255) NULL,
	[DocType] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[RPIO] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[DocumentNumber] [nvarchar](255) NULL,
	[ProcessedDate] [datetime] NULL,
	[AhCode] [nvarchar](255) NULL,
	[AhName] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[OrgName] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[Code] [nvarchar](255) NOT NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ResourceType] [nvarchar](255) NULL,
	[Line] [float] NULL,
	[Subline] [float] NULL,
	[FromTo] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[Amount] [float] NOT NULL,
	[Purpose] [ntext] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TravelActivity]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TravelActivity](
	[TravelActivityId] [int] IDENTITY(713,1) NOT NULL,
	[RpioCode] [text] NULL,
	[RpioName] [text] NULL,
	[BFY] [text] NULL,
	[AhCode] [text] NULL,
	[AhName] [text] NULL,
	[FundCode] [text] NULL,
	[FundName] [text] NULL,
	[AccountCode] [text] NULL,
	[ProgramProjectCode] [text] NULL,
	[ProgramProjectName] [text] NULL,
	[OrgCode] [text] NULL,
	[OrgName] [text] NULL,
	[BocCode] [text] NULL,
	[BocName] [text] NULL,
	[RcCode] [text] NULL,
	[RcName] [text] NULL,
	[FocCode] [text] NULL,
	[FocName] [text] NULL,
	[FirstName] [text] NULL,
	[LastName] [text] NULL,
	[StartDate] [today] NULL,
	[EndDate] [today] NULL,
	[Duration] [float] NULL,
	[DocumentControlNumber] [text] NULL,
	[Obligations] [float] NULL,
	[ULO] [float] NULL,
	[Expenditures] [float] NULL,
	[Extra] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TreasuryAppropriationFundSymbols]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TreasuryAppropriationFundSymbols](
	[ID] [int] NOT NULL,
	[FiscalYear] [text] NULL,
	[ActivityID] [text] NULL,
	[TafsCode] [text] NULL,
	[TafsCaption] [text] NULL,
	[TAFS_10] [text] NULL,
	[TafsCaption_10] [text] NULL,
	[TreasuryAgency] [text] NULL,
	[TreasuryAgencyCode] [text] NULL,
	[TreasuryAccount] [text] NULL,
	[TreasuryAccountCode] [text] NULL,
	[TreasuryAccountTitle] [text] NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[OmbAgencyCode] [text] NULL,
	[OmbAgencyTitle] [text] NULL,
	[OmbBureauCode] [text] NULL,
	[OmbBureauTitle] [text] NULL,
	[OmbAccountCode] [text] NULL,
	[OmbAccountTitle] [text] NULL,
	[BeginningPeriodOfAvailability] [text] NULL,
	[EndingPeriodOfAvailability] [text] NULL,
	[AgencySequence] [text] NULL,
	[BureauSequence] [text] NULL,
	[AccountSequence] [text] NULL,
	[LatestApprovedApportionmentDate] [text] NULL,
	[LatestApportionmentRequestDate] [text] NULL,
	[LatestSF133Date] [text] NULL,
 CONSTRAINT [PK_TreasuryAppropriationFundSymbols] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TreasuryStatements]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TreasuryStatements](
	[ID] [int] NOT NULL,
	[FiscalYear] [text] NULL,
	[LineNumber] [text] NULL,
	[LineTitle] [text] NULL,
	[TaxationCode] [text] NULL,
	[TreasuryAgency] [text] NULL,
	[TreasuryAccount] [text] NULL,
	[SubAccount] [text] NULL,
	[BFY] [text] NULL,
	[EFY] [text] NULL,
	[OmbAgency] [text] NULL,
	[OmbBureau] [text] NULL,
	[OmbAccount] [text] NULL,
	[AgencySequence] [text] NULL,
	[BureauSequence] [text] NULL,
	[AccountSequence] [text] NULL,
	[AgencyTitle] [text] NULL,
	[BureauTitle] [text] NULL,
	[OmbAccountTitle] [text] NULL,
	[TreasuryAccountTitle] [text] NULL,
	[October] [float] NULL,
	[November] [float] NULL,
	[December] [float] NULL,
	[January] [float] NULL,
	[Feburary] [float] NULL,
	[March] [float] NULL,
	[April] [float] NULL,
	[May] [float] NULL,
	[June] [float] NULL,
	[July] [float] NULL,
	[August] [float] NULL,
	[September] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


