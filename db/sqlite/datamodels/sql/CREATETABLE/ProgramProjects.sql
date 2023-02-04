CREATE TABLE IF NOT EXISTS ProgramProjects
(
	ProgramProjectId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyProgramProjects PRIMARY KEY AUTOINCREMENT,
	Code TEXT(80) NOT NULL,
	Name TEXT(80) NULL,
	Title TEXT(80) NULL,
	Laws TEXT(80) NULL,
	Narrative TEXT(80) NULL,
	Definition TEXT(80) NULL,
	ProgramAreaCode TEXT(80) NULL,
	ProgramAreaName TEXT(80) NULL
);

