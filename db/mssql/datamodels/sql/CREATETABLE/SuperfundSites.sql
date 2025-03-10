CREATE TABLE SuperfundSites
(
	SuperfundSitesId INT           NOT NULL UNIQUE,
	RpioCode         NVARCHAR(150) NULL DEFAULT ('NS'),
	RpioName         NVARCHAR(150) NULL DEFAULT ('NS'),
	City             NVARCHAR(150) NULL DEFAULT ('NS'),
	State            NVARCHAR(150) NULL DEFAULT ('NS'),
	SSID             NVARCHAR(150) NULL DEFAULT ('NS'),
	SiteProjectName  NVARCHAR(150) NULL DEFAULT ('NS'),
	EpaSiteId        NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT SuperfundSitesPrimaryKey PRIMARY KEY
		(
		  SuperfundSitesId ASC
			)
);
