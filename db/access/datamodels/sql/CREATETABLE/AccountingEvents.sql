CREATE TABLE AccountingEvents
(
	AccountingEventsId AUTOINCREMENT NOT NULL UNIQUE,
	Code               TEXT( 150 )   NULL DEFAULT NS,
	Name               TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	AccountingEventsPrimaryKey
)
	PRIMARY KEY
(
	AccountsId
)
	);
