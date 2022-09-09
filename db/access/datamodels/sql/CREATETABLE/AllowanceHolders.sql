CREATE TABLE AllowanceHolders 
(
    AllowanceHoldersId INTEGER NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT PrimaryKeyAllowanceHolders PRIMARY KEY(AllowanceHoldersId)
);