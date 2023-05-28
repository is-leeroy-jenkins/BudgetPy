CREATE TABLE ProgramProjectDescriptions 
(
    ProgramProjectDescriptionsId	INT NOT NULL IDENTITY(1,1),
    Code	NVARCHAR(80) NULL,
    Name	NVARCHAR(80) NULL,
    ProgramTitle	NVARCHAR(255) NULL,
    Laws	NVARCHAR(MAX) NULL,
    Description	NVARCHAR(MAX) NULL,
    ProgramAreaCode	NVARCHAR(80) NULL,
    ProgramAreaName	NVARCHAR(80) NULL
);