CREATE TABLE IF NOT EXISTS ReconciliationLines 
(
	ReconciliationLinesId	INTEGER NOT NULL UNIQUE,
	Number TEXT(80) NULL DEFAULT NS,
	Name	TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(ReconciliationLinesId AUTOINCREMENT)
);