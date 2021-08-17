CREATE TABLE ResourcePlanningImplentationOffices
(
	RpioId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyResourcePlanningImplementationOffices PRIMARY KEY AUTOINCREMENT,
	Code TEXT(255) NULL,
	Name TEXT(255) NULL
);

