CREATE TABLE CapitalPlanningInvestmentCodes 
(
    CapitalPlanningInvestmentCodesId AUTOINCREMENT NOT NULL UNIQUE,
    Type TEXT(80) NULL DEFAULT NS,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    CONSTRAINT CapitalPlanningInvestmentCodesPrimaryKey
        PRIMARY KEY(CapitalPlanningInvestmentCodesId)
);