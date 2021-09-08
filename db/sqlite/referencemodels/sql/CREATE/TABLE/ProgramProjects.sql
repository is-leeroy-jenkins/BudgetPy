CREATE TABLE ProgramProjects
(
	ProgramProjectId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyProgramProjects PRIMARY KEY AUTOINCREMENT,
	Code TEXT(255) NOT NULL,
	Name TEXT(255) NULL,
	Title TEXT(255) NULL,
	Laws TEXT(255) NULL,
	Narrative TEXT(255) NULL,
	Definition TEXT(255) NULL,
	ProgramAreaCode TEXT(255) NULL,
	ProgramAreaName TEXT(255) NULL
);

