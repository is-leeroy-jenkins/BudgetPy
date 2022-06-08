CREATE TABLE IF NOT EXISTS StateOrganizations 
(
	StateOrganizationsId	INTEGER NOT NULL UNIQUE,
	Name	TEXT,
	Code	TEXT,
	RpioName	TEXT,
	RpioCode	TEXT,
	PRIMARY KEY(StateOrganizationsId AUTOINCREMENT)
);