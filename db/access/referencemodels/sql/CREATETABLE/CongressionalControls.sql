CREATE TABLE IF NOT EXISTS CongressionalControls 
(
	CongressionalControlsId	INTEGER NOT NULL UNIQUE,
	FundCode	TEXT(255),
	FundName	TEXT(255),
	ProgramAreaCode	TEXT(255),
	ProgramAreaName	TEXT(255),
	ProgramProjectCode	TEXT(255),
	ProgramProjectName	TEXT(255),
	SubProjectCode	TEXT(255),
	SubProjectName	TEXT(255),
	ReprogrammingRestriction	TEXT(255),
	IncreaseRestriction	TEXT(255),
	DecreaseRestriction	TEXT(255),
	MemoRequirement	TEXT(255),
	PRIMARY KEY(CongressionalControlsId AUTOINCREMENT)
);