CREATE TABLE IF NOT EXISTS "ProgramFinancingSchedule" 
(
	"ProgramFinancingScheduleId"	INTEGER NOT NULL UNIQUE,
	"ReportYear"	TEXT(80) NULL DEFAULT 'NS',
	"TreasuryAgencyCode"	TEXT(80) NULL DEFAULT 'NS',
	"TreasuryAccountCode"	TEXT(80) NULL DEFAULT 'NS',
	"LedgerAccountCode"	TEXT(80) NULL DEFAULT 'NS',
	"SectionNumber"	TEXT(80) NULL DEFAULT 'NS',
	"SectionName"	TEXT(80) NULL DEFAULT 'NS',
	"LineNumber"	TEXT(80) NULL DEFAULT 'NS',
	"LineDescription"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAgencyCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbFundCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAccountTitle"	TEXT(80) NULL DEFAULT 'NS',
	"AgencySequence"	TEXT(80) NULL DEFAULT 'NS',
	"AccountSequence"	TEXT(80) NULL DEFAULT 'NS',
	"AgencyName"	TEXT(80) NULL DEFAULT 'NS',
	"FundName"	TEXT(80) NULL DEFAULT 'NS',
	"OriginalAmount"	NUMERIC NULL DEFAULT 0,
	"BudgetAmount"	NUMERIC NULL DEFAULT 0,
	"AgencyAmount"	NUMERIC NULL DEFAULT 0,
	"Amount"	NUMERIC NULL DEFAULT 0,
	PRIMARY KEY("ProgramFinancingScheduleId" AUTOINCREMENT)
);