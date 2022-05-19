CREATE TABLE ResourcePlanningImplentationOffices
(
	RpioId INTEGER NOT NULL UNIQUE CONSTRAINT PK_ResourcePlanningImplementationOffices PRIMARY KEY AUTOINCREMENT,
	Code TEXT(255) NULL,
	Name TEXT(255) NULL
);

