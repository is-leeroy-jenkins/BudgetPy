CREATE TABLE 'SuperfundSites' 
(
	'SiteId' INTEGER NOT NULL,
	'RpioCode' TEXT(255),
	'RpioName' TEXT(255),
	'City' TEXT(255),
	'State' TEXT(255),
	'SSID' TEXT(255),
	'SiteProjectName' TEXT(255),
	'EpaSiteId' TEXT(255),
	PRIMARY KEY('SiteId' AUTOINCREMENT)
);