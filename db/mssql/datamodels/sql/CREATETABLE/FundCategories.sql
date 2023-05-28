CREATE TABLE FundCategories 
(
    FundCategoriesId INT NOT NULL IDENTITY(1,1),
    Code NVARCHAR(80) NULL,
    Name NVARCHAR(80) NULL,
    ShortName NVARCHAR(80) NULL
);