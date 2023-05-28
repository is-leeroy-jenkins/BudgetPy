CREATE TABLE AnnualCarryoverSurvey 
(
    AnnualCarryoverSurveyId INT NOT NULL IDENTITY(1,1),
    BFY NVARCHAR(80) NULL,
    FundCode NVARCHAR(80) NULL,
    FundName NVARCHAR(80) NULL,
    Amount FLOAT NULL
);