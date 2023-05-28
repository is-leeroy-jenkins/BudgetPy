CREATE TABLE FiscalYears 
(
    FiscalYearsId AUTOINCREMENT NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    StartDate TEXT(80) NULL DEFAULT NS,
    ColumbusDay DATETIME NULL,
    VeteransDay DATETIME  NULL,
    ThanksgivingDay DATETIME  NULL,
    ChristmasDay DATETIME NULL,
    NewYearsDay DATETIME NULL,
    MartinLutherKingDay DATETIME NULL,
    WashingtonsDay DATETIME NULL,
    MemorialDay DATETIME NULL,
    JuneteenthDay DATETIME NULL,
    IndependenceDay DATETIME NULL,
    LaborDay DATETIME NULL,
    ExpiringYear TEXT(80) NULL DEFAULT NS,
    ExpirationDate TEXT(80) NULL DEFAULT NS,
    WorkDays TEXT(80) NULL DEFAULT NS,
    WeekDays TEXT(80) NULL DEFAULT NS,
    WeekEnds TEXT(80) NULL DEFAULT NS,
    EndDate TEXT(80) NULL DEFAULT NS,
    Availability TEXT(80) NULL DEFAULT NS,
    CONSTRAINT FiscalYearsPrimaryKey
        PRIMARY KEY(FiscalYearsId)
);