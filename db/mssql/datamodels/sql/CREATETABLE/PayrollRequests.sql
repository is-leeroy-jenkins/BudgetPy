CREATE TABLE PayrollRequests 
(
	PayrollRequestsId	INT NOT NULL IDENTITY(1,1),
	ControlTeamAnalyst	NVARCHAR(80) NULL,
	RpioCode	NVARCHAR(80) NULL,
	DocumentTitle	NVARCHAR(80) NULL,
	Amount	FLOAT NULL,
	FundCode	NVARCHAR(80) NULL,
	Status	NVARCHAR(80) NULL,
	OriginalRequestDate	NVARCHAR(80) NULL,
	LastActivityDate	NVARCHAR(80) NULL,
	BFS	NVARCHAR(80) NULL,
	Comments	NVARCHAR(80) NULL,
	RequestDocument	NVARCHAR(80) NULL,
	Duration	FLOAT NULL
);