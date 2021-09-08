
CREATE TABLE IF NOT EXISTS BudgetParameters
(
   BudgetParameterId  INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyBudgetParameters PRIMARY KEY,
   AhCode TEXT(255),
   BFY TEXT(255),
   RcCode TEXT(255),
   FundCode TEXT(255)
);