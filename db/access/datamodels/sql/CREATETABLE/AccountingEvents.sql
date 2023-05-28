CREATE TABLE AccountingEvents
(
	AccountingEventsId AUTOINCREMENT NOT NULL UNIQUE,
	Code TEXT(80) NULL DEFAULT NS,
	Name TEXT(80) NULL DEFAULT NS,
	CONSTRAINT PrimaryKeyAccountingEvents 
        PRIMARY KEY(AccountingEventsId)
);