CREATE TABLE FundCategories
(
	FundCategoriesId INT           NOT NULL UNIQUE,
	Code             NVARCHAR(150) NULL DEFAULT ('NS'),
	Name             NVARCHAR(150) NULL DEFAULT ('NS'),
	ShortName        NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT FundCategoriesPrimaryKey PRIMARY KEY
		(
		  FundCategoriesId ASC
			)
);
