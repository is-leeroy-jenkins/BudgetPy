CREATE TABLE Goals
(
	GoalsId AUTOINCREMENT NOT NULL UNIQUE,
	Code    TEXT( 150 )   NULL DEFAULT NS,
	Name    TEXT( 150 )   NULL DEFAULT NS,
	Title   TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	GoalsPrimaryKey
)
	PRIMARY KEY
(
	GoalsId
)
	);
