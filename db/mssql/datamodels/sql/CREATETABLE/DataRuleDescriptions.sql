CREATE TABLE DataRuleDescriptions 
(
	DataRuleDescriptionsId	INT NOT NULL IDENTITY(1,1),
	Schedule	NVARCHAR(80) NULL,
	LineNumber	NVARCHAR(80) NULL,
	RuleNumber	NVARCHAR(80) NULL,
	RuleDescription	NVARCHAR(80) NULL,
	ScheduleOrder	NVARCHAR(80) NULL
);