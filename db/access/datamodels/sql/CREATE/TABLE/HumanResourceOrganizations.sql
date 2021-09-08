CREATE TABLE HumanResourceOrganizations
(
   HumanResourceOrganizationId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyHumanResourceOrganizations PRIMARY KEY,
   RcCode NVARCHAR(255),
   DivisionName NVARCHAR(255),
   HrOrgCode NVARCHAR(255),
   HrOrgName NVARCHAR(255)
);
