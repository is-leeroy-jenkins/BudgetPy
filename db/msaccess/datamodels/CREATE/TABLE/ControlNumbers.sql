CREATE TABLE [ControlNumbers]
(
   [CnId] INT NOT NULL IDENTITY (37,1),
   [BFY] NVARCHAR(255),
   [Region] NVARCHAR(255),
   [AhCode] NVARCHAR(255),
   [RegionControlNumber] FLOAT,
   [FundCode] NVARCHAR(255),
   [FundControlNumber] FLOAT,
   [RcCode] NVARCHAR(255),
   [DivisionName] NVARCHAR(255),
   [DivisionControlNumber] FLOAT,
   [DateIssued] DATETIME
);

ALTER TABLE [ControlNumbers] ADD CONSTRAINT [PK_ControlNumbers] PRIMARY KEY ([CnId]);
