CREATE TABLE BudgetaryResourceExecution
(
	BudgetaryResourceExecutionId INTEGER       NOT NULL UNIQUE,
	FiscalYear                   NVARCHAR(150) NULL DEFAULT ('NS'),
	BFY                          NVARCHAR(150) NULL DEFAULT ('NS'),
	EFY                          NVARCHAR(150) NULL DEFAULT ('NS'),
	LastUpdate                   NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode            NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName            NVARCHAR(150) NULL DEFAULT ('NS'),
	TreasuryAccountName          NVARCHAR(150) NULL DEFAULT ('NS'),
	STAT                         NVARCHAR(150) NULL DEFAULT ('NS'),
	CreditIndicator              NVARCHAR(150) NULL DEFAULT ('NS'),
	LineNumber                   NVARCHAR(150) NULL DEFAULT ('NS'),
	LineDescription              NVARCHAR(150) NULL DEFAULT ('NS'),
	SectionName                  NVARCHAR(150) NULL DEFAULT ('NS'),
	SectionNumber                NVARCHAR(150) NULL DEFAULT ('NS'),
	LineType                     NVARCHAR(150) NULL DEFAULT ('NS'),
	FinancingAccounts            NVARCHAR(150) NULL DEFAULT ('NS'),
	November                     DOUBLE        NULL DEFAULT (0.0),
	January                      DOUBLE        NULL DEFAULT (0.0),
	Feburary                     DOUBLE        NULL DEFAULT (0.0),
	April                        DOUBLE        NULL DEFAULT (0.0),
	May                          DOUBLE        NULL DEFAULT (0.0),
	June                         DOUBLE        NULL DEFAULT (0.0),
	August                       DOUBLE        NULL DEFAULT (0.0),
	October                      DOUBLE        NULL DEFAULT (0.0),
	Amount1                      DOUBLE        NULL DEFAULT (0.0),
	Amount2                      DOUBLE        NULL DEFAULT (0.0),
	Amount3                      DOUBLE        NULL DEFAULT (0.0),
	Amount4                      DOUBLE        NULL DEFAULT (0.0),
	CONSTRAINT BudgetaryResourceExecutionPrimaryKey PRIMARY KEY
		(
		  BudgetaryResourceExecutionId ASC
			)
);