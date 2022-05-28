CREATE TABLE ReimbursableFunds (
	ReimbursableFundId	INTEGER,
	RPIO	INTEGER,
	BFY	INTEGER,
	FundCode  TEXT(255),
	AccountCode  TEXT(255),
	RcCode  TEXT(255),
	DivisionName  TEXT(255),
	BocCode	INTEGER,
	DocumentControlNumber  TEXT(255),
	AgreeementNumber  TEXT(255),
	Amount	REAL,
	OpenCommitments	INTEGER,
	Obligations	REAL,
	ULO	INTEGER,
	Available	REAL
)