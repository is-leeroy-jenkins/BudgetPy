CREATE TABLE ProgramDescriptions 
(
	ProgramDescriptionsId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255) NOT NULL,
	Name	TEXT(255),
	Title	TEXT(255),
	Laws	TEXT(255),
	Narrative	TEXT(255),
	Definition	TEXT(255),
	ProgramAreaCode	TEXT(255),
	ProgramAreaName	TEXT(255),
	CONSTRAINT PrimaryKeyProgramDescriptions PRIMARY KEY(ProgramDescriptionsId AUTOINCREMENT)
);