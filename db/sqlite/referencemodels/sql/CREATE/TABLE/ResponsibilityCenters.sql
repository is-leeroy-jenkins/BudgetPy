CREATE TABLE ResponsibilityCenters
(
	ResponsibilityCenterId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyResponsibilityCenters PRIMARY KEY AUTOINCREMENT,
	Code TEXT(255) NULL,
	Name TEXT(255) NULL,
	Title TEXT(255) NULL
);

