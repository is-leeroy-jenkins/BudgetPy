CREATE TABLE  PayPeriods  
(
    PayPeriodsId AUTOINCREMENT NOT NULL UNIQUE,
    Period TEXT(80) NULL DEFAULT NS,
    PayPeriod TEXT(80) NULL DEFAULT NS,
    StartDate TEXT(80) NULL DEFAULT NS,
    EndDate TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PayPeriodsPrimaryKey
        PRIMARY KEY( PayPeriodsId )
);