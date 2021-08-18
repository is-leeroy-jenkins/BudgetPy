CREATE TABLE ControlNumbers
(
   CnId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyControlNumbers PRIMARY KEY,
   BFY TEXT(255),
   Region TEXT(255),
   AhCode TEXT(255),
   RegionControlNumber DOUBLE,
   FundCode TEXT(255),
   FundControlNumber DOUBLE,
   RcCode TEXT(255),
   DivisionName TEXT(255),
   DivisionControlNumber DOUBLE,
   DateIssued DATETIME
);
