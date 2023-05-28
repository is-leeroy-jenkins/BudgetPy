CREATE TABLE AdministrativeRequests 
(
	AdministrativeRequestsId	INT NOT NULL IDENTITY(1,1),
	RequestId	NVARCHAR(80) NULL,
	ControlTeamAnalyst	NVARCHAR(80) NULL,
	RpioCode	NVARCHAR(80) NULL,
	DocumentTitle	NVARCHAR(80) NULL,
	Amount	NVARCHAR(80) NULL,
	FundCode	NVARCHAR(80) NULL,
	BFY	INT,
	Status	NVARCHAR(80) NULL,
	OriginalRequestDate	NVARCHAR(80) NULL,
	LastActivityDate	NVARCHAR(80) NULL,
	Duration	INT,
	BFS	NVARCHAR(80) NULL,
	Comments	NVARCHAR(80) NULL,
	RequestDocument	NVARCHAR(80) NULL,
	RequestType	NVARCHAR(80) NULL,
	TypeCode	NVARCHAR(80) NULL,
	Decision	NVARCHAR(80) NULL
);

