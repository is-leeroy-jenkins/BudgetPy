CREATE TABLE [dbo].[Changes]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](255) NULL,
	[FieldName] [nvarchar](255) NULL,
	[Action] [nvarchar](255) NULL,
	[OldValue] [nvarchar](255) NULL,
	[NewValue] [nvarchar](255) NULL,
	[TimeStamp] [datetime] NULL,
	[Message] [nvarchar](255) NULL
);

