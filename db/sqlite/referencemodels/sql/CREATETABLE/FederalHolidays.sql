CREATE TABLE IF NOT EXISTS FederalHolidays 
(
	FederalHolidaysId	INTEGER NOT NULL UNIQUE,
	BFY	TEXT(255),
	Columbus	TEXT(255),
	Veterans	TEXT(255),
	Thanksgiving	TEXT(255),
	Christmas	TEXT(255),
	NewYears	TEXT(255),
	MartinLutherKing	TEXT(255),
	Presidents	TEXT(255),
	Memorial	TEXT(255),
	Juneteenth	TEXT(255),
	Independence	TEXT(255),
	Labor	TEXT(255),
	PRIMARY KEY(FederalHolidaysId AUTOINCREMENT)
);