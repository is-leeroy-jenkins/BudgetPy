CREATE TABLE IF NOT EXISTS ResourcePlanningOffices 
(
	ResourcePlanningOfficesId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255),
	Name	TEXT(255),
	CONSTRAINT PrimaryKeyResourcePlanningOffices PRIMARY KEY(ResourcePlanningOfficesId AUTOINCREMENT)
);