CREATE TABLE Projects
(
	ProjectsId INT           NOT NULL UNIQUE,
	Code       NVARCHAR(150) NULL DEFAULT ('NS'),
	Name       NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT ProjectsPrimaryKey PRIMARY KEY
		(
		  ProjectsId ASC
			)
);
