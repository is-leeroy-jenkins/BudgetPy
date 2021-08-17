CREATE TABLE IF NOT EXISTS WorkCodes
(
   WorkCodeId  INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyWorkCodes PRIMARY KEY,
   RpioCode TEXT(255) DEFAULT ('NS'),
   WorkCode TEXT(255) DEFAULT ('NS'),
   WorkCodeName TEXT(255) DEFAULT ('NS'),
   ChargeType TEXT(255) DEFAULT ('NS'),
   Notifications TEXT(255) DEFAULT ('NS'),
   PayPeriod TEXT(255) DEFAULT ('NS'),
   BFY TEXT(255) DEFAULT ('NS'),
   ApproverUserName TEXT(255) DEFAULT ('NS'),
   ApprovedDate TEXT(255) DEFAULT ('NS'),
   ModifierUserName TEXT(255) DEFAULT ('NS'),
   ModifiedDate TEXT(255) DEFAULT ('NS'),
   FundCode TEXT(255) DEFAULT ('NS'),
   FocCode TEXT(255) DEFAULT ('NS'),
   CostOrgCode TEXT(255) DEFAULT ('NS'),
   CostOrgName TEXT(255) DEFAULT ('NS'),
   RcCode TEXT(255) DEFAULT ('NS'),
   AccountCode TEXT(255) DEFAULT ('NS'),
   WorkProjectCode TEXT(255) DEFAULT ('NS'),
   WorkProjectName TEXT(255) DEFAULT ('NS'),
   Percentage FLOAT NOT NULL DEFAULT (0.0)
);
