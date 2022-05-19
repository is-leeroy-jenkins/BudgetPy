CREATE TABLE "ApplicationTables" (
	"ApplicationTableId"	INTEGER NOT NULL UNIQUE,
	"TableName"	TEXT(255) NOT NULL DEFAULT 'NS',
	"Model"	TEXT(255) NOT NULL DEFAULT 'NS',
	CONSTRAINT "PrimaryKeyApplicationTables" PRIMARY KEY("ApplicationTableId")
);