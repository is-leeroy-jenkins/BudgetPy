CREATE TABLE AllowanceHolders
(
	AllowanceHoldersId INT           NOT NULL UNIQUE,
	Code               NVARCHAR(150) NULL DEFAULT ('NS'),
	Name               NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT AllowanceHoldersPrimaryKey PRIMARY KEY
		(
		  AllowanceHoldersId ASC
			)
);
