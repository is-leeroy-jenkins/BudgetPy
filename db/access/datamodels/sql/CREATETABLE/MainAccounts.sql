CREATE TABLE MainAccounts
(
	MainAccountsId    AUTOINCREMENT NOT NULL,
	Code              NVARCHAR(150) NULL DEFAULT ('NS'),
	Name              NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(150) NULL DEFAULT ('NS'), CONSTRAINT
(
	MainAccountsPrimaryKey
)
	PRIMARY KEY
(
	MainAccountsId
)
	);