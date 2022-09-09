CREATE TABLE IF NOT EXISTS ResponsibilityCenters (
	ResponsibilityCentersId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255),
	Name	TEXT(255),
	Title	TEXT(255),
	CONSTRAINT PrimaryKeyResponsibilityCenters PRIMARY KEY(ResponsibilityCentersId AUTOINCREMENT)
)