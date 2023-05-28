CREATE TABLE Resources 
(
	ResourcesId	INT NOT NULL IDENTITY(1,1),
	Identifier	NVARCHAR(80) NULL,
	Type	NVARCHAR(80) NULL,
	Location	NVARCHAR(80) NULL,
	FileExtension NULL,
	Caption	NVARCHAR(80) NULL
);