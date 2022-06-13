CREATE TABLE NationalPrograms 
(
    NationalProgramsId INTEGER NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    RpioCode TEXT(80) NULL DEFAULT NS,
    Title TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyNationalPrograms PRIMARY KEY(NationalProgramsId)
);