CREATE TABLE Holidays
(
    HolidaysId AUTOINCREMENT NOT NULL UNIQUE, 
    ColumbusDay DATETIME NULL,
    ThanksgivingDay DATETIME NULL,
    ChristmasDay DATETIME NULL,
    NewYearsDay DATETIME NULL,
    MartinLutherKingDay DATETIME NULL,
    PresidentsDay DATETIME NULL,
    MemorialDay DATETIME NULL,
    VeteransDay DATETIME NULL,
    LaborDay DATETIME NULL,
    CONSTRAINT HoldiaysPrimaryKey 
        PRIMARY KEY(HolidaysId),
);

