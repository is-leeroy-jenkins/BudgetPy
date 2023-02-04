CREATE TABLE IF NOT EXISTS Accounts 
(
	AccountsId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255),
	ProgramAreaCode	TEXT(255),
	GoalCode	TEXT(255),
	ObjectiveCode	TEXT(255),
	NpmCode	TEXT(255),
	NpmName	TEXT(255),
	ProgramProjectCode	TEXT(255),
	ProgramProjectName	TEXT(255),
	ActivityCode	TEXT(255),
	ActivityName	TEXT(255),
	AgencyActivity	TEXT(255),
	PRIMARY KEY(AccountsId AUTOINCREMENT)
);