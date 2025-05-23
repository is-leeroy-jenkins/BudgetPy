CREATE TABLE DocumentControlNumbers
(
	DocumentControlNumbersId AUTOINCREMENT NOT NULL UNIQUE,
	RpioCode                 TEXT( 150 )   NULL DEFAULT NS,
	RpioName                 TEXT( 150 )   NULL DEFAULT NS,
	DocumentType             TEXT( 150 )   NULL DEFAULT NS,
	DocumentNumber           TEXT( 150 )   NULL DEFAULT NS,
	DocumentPrefix           TEXT( 150 )   NULL DEFAULT NS,
	DocumentControlNumber    TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	DocumentControlNumbersPrimaryKey
)
	PRIMARY KEY
(
	DocumentControlNumbersId
)
	);
