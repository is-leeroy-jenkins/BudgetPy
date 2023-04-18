CREATE TABLE ResponsibilityCenters 
(
    ResponsibilityCentersId AUTOINCREMENT NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    Title TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyResponsibilityCenters PRIMARY KEY(ResponsibilityCentersId)
)