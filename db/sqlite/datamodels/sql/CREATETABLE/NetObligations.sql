CREATE TABLE IF NOT EXISTS "NetObligations" 
(
	"NetObligationsId"	INTEGER UNIQUE,
	"BFY"	TEXT(50) DEFAULT 'NS',
	"EFY"	TEXT(50) DEFAULT 'NS',
	"FundCode"	TEXT(50) DEFAULT 'NS',
	"FundName"	TEXT(50) DEFAULT 'NS',
	"RpioCode"	TEXT(50) DEFAULT 'NS',
	"RpioName"	TEXT(50) DEFAULT 'NS',
	"AhCode"	TEXT(50) DEFAULT 'NS',
	"AhName"	TEXT(50) DEFAULT 'NS',
	"OrgCode"	TEXT(50) DEFAULT 'NS',
	"OrgName"	TEXT(50) DEFAULT 'NS',
	"AccountCode"	TEXT(50) DEFAULT 'NS',
	"ProgramProjectName"	TEXT(50) DEFAULT 'NS',
	"BocCode"	TEXT(50) DEFAULT 'NS',
	"BocName"	TEXT(50) DEFAULT 'NS',
	"DocumentNumber"	TEXT(50) DEFAULT 'NS',
	"ProcessedDate"	TEXT(50) DEFAULT 'NS',
	"Net"	TEXT(50) DEFAULT 'NS',
	"Amount"	NUMERIC DEFAULT 0.0,
	PRIMARY KEY("NetObligationsId" AUTOINCREMENT)
);