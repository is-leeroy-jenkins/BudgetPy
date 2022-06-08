CREATE TABLE IF NOT EXISTS "LedgerAccounts" 
(
	"LedgerAccountsId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(80) DEFAULT 'NS',
	"EFY"	TEXT(80) DEFAULT 'NS',
	"FundCode"	TEXT(80) DEFAULT 'NS',
	"FundName"	TEXT(80) DEFAULT 'NS',
	"TreasurySymbol"	TEXTTEXT(80) DEFAULT 'NS',
	"AccountNumber"	TEXT(80) DEFAULT 'NS',
	"AccountName"	TEXT(80) DEFAULT 'NS',
	"BeginningBalance"	NUMERIC DEFAULT 0.0,
	"CreditBalance"	NUMERIC DEFAULT 0.0,
	"DebitBalance"	NUMERIC DEFAULT 0.0,
	"ClosingAmount"	NUMERIC DEFAULT 0.0,
	PRIMARY KEY("LedgerAccountsId" AUTOINCREMENT)
);