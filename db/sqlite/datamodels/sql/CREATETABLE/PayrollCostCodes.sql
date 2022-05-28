CREATE TABLE "ProjectCostCodes" 
(
	"ProjectCostCodesId" INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT,
	"RpioCode"	TEXT,
	"RpioName"	TEXT,
	"AhCode"	TEXT,
	"AhName"	TEXT,
	"FundCode"	TEXT,
	"FundName"	TEXT,
	"AccountCode"	TEXT,
	"ProgramProjectName"	TEXT,
	"BocCode"	TEXT,
	"BocName"	TEXT,
	"OrgCode"	TEXT,
	"OrgName"	TEXT,
	"VendorCode"	TEXT,
	"VendorName"	TEXT,
	PRIMARY KEY("ProjectCostCodeId" AUTOINCREMENT)
);