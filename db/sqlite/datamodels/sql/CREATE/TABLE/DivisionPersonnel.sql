CREATE TABLE IF NOT EXISTS DivisionPersonnel
(
   PersonnelId  INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyDivisionPersonnel PRIMARY KEY,
   RcCode TEXT(255),
   EmployeeId TEXT(255),
   LastName TEXT(255),
   FirstName TEXT(255),
   JobTitle TEXT(255),
   Grade TEXT(255),
   Step TEXT(255),
   HireDate DATETIME,
   Tenure FLOAT,
   HrOrgName TEXT(255),
   Email TEXT(255),
   PhoneNumber TEXT(255),
   Office TEXT(255),
   MailCode TEXT(255)
);
