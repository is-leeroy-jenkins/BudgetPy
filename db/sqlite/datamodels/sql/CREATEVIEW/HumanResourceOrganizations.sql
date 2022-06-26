CREATE TABLE "DocumentControlNumbers" (
	"DocumentControlNumbersId"	INTEGER NOT NULL,
	"RpioCode"	TEXT NOT NULL DEFAULT 'NS',
	"RpioName"	TEXT NOT NULL DEFAULT 'NS',
	"DocumentType"	TEXT NOT NULL DEFAULT 'NS',
	"DocumentNumber"	TEXT NOT NULL DEFAULT 'NS',
	"DocumentPrefix"	TEXT NOT NULL DEFAULT 'NS',
	"DocumentControlNumber"	TEXT NOT NULL DEFAULT 'NS',
	PRIMARY KEY("DocumentControlNumbersId")
)