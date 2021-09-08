CREATE TABLE ControlNumbers
(
	ControlNumberId INTEGER NOT NULL,
	RPIO TEXT(255) NULL,
	RegionNumber DOUBLE NULL,
	BFY TEXT(255) NULL,
	CalendarYear TEXT(255) NULL,
	FundCode TEXT(255) NULL,
	FundNumber TEXT(255) NULL,
	AhCode TEXT(255) NULL,
	RcCode TEXT(255) NULL,
	DivisionName TEXT(255) NULL,
	DivisionNumber DOUBLE NULL,
	DateIssued DATETIME NULL,
	Purpose TEXT(255) NULL
);

