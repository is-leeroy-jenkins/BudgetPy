CREATE TABLE [dbo].[ColumnSchema]
(
	[ColumnSchemaId] [int] IDENTITY(1,1) NOT NULL,
	[DataType] [nvarchar](255) NULL,
	[ColumnName] [nvarchar](255) NULL,
	[TableName] [nvarchar](255) NULL,
	[ColumnCaption] [nvarchar](255) NULL
);


