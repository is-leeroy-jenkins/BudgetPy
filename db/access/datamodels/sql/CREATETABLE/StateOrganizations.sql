CREATE TABLE StateOrganizations 
(
    StateOrganizationsId AUTOINCREMENT NOT NULL UNIQUE,
    Name TEXT(80) NULL DEFAULT NS,
    Code TEXT(80) NULL DEFAULT NS,
    RpioName TEXT(80) NULL DEFAULT NS,
    RpioCode TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(StateOrganizationsId)
);