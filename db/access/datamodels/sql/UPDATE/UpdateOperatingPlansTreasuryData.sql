UPDATE OperatingPlans 
INNER JOIN Funds 
ON (Funds.Code = OperatingPlans.FundCode) 
AND (Funds.BFY = OperatingPlans.BFY) 
AND (Funds.EFY = OperatingPlans.EFY) 
SET OperatingPlans.TreasuryAccountCode = Funds.TreasuryAccountCode, 
OperatingPlans.TreasuryAccountName = Funds.TreasuryAccountName, 
OperatingPlans.BudgetAccountCode = Funds.BudgetAccountCode, 
OperatingPlans.BudgetAccountName = Funds.BudgetAccountName;