CREATE TABLE IF NOT EXISTS "Apportionments" 
(
	"ApportionmentsId"	INTEGER NOT NULL UNIQUE,
	"Year"	TEXT(80) NULL DEFAULT 'NS'
	"ActivityId"	TEXT(80) NULL DEFAULT 'NS'
	"TreasuryFundCode"	TEXT(80) NULL DEFAULT 'NS'
	"TreasuryFundSymbol"	TEXT(80) NULL DEFAULT 'NS'
	"TreasuryAgency"	TEXT(80) NULL DEFAULT 'NS'
	"TreasuryAccountCode"	TEXT(80) NULL DEFAULT 'NS'
	"BFY"	TEXT(80) NULL DEFAULT 'NS'
	"EFY"	TEXT(80) NULL DEFAULT 'NS'
	"AvailabilityType"	TEXT(80) NULL DEFAULT 'NS'
	"TreasuryAccountTitle"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetAgency"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetBureau"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetAccount"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetAgencyTitle"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetBureauTitle"	TEXT(80) NULL DEFAULT 'NS'
	"BudgetAccountTitle"	TEXT(80) NULL DEFAULT 'NS'
	"DateApproved"	TEXT(80) NULL DEFAULT 'NS'
	"LineNumber"	TEXT(80) NULL DEFAULT 'NS'
	"LineSort"	TEXT(80) NULL DEFAULT 'NS'
	"LineDescription"	TEXT(80) NULL DEFAULT 'NS'
	"Amount"	DOUBLE NULL DEFAULT 0.0,
	PRIMARY KEY("ApportionmentsId" AUTOINCREMENT)
);