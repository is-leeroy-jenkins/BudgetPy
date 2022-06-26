
    CREATE TABLE IF NOT EXISTS "PayrollCostCodes" 
    (
        "PayrollCostCodesId"	INTEGER NOT NULL UNIQUE,
        "RpioCode"	TEXT(255) NULL DEFAULT 'NS',
        "AhCode"	TEXT(255) NULL DEFAULT 'NS',
        "BFY"	TEXT(255) NULL DEFAULT 'NS',
        "RcCode"	TEXT(255) NULL  DEFAULT 'NS',
        "RcName"	TEXT(255) NULL DEFAULT 'NS',
        "WorkCode"	TEXT(255) NULL DEFAULT 'NS',
        "WorkCodeName"	TEXT(255) NULL DEFAULT 'NS',
        "HrOrgCode"	TEXT(255) NULL DEFAULT 'NS',
        "HrOrgName"	TEXT(255) NULL DEFAULT 'NS',
        CONSTRAINT "PrimaryKeyPayrollCostCodes" PRIMARY KEY("PayrollCostCodesId" AUTOINCREMENT)
    );