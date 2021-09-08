CREATE TABLE IF NOT EXISTS LocatorData
(
   LocatorId  INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyLocatorData PRIMARY KEY,
   LastName TEXT(255),
   FirstName TEXT(255),
   Email TEXT(255),
   PhoneNumber TEXT(255),
   MailCode TEXT(255),
   Office TEXT(255),
   CellNumber TEXT(255),
   Status TEXT(255)
);