CREATE TABLE FederalHolidays 
(
    FederalHolidaysId AUTOINCREMENT NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    Columbus TEXT(80) NULL DEFAULT NS,
    Veterans TEXT(80) NULL DEFAULT NS,
    Thanksgiving TEXT(80) NULL DEFAULT NS,
    Christmas TEXT(80) NULL DEFAULT NS,
    NewYears TEXT(80) NULL DEFAULT NS,
    MartinLutherKing TEXT(80) NULL DEFAULT NS,
    Presidents TEXT(80) NULL DEFAULT NS,
    Memorial TEXT(80) NULL DEFAULT NS,
    Juneteenth TEXT(80) NULL DEFAULT NS,
    Independence TEXT(80) NULL DEFAULT NS,
    Labor TEXT(80) NULL DEFAULT NS,
    CONSTRAINT FederalHolidaysPrimaryKey
        PRIMARY KEY(FederalHolidaysId)
);