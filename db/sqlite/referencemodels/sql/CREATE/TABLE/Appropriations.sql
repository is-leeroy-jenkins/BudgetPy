CREATE TABLE IF NOT EXISTS "Appropriations" 
(
	"AppropriationsId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(80) NOT NULL,
	"Name"	TEXT(255) DEFAULT 'NS',
	"PublicLaw"	TEXT(80) DEFAULT 'NS',
	"EnactedDate"	DATETIME DEFAULT 'NS',
	CONSTRAINT "PrimaryKeyAppropriations" PRIMARY KEY("AppropriationsId" AUTOINCREMENT)
);