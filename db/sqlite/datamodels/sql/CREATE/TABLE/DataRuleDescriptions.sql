CREATE TABLE "DataRuleDescriptions" 
(
	"DataRuleDescriptionsId"	INTEGER NOT NULL UNIQUE,
	"Schedule"	TEXT,
	"LineNumber"	TEXT,
	"RuleNumber"	TEXT,
	"RuleDescription"	TEXT,
	"ScheduleOrder"	TEXT,
	PRIMARY KEY("DataRuleDescriptionId" AUTOINCREMENT)
);