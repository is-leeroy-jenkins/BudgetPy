CREATE TABLE 'Contacts' 
(
	'ContactsId'	INTEGER NOT NULL UNIQUE,
	'FirstName'	TEXT,
	'LastName'	TEXT,
	'FullName'	TEXT,
	'Email'	TEXT,
	'RPIO'	TEXT,
	'Section'	TEXT,
	PRIMARY KEY('ContactsId' AUTOINCREMENT)
);