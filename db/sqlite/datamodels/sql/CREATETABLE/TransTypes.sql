CREATE TABLE IF NOT EXISTS 'TransTypes' 
(
	'TransTypesId'	INTEGER NOT NULL UNIQUE,
	'FundCode'	TEXT,
	'Appropriation'	TEXT,
	'BFY'	TEXT,
	'EFY'	TEXT,
	'TreasurySymbol'	TEXT,
	'DocType'	TEXT,
	'AppropriationBill'	TEXT,
	'ContinuingResolution'	TEXT,
	'RescissionCurrentYear'	TEXT,
	'RescissionPriorYear'	TEXT,
	'SequesterReduction'	TEXT,
	'SequesterReturn'	TEXT,
	PRIMARY KEY('TransTypesId' AUTOINCREMENT)
);