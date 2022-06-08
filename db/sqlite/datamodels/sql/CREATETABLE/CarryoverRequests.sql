CREATE TABLE IF NOT EXISTS 'CarryoverRequests' 
(
	'CarryoverReissuanceRequestsId'	INTEGER NOT NULL UNIQUE,
	'ControlTeamAnalyst'	TEXT,
	'RpioCode'	TEXT,
	'DocumentTitle'	TEXT,
	'Amount'	TEXT,
	'FundCode'	TEXT,
	'Status'	TEXT,
	'OriginalRequestDate'	TEXT,
	'LastActivityDate'	TEXT,
	'BFS'	TEXT,
	'Comments'	TEXT,
	'RequestDocument'	TEXT,
	'Duration'	TEXT,
	PRIMARY KEY('CarryoverReissuanceRequestsId' AUTOINCREMENT)
);