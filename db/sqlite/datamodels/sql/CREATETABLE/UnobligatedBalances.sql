CREATE TABLE IF NOT EXISTS "UnobligatedBalances" 
(
	"UnobligatedBalancesId"	INTEGER NOT NULL UNIQUE,
	"BudgetYear" TEXT(80) DEFAULT 'NS',
	"BFY" TEXT(80) DEFAULT 'NS',
	"EFY" TEXT(80) DEFAULT 'NS',
	"TreasurySymbol" TEXT(80) DEFAULT 'NS',
	"FundCode" TEXT(80) DEFAULT 'NS',
	"FundName" TEXT(80) DEFAULT 'NS',
	"AccountNumber" TEXT(80) DEFAULT 'NS',
	"AccountName" TEXT(80) DEFAULT 'NS',
	"Amount" NUMERIC DEFAULT 0.0,
	PRIMARY KEY("UnobligatedBalancesId" AUTOINCREMENT)
);