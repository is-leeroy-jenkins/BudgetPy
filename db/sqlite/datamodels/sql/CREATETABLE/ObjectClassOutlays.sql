CREATE TABLE IF NOT EXISTS "ObjectClassOutlays" 
(
	"ObjectClassOutlaysId"	INTEGER NOT NULL UNIQUE,
	"ReportYear"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAgencyCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAgencyName"	TEXT(80) NULL DEFAULT 'NS',
	"OmbBureauCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbBureauName"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAccountCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAccountName"	TEXT(80) NULL DEFAULT 'NS',
	"ObligationType"	TEXT(80) NULL DEFAULT 'NS',
	"DirectReimbursableTitle"	TEXT(80) NULL DEFAULT 'NS',
	"ObjectClassGroupNumber"	TEXT(80) NULL DEFAULT 'NS',
	"ObjectClassGroupName"	TEXT(80) NULL DEFAULT 'NS',
	"BocCode"	TEXT(80) NULL DEFAULT 'NS',
	"BocName"	TEXT(80) NULL DEFAULT 'NS',
	"FinanceObjectClass"	TEXT(80) NULL DEFAULT 'NS',
	"PriorYear"	NUMERIC NULL DEFAULT 0.0,
	"CurrentYear"	NUMERIC NULL DEFAULT 0.0,
	"BudgetYear"	NUMERIC NULL DEFAULT 0.0,
	PRIMARY KEY("ObjectClassOutlaysId" AUTOINCREMENT)
);