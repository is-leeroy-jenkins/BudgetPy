CREATE TABLE BudgetObjectClasses
(
	BudgetObjectClassesId AUTOINCREMENT NOT NULL UNIQUE,
	Code                  TEXT( 150 )   NULL DEFAULT NS,
	Name                  TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	BudgetObjectClassesPrimaryKey
)
	PRIMARY KEY
(
	BudgetObjectClassesId
)
	);
