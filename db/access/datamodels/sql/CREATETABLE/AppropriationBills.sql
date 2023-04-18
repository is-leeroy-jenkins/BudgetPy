CREATE TABLE AppropriationBills
(
   AppropriationBillsId AUTOINCREMENT NOT NULL UNIQUE,
   BFY TEXT(80) NULL DEFAULT NS,
   Title TEXT(80) NULL DEFAULT NS,
   PublicLaw TEXT(80) NULL DEFAULT NS,
   EnactedDate TEXT(80) NULL DEFAULT NS
   PRIMARY KEY( AppropriationBillsId )
);
