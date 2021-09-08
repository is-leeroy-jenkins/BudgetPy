CREATE TABLE ReimbursableSurvey (
	ReimbursableSurveyId	INTEGER NOT NULL UNIQUE,
	BFY	 TEXT(255),
	FundCode	 TEXT(255),
	FundName	 TEXT(255),
	Amount	NUMERIC,
	PRIMARY KEY(ReimbursableSurveyId AUTOINCREMENT)
)