CREATE TABLE IF NOT EXISTS ResourcePlanningOffices 
(
	ResourcePlanningOfficesId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(80) NULL DEFAULT NS,
	Name	TEXT(80) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyResourcePlanningOffices PRIMARY KEY(ResourcePlanningOfficesId AUTOINCREMENT)
);