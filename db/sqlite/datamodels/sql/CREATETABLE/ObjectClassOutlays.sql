CREATE TABLE "ObjectClassOutlays" 
(
	"ObjectClassOutlaysId"	INTEGER NOT NULL UNIQUE,
	"ReportYear"	TEXT,
	"OmbAgencyCode"	TEXT,
	"OmbAgencyName"	TEXT,
	"OmbBureauCode"	TEXT,
	"OmbBureauName"	TEXT,
	"OmbAccountCode"	TEXT,
	"OmbAccountName"	TEXT,
	"Direct/Reimbursable"	TEXT,
	"DirectReimbursableTitle"	TEXT,
	"ObjectClassGroupNumber"	TEXT,
	"ObjectClassGroupName"	TEXT,
	"FinanceObjectClass"	TEXT,
	"PriorYear"	REAL,
	"CurrentYear"	REAL,
	"BudgetYear"	REAL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);