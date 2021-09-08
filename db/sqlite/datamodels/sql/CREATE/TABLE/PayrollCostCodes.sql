CREATE TABLE IF NOT EXISTS ReportingCodes
(
	ReportingCodesId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyReportingCodes PRIMARY KEY AUTOINCREMENT,
    ReportingCode TEXT(255) NULL,
    ReportingCodeName TEXT(255) NULL
);