CREATE TABLE CongressionalControls 
(
	CongressionalControlsId	INT NOT NULL IDENTITY(1,1),
	FundCode	NVARCHAR(80) NULL,
	FundName	NVARCHAR(80) NULL,
	ProgramAreaCode	NVARCHAR(80) NULL,
	ProgramAreaName	NVARCHAR(80) NULL,
	ProgramProjectCode	NVARCHAR(80) NULL,
	ProgramProjectName	NVARCHAR(80) NULL,
	SubProjectCode	NVARCHAR(80) NULL,
	SubProjectName	NVARCHAR(80) NULL,
	ReprogrammingRestriction	NVARCHAR(80) NULL,
	IncreaseRestriction	NVARCHAR(80) NULL,
	DecreaseRestriction	NVARCHAR(80) NULL,
	MemoRequirement	NVARCHAR(80) NULL
);