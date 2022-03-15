CREATE TABLE "UnobligatedBalances" 
(
	"UnobligatedBalancesId"	INTEGER NOT NULL UNIQUE,
	"BudgetYear"	TEXT,
	"AgencyTitle"	TEXT,
	"BureauTitle"	TEXT,
	"OmbAccount"	TEXT,
	"AgencyCode"	TEXT,
	"BureauCode"	TEXT,
	"AccountCode"	TEXT,
	"Transmit"	TEXT,
	"AgencySequence"	TEXT,
	"OmbAccountTitle"	TEXT,
	"LineName"	TEXT,
	"LineNumber"	TEXT,
	"PriorYearAmount"	REAL,
	"CurrentYearAmount"	REAL,
	"BudgetYearAmount"	REAL,
	PRIMARY KEY("UnobligatedBalanceId" AUTOINCREMENT)
);