CREATE TABLE [AppropriationBills]
(
   [ID] INT NOT NULL IDENTITY (1,1),
   [BFY] NVARCHAR(255) DEFAULT ('NS'),
   [Title] NVARCHAR(255) DEFAULT ('NS'),
   [PublicLaw] NVARCHAR(255) DEFAULT ('NS'),
   [EnactedDate] NVARCHAR(255) DEFAULT ('NS')
);
