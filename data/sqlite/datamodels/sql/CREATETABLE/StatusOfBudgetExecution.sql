CREATE TABLE  IF NOT EXISTS StatusOfBudgetExecution 
(
	StatusOfBudgetExecutionId	INTEGER NOT NULL UNIQUE,
	MainAccount	TEXT(150) DEFAULT NS,
	TreasuryAccountCode	TEXT(150) DEFAULT NS,
	LineCaption	TEXT(150) DEFAULT NS,
	LineNumber	TEXT(150) DEFAULT NS,
	LineName	TEXT(150) DEFAULT NS,
	Amount	DOUBLE DEFAULT NS,
	TreasuryAccountName	TEXT(150) DEFAULT NS,
	BudgetAccountCode	TEXT(150) DEFAULT NS,
	BudgetAccountName	TEXT(150) DEFAULT NS,
	PRIMARY KEY(StatusOfBudgetExecutionId AUTOINCREMENT)
)