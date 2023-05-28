CREATE TABLE CarryoverApportionments
(
    CarryoverApportionmentsId INT NOT NULL IDENTITY(1,1),
    BudgetAccount NVARCHAR(80) NULL,
    TreasuryAccount NVARCHAR(80) NULL,
    BFY NVARCHAR(80) NULL,
    EFY NVARCHAR(80) NULL,
    Grouping NVARCHAR(80) NULL,
    Description NVARCHAR(80) NULL,
    LineName NVARCHAR(80) NULL,
    AuthorityType NVARCHAR(80) NULL,
    Request FLOAT NULL,
    Balance FLOAT NULL,
    Deobligations FLOAT NULL,
    Amount FLOAT NULL,
    LineNumber NVARCHAR(80) NULL,
    LineSplit NVARCHAR(80) NULL,
    ApportionmentAccountCode NVARCHAR(80) NULL,
    TreasuryAccountCode NVARCHAR(80) NULL,
    TreasuryAccountName NVARCHAR(80) NULL,
    BudgetAccountCode NVARCHAR(80) NULL,
    BudgetAccountName NVARCHAR(80) NULL
);

