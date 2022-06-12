CREATE TABLE 'AdministrativeRequests' 
(
	'AdministrativeRequestsId'	INTEGER NOT NULL UNIQUE,
	'RequestId'	TEXT,
	'ControlTeamAnalyst'	TEXT,
	'RpioCode'	TEXT,
	'DocumentTitle'	TEXT,
	'Amount'	TEXT,
	'FundCode'	TEXT,
	'BFY'	INTEGER,
	'Status'	TEXT,
	'OriginalRequestDate'	TEXT,
	'LastActivityDate'	TEXT,
	'Duration'	INTEGER,
	'BFS'	TEXT,
	'Comments'	TEXT,
	'RequestDocument'	TEXT,
	'RequestType'	TEXT,
	'TypeCode'	TEXT,
	'Decision'	TEXT,
	PRIMARY KEY('AdministrativeRequestsId' AUTOINCREMENT)
);

