CREATE TABLE OutlayRates
(
	OutlayRatesId     INT           NOT NULL UNIQUE,
	FiscalYear        NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountCode NVARCHAR(150) NULL DEFAULT ('NS'),
	BudgetAccountName NVARCHAR(150) NULL DEFAULT ('NS'),
	Category          NVARCHAR(150) NULL DEFAULT ('NS'),
	Baseline          NVARCHAR(150) NULL DEFAULT ('NS'),
	Year1             FLOAT         NULL DEFAULT (0.0),
	Year2             FLOAT         NULL DEFAULT (0.0),
	Year3             FLOAT         NULL DEFAULT (0.0),
	Year4             FLOAT         NULL DEFAULT (0.0),
	Year5             FLOAT         NULL DEFAULT (0.0),
	Year6             FLOAT         NULL DEFAULT (0.0),
	Year7             FLOAT         NULL DEFAULT (0.0),
	Year8             FLOAT         NULL DEFAULT (0.0),
	Year9             FLOAT         NULL DEFAULT (0.0),
	Year10            FLOAT         NULL DEFAULT (0.0),
	Year11            FLOAT         NULL DEFAULT (0.0),
	CONSTRAINT OutlayRatesPrimaryKey PRIMARY KEY
		(
		  OutlayRatesId ASC
			)
);