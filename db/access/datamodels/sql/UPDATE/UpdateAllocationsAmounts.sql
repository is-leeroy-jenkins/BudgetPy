UPDATE Allocations
	INNER JOIN StatusOfFunds
ON (Allocations.RcCode = StatusOfFunds.RcCode)
	AND (Allocations.BocCode = StatusOfFunds.BocCode)
	AND (Allocations.OrgCode = StatusOfFunds.OrgCode)
	AND (Allocations.AccountCode = StatusOfFunds.AccountCode)
	AND (Allocations.FundCode = StatusOfFunds.FundCode)
	AND (Allocations.AhCode = StatusOfFunds.AhCode)
	AND (Allocations.BudgetLevel = StatusOfFunds.BudgetLevel)
	AND (Allocations.BFY = StatusOfFunds.BFY)
SET Allocations.Amount = StatusOfFunds.Amount WHERE Allocations.Amount <> StatusOfFunds.Amount;