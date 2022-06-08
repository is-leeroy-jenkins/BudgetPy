CREATE TABLE IF NOT EXISTS AccountingEvents 
(
	AccountingEventsId	INTEGER NOT NULL UNIQUE,
	Code	TEXT(255),
	Name	TEXT(255),
	CONSTRAINT PrimaryKeyAccountingEvents PRIMARY KEY(AccountingEventsId AUTOINCREMENT)
);