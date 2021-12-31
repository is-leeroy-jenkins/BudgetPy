CREATE TABLE "GrowthRates" 
(
	"GrowthRatesId"	INTEGER NOT NULL UNIQUE,
	"RateId"	TEXT,
	"DESCRIPTION"	TEXT,
	"BudgetYearRate"	REAL,
	"OutYear1"	REAL,
	"OutYear2"	REAL,
	"OutYear3"	REAL,
	"OutYear4"	REAL,
	"OutYear5"	REAL,
	"OutYear6"	REAL,
	"OutYear7"	REAL,
	"OutYear8"	REAL,
	"OutYear9"	REAL,
	"Sort"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
)