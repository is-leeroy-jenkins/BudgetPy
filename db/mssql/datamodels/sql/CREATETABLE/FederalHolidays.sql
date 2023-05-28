CREATE TABLE FederalHolidays 
(
	FederalHolidaysId	INT NOT NULL IDENTITY(1,1),
	BFY	NVARCHAR(80) NULL,
	ColumbusDay	DATETIME NULL,
	VeteransDay	DATETIME NULL,
	ThanksgivingDay	DATETIME NULL,
	ChristmasDay	DATETIME NULL,
	NewYearsDay	DATETIME NULL,
	MartinLutherKingsDay	DATETIME NULL,
	PresidentsDay	DATETIME NULL,
	MemorialDay	DATETIME NULL,
	JuneteenthDay	DATETIME NULL,
	IndependenceDay	DATETIME NULL,
	LaborDay	DATETIME NULL
);