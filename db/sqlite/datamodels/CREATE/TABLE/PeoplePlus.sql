CREATE TABLE IF NOT EXISTS PeoplePlus
(
   PeoplePlusId  INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyPeoplePlus PRIMARY KEY,
   RcCode TEXT(255),
   DivisionName TEXT(255),
   EpaNumber TEXT(255),
   LastName TEXT(255),
   FirstName TEXT(255),
   ReportingCode TEXT(255),
   ReportingCodeName TEXT(255),
   WorkCode TEXT(255),
   Hours FLOAT
);
