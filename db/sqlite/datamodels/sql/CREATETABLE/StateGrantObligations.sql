CREATE TABLE IF NOT EXISTS "StateGrantObligations" 
(
	"StateGrantObligationsId"	INTEGER NOT NULL UNIQUE,
	"RpioCode"	TEXT(80) DEFAULT 'NS',
	"RpioName"	TEXT(80) DEFAULT 'NS',
	"FundCode"	TEXT(80) DEFAULT 'NS',
	"FundName"	TEXT(80) DEFAULT 'NS',
	"AhCode"	TEXT(80) DEFAULT 'NS',
	"AhName"	TEXT(80) DEFAULT 'NS',
	"OrgCode"	TEXT(80) DEFAULT 'NS',
	"OrgName"	TEXT(80) DEFAULT 'NS',
	"StateCode"	TEXT(80) DEFAULT 'NS',
	"StateName"	TEXT(80) DEFAULT 'NS',
	"AccountCode"	TEXT(80) DEFAULT 'NS',
	"ProgramProjectCode"	TEXT(80) DEFAULT 'NS',
	"ProgramProjectName"	TEXT(80) DEFAULT 'NS',
	"RcCode"	TEXT(80) DEFAULT 'NS',
	"RcName"	TEXT(80) DEFAULT 'NS',
	"BocCode"	TEXT(80) DEFAULT 'NS',
	"BocName"	TEXT(80) DEFAULT 'NS',
	"Amount"	NUMERIC DEFAULT 0.0,
	PRIMARY KEY("StateGrantObligationsId" AUTOINCREMENT)
);