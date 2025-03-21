CREATE TABLE Organizations
(
	OrganizationsId INT           NOT NULL UNIQUE,
	BFY             NVARCHAR(150) NULL DEFAULT ('NS'),
	Code            NVARCHAR(150) NULL DEFAULT ('NS'),
	PreventNewUse   NVARCHAR(150) NULL DEFAULT ('NS'),
	Name            NVARCHAR(150) NULL DEFAULT ('NS'),
	Status          NVARCHAR(150) NULL DEFAULT ('NS'),
	SecurityOrg     NVARCHAR(150) NULL DEFAULT ('NS'),
	Usage           NVARCHAR(150) NULL DEFAULT ('NS'),
	UseAsCostOrg    NVARCHAR(150) NULL DEFAULT ('NS'),
	SubCodeRequired NVARCHAR(150) NULL DEFAULT ('NS'),
	RpioCode        NVARCHAR(150) NULL DEFAULT ('NS'),
	AhCode          NVARCHAR(150) NULL DEFAULT ('NS'),
	RcCode          NVARCHAR(150) NULL DEFAULT ('NS'),
	SubRcCode       NVARCHAR(150) NULL DEFAULT ('NS'),
	Description     NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT OrganizationsPrimaryKey PRIMARY KEY
		(
		  OrganizationsId ASC
			)
);
