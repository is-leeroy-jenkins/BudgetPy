CREATE TABLE IF NOT EXISTS 'Appropriations' 
(
	'AppropriationsId'	INTEGER NOT NULL UNIQUE,
	'BFY'	TEXT(255) NOT NULL,
	'Title'	TEXT(255),
	'PublicLaw'	TEXT(255),
	'EnactedDate'	DATETIME,
	CONSTRAINT 'PrimaryKeyAppropriations' PRIMARY KEY('AppropriationsId' AUTOINCREMENT)
);