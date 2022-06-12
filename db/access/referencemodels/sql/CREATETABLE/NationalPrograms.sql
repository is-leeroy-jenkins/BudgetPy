CREATE TABLE IF NOT EXISTS NationalPrograms 
(
	NationalProgramsId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255) NOT NULL,
	Name	TEXT(255),
	RpioCode	TEXT(255),
	Title	TEXT(255),
	CONSTRAINT PrimaryKeyNationalPrograms PRIMARY KEY(NationalProgramsId AUTOINCREMENT)
);