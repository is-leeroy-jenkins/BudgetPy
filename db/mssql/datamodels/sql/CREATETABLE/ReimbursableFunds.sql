CREATE TABLE ReimbursableFunds 
(
	ReimbursableFundsId	INT NOT NULL IDENTITY(1,1),
	RpioCode	NVARCHAR(80) NULL,
	BFY	NVARCHAR(80) NULL,
	FundCode	NVARCHAR(80) NULL,
	AccountCode	NVARCHAR(80) NULL,
	RcCode	NVARCHAR(80) NULL,
	RcName	NVARCHAR(80) NULL,
	BocCode	NVARCHAR(80) NULL,
	DocumentControlNumber	NVARCHAR(80) NULL,
	AgreeementNumber	NVARCHAR(80) NULL,
	Amount	FLOAT NULL,
	OpenCommitments	FLOAT NULL,
	Obligations	FLOAT NULL,
	ULO	FLOAT NULL,
	Available	FLOAT NULL
);