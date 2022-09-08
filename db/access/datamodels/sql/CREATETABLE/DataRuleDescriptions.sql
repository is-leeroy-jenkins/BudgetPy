CREATE TABLE DataRuleDescriptions 
(
    DataRuleDescriptionsId AUTOINCREMENT NOT NULL UNIQUE,
    Schedule TEXT(80) NULL DEFAULT NS,
    LineNumber TEXT(80) NULL DEFAULT NS,
    RuleNumber TEXT(80) NULL DEFAULT NS,
    RuleDescription TEXT(80) NULL DEFAULT NS,
    ScheduleOrder TEXT(80) NULL DEFAULT NS,
    CONSTAINT DataRuleDescriptionsPrimaryKey 
        PRIMARY KEY(DataRuleDescriptionsId)
);